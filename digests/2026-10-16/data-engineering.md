# DuckDB benchmarks its v2.0-dev build on NVIDIA's new Vera CPU

A quiet news day for data engineering, with the feed dominated by SEO content and wire filler rather than hard news. The most substantive items came from DuckDB itself — a TPC-H benchmark of its in-development v2.0 build and an independent extension that adds time travel and writable branches to DuckDB files — alongside practical community writing on Spark data skew and lakehouse table formats.

## Top stories
- **[Benchmarking DuckDB v2.0-dev on NVIDIA Vera](https://duckdb.org/2026/10/16/nvidia-vera-benchmark.html)** — DuckDB Blog. The team ran the full TPC-H benchmark at scale factor 1,000 against DuckDB's in-development v2.0 build on NVIDIA's new Vera CPU. *Why it matters:* an early performance signal ahead of the v2.0 release for teams evaluating DuckDB on larger analytical workloads.
- **[DuckDB Snapshots, Time Travel and Writable Branches](https://tobilg.com/posts/differential-storage-for-duckdb/)** — Hacker News / tobilg.com. A new experimental extension, duckdb-differential, adds snapshots, time travel, writable branches, clones and restore to native DuckDB databases, sharing unchanged data through immutable storage chunks and optionally publishing versions to S3. *Why it matters:* gives DuckDB users a way to validate imports, reproduce reports against fixed inputs, and test migrations without touching the live database.

## Worth reading
- **[Your Spark Job Has 200 Executors. Why Is Only One of Them Working?](https://dev.to/analyticsdurgesh/your-spark-job-has-200-executors-why-is-only-one-of-them-working-3mj)** — a walkthrough of diagnosing data skew when one straggler task stalls a job no matter how many executors or how much memory you add.
- **[Iceberg vs Delta vs Hudi on AWS: A Practitioner's Comparison](https://medium.com/@ng.th.thuyy/iceberg-vs-delta-vs-hudi-on-aws-a-practitioners-comparison-91154316a814?source=rss------data_engineering-5)** — compares production trade-offs between the three lakehouse table formats on AWS beyond what benchmarks show.
- **[What's Inside an Iceberg Table?](https://bsky.app/profile/duckdb.org/post/3mxwxlt7ujc2a)** — DuckDB walks through the internal layers of an Iceberg table using plain SQL.

## Community pulse
- r/dataengineering discussed designing a [self-service AWS sandbox account system](https://www.reddit.com/r/dataengineering/comments/1x6lyz3/looking_for_a_selfservice_aws_sandbox_account/), with spending and time limits, locked-down IAM, and automated cleanup for safe employee experimentation.
