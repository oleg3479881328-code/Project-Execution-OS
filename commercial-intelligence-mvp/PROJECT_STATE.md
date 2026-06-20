---
project_name: Commercial Intelligence MVP
project_mode: compact
status: active
updated_at: 2026-06-20
source_of_truth: repository
---

# PROJECT_STATE.md

## Current State

`Commercial Intelligence MVP` is an active bounded subproject inside `Project Execution OS`.

The minimum transfer-ready set for this subproject is:

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

## Latest Confirmed Milestone

- MVP scaffold created under `commercial-intelligence-mvp/`.
- Deterministic-first CLI architecture selected.
- Website extraction, context inference, competitor query planning, report rendering, and model tests were implemented.
- Validation passed for `python -m compileall src`, `pytest`, and `python -m src.cli audit --url https://example.com --out reports/example --no-web`.

## Current Focus

Preserve verified execution evidence and prepare the MVP for review or a real-site validation pass.

## Current Next Safe Action

Run the CLI against a real customer site, compare inferred context with known facts, and tighten heuristics where confidence is weak.

## Active Files For Re-entry

1. `PROJECT.md`
2. `PROJECT_STATE.md`
3. `logs/latest.md`
4. `README.md`
5. `src/cli.py`
6. `tests/test_models.py`

## Known Blockers

- Live competitor discovery depends on an external search API key such as `TAVILY_API_KEY`.
- V1 extracts only the initial website page plus linked key pages; it is not a full crawler.

## Do-Not-Break Rules

- Do not fabricate executed web search.
- Do not silently widen scope into SaaS, outreach, CRM sync, or autonomous lead contact.
- Keep the folder removable as a bounded MVP.
