# ClickHouse ships a durable layer for agent memory on an otherwise quiet day

The window was almost entirely Google News noise — Snowflake stock coverage, an unrelated "snowflake" pun cycle, and wire stories with no platform-engineering content — leaving one real technical post plus a couple of practitioner Reddit threads.

## Top stories
- **[chDB Durable Layer for agent memory](https://clickhouse.com/blog/chdb-durable-layer-for-agent-memory)** — ClickHouse Blog. A durable layer for chDB that keeps agent memory queryable locally while making its analytical state recoverable across laptops, CI jobs and short-lived sandboxes. *Why it matters:* addresses a gap for teams using embedded analytical databases to give AI agents persistent, inspectable memory rather than ephemeral state.

## Community pulse
- A Databricks Asset Bundles thread pointed out that the `on_bundle_deploy` trigger can run a job automatically right after deployment, useful for one-time post-deploy tasks like DDLs or calendar table population ([r/databricks](https://www.reddit.com/r/databricks/comments/1wrwv7k/trigger_on_bundle_deploy/)).
- A thread asking what people are building with Databricks' new Genie App Builder drew replies but little detail so far ([r/databricks](https://www.reddit.com/r/databricks/comments/1wrz2yn/genie_app_builder/)).
