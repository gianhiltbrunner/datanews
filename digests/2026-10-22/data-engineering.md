# DuckDB 2.0.0 LTS "Cinnamon Teal" ships as its biggest feature release yet

DuckDB's 2.0 launch dominates an otherwise thin day for substantive data engineering writing, with a fresh benchmark already comparing it against Polars and Spark. Elsewhere, two field-tested posts on BigQuery testing and PySpark data-quality CI stand out from the usual flood of career and tutorial content.

## Top stories
- **[DuckDB 2.0.0 LTS "Cinnamon Teal"](https://duckdb.org/2026/10/21/announcing-duckdb-200)** — DuckDB. The team shipped its biggest feature release yet: a server protocol for DuckDB-as-a-service, async I/O, a first-class VARIANT type, triggers (including MERGE INTO and RETURNING support), an extensible SQL parser and an agent mode. *Why it matters:* a major LTS version from the project anchoring much of today's embedded-OLAP tooling is worth planning around, including for breaking changes in the 1.x→2.x jump.

## Worth reading
- **[DuckDB 2.0 vs Polars vs Spark on One Machine: 150M Rows Under a 4.5 GiB Cap](https://dev.to/firfircelik/duckdb-20-vs-polars-vs-spark-on-one-machine-150m-rows-under-a-45-gib-cap-h38)** — DEV. A same-day benchmark finds DuckDB 2.0 finishing every run 5–12x faster than local PySpark at 150M rows under a 1 GB memory cap, while Polars hits a wall on window dedup.
- **[What Breaks When You Migrate Petabytes: A Field Guide](https://dev.to/prajaktashende/what-breaks-when-you-migrate-petabytes-a-field-guide-4g4n)** — DEV. A Google Cloud database engineer lists the five predictable places petabyte-scale migrations break, starting with throughput math nobody does before committing to dates.
- **[Don't mock BigQuery, test on BigQuery: the rewrite of BigTesty](https://dev.to/gde/dont-mock-bigquery-test-on-bigquery-the-rewrite-of-bigtesty-62g)** — DEV. Argues that mocks and shared test datasets both fail for BigQuery SQL involving MERGE, QUALIFY and UNNEST, and walks through a rewritten tool that runs tests against real BigQuery instead.
- **[Testing PySpark Data Quality in CI: A Practical Retail Media Example](https://dev.to/rupak_kulkarni_08b45c5846/testing-pyspark-data-quality-in-ci-a-practical-retail-media-example-55a4)** — DEV. Walks through pytest checks and GitHub Actions configuration that enforce data-quality validation before a retail-media pipeline produces Gold-layer metrics.
- **[AI Changes the Data Interface, Not the Query Engine](https://www.infoq.com/articles/ai-changes-data-interface/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering)** — InfoQ. Presents a disaster-recovery analytics workflow where an AI agent generates constrained SQL or Python and DuckDB computes reproducible facts from Parquet, with signals for when an embedded engine suffices versus a managed lakehouse.

## Community pulse
- On r/dataengineering, practitioners debated [how to handle updates in fact tables](https://www.reddit.com/r/dataengineering/comments/1xbuxzd/how_should_we_handle_updates_in_fact_tables/) when source records can change after the fact and incremental loading based on a single update timestamp isn't reliable.
- Also on r/dataengineering, a post describes [testing dbt v2 and running multiple engines in a single project](https://www.reddit.com/r/dataengineering/comments/1xbt65i/i_tested_dbt_v2_and_how_to_run_multiple_engines/).
