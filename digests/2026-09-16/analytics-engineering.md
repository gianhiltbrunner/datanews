# Snowflake's external lineage goes GA, with limits worth knowing before you rely on it

dbt-core kept shipping small patches inside its new 2.0 line and Cube added a CI-focused generation command, while practitioner writing focused on semantic layer design trade-offs and keeping dbt pipelines resilient to bad source data.

## Top stories
- **[Snowflake External Lineage Is GA: The 8 Limits and 1 Trap Nobody Warns You About](https://medium.com/tech-with-abhishek/snowflake-external-lineage-is-ga-the-8-limits-and-1-trap-nobody-warns-you-about-3c807470dbb3?source=rss------dbt-5)** — Medium (Tech with Abhishek). A practitioner's read-through of the GA documentation, covering what changed since preview and the constraints that catch teams out. *Why it matters:* GA lineage features get adopted fast, and the gaps matter before you build on them.
- **[One Unified Explore in Semantic Layer Is a Performance Liability, Not a Design Virtue](https://medium.com/@dv-engineering/one-unified-explore-in-semantic-layer-is-a-performance-liability-not-a-design-virtue-57a6a3567063?source=rss------analytics_engineering-5)** — Medium. An argument against collapsing every model into one semantic-layer explore, on performance grounds. *Why it matters:* it pushes back on a common semantic-layer design default.
- **[When Bad Data Shouldn't Break Your dbt Pipeline](https://medium.com/@jan.busse/when-bad-data-shouldnt-break-your-dbt-pipeline-ddea13ed768e?source=rss------dbt-5)** — Medium. Describes a validate-before-publish pattern that falls back to a bounded last-known-good state on Snowflake. *Why it matters:* a concrete pattern for a failure mode most dbt pipelines hit eventually.

## Releases & tools
- **[dbt-core v2.0.4](https://github.com/dbt-labs/dbt/releases/tag/v2.0.4)** — the latest patch in the new 2.0 line; the prior v2.0.2 restored the bundled docs UI in pip-installed wheel builds so `dbt docs generate` works again.
- **[Cube v1.7.39](https://github.com/cube-js/cube/releases/tag/v1.7.39)** — adds a `cube dbt generate` CLI command for CI-side Cube schema generation, plus assorted rolling-window and MSSQL pushdown fixes.

## Worth reading
- **[CI/CD for dbt (Slim CI)](https://npogeant.medium.com/ci-cd-for-dbt-slim-ci-74dfa5658ccc?source=rss------dbt-5)** — on trusting production state for everything that hasn't changed rather than rebuilding it in CI.
- **[The Semantic Layer: Semantic Views, dbt Metrics, and Business Definitions](https://medium.com/dataaichronicles/the-semantic-layer-semantic-views-dbt-metrics-and-business-definitions-71b54fe640cf?source=rss------dbt-5)** — on turning a business glossary into an executable contract the query engine enforces.
