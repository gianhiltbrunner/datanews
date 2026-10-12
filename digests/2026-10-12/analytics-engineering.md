# dbt Labs' roundup tracks the shape of the post-AI data stack

Beyond dbt Labs' weekly roundup of the wider AI-and-data landscape, the strongest pieces looked at semantic layers built for AI agents and the hidden cost of default dbt/BigQuery configs. Tooling news was light: a breaking change in SQLGlot's optimizer and routine feature releases from Lightdash and Cube.

## Top stories
- **[Roundup: Personal agents, AI policy, GPT-6.1 Astra, and Jev decision models](https://roundup.getdbt.com/p/roundup-personal-agents-ai-policy)** — The Analytics Engineering Roundup (dbt Labs). This week's roundup covers the political fight over data centers, the shape of the post-AI data stack, claims of physical AI, and an update on the OpenAI/Hugging Face incident. *Why it matters:* a regular pulse check on how the wider AI debate is reshaping the data stack analytics engineers work in.
- **[Semantic Layers (Part 2): Building One Your AI Agents Can Use](https://yasharma06.medium.com/semantic-layers-part-2-building-one-your-ai-agents-can-use-ca44d04e7628)** — Medium. A walkthrough of going from YAML metric definitions to an AI agent that answers "what was our revenue?" with the same number Finance would give. *Why it matters:* semantic-layer consistency is the concrete problem standing between AI agents and trustworthy self-serve analytics.
- **[Your dbt BigQuery Configs Are Lying to You](https://medium.com/@Timothy_Reeves/why-your-dbt-bigquery-configs-are-lying-to-you-94ecb22f9c7b)** — Medium. The author traces a metrics pipeline's ballooning BigQuery storage costs back to misleading default dbt configuration choices. *Why it matters:* a reminder that dbt's BigQuery defaults can quietly drive up warehouse spend.

## Releases & tools
- **[Lightdash 2.566.0](https://github.com/lightdash/lightdash/releases/tag/2.566.0)** — Rebuilds the Agents permissions page into a single, organization-wide list of limits.
- **[Cube v1.8.3](https://github.com/cube-js/cube/releases/tag/v1.8.3)** — Adds read-only mode with export-bucket support for the Athena driver, plus Tesseract multi-stage query performance improvements.
- **[SQLGlot v30.22.0](https://github.com/tobymao/sqlglot/releases/tag/v30.22.0)** — Breaking change: removes `infer_schema` from the optimizer.

## Worth reading
- **[op-lake: an enterprise-scale, self-hosted lakehouse with end-to-end Unity Catalog governance](https://medium.com/databrickscommunity/op-lake-an-enterprise-scale-self-hosted-lakehouse-with-end-to-end-unity-catalog-governance-on-67991751ca21)** — A write-up of a self-hosted lakehouse project built around Unity Catalog governance.
- **[Show HN: KV-CLI – Fast, local dbt/pipeline static analysis in Rust](https://github.com/kovallent/kv-cli)** — A new Rust CLI for local, static analysis of dbt and pipeline projects.
