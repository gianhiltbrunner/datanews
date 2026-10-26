# Databricks brings DataFrame caching to serverless compute, in preview

Signal was thin and the Google News feeds were dominated by unrelated matches on the word "Snowflake." The one concrete platform story is Databricks enabling `df.cache()`/`df.persist()` on serverless compute, with practitioners already flagging that it behaves differently from the classic-cluster cache. Reddit also surfaced a cluster of smaller Databricks platform friction points.

## Top stories
- **[DataFrame caching is now in Public Preview on Databricks serverless compute](https://www.reddit.com/r/databricks/comments/1xfp1f7/dataframe_caching_is_now_in_public_preview_on/)** — r/databricks. `df.cache()` and `df.persist()` now work on serverless compute, removing a common reason teams kept a classic cluster around for iterative or repeated-join workloads — but a practitioner notes it isn't the same cache behavior as on classic clusters. *Why it matters:* serverless adoption has been held back by exactly this kind of cache gap.

## Worth reading
- **[Allianz, Hartford on scaling AI: Set data standards first](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOanVKT0dRdzloc1ZSTmw3VXAyMGVLZG15RWliQ2FTS0NQTERkMDZpeHlNbFNBZGlmU0VFYkJ4aHZ5LVlVa1NpdmpuWnpwX1Z2LUdrUDYzeEJGV1FHWlVLUlhVanJQQ0E4eUY4bWxWZHJDTWs5dEhNdjg0NHFuWnZ1b1V6YktNWURndE5F?oc=5)** — Digital Insurance. Two insurers say AI initiatives stall without data standards in place first.

## Community pulse
- Databricks practitioners on r/databricks traded platform friction points: the [Lakeflow Pipelines Editor](https://www.reddit.com/r/databricks/comments/1xfga8q/pipelines_editor_run_selected_code_ignores_the/) ignoring a pipeline's default catalog/schema when running selected code, a [Power BI import-mode gateway strategy](https://www.reddit.com/r/databricks/comments/1xfekwg/power_bi_import_gateway_strategy/) question for teams new to the platform, and a post arguing [AI data assistants fail without Unity Catalog governance](https://www.reddit.com/r/databricks/comments/1xf9awc/beyond_the_dashboard_why_ai_data_assistants_fail/) underneath them.
