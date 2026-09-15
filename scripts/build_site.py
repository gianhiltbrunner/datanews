#!/usr/bin/env python3
"""Render committed digests into RSS feeds, HTML pages and the OPML reading list."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

import markdown

from common import ROOT, load_sources, site_url

DIGESTS = ROOT / "digests"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ATOM = "http://www.w3.org/2005/Atom"
ALL_DOMAINS = {"slug": "all", "title": "All domains", "focus": "the most important stories across every domain"}

CSS = """
:root{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#6b6a65;--line:#e4e1d8;--accent:#1f5f8b}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--fg:#ecebe6;--muted:#9c9a92;--line:#2c2b28;--accent:#7cb7e0}}
body{background:var(--bg);color:var(--fg);font:16px/1.6 ui-sans-serif,system-ui,-apple-system,sans-serif;margin:0;padding-inline:16px}
main{max-width:46rem;margin:0 auto;padding-block:2.5rem 4rem}
a{color:var(--accent)} h1{font-size:1.7rem;line-height:1.25;margin:.2rem 0 1rem}
h2{font-size:1.1rem;margin-top:2rem;border-top:1px solid var(--line);padding-top:1rem}
.meta{color:var(--muted);font-size:.9rem} ul{padding-left:1.2rem} li{margin:.45rem 0}
.feeds a{display:inline-block;margin:.15rem .6rem .15rem 0}
"""

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>{alternate}<style>{css}</style></head>
<body><main>{body}</main></body></html>
"""


def digest_days() -> list[Path]:
    days = [p for p in DIGESTS.glob("*") if p.is_dir() and DATE_RE.match(p.name)] if DIGESTS.exists() else []
    return sorted(days, reverse=True)


def load_digests(slug: str, limit: int) -> list[dict]:
    entries = []
    for day in digest_days():
        path = day / f"{slug}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8").strip()
        first, _, rest = text.partition("\n")
        if first.startswith("# "):
            headline, body = first[2:].strip(), rest
        else:
            headline, body = f"Digest for {day.name}", text
        entries.append({
            "slug": slug,
            "date": day.name,
            "headline": headline,
            "html": markdown.markdown(body, extensions=["extra", "sane_lists"]),
        })
        if len(entries) >= limit:
            break
    return entries


def pub_date(date: str) -> str:
    return format_datetime(datetime.fromisoformat(date).replace(hour=6, tzinfo=timezone.utc))


def write_page(path: Path, title: str, body: str, feed_url: str | None = None) -> None:
    alternate = f'<link rel="alternate" type="application/rss+xml" href="{html.escape(feed_url)}">' if feed_url else ""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(PAGE.format(title=html.escape(title), alternate=alternate, css=CSS, body=body), encoding="utf-8")


