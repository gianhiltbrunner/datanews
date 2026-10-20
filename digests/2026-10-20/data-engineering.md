# ClickHouse merge engines can quietly change what your SELECT returns

A quiet day dominated by SEO tutorials and career chatter, but two solid technical write-ups stood out: a dive into how ClickHouse's merge-aware table engines alter query results between merges, and a reproducible fix that cut DuckDB-WASM extension loading from 6.8 to 2.3 seconds.

## Top stories
- **[When ClickHouse merges change your query results](https://dev.to/maksim-gr/when-clickhouse-merges-change-your-query-results-5d99)** — DEV. Explains why `SummingMergeTree`, `AggregatingMergeTree` and `CollapsingMergeTree` can return different results for the same query depending on how many background merges have run, since a merge can sum, collapse or remove rows rather than just reorganize storage. *Why it matters:* teams relying on these engines for dedup or rollups can get silently inconsistent reads without realizing merges are the cause.
- **[DuckDB-WASM startup: from 6.8 to 2.3 seconds with Haybarn-WASM](https://query.farm/blog/duckdb-wasm-startup-time/)** — Hacker News / Query.Farm. Haybarn-WASM, a drop-in DuckDB-WASM fork, cut the time to load six extensions by making Emscripten's linking setup lazy and prefetching, hashing and compiling extensions in parallel with the browser's native WebCrypto instead of in-engine WASM SHA-256. *Why it matters:* a concrete, measured fix for one of the main complaints about using DuckDB-WASM in browser-based data tools.

## Worth reading
- **[Lakeflow Connect vs. Custom Spark Ingestion: Choosing Your Data Pipeline](https://dev.to/aniketsoni/lakeflow-connect-vs-custom-spark-ingestion-choosing-your-data-pipeline-f75)** — Walks through what a hand-rolled Spark Structured Streaming ingestion job has to manage itself (schema evolution, rate limits, monitoring) versus using Databricks' managed Lakeflow Connect.
- **[Article: From Microservices to Agents: the Next Evolution of Distributed Systems](https://www.infoq.com/articles/distributed-systems-microservices-agentic-ai/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering)** — Argues that agentic AI systems shift the unit of decomposition from services to decisions, raising new observability and reliability demands on the data and platform layers underneath.
- **[The Five Camps of Data Modeling (and Which One You're Stuck In)](https://bsky.app/profile/rmoff.net/post/3myagmpxxeu2w)** — Robin Moffatt shared Joe Reis's framing of data modelling practitioners into five distinct camps.

## Community pulse
- On r/dataengineering, someone built [git-like diffing for DuckLake tables](https://www.reddit.com/r/dataengineering/comments/1xa581i/gitlike_diffing_for_ducklake_tables/), letting users browse snapshots and see row- and cell-level differences on import.
- Also on r/dataengineering, a thread debated [using pg_cron to trigger batch extracts](https://www.reddit.com/r/dataengineering/comments/1x9y9pe/pg_cron_to_trigger_a_batch_extract/) directly from Postgres, weighing the convenience against mixing operational scheduling into a database meant only for activity data.
