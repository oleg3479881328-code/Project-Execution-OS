# PROJECT.md

## Project

- Name: `Commercial Intelligence MVP`
- Type: `Python CLI commercial intelligence audit tool`
- Short description: `bounded MVP that turns a public customer seed into a commercial intelligence report`

## Purpose

- Build the first runnable MVP for the Commercial Intelligence Agent.
- Accept minimal public `customer_seed` input such as website, company name, phone, email, address, profile link, or short description.
- Infer business context, generate a competitor research plan, optionally execute live search when configured, and produce actionable growth recommendations.

## Source Of Truth

- Source of truth for execution: this folder plus the parent repository `Project Execution OS`.
- Canonical system entrypoint:
  `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`
- Issue handoff surface:
  `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/65`

## Current Status

- Mode: `implementation`
- Phase: `first runnable MVP`
- Status: `active`

## Done So Far

- Candidate module and handoff contract were defined in `agent-modules/commercial-intelligence-agent/`.
- MVP folder initialized for standalone bounded implementation.

## Current Focus

- Deliver a working CLI that creates `report.md`, `report.json`, and `sources.json` from a generic customer seed.

## Next Practical Step

- Validate the CLI on representative non-URL seeds and tighten seed resolution heuristics where confidence is weak.

## Key Decisions And Constraints

- The product name is `Commercial Intelligence Agent`; do not rename it to `AI Growth Scout`.
- Input is generic `customer_seed`; website URL is only one supported seed path.
- V1 stays deterministic-first and does not require LangGraph or CrewAI.
- Live competitor discovery must not be fabricated when no web-search key exists.
- Output must separate confirmed facts, assumptions, recommendations, and risks.

## Read Next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. `README.md`
4. `src/cli.py`
5. `tests/test_models.py`
