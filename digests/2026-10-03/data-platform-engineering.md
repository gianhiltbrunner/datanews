# Spanner Adds Native Transactional Queues as Snowflake Guides Iceberg Migration

Google Cloud gave Spanner native transactional messaging aimed at agentic workloads, while Snowflake published the first half of a guide for moving native tables onto Iceberg. ClickHouse detailed the storage-engineering choices behind its managed Postgres backups, and AWS and Azure both shipped incremental reliability and cost features for their managed databases.

## Top stories
- **[Announcing Spanner queues: Transactional messaging for agentic workloads and beyond](https://cloud.google.com/blog/products/databases/spanner-queues-provide-native-transactional-messaging/)** — Google Cloud. Spanner queues reach general availability, letting applications dispatch asynchronous messages from the same transaction that updates operational state, instead of running a separate message queue with its own commit point. *Why it matters:* removes a common source of inconsistency in systems — including AI agents — that mix a database with an external queue.
- **[Converting Snowflake Native Tables to Iceberg — Part 1](https://medium.com/snowflake/converting-snowflake-native-tables-to-iceberg-part-1-603fdb0fdcd1?source=rss----34b6daafc07---4)** — Snowflake Engineering (Medium). The first of a two-part guide covering why and when to convert native tables to Iceberg and the decisions involved, ahead of a second part on execution and cutover. *Why it matters:* a vendor-authored playbook for a migration many lakehouse teams are already weighing.
- **[What is direct I/O, and why does ClickHouse Managed Postgres use it for backups?](https://clickhouse.com/blog/direct-io-managed-postgres-backups)** — ClickHouse Blog. Explains why ClickHouse Managed Postgres uses direct I/O and stripe-sized reads for backups, to keep them fast without evicting the page cache or hurting query latency. *Why it matters:* a concrete storage-engineering tradeoff relevant to anyone running managed Postgres backups at scale.

## Releases & tools
- **[Amazon Aurora DSQL now supports partial indexes](https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-dsql-partial-indexes/)** — AWS. Indexes can now cover just a filtered subset of a table (e.g. open orders among years of history), keeping the index small as the table grows and cutting storage cost.
- **[Public Preview: Major version upgrades (MVU) for Azure Database for PostgreSQL elastic clusters](https://azure.microsoft.com/updates?id=571504)** — Azure. Elastic clusters can now be upgraded in place to a newer PostgreSQL major version without provisioning a replacement cluster or migrating data.

## Worth reading
- **[How I Would Design a Modern Enterprise Data Platform](https://oswinrh.medium.com/how-i-would-design-a-modern-enterprise-data-platform-ad79225edb36?source=rss------data_platform-5)** — Medium. A personal take on architecting a data platform that's scalable today and flexible enough for AI workloads tomorrow.
