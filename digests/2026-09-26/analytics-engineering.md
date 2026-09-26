# dbt Labs publishes a practical migration guide from dbt Core v1 to v2 on Snowflake

A quieter 72-hour window dominated by Medium tutorials and Google News noise, but dbt's v1-to-v2 transition and Databricks' spreadsheet acquisition for Genie stood out as the pieces worth a practitioner's attention. Cube shipped several releases, including a notable CLI deprecation.

## Top stories
- **[From dbt Core v1 to dbt v2 on Snowflake: A Practical Migration Guide](https://medium.com/snowflake/from-dbt-core-v1-to-dbt-v2-on-snowflake-a-practical-migration-guide-4eb137573a1f?source=rss------dbt-5)** — Snowflake Builders Blog (Medium). Walks through preparing an existing Snowflake dbt project for dbt v2, validating compatibility, and handling gaps in static analysis. *Why it matters:* dbt v2 is a major version change, and this is a concrete checklist for teams planning the jump.
- **[Databricks acquires Row Zero, gives Genie a spreadsheet](https://news.google.com/rss/articles/CBMiowFBVV95cUxQR2R6YjVkVmxSTUdwVl9XZ0tlaklUTjZSRzlWaEc5VGhwZnROSF8xN2ozYXN3cUk3ZUwzbGdIUGM4TXNVUF9kb3BHUXlvYldVY1RzZXY3bk5GTVpVQUQ1bDZkTzFMbnNQWjVobXVjaUNLSFZXQlB3R1pFSHRncEd5ZVY0M1dNYUJpMVBwVy1DYjlUSEdneXdISDhoQ1FTYnM1MzZr?oc=5)** — Google News (Techzine Global). Databricks is acquiring spreadsheet startup Row Zero, adding a spreadsheet interface to its Genie AI assistant. *Why it matters:* another sign that BI and spreadsheet-style analysis are converging with AI agents rather than staying separate tools.
- **[Your dbt Job Finished on Time. Did Every Model Need to Run?](https://medium.com/@arienugroho650/your-dbt-job-finished-on-time-did-every-model-need-to-run-03cbb5f99bb0?source=rss------dbt-5)** — Medium. Uses dbt's state-comparison feature to ask when an existing model result is still good enough to reuse rather than rerun. *Why it matters:* a low-effort lever for cutting warehouse compute spend that's easy to overlook.

## Releases & tools
- **[v1.7.46](https://github.com/cube-js/cube/releases/tag/v1.7.46)** — Cube. Latest of several releases this window; v1.7.45 deprecated the `cubejs` CLI in favor of the native Cube CLI and sped up schema validation for large data models.

## Worth reading
- **[Building a Workday HR Pipeline from Scratch](https://medium.com/@praveen.ch2000/building-a-workday-hr-pipeline-from-scratch-0372e517c3de?source=rss------dbt-5)** — Medium. Builds a Mock API → Airflow → Snowflake → dbt pipeline with real incremental loads and SCD2 history.
