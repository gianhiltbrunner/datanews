# Recovering corrupted Iceberg partitions without a full table scan

Away from a heavy dose of Snowflake and Databricks stock-market chatter, the platform-engineering feeds carried two solid pieces of practitioner engineering: an incident write-up on recovering corrupted Iceberg partitions, and a ClickHouse post on running Postgres on NVMe alongside analytical workloads. Modern Data 101 published a longer architectural essay on dependency graphs for agentic systems, Apache Iceberg cut a new release candidate, and DataHub backported a batch of CVE fixes.

## Top stories
- **[How I Fixed Corrupted Iceberg Partition Files Without Full Table Scans or Data Loss](https://medium.com/towards-data-engineering/how-i-fixed-corrupted-iceberg-partition-files-without-full-table-scans-or-data-loss-f1a328cef12f?source=rss------data_platform-5)** — Towards Data Engineering (Medium). Diagnoses missing Parquet magic bytes causing failed split readers in production Iceberg tables, and lays out a 4-step recovery playbook that avoids rescanning the whole table. *Why it matters:* it's a concrete recovery path for a failure mode that otherwise looks like it demands a costly full rebuild.
- **[Postgres on NVMe: performance and the convergence of transactions and analytics](https://clickhouse.com/blog/postgres-on-nvme)** — ClickHouse Blog. Examines how local NVMe storage changes Postgres transaction performance, and where ClickHouse still remains necessary for fast analytics as workloads scale. *Why it matters:* it's a data point in the ongoing debate over how far a single Postgres instance can go before you need a separate analytical engine.
- **[The Unified Dependency Graph: Stop Agentic AI From Outrunning Its Own Architecture](https://moderndata101.substack.com/p/the-unified-dependency-graph)** — Modern Data 101. Uses the Stoic distinction between bodies and "subsistent" entities to argue infrastructure needs an explicit dependency graph for agentic AI systems to keep pace with their own state. *Why it matters:* it's an argument for treating dependency tracking as first-class infrastructure before agentic AI outpaces platform teams' ability to govern it.

## Releases & tools
- **[v1.6.0.3rc1](https://github.com/datahub-project/datahub/releases/tag/v1.6.0.3rc1)** — DataHub releases. Backports a batch of CVE and security fixes to the v1.6.0 LTS line, including a mariadb-java-client CVE, Jackson/Parquet/Spring/Kafka dependency bumps, and authorization fixes for asset settings and form assignment.
- **[apache-iceberg-1.12.0-rc1](https://github.com/apache/iceberg/releases/tag/apache-iceberg-1.12.0-rc1)** — Apache Iceberg releases. First release candidate for Iceberg 1.12.0.

## Worth reading
- **[Migrate SQL Server multi-result-set procedures to PostgreSQL](https://aws.amazon.com/blogs/database/migrate-sql-server-multi-result-set-procedures-to-postgresql/)** — AWS Database Blog. Compares session-scoped temporary tables and JSON aggregation as PostgreSQL-native replacements for SQL Server's multi-result-set stored procedures.
- **[Maximizing Apache Spark availability: Mitigating compute stockouts with flexible VMs and other best practices](https://cloud.google.com/blog/products/data-analytics/maximize-apache-spark-availability-with-flexible-vms/)** — Google Cloud — Data Analytics. Recommends flexible VMs as a way to keep Spark pipelines running through regional or zonal compute stockouts driven by AI-driven demand.

## Community pulse
- Simon Willison shared notes on "Jev" and a new category of "system one" decision models, prompting discussion of what counts as a decision model versus a traditional one ([Bluesky](https://bsky.app/profile/simonwillison.net/post/3mw2tsop42c2u)).
