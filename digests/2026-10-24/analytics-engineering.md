# A Carnegie Mellon researcher explains why data agents still can't do real analysis

The most substantive idea this week came from outside a vendor blog: Carnegie Mellon's Shreya Shankar on why data agents fall short at real analytics work. Otherwise it was a maintenance week — Cube, Lightdash and Great Expectations all shipped incremental releases, and a couple of Medium writers worked through the practicalities of the dbt v1-to-v2 migration and reviewing AI-generated dbt code.

## Top stories
- **[Can data agents do real analysis?](https://roundup.getdbt.com/p/can-data-agents-do-real-analysis)** — The Analytics Engineering Roundup (dbt Labs). Carnegie Mellon Professor Shreya Shankar explains why data agents fall short at real analytics work, what a semantic layer changes about that, and how to evaluate LLM outputs you can actually trust. *Why it matters:* it's a grounded counterpoint to the steady stream of "AI agent does analytics" announcements elsewhere this week.

## Releases & tools
- **[Cube v1.8.12](https://github.com/cube-js/cube/releases/tag/v1.8.12)** — Bug fixes and backend performance work, including faster Decimal128 formatting and lower-allocation JSON serialization; Cube's LTS branch separately picked up a Node.js security upgrade addressing a high-severity advisory.
- **[Lightdash 3.52.0](https://github.com/lightdash/lightdash/releases/tag/3.52.0)** — Makes URL values clickable in results tables, following two prior patches this week on dashboard analysis tooling and an AI-reply guardrail fix.
- **[Great Expectations 1.24.1](https://github.com/fivetran/great_expectations/releases/tag/1.24.1)** — Extends the four LIKE-pattern expectations to Oracle and SingleStore, and widens MySQL dialect coverage, closing gaps where these expectations previously raised `NotImplementedError`.

## Worth reading
- **[Upgrading from dbt v1 to dbt v2: A Practical Guide for Snowflake Teams](https://medium.com/@pranayvatsal/upgrading-from-dbt-v1-to-dbt-v2-a-practical-guide-for-snowflake-teams-f4be01026c2c?source=rss------dbt-5)** — Medium. A practitioner's walkthrough for Snowflake teams moving onto dbt v2, the Rust engine formerly called Fusion that went GA at dbt Summit.
- **[How to Review AI-Generated dbt Code Before It Reaches Production](https://medium.com/@anandandbeyond/how-to-review-ai-generated-dbt-code-before-it-reaches-production-0ed805e68b71?source=rss------dbt-5)** — Medium. A review checklist for dbt models that compile and pass `dbt build` but still need human scrutiny before shipping.
- **[I Built a Marketing Intelligence Dashboard That Answers Business Questions in Plain English](https://medium.com/@fuddiebiola/i-built-a-marketing-intelligence-dashboard-that-answers-business-questions-in-plain-english-6d12698b5db1?source=rss------dbt-5)** — Medium. Combines dbt, DuckDB and a governed semantic layer with Wren AI to turn fragmented marketing data into a natural-language decision-support tool.
