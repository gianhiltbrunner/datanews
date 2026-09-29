# DuckDB extensions bring plain-English filtering to SQL via the new "Jev" model

A quiet day buried under SEO tutorials, certification ads and career-anxiety threads, but a few real signals surfaced: DuckDB's community is already building natural-language row filters on a new typed-answer model, Databricks widened lakehouse support for multimodal files, and one team open-sourced a cross-tool pipeline-failure digest. Splink also shipped a major version for billion-row record linkage.

## Top stories
- **[Jev and DuckDB: Plain-English Conditions in SQL](https://duckdb.org/2026/09/29/jev.html)** — DuckDB Blog. TypeSafe AI released Jev, a model that returns typed answers instead of text, on September 15; within ten days, community extensions let you filter, classify and score DuckDB rows with plain-English conditions. *Why it matters:* brings natural-language predicates straight into the SQL layer instead of a separate AI pipeline step.
- **[From Podcast Video to Searchable Insight with Databricks FILE data type](https://dataengineeringcentral.substack.com/p/from-podcast-video-to-searchable)** — Data Engineering Central. Databricks' new FILE type brings unstructured multimodal assets — video, audio and similar — into the Lakehouse with the same ease as tabular data. *Why it matters:* lakehouse platforms are extending native support for the multimodal data that agentic and search workloads increasingly need.
- **[Project Sentinel: One Morning Digest for Every Failure in Our Data Stack](https://dev.to/gentjan_likaj/project-sentinel-one-morning-digest-for-every-failure-in-our-data-stack-2i73)** — DEV. Collects health metadata from Airflow, Glue, dbt and Tableau into S3, serves it through a thin API, and has an AI agent write a daily report. *Why it matters:* a concrete pattern for unifying pipeline observability that's normally scattered across four separate tools.

## Releases & tools
- **[DuckDB v1.5.6 Bugfix Release](https://github.com/duckdb/duckdb/releases/tag/v1.5.6)** — the sixth patch release in the 1.5 line, shipping bugfixes, performance improvements and security patches.
- **[Splink 5 – Open-source probabilistic record linkage at billion-row scale](https://www.reddit.com/r/dataengineering/comments/1wt2g6q/splink_5_opensource_probabilistic_record_linkage/)** — a major version bump for the open-source record-linkage library, announced by its maintainer.

## Worth reading
- **[Keep schema errors next to the rows that caused them](https://dev.to/nimbliquestudio/keep-schema-errors-next-to-the-rows-that-caused-them-153g)** — DEV. Three invariants for an auditable CSV-to-JSON normalization step, so a pipeline that "looks healthy" stops silently dropping inconvenient rows.
- **[North Star KPI Tests](https://dev.to/gentjan_likaj/north-star-kpi-tests-4h4c)** — DEV. Argues a saved KPI total plus a simpler reference calculation catches reporting errors — like double-counted leads — that a full historical rebuild can hide.
- **[The Real Data Behind the Data Engineering Hiring Panic](https://dev.to/datadriven/the-real-data-behind-the-data-engineering-hiring-panic-3dhh)** — DEV. Traces a viral "tech lost 150K jobs, data engineering grew 414%" graphic back to no findable dataset, then checks what Stanford payroll research, LinkedIn and the BLS actually show.

## Community pulse
- Several r/dataengineering threads worried aloud about AI hollowing out entry-level roles, including one asking [whether the field is still a sustainable career path for a junior](https://www.reddit.com/r/dataengineering/comments/1wskzeo/is_data_engineering_still_a_sustainable_career/) and another puzzling over [feeds full of self-proclaimed AI experts](https://www.reddit.com/r/dataengineering/comments/1wshc5q/why_is_my_linkedin_feed_filled_with_knowledge/).
- A thread on [why text-to-SQL still isn't working in practice](https://www.reddit.com/r/dataengineering/comments/1wt5pbk/why_texttosql_is_not_successful/) despite tools like Omni and Sigma drew practitioner debate.
