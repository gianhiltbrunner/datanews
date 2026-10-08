# DuckDB ships view-only catalog files as its DuckLake lakehouse format draws fresh attention

The clearest engineering news in the window is DuckDB-shaped: a new view-only mode lets a database file hold nothing but view definitions over external Parquet, and its DuckLake lakehouse format resurfaced on Hacker News with real engagement. Beyond that, the feed is dominated by thin Medium/DEV tutorials and repeated wire items, though a candid 400 TB Postgres-to-Iceberg migration write-up and a breaking change in dlt stand out.

## Top stories
- **[A DuckDB Database with No Data in It](https://duckdb.org/2026/10/07/view-only-mode)** — DuckDB Blog / DuckDB (Bluesky) / Hacker News. A new view-only mode lets a `.duckdb` file store nothing but view definitions pointing at Parquet on object storage, so the catalog file stays a few hundred KB regardless of how much data it describes. *Why it matters:* it turns a DuckDB file into a tiny, shareable pointer to a dataset rather than a copy of it, useful for distributing read-only access to large external data.
- **[DuckDB Ducklake](https://github.com/duckdb/ducklake)** — Hacker News (42 points). The repo for DuckDB Labs' open lakehouse table format drew renewed discussion. *Why it matters:* DuckLake competes with Iceberg and Delta Lake as a simpler, SQL-native way to add lakehouse semantics on top of plain files.

## Releases & tools
- **[dlt 1.31.0](https://github.com/dlt-hub/dlt/releases/tag/1.31.0)** — removes the unofficial pendulum helper functions from `dlt.common.time` with no compatibility aliases and now requires `pendulum>=3`; pipelines importing those helpers directly need updating before upgrading.

## Worth reading
- **[TRM Labs' 400 TB Migration: Lessons for Data Engineer Interviews](https://dev.to/datadriven/trm-labs-400-tb-migration-lessons-for-data-engineer-interviews-2165)** — DEV. Revisits TRM Labs' write-up on moving roughly 400 TB of Postgres onto StarRocks on Apache Iceberg, framed around what a credible migration story covers: how the plan was validated, how it turned out wrong, and what changed as a result.
- **[Survey Finds AI-Generated Code Increases Debugging and Failure Rates and Creates a Comprehension Gap](https://www.infoq.com/news/2026/10/survey-complex-codebases-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering)** — InfoQ. A Coleman Parkes survey for Undo finds AI coding agents have accelerated code generation but shifted the bottleneck to debugging, comprehension and maintenance.
- **[Fivetran vs Estuary for Real-Time ETL](https://dev.to/jaume_bogu_c05b19569765/fivetran-vs-estuary-for-real-time-etl-4ecj)** — DEV. Argues the real split is log-based CDC in seconds (Estuary) versus scheduled ELT with a one-minute floor (Fivetran), and that "real-time" means something different on every vendor's pricing page.

## Community pulse
- An r/dataengineering thread on making the dbt dev cycle less painful described a stg → int → dm layering across three GCP environments where even a one-column KPI change means a full commit-CI-wait loop per environment, prompting other practitioners to compare notes on shortening that cycle ([discussion](https://www.reddit.com/r/dataengineering/comments/1wzvd8a/how_to_actually_make_the_development_cycle_easier/)).
