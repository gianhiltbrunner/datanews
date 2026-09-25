# dbt v2 migration prep is the one solid story on a quiet analytics engineering day

The feed skewed almost entirely toward thin Medium filler and Google News keyword matches on "semantic layer," with no Reddit, Hacker News or Bluesky discussion at all. The one substantive piece was a practical guide to migrating an existing Snowflake dbt project to dbt v2, alongside routine patch releases from Lightdash and Cube.

## Top stories
- **[From dbt Core v1 to dbt v2 on Snowflake: A Practical Migration Guide](https://medium.com/snowflake/from-dbt-core-v1-to-dbt-v2-on-snowflake-a-practical-migration-guide-4eb137573a1f?source=rss------dbt-5)** — Medium (Snowflake Engineering). dbt v2 (the "Fusion" engine) went generally available on September 16, 2026; this walks through preparing an existing Snowflake dbt project for the move, validating compatibility and handling static-analysis gaps, with the author noting the prep work mattered more than the engine swap itself. *Why it matters:* concrete guidance for teams that haven't started their own dbt v2 migration yet.

## Releases & tools
- **[2.339.1](https://github.com/lightdash/lightdash/releases/tag/2.339.1)** — Lightdash. Latest patch fixes a metric-formatting bug in chart drill-down labels, following two feature releases this week that added AI-agent MCP-server management and a compiled-SQL view for semantic-layer nodes in Composer.
- **[v1.7.45](https://github.com/cube-js/cube/releases/tag/v1.7.45)** — Cube. Latest release speeds up schema-compiler validation and YAML transpilation for large data models and deprecates the legacy `cubejs` CLI in favor of a native Cube CLI.
