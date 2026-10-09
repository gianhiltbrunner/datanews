# Netflix details an AI-driven observability ontology spanning 38M events/sec

Today's strongest pieces are architecture write-ups from Netflix and Spotify on using LLM agents to manage production systems, alongside a run of practitioner posts on data-quality patterns. Releases were limited to routine provider packages, and wire coverage was mostly noise.

## Top stories
- **[Presentation: Ontology‐Driven Observability: Building the E2E Knowledge Graph at Netflix Scale](https://www.infoq.com/presentations/netflix-observability-aiops-ontology-scale/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering)** — InfoQ. Netflix engineers describe replacing reactive monitoring with an AI-driven operational ontology, unifying MELT telemetry into a queryable knowledge graph to enable automated triage and root-cause analysis across 38M events/sec. *Why it matters:* a concrete example of agentic workflows (using Claude and graph databases) applied to observability at extreme scale.
- **[Presentation: Multi-Agent Patterns from Spotify's AI Powered Advertising Platform](https://www.infoq.com/presentations/spotify-multi-agent-ai-architecture/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering)** — InfoQ. Spotify shares how its Ads Manager runs production multi-agent systems on Google ADK Java, covering domain ownership, deterministic guardrails, and cost management while avoiding monolithic agent designs. *Why it matters:* practical guardrails for teams putting agentic systems into production data pipelines.

## Worth reading
- **[Write-Audit-Publish: Never Promote a Bad Table Again](https://dev.to/vaishnavprabhu/write-audit-publish-never-promote-a-bad-table-again-94i)** — A walkthrough of staging data, auditing it against quality gates, and only then publishing, instead of catching bad data after it's already live.
- **[Fan-Out Joins: The Silent Cause of Inflated Metrics](https://dev.to/vaishnavprabhu/fan-out-joins-the-silent-cause-of-inflated-metrics-c86)** — Explains how a non-unique join key silently multiplies fact rows and inflates aggregates without ever throwing an error.
- **[Why Your Orchestrator Task "Succeeded" But Your Data Is Wrong](https://dev.to/vaishnavprabhu/why-your-orchestrator-task-succeeded-but-your-data-is-wrong-1gde)** — Argues that an orchestrator's green checkmark only proves the process ran, not that the output data is correct.

## Community pulse
- On r/dataengineering, a practitioner asked for a [simplified Dataform release process](https://www.reddit.com/r/dataengineering/comments/1x0rtsj/suitable_release_process_for_dataform_and_git/), weighing a single protected branch against the team's current three-branch (dev/staging/prod) setup.
- Hacker News saw two new DuckDB-adjacent tools posted: [Pivot](https://pivotlake.io/), claiming 2x+ faster analytics on Iceberg than ClickHouse/DuckDB, and [Datapuddle](https://datapuddle.app/), a native macOS DuckDB client.
