# dbt Ships a v2 Migration Guide as dbt Charts Brings Dashboards Into Git

A practical first guide to migrating from dbt Core v1 onto the Rust-based dbt v2 (Fusion) started circulating, alongside a look at dbt Charts, which puts dashboards under Git, CI/CD and lineage tracking. Cube shipped several semantic-layer fixes worth knowing about if you're running access policies or multi-tenant deployments.

## Top stories
- **[How to migrate from dbt Core™ v1 to dbt™ v2?](https://medium.com/paradime-labs/how-to-migrate-from-dbt-core-v1-to-dbt-v2-4d8264c03440?source=rss------dbt-5)** — Medium (Paradime). A first practical guide for teams moving from dbt Core v1 onto dbt v2/Fusion, the Rust rewrite that ships as a self-contained binary and connects via ADBC. *Why it matters:* teams now have a concrete migration path instead of waiting on scattered release notes.
- **[dbt Charts: What Happens When Dashboards Become Code](https://medium.com/@sendoamoronta/dbt-charts-what-happens-when-dashboards-become-code-6f39e691ad26?source=rss------dbt-5)** — Medium. A look at dbt Charts, which brings dashboards into Git, CI/CD, lineage and impact analysis alongside the rest of the dbt project. *Why it matters:* another sign of BI artifacts being pulled into the same version-controlled workflow as transformation code.

## Releases & tools
- **[v1.7.50](https://github.com/cube-js/cube/releases/tag/v1.7.50)** — Cube. The 1.7.48–1.7.50 run of releases adds multi-tenant schema-compiler caching (`CUBEJS_COMPILER_MULTI_TENANT_SHARING`) and now requires explicit `includes` or `excludes` on `accessPolicy` member levels — worth checking if you rely on Cube's row/field-level access control.

## Worth reading
- **[dbt Materializations: How to Choose Between View, Table, and Materialized View — [dbt Series #8]](https://levelup.gitconnected.com/dbt-materializations-how-to-choose-between-view-table-and-materialized-view-dbt-series-8-b1fdb9b535fe?source=rss------dbt-5)** — Medium (Level Up Coding). A cost-and-freshness framework for picking between dbt's view, table and materialized-view materializations.
- **[MIN_BY and MAX_BY in Snowflake: One Line Instead of a Window Function](https://medium.com/@karthikrajashekaran/min-by-and-max-by-in-snowflake-one-line-instead-of-a-window-function-93fb96c5ba92?source=rss------analytics_engineering-5)** — Medium. A practical look at replacing `QUALIFY ROW_NUMBER()` patterns with `MIN_BY`/`MAX_BY`, including the NULL-handling and tie-breaking gotchas.
