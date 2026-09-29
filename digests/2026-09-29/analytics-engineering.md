# When one shared role can let an AI agent see more than its user

A thin window of mostly personal-blog volume, but two pieces stood out: a governance write-up on AI agents inheriting excess access through shared roles, and Paradime's new state-aware orchestration for dbt Fusion. Lightdash also shipped three releases in one day, including an AI-call usage ledger.

## Top stories
- **[One Shared Role Away From a Data Leak](https://npogeant.medium.com/one-shared-role-away-from-a-data-leak-22cc2925371b?source=rss------analytics_engineering-5)** — Medium. Walks through a case where an AI agent inherited more access than the person asking it did, because permissions were granted at the level of a shared role rather than the individual. *Why it matters:* a concrete failure mode as more analytics workflows hand AI agents warehouse credentials scoped for a team rather than a person.
- **[Introducing Paradime State (for dbt™ Fusion)](https://kaustav.medium.com/introducing-paradime-state-for-dbt-fusion-2dd16673a1cd?source=rss------dbt-5)** — Medium. Paradime State brings state-aware orchestration to both humans and agents in Paradime Bolt, so a run only touches models that actually changed. *Why it matters:* extends dbt's own state-comparison idea to agent-driven runs, which otherwise tend to rebuild everything.

## Releases & tools
- **[Lightdash 2.365.0](https://github.com/lightdash/lightdash/releases/tag/2.365.0)** — the latest of three Lightdash releases today, adding custom chart hierarchies with subtotal support across the Explorer, Chart Studio and version history, plus an AI-call usage ledger and roadmap-view tracking introduced in the same run.

## Worth reading
- **[From dbt Jobs to Enterprise Lineage: OpenLineage, Marquez and IBM watsonx.data Intelligence](https://medium.com/@alexander.seelert_41275/from-dbt-jobs-to-enterprise-lineage-openlineage-marquez-and-ibm-watsonx-data-intelligence-70267cff4960?source=rss------dbt-5)** — Medium. Loads data into Iceberg, transforms it with dbt on Presto, and emits OpenLineage events into Marquez and watsonx.data for enterprise-wide lineage.
- **[A Time Capsule, Part One: How I'm Using AI as an Analytics Manager in September 2026](https://medium.com/@ebwydra/a-time-capsule-part-one-how-im-using-ai-as-an-analytics-manager-in-september-2026-e1671e8f132a?source=rss------analytics_engineering-5)** — Medium. A note-to-future-self snapshot of how one analytics manager is actually using AI day to day, meant as a dated marker rather than a manifesto.

## Community pulse
- A Hacker News [Show HN for duckdb.mk](https://github.com/ltrgoddard/duckdb.mk) drew interest for stripping dbt-style SQL builds down to DuckDB's own SQL-to-AST parsing plus a Makefile, skipping dbt's configuration and boilerplate entirely.
