# A sharp write-up on Athena silently reinterpreting local timestamps as UTC

A quiet day for data engineering: the Google News and Medium feeds were dominated by interview-prep posts, syndicated job-market wire stories and a run of spam. The one standout is a debugging write-up on a timezone bug that produces wrong answers with no error, alongside a new open-source local-first SQL ETL tool and a Bluesky-shared essay on AI agents reshaping software influence.

## Top stories
- **[Athena read my timestamps as UTC. It didn't tell me.](https://dev.to/trcollinson/athena-read-my-timestamps-as-utc-it-didnt-tell-me-oah)** — DEV. Testing against a simulated plant database, the author shows that `scan_on AT TIME ZONE 'America/Denver'` means "convert from this zone" in DuckDB but "label as this zone" in Athena, so the same SQL silently produces opposite, equally plausible UTC values depending on the engine. *Why it matters:* the bug throws no error and still returns a valid-looking timestamp, so it only surfaces downstream when numbers don't add up.

## Worth reading
- **[Announcing det: Fast, local-first SQL ETL workspace and pipeline orchestration engine](https://dev.to/saurabhr2/announcing-det-fast-local-first-sql-etl-workspace-and-pipeline-orchestration-engine-2a74)** — DEV. A new open-source tool built on Apache DataFusion and Arrow lets teams write production ETL pipelines in plain SQL, without Jinja templating or a database server.

## Community pulse
- Robin Moffatt [shared](https://bsky.app/profile/rmoff.net/post/3mxrdt7si6a2a) Stephen O'Grady's essay "Agents: The New, New Kingmakers," on how agentic AI is reshaping who holds influence in software.
