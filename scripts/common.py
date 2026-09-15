"""Shared helpers for the datanews scripts."""

from __future__ import annotations

import os
import re
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.yaml"
USER_AGENT = "Mozilla/5.0 (compatible; datanews-bot/1.0; +https://github.com/)"
RETRYABLE = {429, 500, 502, 503, 504}


def load_sources(path: Path = SOURCES) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def http_get(url: str, timeout: int = 20, retries: int = 2) -> tuple[int, bytes]:
    """GET a URL. Returns (status, body); status 0 means a network error."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/rss+xml, application/atom+xml, application/xml;q=0.9, */*;q=0.8",
    }
    for attempt in range(retries + 1):
        last = attempt == retries
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
