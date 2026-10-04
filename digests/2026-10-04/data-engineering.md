# Dbt schema tests catch fewer bad batches than teams assume

No releases landed in today's look-back window, so signal came from two practitioner reliability write-ups and a new open-source master data tool shared on Reddit. Most of the rest of the feed was career posts, self-promotion and off-topic news.

## Top stories
- **[A unique + not_null suite stopped 3 of 17 bad batches. Here is what got through.](https://dev.to/jigonyoo/a-unique-notnull-suite-stopped-3-of-17-bad-batches-here-is-what-got-through-3d8h)** — DEV. The author built a fault-injection tool that plants one realistic data fault at a time into a copy of a dbt project's seed data and measures what the standard `unique`/`not_null` tests actually catch, finding they stopped only 3 of 17 injected faults. *Why it matters:* it puts a number on how little coverage the most common dbt schema tests really provide.
- **[Make Document Pipelines Fail Loudly](https://dev.to/humbertovillanueva/make-document-pipelines-fail-loudly-24ie)** — DEV. The author argues document-processing pipelines should give every failure a small, honest set of named states instead of silently skipping a page or dropping a field, since silent partial failures surface later as confidently wrong answers rather than crashes. *Why it matters:* a concrete reliability pattern for pipelines handling unstructured or semi-structured sources.

## Worth reading
- **[Migrating Data Between Two Postgres Databases Without Shared Access: Durable ID Remapping…](https://macxima.medium.com/migrating-data-between-two-postgres-databases-without-shared-access-durable-id-remapping-0ba6fe01d72d?source=rss------data_engineering-5)** — Medium. Walks through migrating data between two Postgres databases that can't share direct access, using durable ID remapping to preserve referential integrity.
- **[Leaving SAP HANA? Understand What You're Taking With You.](https://dev.to/swaroop_krishna_e2f4b83b2/leaving-sap-hana-understand-what-youre-taking-with-you-5h70)** — DEV. Describes using an enterprise data agent on Snowflake Cortex to trace how SAP HANA business logic actually behaves before rebuilding it in Snowflake or Microsoft Fabric, since a faithful-looking rebuild can quietly change what a report's columns mean.

## Community pulse
- On r/dataengineering, a builder shared **[Eddytor](https://www.reddit.com/r/dataengineering/comments/1wwskfw/eddytor_a_free_master_data_platform_in_your_own/)**, a free, open-source master data platform built on Delta Lake that runs against a team's own storage (Azure, S3-compatible, or GCP), aimed at teams still relying on deprecated Microsoft Master Data Services or unmaintained PowerApps/SharePoint setups.
