# Can data agents actually analyze data? A Carnegie Mellon professor says not yet

The strongest piece of the window is dbt Labs' roundup interview on why data agents still fall short of real analysis work. Alongside it, practitioners are writing up the move from dbt's legacy engine to the new Rust-based dbt v2 (Fusion), and Cube shipped a security patch worth knowing about on its LTS branch.

## Top stories
- **[Can data agents do real analysis?](https://roundup.getdbt.com/p/can-data-agents-do-real-analysis)** — The Analytics Engineering Roundup (dbt Labs). Carnegie Mellon's Shreya Shankar explains why data agents fall short at real analytics work, what a semantic layer changes, and how to evaluate LLM outputs you can actually trust. *Why it matters:* a grounded counterpoint to "AI will do your analytics" claims, from someone who studies LLM data work directly.
- **[Upgrading from dbt v1 to dbt v2: A Practical Guide for Snowflake Teams](https://medium.com/@pranayvatsal/upgrading-from-dbt-v1-to-dbt-v2-a-practical-guide-for-snowflake-teams-f4be01026c2c?source=rss------dbt-5)** — Medium. A migration walkthrough for dbt v2, the Rust-based engine formerly called Fusion, which went GA at dbt Summit after its September release. *Why it matters:* practical guidance for Snowflake teams planning the move off the legacy engine.

## Releases & tools
- **[Cube v1.6.75 LTS](https://github.com/cube-js/cube/releases/tag/v1.6.75)** — security upgrade of Node.js (22.22.0 → 22.23.4) on the LTS branch, closing a high-severity issue.

## Worth reading
- **[How to Review AI-Generated dbt Code Before It Reaches Production](https://medium.com/@anandandbeyond/how-to-review-ai-generated-dbt-code-before-it-reaches-production-0ed805e68b71?source=rss------dbt-5)** — practical checklist for reviewing LLM-written dbt models before they ship, beyond "it compiles and `dbt build` passes."
- **[Snowflake Open Data Sharing: Share Iceberg Tables Without Requiring a Snowflake Account](https://medium.com/tech-with-abhishek/snowflake-open-data-sharing-share-iceberg-tables-without-requiring-a-snowflake-account-d98d53c2896b?source=rss------dbt-5)** — a deep dive into sharing Iceberg tables with external consumers via REST catalogs and programmatic access tokens.