def write_rss(path: Path, domain: dict, entries: list[dict], base: str) -> None:
    ET.register_namespace("atom", ATOM)
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    feed_url = f"{base}/feeds/{domain['slug']}.xml"
    ET.SubElement(channel, "title").text = f"datanews · {domain['title']}"
    ET.SubElement(channel, "link").text = f"{base}/"
    ET.SubElement(channel, "description").text = f"Daily AI digest: {domain['focus']}"
    ET.SubElement(channel, "language").text = "en"
    ET.SubElement(channel, "lastBuildDate").text = format_datetime(datetime.now(timezone.utc))
    ET.SubElement(channel, f"{{{ATOM}}}link", href=feed_url, rel="self", type="application/rss+xml")
    for entry in entries:
        item = ET.SubElement(channel, "item")
        label = f" · {entry['label']}" if entry.get("label") else ""
        ET.SubElement(item, "title").text = f"{entry['date']}{label} · {entry['headline']}"
        ET.SubElement(item, "link").text = f"{base}/digests/{entry['date']}/{entry['slug']}.html"
        ET.SubElement(item, "guid", isPermaLink="false").text = f"datanews-{entry['slug']}-{entry['date']}"
        ET.SubElement(item, "pubDate").text = pub_date(entry["date"])
        ET.SubElement(item, "description").text = entry["html"]
    tree = ET.ElementTree(rss)
    ET.indent(tree)
    path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def build_opml(domains: list[dict], base: str) -> ET.ElementTree:
    opml = ET.Element("opml", version="2.0")
    head = ET.SubElement(opml, "head")
    ET.SubElement(head, "title").text = "datanews — data platform, analytics & data engineering"
    ET.SubElement(head, "dateCreated").text = format_datetime(datetime.now(timezone.utc))
    body = ET.SubElement(opml, "body")
    for domain in domains:
        folder = ET.SubElement(body, "outline", text=domain["title"], title=domain["title"])
        for feed in domain["feeds"]:
            attrs = {"type": "rss", "text": feed["title"], "title": feed["title"], "xmlUrl": feed["url"]}
            if feed.get("site"):
                attrs["htmlUrl"] = feed["site"]
            ET.SubElement(folder, "outline", attrs)
    digests = ET.SubElement(body, "outline", text="AI Digests", title="AI Digests")
    for domain in [*domains, ALL_DOMAINS]:
        name = f"datanews · {domain['title']}"
        ET.SubElement(digests, "outline", type="rss", text=name, title=name,
                      xmlUrl=f"{base}/feeds/{domain['slug']}.xml", htmlUrl=f"{base}/")
    tree = ET.ElementTree(opml)
    ET.indent(tree)
    return tree


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(ROOT / "public"))
    parser.add_argument("--limit", type=int, default=30, help="digests per feed")
    args = parser.parse_args()

    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    (out / ".nojekyll").touch()

    base = site_url()
    domains = load_sources()["domains"]
    index_sections = []

    entries_by_slug = {d["slug"]: load_digests(d["slug"], args.limit) for d in [ALL_DOMAINS, *domains]}
    # The all-domains feed carries the cross-domain overview plus every full domain digest.
    combined = [dict(e, label="Top 5") for e in entries_by_slug["all"]]
    combined += [dict(e, label=d["title"]) for d in domains for e in entries_by_slug[d["slug"]]]
    combined.sort(key=lambda e: e["date"], reverse=True)

    for domain in [ALL_DOMAINS, *domains]:
        slug = domain["slug"]
        entries = entries_by_slug[slug]
        feed_url = f"{base}/feeds/{slug}.xml"
        write_rss(out / "feeds" / f"{slug}.xml", domain, combined if slug == "all" else entries, base)
        for entry in entries:
            page = (f'<p class="meta"><a href="../../index.html">datanews</a> · {html.escape(domain["title"])} · {entry["date"]}</p>'
                    f"<h1>{html.escape(entry['headline'])}</h1>{entry['html']}")
            write_page(out / "digests" / entry["date"] / f"{slug}.html", entry["headline"], page, feed_url)
        links = "".join(
            f'<li><a href="digests/{e["date"]}/{slug}.html">{e["date"]} · {html.escape(e["headline"])}</a></li>'
            for e in entries[:7]
        ) or "<li>No digests yet.</li>"
        index_sections.append(
            f'<h2>{html.escape(domain["title"])} <a class="meta" href="feeds/{slug}.xml">RSS</a></h2><ul>{links}</ul>'
        )

    opml = build_opml(domains, base)
    opml.write(ROOT / "datanews.opml", encoding="utf-8", xml_declaration=True)
    opml.write(out / "datanews.opml", encoding="utf-8", xml_declaration=True)

    feed_count = sum(len(d["feeds"]) for d in domains)
    intro = (
        "<h1>datanews</h1>"
        "<p>Daily AI-written digests for data platform engineering, analytics engineering and data engineering, "
        f"summarised from {feed_count} Substack, Bluesky, blog, Reddit and Hacker News feeds.</p>"
        '<p class="feeds"><a href="datanews.opml">Download OPML</a><a href="feeds/all.xml">All-domains RSS</a></p>'
    )
    write_page(out / "index.html", "datanews", intro + "".join(index_sections), f"{base}/feeds/all.xml")
    print(f"Built site for {base} → {out}")


if __name__ == "__main__":
    main()
