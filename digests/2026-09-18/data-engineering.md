# A quiet day for pipelines, but Airflow patches a DAG-enumeration flaw

Data engineering feeds were dominated by AI-agent think-pieces and vendor tutorials, but two solid practitioner write-ups stood out: a testing war story on why untested feature claims quietly rot, and a survey of the Iceberg maintenance tooling landscape. Apache Airflow 3.3.2 closed a minor information-disclosure gap in its backfill API, and DuckDB got a moment in the spotlight ahead of a dbt Summit talk.

## Top stories
- **[A test you can't run is a test you don't have](https://dev.to/ashg2099/a-test-you-cant-run-is-a-test-you-dont-have-15dk)** — DEV. When extending the DuckDB-only data-quality tool Upstrace to a second warehouse, the author picked Postgres over Snowflake specifically because a Snowflake trial account would expire, leaving an untested (and eventually false) compatibility claim in the code; they wrapped the new Postgres driver to match DuckDB's existing API rather than retrofitting every call site. *Why it matters:* a concrete argument that a test only counts as coverage if it keeps running in CI, not just once at write time.
- **[Apache Iceberg Maintenance Tools: From Spark Procedures to Autonomous Control Planes](https://dev.to/jonisar/apache-iceberg-maintenance-tools-from-spark-procedures-to-autonomous-control-planes-lbi)** — DEV. A survey of how Iceberg table maintenance — compaction, snapshot expiry, orphan-file cleanup and dangling delete-record removal — has moved from manual Spark procedures toward autonomous, engine-agnostic control planes as tables accumulate thousands of small files and bloated metadata in production. *Why it matters:* maintenance debt is the quiet tax on every growing lakehouse, and the tooling for paying it down is maturing fast.

## Releases & tools
- **[Apache Airflow 3.3.2](https://github.com/apache/airflow/releases/tag/3.3.2)** — patches the backfill endpoints (`GET /backfills/{id}` plus pause/unpause/cancel) so they no longer let a caller enumerate which backfill IDs exist across DAGs they aren't authorized to see.

## Worth reading
- **[The Lakehouse Wasn't Built for AI Agents](https://news.google.com/rss/articles/CBMib0FVX3lxTE50STd1M0pVN0pTRlpzY0F2aWhvZUhvbG9xek5CT2hKbThmYmh1UnF0Mjg3akFreE5pcmxxZVl6eUlCRmJYOUY0Mk5SZkNFMXlYYU5jWUJlNGhHMlcxQThSVXdKV0dvbDBPcXVWRnQ5bw?oc=5)** — HackerNoon, via Google News. Argues that lakehouse table formats and query engines were designed around batch analytics access patterns, not the high-frequency, small-read patterns of AI agents.

## Community pulse
- On DuckDB's Bluesky, a reminder that [Hannes Mühleisen is speaking at dbt Summit in Las Vegas](https://bsky.app/profile/duckdb.org/post/3mvqtv6qrek2i) on running "dbt without the warehouse" using DuckDB end to end.
- On r/dataengineering, a [thread on migrating 150 dataframes and 200 poorly-documented IBM DataStage jobs to Python/Spark](https://www.reddit.com/r/dataengineering/comments/1wj8l0g/datastage_to_pythonspark/) captured the familiar pain of inheriting undocumented legacy pipelines, and a separate [thread on JIRA API ingestion](https://www.reddit.com/r/dataengineering/comments/1wiv4fs/api_ingestion_strategies/) debated whether SCD2 is overkill for a straightforward bronze/silver load.
