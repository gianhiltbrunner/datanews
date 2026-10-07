# A hijacked app notification turns into a Snowflake breach dispute, while Polars 2.0 ships

The day's biggest story is a security incident: attackers hijacked ASOS's own app notifications to threaten customers with a claimed Snowflake breach, which ASOS has partly confirmed and Snowflake disputes. Elsewhere, Polars 2.0 landed with streaming on by default and breaking SQL changes, two real engineering teams (Airbnb, IFCO/Databricks) published substantive operational write-ups, and a running thread questioned whether governed semantic layers are actually what AI agents use for context.

## Top 5 across domains
- **[Data Platform Engineering]** Attackers hijacked ASOS's app notifications to claim a Snowflake breach; ASOS confirmed "unauthorised activity" while Snowflake disputes its platform was compromised, and a GDPR disclosure clock has reportedly started.
- **[Data Engineering]** Polars 2.0 makes the streaming engine the default and SQL a first-class citizen, with breaking changes to SQL window-function and numeric-literal semantics.
- **[Data Platform Engineering]** Airbnb detailed how it captures real production database traffic and replays it offline to load-test and de-risk version upgrades, instead of relying on synthetic benchmarks.
- **[Analytics Engineering]** Companies building governed dbt semantic layers are finding their AI agents pull context from elsewhere instead, undercutting the layer's one-source-of-truth promise.
- **[Data Engineering]** An InfoQ write-up detailed a custom layer on top of Kafka partitions that guarantees strict per-session message ordering across thousands of independent channels.
