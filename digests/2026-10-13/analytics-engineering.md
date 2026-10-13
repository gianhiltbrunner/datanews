# Cube ships a SQL-injection fix and new refresh-timer control in v1.8.5

A slow window dominated by vendor press releases about "AI-ready" warehouses, but a practitioner's postmortem of a Snowflake/dbt/Airflow build and a piece on semantic layers for AI agents stood out, alongside a security fix in Cube's query layer.

## Top stories
- **[I built an S3, Snowflake, dbt and Airflow pipeline. Here is what broke, and why.](https://medium.com/@kracshan2000/i-built-an-s3-snowflake-dbt-and-airflow-pipeline-here-is-what-broke-and-why-a5575175a888?source=rss------dbt-5)** — Medium. A data engineer with a Microsoft Fabric/PySpark background documents what failed while learning the AWS/Snowflake/dbt/Airflow stack. *Why it matters:* a candid account of the stack's rough edges from someone crossing over from a different ecosystem.
- **[Semantic Layers (Part 2): Building One Your AI Agents Can Use](https://yasharma06.medium.com/semantic-layers-part-2-building-one-your-ai-agents-can-use-ca44d04e7628?source=rss------dbt-5)** — Medium. The post walks through going from YAML metric definitions to an AI agent that answers a question like "what was our revenue?" with the same number as Finance. *Why it matters:* semantic layers are increasingly being built with AI-agent consumers in mind, not just BI tools.

## Releases & tools
- **[Cube v1.8.5](https://github.com/cube-js/cube/releases/tag/v1.8.5)** — The newest release follows v1.8.4, which guarded cubesql's member-expression SQL evaluation against JS injection; v1.8.5 adds `CUBEJS_SCHEDULED_REFRESH_TIMER_INTERVAL_ONLY` so a numeric `scheduledRefreshTimer` doesn't also enable the refresh scheduler, plus several cubesql query-planning fixes.

## Worth reading
- **[Automating Snowflake-to-BigQuery dbt Migrations with AI Skills](https://medium.com/google-cloud/automating-snowflake-to-bigquery-dbt-migrations-with-ai-skills-698586704570?source=rss------dbt-5)** — Google Cloud. A look at using AI-driven "skills" to help automate the non-trivial work of migrating a mature dbt-based warehouse from Snowflake to BigQuery.
- **[dbt in Production: From SQL Transformations to Reliable Data Platforms](https://blog.stackademic.com/dbt-in-production-from-sql-transformations-to-reliable-data-platforms-417361e31ddc?source=rss------dbt-5)** — Stackademic. Argues that writing dbt SQL models is the easy part, and that the real engineering work is building a reliable transformation system around them.

## Community pulse
- A low-key [Show HN: KV-CLI](https://github.com/kovallent/kv-cli) introduces a fast, local static analysis tool for dbt and other pipeline code written in Rust.
