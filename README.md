# datanews

A curated RSS reading list (OPML) for **Data Platform Engineering**, **Analytics Engineering** and **Data Engineering**, plus a **daily AI digest** of the most important news in each domain. Sources are Substack, Bluesky, engineering blogs, Reddit and Hacker News.

It runs entirely on GitHub Actions. Every morning:

1. `scripts/fetch_items.py` pulls the last ~26 hours of items from every feed in [`sources.yaml`](sources.yaml).
2. A Claude Code agent ([`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action)) reads those items, opens the most important articles, and writes one Markdown digest per domain to `digests/YYYY-MM-DD/`, following [`prompts/digest.md`](prompts/digest.md).
3. `scripts/build_site.py` turns the digests into RSS feeds, HTML pages and the OPML file, and the result is deployed to GitHub Pages.

## Subscribe

Import `https://<owner>.github.io/<repo>/datanews.opml` into your RSS reader (Feedly, Inoreader, NetNewsWire, Reeder, Miniflux…). It contains:

| Folder | Contents |
|---|---|
| Data Engineering | Source feeds for pipelines, streaming, lakehouse, DuckDB… |
| Analytics Engineering | Source feeds for dbt, semantic layers, BI, data quality… |
| Data Platform Engineering | Source feeds for platforms, catalogs, data contracts, cloud data services… |
| AI Digests | `feeds/data-engineering.xml`, `feeds/analytics-engineering.xml`, `feeds/data-platform-engineering.xml`, `feeds/all.xml` |

If you only want the summaries, subscribe to a single digest feed.

## Setup

1. Push this repository to GitHub.
2. **Choose how the agent authenticates.** Add one of these repository secrets:
   - `CLAUDE_CODE_OAUTH_TOKEN`: uses your Claude Pro/Max subscription. Generate it locally with `claude setup-token`.
   - `OPENROUTER_API_KEY`: routes Claude Code through [OpenRouter](https://openrouter.ai/docs/guides/guides/claude-code-integration).

   ```sh
   gh secret set CLAUDE_CODE_OAUTH_TOKEN   # or: gh secret set OPENROUTER_API_KEY
   ```
3. Enable **Settings → Pages → Source: GitHub Actions**.
4. Start a first run from **Actions → Daily digest → Run workflow**, or with `gh workflow run daily-digest.yml`.

### Optional repository variables

| Variable | Default | Purpose |
|---|---|---|
| `LLM_PROVIDER` | auto: `claude-oauth` if its secret exists, else `openrouter` | Force `claude-oauth` or `openrouter` |
| `DIGEST_MODEL` | `claude-opus-5` for OAuth, `anthropic/claude-opus-5` for OpenRouter | Model passed to Claude Code |
| `SITE_URL` | `https://<owner>.github.io/<repo>` | Base URL used in feeds and the OPML, if you use a custom domain (set it as workflow env) |

The manual run has a `skip_agent` option that rebuilds the feeds and OPML without calling the LLM.

## Adding sources

Add an entry under the right domain in `sources.yaml`:

```yaml
  - title: Someone (Bluesky)
    url: https://bsky.app/profile/<handle>/rss   # Substack: https://<name>.substack.com/feed
    site: https://bsky.app/profile/<handle>
    type: bluesky                                # substack | bluesky | blog | reddit | hackernews
```

Then check that it works:

```sh
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/validate_sources.py          # --prune removes dead feeds
```

The **Validate sources** workflow runs every Monday and opens an issue when feeds die. Reddit and Hacker News feeds sometimes return 429 or 502 when rate-limited; those failures are usually temporary.

## Run locally

```sh
.venv/bin/python scripts/fetch_items.py --hours 26
claude -p "DATE=$(date -u +%F)
Follow the instructions in prompts/digest.md." --allowedTools Read,Write,Glob,WebFetch
.venv/bin/python scripts/build_site.py
python3 -m http.server -d public 8000
```
