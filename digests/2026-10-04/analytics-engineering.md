# dbt's Rust-based v2 (Fusion) prompts fresh migration guidance

The dbt ecosystem's shift to the Rust-rewritten v2/Fusion runtime drew fresh migration guidance, alongside an argument for open data infrastructure and a concrete backfill-idempotency write-up. Lightdash and Cube both shipped minor releases.

## Top stories
- **[How to migrate from dbt Core™ v1 to dbt™ v2?](https://medium.com/paradime-labs/how-to-migrate-from-dbt-core-v1-to-dbt-v2-4d8264c03440?source=rss------dbt-5)** — Medium (Paradime Labs). Explains dbt™ v2 ("Fusion"), the Rust rewrite of dbt-core that ships as a self-contained binary and connects via ADBC, and lays out what changes for teams moving off dbt Core v1. *Why it matters:* Fusion is the biggest architectural shift in the dbt ecosystem in years, and most dbt shops will eventually face this migration.
- **[No More Vendor Lock-In](https://learnanalyticsengineering.substack.com/p/wth-is-open-data-infrastructure)** — Learn Analytics Engineering (Madison Schott). Argues the real cost of vendor lock-in isn't the migration itself but everything around it — researching alternatives, negotiating new contracts, backing up data, and re-validating transfers — and makes the case for open data infrastructure. *Why it matters:* a practical framing for teams weighing build-vs-buy and lock-in risk in their stack.
- **[Idempotent backfills and state consistency in data pipelines](https://medium.com/@lara.evdokimova/idempotent-backfills-and-state-consistency-in-data-pipelines-5416063c19a8?source=rss------dbt-5)** — Medium. Walks through a historical-backfill incident to show how re-running a backfill without idempotency guarantees can leave pipeline state inconsistent. *Why it matters:* backfill idempotency is a common failure point in analytics pipelines that rarely gets this concrete a treatment.

## Releases & tools
- **[Lightdash 2.424.0](https://github.com/lightdash/lightdash/releases/tag/2.424.0)** — Adds the ability to attach text documents to AI agent conversations; the preceding patches (2.423.1, 2.423.2) fixed AI-agent credit-key scoping and avatar rendering in embedded sessions.
- **[Cube v1.7.50](https://github.com/cube-js/cube/releases/tag/v1.7.50)** — Latest patch fixes a Tesseract pre-aggregation walk bug that doubled work per level; the prior v1.7.49 added Presto/Trino query trace tokens and cross-stage schema-compiler caching.

## Worth reading
- **[The Business Question Comes Before the Data Model](https://medium.com/@pchandrika0613/the-business-question-comes-before-the-data-model-5935cac885fb?source=rss------analytics_engineering-5)** — Medium. Argues a technically well-built data model can still fail if it answers the wrong business question.
- **[Why Does Data Analytics Take So Long To Answer One Simple Question?](https://medium.com/@DataDecoded-101/why-does-data-analytics-take-so-long-to-answer-one-simple-question-179f070547f3?source=rss------analytics_engineering-5)** — Medium. Cites a survey of 510 analysts finding 78% of the working day goes to things other than running the query itself.
