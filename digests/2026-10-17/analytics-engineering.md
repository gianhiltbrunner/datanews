# dbt Labs: AI analysts need open data infrastructure, not SaaS lock-in

dbt Labs' roundup led the way with a conversation on why companies are building their own AI analysts rather than wiring agents straight into SaaS tools. Elsewhere, a Medium piece used a SIGMOD paper on automated merge-logic generation to question who writes `is_incremental()` blocks now, and Lightdash and Cube both shipped incremental releases.

## Top stories
- **[Open Data Infrastructure in the age of AI agents](https://roundup.getdbt.com/p/open-data-infrastructure-in-the-age)** — The Analytics Engineering Roundup (dbt Labs). George Fraser, Tristan Handy and a16z's Martin Casado discuss why companies are building their own AI analysts instead of connecting agents directly to SaaS tools, and why that argues for keeping the data stack open. *Why it matters:* a case for why analytics engineering infrastructure choices matter even as AI agents take on more analysis work.
- **[Who writes your is_incremental() block now?](https://medium.com/@shaantanutripathi/who-writes-your-is-incremental-block-now-87aa5653b014?source=rss------dbt-5)** — Medium. Reads the Enzyme paper (SIGMOD 2026) through the eyes of someone who still writes MERGE logic by hand, on automating incremental-model logic generation. *Why it matters:* a preview of how much of today's hand-written dbt incremental logic could become automated.

## Releases & tools
- **[dbt-core 1.12.6](https://github.com/dbt-labs/dbt/releases/tag/v1.12.6)** — announces dbt v2 (Fusion) availability via an INFO message on `dbt --version`, relays the Fusion parser's log output through `--log-format otel`, and fixes bare wildcard FQN selectors and cumulative metrics with an `input_metric`.
- **[Lightdash 2.601.0](https://github.com/lightdash/lightdash/releases/tag/2.601.0)** — adds a Lightdash plugin for Claude with a per-instance MCP URL, following 2.600.0's addition of scikit-learn and polars to the Python-runner sandbox.
- **[Cube v1.8.8](https://github.com/cube-js/cube/releases/tag/v1.8.8)** — the prior v1.8.7 added a `--security-context` flag for `cube evals run`, COUNT(DISTINCT) query planning, and timestamp/interval arithmetic on non-constant operands in cubesql.

## Worth reading
- **[What's new in dbt v2 / dbt Fusion vs. dbt core? Everything explained](https://medium.com/@hugolu87/whats-new-in-dbt-v2-dbt-fusion-vs-dbt-core-everything-explained-7c41d9f6984d?source=rss------dbt-5)** — a rundown of what's changing as dbt v2 and the Fusion engine roll out.
- **[dbt Snapshots Can't Handle Late Data. So We Built One That Can](https://blog.dataengineerthings.org/dbt-snapshots-cant-handle-late-data-so-we-built-one-that-can-ef107cc9e02e?source=rss------dbt-5)** — extends the dbt snapshot pattern to data that arrives in batches rather than strictly in order.
- **[AtScale: semantic layers boost AI accuracy on enterprise data](https://news.google.com/rss/articles/CBMixwFBVV95cUxOZzJ5aUpzaFlibVNEbE04eU9KMnNZeDE2dnFFQkxEZi02TDE5eWpwYktiWm1tdkRCOFViQ3RlTU1ZbmhGYjMtR3FidElOYXlTVnB4X3JYX2JyVW5Kb2ZZYWduZ25pemNra2dKV2M5alltQmRNUTY5NjdtVGNXbExhVk9lSG1tQ19NZkJOZ01nV1JQZ0M2TldfWmxYNWpLYUh6Q2p1WjZZQjBnX0FjaTd3QTZfWUpGYUF6bzBTbXQ0WFM1azNDNlhJ?oc=5)** — AtScale's own research claims semantic layers roughly double AI accuracy on enterprise data, timed to its launch of AtScale for AI.
