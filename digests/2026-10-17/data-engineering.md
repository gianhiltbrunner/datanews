# Amazon acquires DuckLabs, the company behind DuckDB

The day's biggest story is Amazon's acquisition of DuckLabs, bringing DuckDB's founders into AWS and DuckDB into Amazon Aurora PostgreSQL. Beyond that, Netflix detailed how it builds a knowledge graph for observability at its scale, and DuckDB published a practical walkthrough on turning JSON columns into typed columns in SQL.

## Top stories
- **[Amazon Acquires DuckLabs and Integrates DuckDB in Amazon Aurora PostgreSQL](https://www.infoq.com/news/2026/10/amazon-acquires-ducklabs/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering)** — InfoQ. Amazon has acquired DuckLabs; co-founders Hannes Mühleisen and Mark Raasveldt will keep leading the DuckDB team under AWS, and Amazon Aurora PostgreSQL already has its first DuckDB-powered feature. *Why it matters:* a major cloud vendor now owns the company behind one of the most widely adopted analytical databases, though Amazon says DuckDB will stay open source.
- **[Ontology-Driven Observability: Building an End-to-End Knowledge Graph at Netflix Scale](https://netflixtechblog.com/ontology-driven-observability-building-an-end-to-end-knowledge-graph-at-netflix-scale-421392cf5adf?source=rss----2615bd06b42e---4)** — Netflix Tech Blog. Netflix explains how it models its infrastructure as a knowledge graph to keep observability coherent across a system that handles over 2 billion requests and 38 million logging events per second. *Why it matters:* a concrete pattern for teams whose monitoring has outgrown what fits on one dashboard.

## Worth reading
- **[Turning a JSON column into typed columns, in SQL](https://duckdb.org/2026/10/16/json-to-typed-columns)** — DuckDB. Walks through using `read_json`'s schema inference, adjusting the inferred schema, and converting a JSON column into typed columns without writing the data to a file first.

## Community pulse
- Robin Moffatt [shared Chris Gambill's post](https://bsky.app/profile/rmoff.net/post/3mxyv7x7hqx2p) on moving from data contracts to quality checks.
- r/dataengineering discussed [building tools to help SQL agents understand unfamiliar databases](https://www.reddit.com/r/dataengineering/comments/1x7iq1p/built_two_tools_to_help_sql_agents_understand/), including surfacing column stats, sample rows, and filtering out irrelevant tables.
- r/dataengineering asked [how others find data mismatches between two large tables](https://www.reddit.com/r/dataengineering/comments/1x7e13n/how_do_you_find_data_mismatches_between_two_large/) when comparing source and target tables with millions of rows.
- r/dataengineering debated [whether to still write SQL by hand](https://www.reddit.com/r/dataengineering/comments/1x7m91c/how_it_feels_writing_sql_by_hand_just_to_prove_i/) versus letting an AI agent handle it.
