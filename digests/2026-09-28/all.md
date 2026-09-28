# AWS closes an Aurora DSQL gap as Fabric Runtime 2.0 and a GovCloud migration make the rounds

A thin day across all three domains, with most feeds dominated by SEO content and unrelated wire stories rather than original engineering writing. The standouts were a database feature addition from AWS, a practitioner migration checklist for a forced runtime upgrade, a dependency-compatibility fix from Great Expectations, and a new durable-storage feature from ClickHouse.

## Top 5 across domains
- **[Data Engineering]** **[AWS Introduces Foreign Key Constraints in Aurora DSQL](https://www.infoq.com/news/2026/09/aurora-dsql-foreign-keys/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering)** — closes a gap users had explicitly called out as an adoption blocker for the serverless distributed SQL database.
- **[Data Engineering]** **[Fabric Runtime 2.0 is becoming the default. Here is what actually breaks.](https://dev.to/firfircelik/fabric-runtime-20-is-becoming-the-default-here-is-what-actually-breaks-12i9)** — a migration checklist ahead of Fabric Runtime 2.0 losing its opt-in status for new workspaces.
- **[Analytics Engineering]** **[Great Expectations 1.23.2](https://github.com/fivetran/great_expectations/releases/tag/1.23.2)** — fixes a SQLAlchemy 2.1 regression that broke GX against Snowflake, Databricks, BigQuery, Postgres and SQL Server.
- **[Data Platform Engineering]** **[chDB Durable Layer for agent memory](https://clickhouse.com/blog/chdb-durable-layer-for-agent-memory)** — makes chDB's local agent-memory state recoverable across laptops, CI and short-lived sandboxes.
- **[Analytics Engineering]** **[What Nobody Tells You About Moving Snowflake to GovCloud](https://medium.com/@kausik.kb.bhowmik/what-nobody-tells-you-about-moving-snowflake-to-govcloud-0dca8cc9d68e?source=rss------analytics_engineering-5)** — a first-hand account of what broke migrating a Snowflake account into a government cloud region.
