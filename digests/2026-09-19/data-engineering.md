# DuckDB-Wasm gains persistent browser storage as pipeline feeds thin out

Data engineering feeds were mostly SEO tutorials, stock tickers mentioning Innodata, and Medium self-promotion today, with nothing from the usual substack and engineering-blog regulars. Two technical items broke through the noise: DuckDB-Wasm can now persist databases to disk in the browser, and MariaDB Community Server reached its 13.0 general-availability milestone.

## Top stories
- **[Persistent Databases in the Browser with DuckDB-Wasm and OPFS](https://duckdb.org/2026/09/18/opfs-wasm)** — DuckDB Blog, via Hacker News and Bluesky. DuckDB-Wasm can now use the Origin Private File System (OPFS) in modern browsers as a storage backend, so databases survive a tab close instead of vanishing with the Wasm heap as they did at 2021 launch. *Why it matters:* removes a major limitation for building real client-side analytics apps on DuckDB-Wasm without a server round-trip.

## Releases & tools
- **[MariaDB Community Server 13.0](https://www.infoq.com/news/2026/09/mariadb-13-released/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering)** — reached general availability with expanded Oracle-compatibility mode, new procedural SQL and DML capabilities, and performance improvements.

## Worth reading
- **[Is DuckDB safe for production? The honest limitations](https://dev.to/mohammed_arshadansari_f2/is-duckdb-safe-for-production-the-honest-limitations-2h8k)** — DEV. A clear-eyed rundown of DuckDB's single-writer concurrency model and where it does, and doesn't, hold up outside single-process workloads.
