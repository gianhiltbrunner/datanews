# Who should own incremental logic: dbt authors, or the engine itself?

A quiet news day in analytics engineering was carried by two write-ups questioning how incremental transformation logic gets written — one pointing to new research on auto-generating it, the other extending dbt snapshots to handle late-arriving batched data. Lightdash shipped a notable feature for resolving cross-source dbt refs without dbt-loom.

## Top stories
- **[Who writes your is_incremental() block now?](https://medium.com/@shaantanutripathi/who-writes-your-is-incremental-block-now-87aa5653b014?source=rss------dbt-5)** — Medium. Written from the perspective of an engineer who still hand-writes MERGE logic, the piece reacts to the Enzyme paper (SIGMOD 2026) on automating incremental transformation logic. *Why it matters:* if incremental logic can be generated reliably, it changes what dbt authors spend their time hand-maintaining.
- **[dbt Snapshots Can't Handle Late Data. So We Built One That Can](https://blog.dataengineerthings.org/dbt-snapshots-cant-handle-late-data-so-we-built-one-that-can-ef107cc9e02e?source=rss------dbt-5)** — Medium (Data Engineer Things). Extends dbt's snapshot pattern to correctly track history for data that arrives in late batches, not just in real time. *Why it matters:* late-arriving data is a common gap in standard dbt snapshot recipes.

## Releases & tools
- **[2.603.0](https://github.com/lightdash/lightdash/releases/tag/2.603.0)** — Lightdash's latest release lets it resolve cross-source dbt refs without requiring dbt-loom.

## Worth reading
- **[What's new in dbt v2 / dbt Fusion vs. dbt core? Everything explained](https://medium.com/@hugolu87/whats-new-in-dbt-v2-dbt-fusion-vs-dbt-core-everything-explained-7c41d9f6984d?source=rss------dbt-5)** — A round-up of the differences between dbt Fusion and dbt Core.
- **[Snowflake-as-Code: Centralized Object Management with Git and Schemachange Migrations](https://medium.com/@a.shchepetnov/snowflake-as-code-deploying-dbt-cortex-agents-and-streamlit-3caf0f12fc87?source=rss------dbt-5)** — A deployment guide for unifying dbt, Cortex Agents, Semantic Views and Streamlit under Git-based Snowflake object management.
