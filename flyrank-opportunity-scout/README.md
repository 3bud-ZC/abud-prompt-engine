# FlyRank Opportunity Scout

A local-first Python agent that converts approved Google Search Console and GA4 CSV exports into a ranked content-opportunity brief.

## Core job

The agent reads two file-based data sources, joins them only on `landing_page`, calculates transparent opportunity scores, classifies query intent, and writes both JSON and Markdown outputs.

## Why this scope

The MVP intentionally does one job end to end. It does not connect directly to confidential production systems, publish content, edit metadata, or make irreversible changes.

## Files

- `agent.py` — validation, aggregation, scoring, intent classification, and report generation
- `sample_data/gsc.csv` — synthetic GSC-shaped test input
- `sample_data/ga4.csv` — synthetic GA4-shaped test input
- `BUILD_LOG.md` — build decisions, cuts, and iteration record
- `RUN_CAPTURE.txt` — raw terminal output from the demonstration run

## Run

```bash
python agent.py \
  --gsc sample_data/gsc.csv \
  --ga4 sample_data/ga4.csv \
  --output output
```

The agent creates:

- `output/opportunity_report.json`
- `output/opportunity_brief.md`

## Input contract

GSC columns:

```text
landing_page,query,impressions,clicks,position
```

GA4 columns:

```text
landing_page,sessions,engaged_sessions,conversions
```

## Guardrails

- GSC and GA4 are never joined on query.
- Blank query rows are retained and labeled as anonymized demand.
- Missing required columns stop the run with a clear error.
- The agent only recommends actions; it never publishes or edits content.
- Opportunity scores require human review before business action.
- No real FlyRank or Flewd client data is included in this public repository.

## Platform choice

Python was chosen over a paid hosted agent or n8n workflow because the task is data-heavy, must be reproducible, can operate locally, and benefits from explicit scoring logic that can be audited line by line.

## Demo-data disclosure

The included CSV files are synthetic and exist only to prove the full loop. Confidential internship data must remain in approved local storage and should not be committed to GitHub.
