# Iceberg's demo-to-production gap dominates a quiet data engineering day

Today's feed was thin on substacks and releases, and heavy on SEO-driven Medium/DEV filler and Google News wire noise (funding rounds, vendor launches, keyword-matched non-stories). The pieces that stood out were practitioner explainers on lakehouse formats and DuckDB's expanding footprint, plus DuckDB's continued push into the dbt ecosystem.

## Top stories
- **[Iceberg Is Easy to Demo. The Maintenance Bill Arrives Later.](https://dev.to/andrew_tan_layline/iceberg-is-easy-to-demo-the-maintenance-bill-arrives-later-fgn)** — DEV. Argues that Iceberg's demo moment (time travel, schema evolution) hides the real cost: compaction, retention, multi-catalog sprawl and keeping batch/streaming paths consistent once the table is in production. *Why it matters:* a counterweight to lakehouse hype that's useful when scoping the operational cost of adopting Iceberg.
- **[What a Delta table actually is: Parquet files plus a transaction log](https://dev.to/dino_david_c5d8f55f119b7f/what-a-delta-table-actually-is-parquet-files-plus-a-transaction-log-325b)** — DEV. Walks through Delta Lake from first principles — a directory of plain Parquet files plus a JSON transaction log — showing how ACID guarantees, time travel and schema enforcement all fall out of that one mechanism. *Why it matters:* a clear mental model for anyone debugging or explaining Delta Lake behavior rather than treating it as a black box.
- **[Can DuckDB be your SaaS product's warehouse? Where the ceiling actually is](https://dev.to/mohammed_arshadansari_f2/can-duckdb-be-your-saas-products-warehouse-where-the-ceiling-actually-is-76n)** — DEV. Splits "small SaaS analytics" into three distinct workloads — internal analytics, customer-facing dashboards and embedded multi-tenant analytics — and argues DuckDB comfortably covers the first two well past the point most teams expect. *Why it matters:* a concrete framework for deciding when to reach for Snowflake/BigQuery versus staying on DuckDB.

## Releases & tools
- **[DuckDB Now Ships inside dbt v2](https://bsky.app/profile/duckdb.org/post/3mwa236zmjc23)** — DuckDB (Bluesky). A new blog post walks through setting up dbt v2 with DuckLake and Iceberg catalogs, querying dbt's Parquet metadata with DuckDB, and migrating existing projects to v2.

## Worth reading
- **[Choosing an Event Bus: Kafka vs Kinesis vs Redpanda](https://dev.to/beefedai/choosing-an-event-bus-kafka-vs-kinesis-vs-redpanda-12l7)** — DEV. Compares the three on throughput, latency, exactly-once guarantees and operational complexity for real-time pipeline use cases.
- **[Call an API from Every Row in DuckDB, Without the Loop](https://query.farm/blog/call-an-api-from-every-row-in-duckdb/)** — Hacker News. A technique for issuing per-row API calls from DuckDB SQL without a manual loop.
- **[Beyond Kubernetes at Modal: How to Scale 1 Million Concurrent Sandboxes in Seconds](https://www.infoq.com/news/2026/09/modal-scaling-sandboxes/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering)** — InfoQ. Modal staff engineers describe rebuilding their sandbox infrastructure to support millions of concurrent sandboxes and tens of thousands of creations per second.

## Community pulse
- A recurring r/dataengineering thread argues AI tools handle ETL scaffolding fine but consistently struggle at rational data modeling, especially in dbt/SQL, with several commenters saying they now write the model themselves and use AI only for review ([r/dataengineering](https://www.reddit.com/r/dataengineering/comments/1woljes/does_ai_struggle_at_data_modeling/)).
- A team running a 7TB SQL Server instance (one 2.5TB database) is seeing high read/write latency for the past two weeks and is asking r/dataengineering for diagnosis approaches ([r/dataengineering](https://www.reddit.com/r/dataengineering/comments/1wo69gd/slow_reads_and_writes/)).
