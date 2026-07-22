# FL-07 Build Log

## Iteration 1 — Narrow the job

Started from the FL-06 specification: identify and rank content opportunities from GSC and GA4 exports.

Cut from the first MVP:

- Direct BigQuery access
- Embedding models
- HDBSCAN clustering
- Automatic content edits
- Scheduled weekly runs
- External LLM calls
- Dashboard UI

Reason: the assignment rewards one reliable end-to-end loop more than a broad unfinished system.

## Iteration 2 — Define the file connection

Implemented two CSV inputs as the live file/data connection:

- GSC page/query export
- GA4 page-level export

Added schema validation before processing. A missing required column stops the run and names the missing fields.

## Iteration 3 — Respect the data shape

The agent joins GSC and GA4 only on `landing_page`. It does not attempt a query-level join because GA4 organic data does not provide the GSC query dimension.

Blank GSC queries are counted as anonymized rows. They are not dropped or treated as corrupt data.

## Iteration 4 — Transparent scoring

Added a weighted opportunity score using:

- Search demand
- CTR gap
- Striking-distance ranking signal
- Engagement gap
- Conversion signal

Every component is visible in `agent.py`; there is no hidden model or unexplained black-box decision.

## Iteration 5 — Action output

The agent writes:

- A machine-readable JSON report
- A reviewer-readable Markdown brief
- Terminal output showing ranked pages and recommended actions

## What broke and how it changed

- Initial concept depended on real confidential data. Public demo data was replaced with synthetic, schema-compatible CSV files.
- The FL-06 design included semantic embeddings and clustering. They were deferred because they add setup, model, and evaluation risk before the basic scoring loop is proven.
- A dashboard was excluded because the brief asks for an intelligence layer rather than a presentation-only surface.

## Current limitations

- Intent classification is deterministic keyword logic, not embeddings.
- The score weights are initial product assumptions and need calibration on approved historical outcomes.
- GA4 JSON flattening is outside this narrow MVP; the agent expects a page-level export.
- No direct publishing or mutation tools are allowed.

## Next iteration

After evaluation on approved local data:

1. Add a GA4 raw-export flattener.
2. Add semantic intent classification.
3. Compare score rankings against human expert prioritization.
4. Add trend features across time windows.
5. Add a local HTML report without changing the core scoring logic.
