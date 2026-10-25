# A Carnegie Mellon researcher explains why data agents still can't do real analysis

The standout piece this cycle is Shreya Shankar's case for why LLM data agents fall short of real analytical work and what a semantic layer changes about that. Elsewhere, dbt's v1-to-v2 (Fusion) migration is generating practical guidance, and Cube patched a high-severity Node.js vulnerability in its LTS line.

## Top stories
- **[Can data agents do real analysis?](https://roundup.getdbt.com/p/can-data-agents-do-real-analysis)** — The Analytics Engineering Roundup (dbt Labs). Carnegie Mellon professor Shreya Shankar explains why data agents fall short at real analytics work, what a semantic layer changes, and how to evaluate LLM outputs you can actually trust. *Why it matters:* as teams rush to put agents on top of their warehouses, this is a grounded counterpoint on where the current generation of agents actually fails.
- **[Upgrading from dbt v1 to dbt v2: A Practical Guide for Snowflake Teams](https://medium.com/@pranayvatsal/upgrading-from-dbt-v1-to-dbt-v2-a-practical-guide-for-snowflake-teams-f4be01026c2c?source=rss------dbt-5)** — Medium. A migration guide for Snowflake teams moving onto dbt v2, the Rust-based engine formerly called Fusion that was released in September and announced GA at dbt Summit. *Why it matters:* a core engine swap touches every model in a project, and practical migration notes are scarce this early.
- **[How to Review AI-Generated dbt Code Before It Reaches Production](https://medium.com/@anandandbeyond/how-to-review-ai-generated-dbt-code-before-it-reaches-production-0ed805e68b71?source=rss------dbt-5)** — Medium. A checklist for reviewing Cursor- or Claude Code-generated dbt models beyond "it compiles and dbt build passes."

## Releases & tools
- **[Cube v1.8.13](https://github.com/cube-js/cube/releases/tag/v1.8.13)** — Latest release fixes Top N pushdown ordering and adds a CLI onboarding command; Cube also patched a high-severity Node.js vulnerability in its v1.6 LTS line (v1.6.75).

## Worth reading
- **[Dagster and dbt: do you need both?](https://medium.com/@hikmahtech/dagster-and-dbt-do-you-need-both-964b60a29680?source=rss------dbt-5)** — Medium. A look at where orchestration and transformation responsibilities split between the two tools.
- **[Snowflake Open Data Sharing: Share Iceberg Tables Without Requiring a Snowflake Account](https://medium.com/tech-with-abhishek/snowflake-open-data-sharing-share-iceberg-tables-without-requiring-a-snowflake-account-d98d53c2896b?source=rss------dbt-5)** — Medium. An engineering deep dive into sharing Iceberg tables with external consumers via REST catalogs and programmatic access tokens, with no Snowflake account required.
- **[I Built a Marketing Intelligence Dashboard That Answers Business Questions in Plain English](https://medium.com/@fuddiebiola/i-built-a-marketing-intelligence-dashboard-that-answers-business-questions-in-plain-english-6d12698b5db1?source=rss------analytics_engineering-5)** — Medium. A case study combining dbt, DuckDB and Wren AI behind a governed semantic layer to turn fragmented marketing data into a natural-language decision tool.
