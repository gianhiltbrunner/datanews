"""Shared helpers for the datanews scripts."""

from __future__ import annotations

import json
import os
import re
import subprocess
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit

import feedparser
import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.yaml"
USER_AGENT = "Mozilla/5.0 (compatible; datanews-bot/1.0; +https://github.com/)"
RETRYABLE = {429, 500, 502, 503, 504}
# Substack's bot protection blocks cloud IPs (e.g. GitHub runners); rss2json fetches on our behalf.
RSS2JSON = "https://api.rss2json.com/v1/api.json?rss_url="
# Hosts that rate-limit bursts: minimum seconds between requests.
HOST_SPACING = {"www.reddit.com": 4.0, "hnrss.org": 2.0, "api.rss2json.com": 1.5}
_host_locks = {host: threading.Lock() for host in HOST_SPACING}
_host_last: dict[str, float] = {}


def load_sources(path: Path = SOURCES) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _throttle(url: str) -> None:
    host = urlsplit(url).netloc
    if host not in HOST_SPACING:
        return
    with _host_locks[host]:
        wait = _host_last.get(host, 0.0) + HOST_SPACING[host] - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        _host_last[host] = time.monotonic()


def http_get(url: str, timeout: int = 20, retries: int = 2) -> tuple[int, bytes]:
    """GET a URL. Returns (status, body); status 0 means a network error."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/rss+xml, application/atom+xml, application/xml;q=0.9, */*;q=0.8",
    }
    for attempt in range(retries + 1):
        last = attempt == retries
        _throttle(url)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as e:
            if e.code not in RETRYABLE or last:
                return e.code, b""
            retry_after = e.headers.get("Retry-After", "")
            delay = int(retry_after) if retry_after.isdigit() else 2 * (attempt + 1) ** 2
            time.sleep(min(delay, 30))
        except (urllib.error.URLError, TimeoutError, OSError):
            if last:
                return 0, b""
            time.sleep(2 * (attempt + 1))
    return 0, b""


def _from_feedparser(entry) -> dict:
    published = None
    for key in ("published_parsed", "updated_parsed"):
        if parsed := entry.get(key):
            published = datetime(*parsed[:6], tzinfo=timezone.utc)
            break
    content = entry.get("summary") or (entry.get("content") or [{}])[0].get("value", "")
    return {"title": entry.get("title", ""), "link": entry.get("link"), "published": published, "content": content}


def _from_rss2json(item: dict) -> dict:
    published = None
    if item.get("pubDate"):
        published = datetime.strptime(item["pubDate"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    content = item.get("content") or item.get("description") or ""
    return {"title": item.get("title", ""), "link": item.get("link"), "published": published, "content": content}


def fetch_entries(url: str, retries: int = 2) -> tuple[list[dict], str | None]:
    """Fetch a feed as entries {title, link, published, content}. Returns (entries, error)."""
    status, body = http_get(url, retries=retries)
    if status == 200 and body:
        return [_from_feedparser(e) for e in feedparser.parse(body).entries], None
    if status != 403:
        return [], f"HTTP {status}"
    proxy_status, proxy_body = http_get(RSS2JSON + quote(url, safe=""), retries=retries)
    if proxy_status != 200 or not proxy_body:
        return [], f"HTTP 403; rss2json HTTP {proxy_status}"
    data = json.loads(proxy_body)
    if data.get("status") != "ok":
        return [], f"HTTP 403; rss2json: {data.get('message', 'error')}"
    return [_from_rss2json(item) for item in data.get("items", [])], None


def site_url() -> str:
    """Public GitHub Pages URL: $SITE_URL, else derived from the GitHub repository."""
    if url := os.environ.get("SITE_URL"):
        return url.rstrip("/")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        remote = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True, text=True, cwd=ROOT,
        ).stdout.strip()
        if m := re.search(r"github\.com[:/]([^/]+/[^/]+?)(?:\.git)?$", remote):
            repo = m.group(1)
    if not repo:
        return "http://localhost:8000"
    owner, name = repo.split("/", 1)
    if name.lower() == f"{owner.lower()}.github.io":
        return f"https://{name.lower()}"
    return f"https://{owner.lower()}.github.io/{name}"
