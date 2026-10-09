# Dell adds a semantic layer to its AI Data Platform as coverage debates whether agents even use them

Dell's semantic-layer push for AI agents dominated wire coverage, while commentary pieces questioned whether agents actually read semantic layers at all. On the tooling side, Lightdash, Cube and Great Expectations all shipped feature releases.

## Top stories
- **[Dell expands AI Data Platform with semantic layer for agents](https://news.google.com/rss/articles/CBMiigFBVV95cUxPclNnRXFYUXdDajc4M0s1MzhYcC1jZEk1a2dfc25DQTdldEhackZKUHIwNzBfSEZSTXFUdkZBbVNtUU03Ung2RWEzUzdxWHB4UFNpZERpNXZ5bFZvdUMxTllFQUtrdnV6ei1TMVRjMV9zVnFhT3NHQUNkMFlOSHpDZmlKdUhQaGxFdEE?oc=5)** — Google News (multiple outlets). Dell is rolling out a semantic layer, cuDF GPU acceleration, a knowledge graph and governed multi-tenant PowerScale clusters across its AI Data Platform. *Why it matters:* a major infrastructure vendor is betting that agentic AI workloads need a governed semantic layer, not just raw warehouse access.
- **[Few AI agents rely on semantic layers](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPWjllM2V1NTFFNFNlem8xNGZlRy1nVWxFdFc3YTlRXzRyYThXSVY3LWNjUzNVb21RMDVYZGlDdElXV2U2VFFfU0FSSExpdDFuS0JUT3Q2NlY4SlZKb0NqdV9pbFc1YU45UnRrbXE2NTh0ZXFoWjJ5VzhWX2NUYVdRYVpnUVhZNk9fcEJkM2NNYnpSd1dobzBVSXhadzAxcVdFVVdoMVBjNWYwRFZBYm9SekZrSkZ1aXpIUWRZeDZmNF94MGM2enZpR2VpUkFGYVlUS2c?oc=5)** — Google News (VentureBeat). Coverage argues that despite vendor investment in semantic layers, most production AI agents still bypass them and query data directly. *Why it matters:* a direct counterpoint to the Dell-style semantic-layer push, and a live debate for anyone building the metrics layer AI agents are supposed to use.
- **[The SQL Looked Right. The Number Wasn't.](https://medium.com/@seanlukeholland/the-sql-looked-right-the-number-wasnt-06f92cbd6ec2?source=rss------analytics_engineering-5)** — Medium. Four modelling decisions from building a SaaS retention model in dbt, and why they matter more now that AI is writing some of the queries. *Why it matters:* a concrete case for stricter modelling discipline as LLMs start generating SQL against these models.

## Releases & tools
- **[2.501.1](https://github.com/lightdash/lightdash/releases/tag/2.501.1)** — Lightdash's latest release adds dashboard filter controls (create, edit and apply filters per tile or tab) and runs BigQuery AI agents under per-warehouse service-account identity rules.
- **[v1.8.2](https://github.com/cube-js/cube/releases/tag/v1.8.2)** — Cube's newest release fixes a cyclic join-tree infinite loop and several query-planning bugs, plus performance improvements to rollup and UNION ALL planning.
- **[1.24.0](https://github.com/fivetran/great_expectations/releases/tag/1.24.0)** — Great Expectations now supports Python 3.14, with the clickhouse and teradata extras not yet available on that version.

## Worth reading
- **[Data Quality Pipelines with dbt: Quarantine Bad Rows Before They Reach Analytics](https://medium.com/@anusarijal1919/data-quality-pipelines-with-dbt-quarantine-bad-rows-before-they-reach-analytics-by-anusha-rijal-b34c05c65c53?source=rss------analytics_engineering-5)** — A pattern for routing rows that fail dbt tests into a quarantine table instead of just failing the run.
- **[What's New in Wire 4.x: Multi-Agent Development, dbt Charts, Agents Schema & More](https://blog.rittmananalytics.com/whats-new-in-wire-4-x-multi-agent-development-dbt-charts-agents-schema-more-7d07acb467a7?source=rss------dbt-5)** — Rittman Analytics' Claude Code/Gemini CLI plugin for analytics engineering delivery picks up multi-agent development support and dbt chart generation in version 4.1.0.

## Community pulse
- On r/analyticsengineering, a thread works through [BigQuery's pricing models](https://www.reddit.com/r/analyticsengineering/comments/1x0trse/making_sense_of_bigquery_pricing_models_ondemand/) — on-demand, capacity and editions — for 2026.
