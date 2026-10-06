# A quiet day: a data-quality warning on AI outputs, and routine Lightdash patches

A thin window for analytics engineering, with no Reddit or Hacker News discussion surfacing (both dbt subreddits errored out) and most blog activity limited to tutorials. The one industry-level signal worth flagging is a survey finding on how often enterprises catch errors in AI-touched data, plus a modelling debate on where the real layering decision in a dbt project sits.

## Top stories
- **[64% of enterprises find AI errors in data](https://news.google.com/rss/articles/CBMiigJBVV95cUxOdmhkRFRWbjBXSVM1SnpBNkVDbHJQbWI5bUxTN0pEcGRKY2hpcGxmczJRaTB5RktUMlBoUzhwYTZtM21FMWRDRC1Zc2J0VnlMZlVyY3Q4S2ZZcFZDbmVlQnBqSkc1NHZLWkNSQ0tXbFY4LVR3UHNqUGRvRDhXOFlKS3VXR1ZkdXMxN1hiaE55N0wwQXpaQmJ5eFdNXzNQdjYzSGFyQndkelE3Q2lldnp3LWtuVDU1MC1IaHpFUlRsdGhHUl9rUDY1YmlPd0wwa1RrZDU3RHg2NHpHMmdENURlRHJ2WFJKN3F3U0RTUC1CQXNpM19ERmplT3hlbV80Q1Jfb1N2QWVwZzdvdw?oc=5)** — VentureBeat (via Google News). A new report puts the share of enterprises finding errors in AI-touched data at 64%. *Why it matters:* it's a reminder that semantic layers, metrics, and the testing underneath them matter more, not less, once that data starts feeding AI agents.

## Releases & tools
- **[2.439.1](https://github.com/lightdash/lightdash/releases/tag/2.439.1)** — Lightdash. Latest in a same-day string of patches; the preceding releases added messaging on the AI Credits page for paused/exceeded allowances ([2.439.0](https://github.com/lightdash/lightdash/releases/tag/2.439.0)) and let embed viewers without the SQL scope have compiled SQL hidden from them ([2.438.0](https://github.com/lightdash/lightdash/releases/tag/2.438.0)).

## Worth reading
- **[Staging, intermediate, marts… ou Data Vault ? Le vrai choix se joue au milieu](https://medium.com/@thom.luq/staging-intermediate-marts-ou-data-vault-le-vrai-choix-se-joue-au-milieu-e2a54e726c1c?source=rss------dbt-5)** — Medium. Argues that the meaningful modelling decision in a dbt project isn't staging/intermediate/marts versus Data Vault, but what actually happens in the middle layer.
