#!/usr/bin/env python3
"""Fetch recent items from every feed in sources.yaml into build/items/<domain>.json."""

from __future__ import annotations

import argparse
import html
import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from common import ROOT, fetch_entries, load_sources

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
TRACKING_PARAMS = {"ref", "ref_src", "source", "publication_id", "post_id"}


def clean_text(value: str, limit: int) -> str:
    text = WS_RE.sub(" ", html.unescape(TAG_RE.sub(" ", value or ""))).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def canonical(link: str) -> str:
    parts = urlsplit(link.strip())
    query = [
        (k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if not k.startswith("utm_") and k not in TRACKING_PARAMS
    ]
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, urlencode(query), ""))


def fetch_feed(feed: dict, cutoff: datetime, per_feed: int) -> tuple[list[dict], str | None]:
    entries, error = fetch_entries(feed["url"])
    if error:
        return [], error
    items = []
    for entry in entries:
        published, link = entry["published"], entry["link"]
        if not link or published is None or published < cutoff:
            continue
        excerpt = clean_text(entry["content"], 600)
        title = clean_text(entry["title"], 200)
        if feed["type"] == "bluesky" or not title:
            title = clean_text(excerpt, 100)
        items.append({
            "title": title,
            "link": link,
            "source": feed["title"],
            "type": feed["type"],
            "published": published.isoformat(),
            "excerpt": excerpt,
        })
    items.sort(key=lambda i: i["published"], reverse=True)
    return items[:per_feed], None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hours", type=float, default=26, help="look-back window")
    parser.add_argument("--per-feed", type=int, default=15, help="max items per feed")
    parser.add_argument("--max-items", type=int, default=150, help="max items per domain")
    parser.add_argument("--out", default=str(ROOT / "build" / "items"))
    args = parser.parse_args()

    sources = load_sources()
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=args.hours)
    jobs = [(domain, feed) for domain in sources["domains"] for feed in domain["feeds"]]

    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(lambda job: fetch_feed(job[1], cutoff, args.per_feed), jobs))

    out = ROOT / args.out  # an absolute --out replaces ROOT
    out.mkdir(parents=True, exist_ok=True)
    stats = {"generated_at": now.isoformat(), "window_hours": args.hours, "feeds": []}
    by_domain: dict[str, list[dict]] = {d["slug"]: [] for d in sources["domains"]}
    seen: dict[str, set[str]] = {d["slug"]: set() for d in sources["domains"]}

    for (domain, feed), (items, error) in zip(jobs, results):
        stats["feeds"].append({"domain": domain["slug"], "title": feed["title"], "items": len(items), "error": error})
        if error:
            print(f"warn  {domain['slug']:<28} {feed['title']}: {error}")
        for item in items:
            key = canonical(item["link"])
            if key not in seen[domain["slug"]]:
                seen[domain["slug"]].add(key)
                by_domain[domain["slug"]].append(item)

    for domain in sources["domains"]:
        items = sorted(by_domain[domain["slug"]], key=lambda i: i["published"], reverse=True)[: args.max_items]
        payload = {
            "domain": domain["slug"],
            "title": domain["title"],
            "focus": domain["focus"],
            "window_hours": args.hours,
            "generated_at": now.isoformat(),
            "item_count": len(items),
            "items": items,
        }
        (out / f"{domain['slug']}.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"ok    {domain['slug']:<28} {len(items)} items")

    (out / "_stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
