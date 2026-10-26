# Razorpay's play-by-play of moving 2,500 Airflow DAGs to version 3

A thin day for headline news: the best material is two practitioner write-ups — Razorpay's migration of thousands of production DAGs to Airflow 3, and a close look at how Databricks' new Auto CDF changes where change-data-feed costs land. DuckDB got attention on two fronts, from securing a shared server to speeding up community-extension builds, and Polars shipped a release with a breaking change worth knowing about.

## Top stories
- **[How Razorpay Moved 2,500 DAGs to Airflow 3, One DAG at a Time](https://engineering.razorpay.com/how-razorpay-moved-2-500-dags-to-airflow-3-one-dag-at-a-time-71419355a07b?source=rss------data_engineering-5)** — Razorpay Engineering (Medium). Razorpay's data engineering team walks through migrating its Airflow scheduler from 2.10 to 3.3 across 2,500 production DAGs incrementally rather than in one cutover. *Why it matters:* it's a rare real-numbers account of an Airflow 3 migration at scale, useful for any team planning the same move.
- **[Auto CDF Moved the CDC Tax From Writes to Reads: Delta CDF vs Auto CDF vs Spark 4.2 CHANGES](https://dev.to/firfircelik/auto-cdf-moved-the-cdc-tax-from-writes-to-reads-delta-cdf-vs-auto-cdf-vs-spark-42-changes-9bb)** — DEV. Argues that Databricks' Auto CDF (GA since September) and Spark 4.2's new `CHANGES` SQL clause don't eliminate the cost of change-data-feed, they relocate it from the writer to the reader. *Why it matters:* a sharper framing than the "free CDC, turn it on" takes that followed Auto CDF's release.

## Releases & tools
- **[Python Polars 2.1.0](https://github.com/pola-rs/polars/releases/tag/py-2.1.0)** — disallows mixed string/numeric arithmetic in eager mode (breaking change), alongside several streaming and sort-memory performance improvements.

## Worth reading
- **[Securing a DuckDB Server in Production](https://blog.starlake.ai/securing-duckdb-server-in-production)** — catalogs eight ways a shared DuckDB server leaks or grants more than expected, from credentials readable in SQL to the CLI being misused as a daemon, with mitigations for each.
- **[Building DuckDB's Community Extensions, Faster and More Consistently](https://query.farm/blog/duckdb-community-extensions-distribution/)** — Query Farm's Haybarn rebuilds the full community-extension catalogue about 2.4x faster than the official pipeline, using a shared dependency cache and prebuilt Linux build containers.

## Community pulse
- A BI manager on r/dataengineering [asked whether AWS CDK is a reasonable substitute for dbt](https://www.reddit.com/r/dataengineering/comments/1xfp5i5/using_aws_cdk_instead_of_dbt_to_manage_and_deploy/) to manage warehouse views, after inheriting a CDK-based setup their CTO is reluctant to replace.
