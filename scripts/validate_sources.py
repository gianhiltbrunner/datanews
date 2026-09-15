#!/usr/bin/env python3
"""Check every feed in sources.yaml; optionally prune dead ones. Exits 1 if any feed is dead."""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor

import yaml

from common import SOURCES, fetch_entries, load_sources

HEADER = """\
# datanews sources — one entry per domain; each domain becomes an OPML folder.
# type: substack | bluesky | blog | reddit | hackernews
# Bluesky profile feeds: https://bsky.app/profile/<handle>/rss
# Run `python scripts/validate_sources.py` after editing.
"""


def check(feed: dict) -> tuple[bool, str]:
    entries, error = fetch_entries(feed["url"], retries=3)
    if error:
        return False, error
    return bool(entries), f"{len(entries)} entries"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prune", action="store_true", help="remove dead feeds from sources.yaml")
    parser.add_argument("--report", help="write a Markdown report of dead feeds to this path")
    args = parser.parse_args()

    sources = load_sources()
    jobs = [(domain, feed) for domain in sources["domains"] for feed in domain["feeds"]]
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda job: check(job[1]), jobs))

    dead, limited = [], 0
    for (domain, feed), (ok, detail) in zip(jobs, results):
        # 429 means the host is throttling us (common from shared CI IPs), not that the feed is gone.
        rate_limited = not ok and "429" in detail
        label = "OK  " if ok else "WAIT" if rate_limited else "DEAD"
        print(f"{label}  {domain['slug']:<26} {feed['title']:<48} {detail}")
        if rate_limited:
            limited += 1
        elif not ok:
            dead.append((domain, feed, detail))

    print(f"\n{len(jobs) - len(dead) - limited}/{len(jobs)} feeds OK, {limited} rate-limited, {len(dead)} dead")

    if args.report and dead:
        lines = ["The weekly source check found feeds that failed:", "", "| Domain | Feed | Result |", "|---|---|---|"]
        lines += [f"| {d['title']} | [{f['title']}]({f['url']}) | {detail} |" for d, f, detail in dead]
        lines += ["", "Fix the URL or run `python scripts/validate_sources.py --prune`."]
        with open(args.report, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")

    if args.prune and dead:
        dead_urls = {f["url"] for _, f, _ in dead}
        for domain in sources["domains"]:
            domain["feeds"] = [f for f in domain["feeds"] if f["url"] not in dead_urls]
        body = yaml.safe_dump(sources, sort_keys=False, allow_unicode=True, width=1000)
        SOURCES.write_text(HEADER + body, encoding="utf-8")
        print(f"Pruned {len(dead_urls)} feeds from {SOURCES.name}")

    sys.exit(1 if dead and not args.prune else 0)


if __name__ == "__main__":
    main()
