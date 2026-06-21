# Commercial Intelligence MVP

First runnable MVP for the `Commercial Intelligence Agent`.

It accepts a generic `customer_seed`, resolves the seed type, extracts public website evidence when a website is provided or discovered, infers business context, builds a competitor search plan, optionally performs live competitor discovery with Tavily, and writes:

- `report.md`
- `report.json`
- `sources.json`

## Scope

This v1 is a bounded Python CLI inside `Project Execution OS`.

It is intentionally not:

- a SaaS app
- a CRM
- an outreach bot
- a dashboard
- a large multi-agent runtime

## Existing Solution First

This MVP follows the parent repository's reuse-first rule:

- deterministic Python CLI first
- `requests` + `BeautifulSoup` for extraction
- optional Tavily search adapter for live discovery
- no LangGraph or CrewAI until a concrete stateful workflow need exists

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Optional environment variables:

```bash
TAVILY_API_KEY=tvly-...
```

## Run

```bash
python -m src.cli audit --seed https://example.com --out reports/example
python -m src.cli audit --seed "ACME Dental, Mason Ohio" --seed-type company_name --out reports/acme --no-web
python -m src.cli audit --seed "+1 513 555 1212" --seed-type phone_number --out reports/phone --no-web
```

Optional flags:

```bash
--url https://example.com
--seed-type website_url
--country US
--language en
--known-competitor https://competitor.example
--goal "more qualified demo requests"
--max-competitors 5
--no-web
```

`--seed` is the primary interface.
`--url` remains only as a backward-compatible alias that maps to website seed handling.
`--no-web` disables live competitor search but still resolves the seed and analyzes any directly reachable website.

## Output

`report.md`
Human-readable audit with:

- Seed Resolution
- Executive diagnosis
- Inferred business context
- Competitor map
- Offer and funnel diagnosis
- Distribution opportunities
- 30-day action plan
- Assumptions and risks

`report.json`
Structured Pydantic-shaped report data.

`sources.json`
Execution metadata including attempted sources, succeeded and failed calls, assumptions, and query plan.

## Validation

```bash
python -m compileall src
pytest
python -m src.cli audit --url https://example.com --out reports/example --no-web
```

## Limitations

- V1 is heuristic-heavy and does not claim full market coverage.
- Without `TAVILY_API_KEY`, competitor discovery is downgraded to query-plan mode.
- It inspects the homepage plus a small set of obvious linked pages, not a complete crawl.
- When no website is provided or discovered, website and funnel sections become plan-and-risk oriented rather than evidence-rich.
- Geography and business-model inference are best-effort and confidence-tagged.

## Next Steps

- Improve seed-type detection and entity resolution beyond heuristic matching.
- Add optional content extraction adapters for Firecrawl or Tavily Extract.
- Expand competitor analysis when live source retrieval is available.
