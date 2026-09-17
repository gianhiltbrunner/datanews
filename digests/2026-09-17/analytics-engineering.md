# dbt v2.0 goes GA, completing the Fusion engine rewrite and a rename from dbt Core

dbt Labs shipped dbt v2.0 as a general-availability, complete rewrite of the Fusion engine under a new name, and followed up with a licensing FAQ to clear up confusion with dbt OSS, plus new capabilities aimed at agent-ready data announced at dbt Summit 2026. Elsewhere, practitioners wrote about keeping dbt pipelines resilient to bad source data and where duplicate metrics between dbt's Semantic Layer and Power BI actually come from.

## Top stories
- **[dbt v2.0 is GA](https://docs.getdbt.com/blog/dbt-v2-is-ga)** — dbt Developer Blog. The dbt Fusion engine has reached General Availability under a new name, simply "dbt," described as a complete rewrite laying the foundation for the next decade of the project. *Why it matters:* it's the biggest structural change to the core tool most analytics engineers use daily.
- **[Fivetran + dbt Labs Announces New Capabilities to Make Enterprise Data Agent-Ready at dbt Summit 2026](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQMTNzZGwtZXpQLXU1YU1tX0FJWmpsTGpHamh6V0RNM21DQjFlWl9nd2xXb1JCdkdXNGVLUmNheDJjOWM4dklOQzY3dXJDd2RrUHN0YUtXaW9aa29FeDdRZk1wV0taQVlFRjFLWF81WWVvZDZtX1VoNG13N0pJT1Bva2pMTzBsWWdpSjYyeWR1bHdpOUpRRVRneEhGUnpTMlI4NjBlUlhJRzMyd2ZYblJuQl9zNUZvRUxWZkg0MFoxa3l2eXVJUmFQMU1yeUtURk5IMUc5U0IwU1lZd1BsN1QtS001QW02bVI4VlpNSw?oc=5)** — Business Wire. Fivetran and dbt Labs announced joint capabilities aimed at making enterprise data ready for AI agents, unveiled at dbt Summit 2026. *Why it matters:* it's dbt Labs pairing its v2.0 launch with a concrete ingestion partnership, not just an engine rewrite.

## Releases & tools
- **[dbt v2.0.4](https://github.com/dbt-labs/dbt/releases/tag/v2.0.4)** — the newest patch in the v2.0 line, following v2.0.0's GA release and v2.0.3's addition of a PyPI banner for dbt-oss.
- **[dbt_context_engineering](https://docs.getdbt.com/blog/dbt-context-engineering)** — dbt Developer Blog. A new dbt-published package for modeling the context AI agents read from your project.

## Worth reading
- **[What's the difference between dbt and dbt OSS?](https://docs.getdbt.com/blog/comparing-dbt-and-dbt-oss)** — dbt Labs' own FAQ, published alongside the v2.0 GA, on why the free distribution of dbt v2 is now the default recommendation over dbt OSS.
- **[dbt Semantic Layer vs Power BI: Where the Duplicate Metrics Actually Come From](https://medium.com/tech-with-abhishek/dbt-semantic-layer-vs-power-bi-where-the-duplicate-metrics-actually-come-from-f5dbef2c20ab?source=rss------dbt-5)** — a technical breakdown of why "revenue" can quietly diverge between a dbt Semantic Layer and a Power BI report.
- **[When Bad Data Shouldn't Break Your dbt Pipeline](https://medium.com/@jan.busse/when-bad-data-shouldnt-break-your-dbt-pipeline-ddea13ed768e?source=rss------dbt-5)** — a validate-before-publish pattern with a bounded last-known-good fallback on Snowflake.

## Community pulse
- On r/analyticsengineering, [a post on why analytics projects burn most of their budget before the first dashboard exists](https://www.reddit.com/r/analyticsengineering/comments/1winzfg/why_does_an_analytics_project_spend_most_of_its/) traced it to Medallion Architecture work on Databricks absorbing changing business rules without breaking production reports.
- Also on r/analyticsengineering, [a thread on replacing a BI tool selection cycle with a semantic layer](https://www.reddit.com/r/analyticsengineering/comments/1wi2861/instead_of_another_bi_tool_selection_cycle_we_put/) described consolidating six conflicting definitions of "net sales" into one enforced metric.
