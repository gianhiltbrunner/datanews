# dbt's green test suite hid three rows that silently vanished

A light news day for analytics engineering, dominated by two practitioner essays on where dbt's testing and AI-authorship assumptions quietly fail, plus a vendor claim about semantic layers improving AI accuracy.

## Top stories
- **[I rebuilt my hand-written pipeline in dbt and planted the bugs myself](https://medium.com/@immairaj/i-rebuilt-my-hand-written-pipeline-in-dbt-and-planted-the-bugs-myself-dc47e145b772?source=rss------dbt-5)** — Medium. All 31 dbt tests passed on a deliberately-bugged rebuild of a hand-written pipeline, yet three rows still vanished without a record. *Why it matters:* a fully green test suite is a common proxy for correctness, and this is a concrete case of where that proxy fails.
- **[Who writes your is_incremental() block now?](https://medium.com/@shaantanutripathi/who-writes-your-is-incremental-block-now-87aa5653b014?source=rss------dbt-5)** — Medium. Reads the Enzyme paper (SIGMOD 2026) from the perspective of someone who still writes dbt's incremental MERGE logic by hand. *Why it matters:* raises the question of who — or what — is authoring the MERGE logic inside incremental models as AI coding tools spread.

## Worth reading
- **[The Complete Guide to dbt Slim CI (with video tutorial)](https://medium.com/@hugolu87/the-complete-guide-to-dbt-slim-ci-with-video-tutorial-261b01895abf?source=rss------dbt-5)** — A walkthrough of setting up dbt's Slim CI to only build and test modified models.
- **[Snowflake Apache ICEBERG Tables: Utility & Implementation w/ dbt](https://medium.com/@eddaouissam/snowflake-apache-iceberg-tables-utility-implementation-w-dbt-data-build-tool-ace1fd2079d4?source=rss------dbt-5)** — Implementation notes on using Snowflake's Iceberg table support from dbt.
- **[AtScale Finds Semantic Layer Boosts AI Accuracy on Enterprise Data by Up to 2.4x](https://news.google.com/rss/articles/CBMixwFBVV95cUxOZzJ5aUpzaFlibVNEbE04eU9KMnNZeDE2dnFFQkxEZi02TDE5eWpwYktiWm1tdkRCOFViQ3RlTU1ZbmhGYjMtR3FidElOYXlTVnB4X3JYX2JyVW5Kb2ZZYWduZ25pemNra2dKV2M5alltQmRNUTY5NjdtVGNXbExhVk9lSG1tQ19NZkJOZ01nV1JQZ0M2TldfWmxYNWpLYUh6Q2p1WjZZQjBnX0FjaTd3QTZfWUpGYUF6bzBTbXQ0WFM1azNDNlhJ?oc=5)** — HPCwire. AtScale-sponsored research reports enterprise AI accuracy gains of up to 2.4x when queries go through a semantic layer.
