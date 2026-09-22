# The real cost of Iceberg table maintenance comes into focus

Most of the feed was SEO-driven Medium/DEV filler and Google News stories that only coincidentally matched "data engineering," with none of the usual substack or engineering-blog regulars publishing. The pieces that stood out were all practitioner write-ups on DuckDB and Iceberg — quantifying what unmaintained lakehouse tables actually cost, and two concrete guides to running DuckDB and entity resolution in production. Dagster shipped a small patch, and the community pulse leaned on a Reddit investigation into PDF table extraction and a DuckCon talk teaser.

## Top stories
- **[The Real Cost of Apache Iceberg Table Maintenance](https://dev.to/jonisar/the-real-cost-of-apache-iceberg-table-maintenance-3kg)** — DEV. Breaks down four cost categories teams underestimate: orphaned/unreferenced data often running 25–40% of object storage bills (one audit found 200 TB of orphan data costing ~$4,700/month), a roughly 20x query-cost gap between sorted and unsorted tables, and Spark-based compaction costing about 10x more than a purpose-built engine on the same job. *Why it matters:* it turns a vague "maintenance is important" warning into concrete numbers teams can use to justify tooling and scheduling changes.
- **[Running DuckDB on your own infrastructure: a production setup](https://dev.to/mohammed_arshadansari_f2/running-duckdb-on-your-own-infrastructure-a-production-setup-530d)** — DEV. Lays out a self-hosted DuckDB pattern: object storage laid out as partitioned Parquet, a single writer process producing new partitions, and many read-only reader processes querying across them. *Why it matters:* it's a concrete blueprint for teams considering DuckDB outside a managed warehouse.
- **[What Splink actually runs on DuckDB when it scores entity pairs](https://dev.to/hannune/what-splink-actually-runs-on-duckdb-when-it-scores-entity-pairs-1e3o)** — DEV. Traces the actual SQL Splink's entity-resolution library generates on DuckDB for blocking and scoring, run against a 44,798-entity registry. *Why it matters:* it demystifies a popular entity-resolution tool for anyone trying to debug or tune it.

## Releases & tools
- **[1.13.24 (core) / 0.29.24 (libraries)](https://github.com/dagster-io/dagster/releases/tag/1.13.24)** — Dagster releases. Adds cross-account service discovery for the ECS agent (via a new `service_discovery_reconcile_interval` option) and clearer errors when a project's root module isn't importable.

## Worth reading
- **[Databricks classic vs serverless compute: the limitation list decides it](https://dev.to/dino_david_c5d8f55f119b7f/databricks-classic-vs-serverless-compute-the-limitation-list-decides-it-527j)** — DEV. Contrasts classic compute, where you own the VMs, autoscaling and networking, against serverless, where Databricks controls the machines.
- **[A View Count Is Not a Fact: Snapshot-Delta Design for Video Metrics Datasets](https://dev.to/thordata-flora/a-view-count-is-not-a-fact-snapshot-delta-design-for-video-metrics-datasets-1j9j)** — DEV. Argues scraped engagement metrics should be modeled as snapshot-deltas rather than static facts, since every capture is already stale.

## Community pulse
- A Reddit investigation into PDF table extraction failure modes found that something as small as a misplaced header can break extraction, and is cataloguing which specific layout quirks trip up which tools ([r/dataengineering](https://www.reddit.com/r/dataengineering/comments/1wm9fbk/a_misplaced_header_is_enough_to_make_pdf_table/)).
- DuckDB's Bluesky account flagged a DuckCon talk on search-first retrieval for DuckDB-powered agents, bringing full-text and semantic search to DuckLake ([DuckDB on Bluesky](https://bsky.app/profile/duckdb.org/post/3mw2xsul3f22z)).
