# Codex Handoff Contract — Build Commercial Intelligence Agent MVP

Packet Type: Implementation handoff contract
Status: candidate

## Objective

Build the first runnable MVP for the Commercial Intelligence Agent.

The MVP must accept minimal input — preferably a single customer website URL — infer business context, discover competitors, analyze the customer's offer/funnel/visibility, and produce a Markdown report plus structured JSON output.

## Source Decision / Design

Use the candidate module in:

```text
agent-modules/commercial-intelligence-agent/
```

Required source docs:

```text
agent-modules/commercial-intelligence-agent/README.md
agent-modules/commercial-intelligence-agent/skills/commercial-intelligence-research/SKILL.md
agent-modules/commercial-intelligence-agent/commands/run-commercial-intelligence-audit.md
agent-modules/commercial-intelligence-agent/references/sources.md
docs/EXISTING_SOLUTION_FIRST_STANDARD.md
docs/RESEARCH_STANDARD.md
docs/CODEX_HANDOFF_STANDARD.md
```

## Allowed Scope

Create an MVP in a new bounded project folder or approved module subfolder selected by the maintainer.

Preferred MVP scope:

```text
commercial-intelligence-mvp/
├── README.md
├── AGENTS.md
├── PROJECT.md
├── .env.example
├── requirements.txt
├── src/
│   ├── cli.py
│   ├── models.py
│   ├── extract_site.py
│   ├── infer_context.py
│   ├── discover_competitors.py
│   ├── analyze_competitors.py
│   ├── diagnose_offer.py
│   ├── plan_distribution.py
│   └── render_report.py
├── examples/
│   └── sample_input.json
├── reports/
│   └── .gitkeep
└── tests/
    └── test_models.py
```

If Project Execution OS requires a different folder location, follow the current repository standard and record the decision.

## Out Of Scope

Do not build:

- a SaaS app;
- payments;
- login/accounts;
- autonomous outreach;
- CRM sync;
- email sending;
- browser stealth bypass as a default;
- uncontrolled scraping of private data;
- a huge multi-agent runtime;
- vector database unless proven necessary;
- production dashboard in v1.

## Repository Context

Repository:

```text
oleg3479881328-code/Project-Execution-OS
```

This handoff must follow Project Execution OS rules.

## Files Allowed To Change

Allowed:

```text
agent-modules/commercial-intelligence-agent/**
commercial-intelligence-mvp/**
```

Optional only if repository standards require indexing:

```text
indexes/**
PROJECT_INDEX.md
CHANGELOG.md
```

## Forbidden Changes

Do not modify unrelated Project Execution OS standards.
Do not change global routing rules.
Do not rename existing folders.
Do not add secrets.
Do not commit API keys.
Do not claim validation unless commands were run.

## Existing Solution Search Required

Yes.

Before implementation, inspect and record adaptation decisions for:

- Firecrawl docs/API or SDK if used;
- Tavily docs/API or SDK if used;
- Apify Actors / Crawlee only if chosen;
- LangGraph or CrewAI only if orchestration is actually needed;
- donor repos listed in `references/sources.md`;
- simple Python alternatives before heavy frameworks.

Use the smallest adequate solution.

Recommended v1 default:

```text
Python CLI + Pydantic models + requests/BeautifulSoup or Firecrawl/Tavily adapter + Markdown/JSON report.
```

Do not choose LangGraph or CrewAI for v1 unless there is a concrete stateful workflow need.

## Implementation Instructions

### 1. Build CLI

Command shape:

```bash
python -m src.cli audit --url https://example.com --out reports/example
```

Optional arguments:

```bash
--country
--language
--known-competitor
--goal
--max-competitors
--no-web
```

### 2. Data Models

Create Pydantic models for:

- CustomerInput;
- ExtractedWebsite;
- InferredContext;
- CompetitorCandidate;
- CompetitorAnalysis;
- CustomerVoiceFinding;
- OfferDiagnosis;
- FunnelIssue;
- DistributionOpportunity;
- GrowthAction;
- CommercialIntelligenceReport.

Every inferred field must carry confidence and source.

### 3. Website Extraction

Implement a simple extraction layer:

- homepage fetch;
- title/meta/headings extraction;
- links extraction;
- contact and service page detection;
- CTA detection using simple patterns;
- schema/JSON-LD extraction when present;
- language/country/currency/phone/address hints.

Support adapter interface so Firecrawl/Tavily can replace simple extraction later.

### 4. Context Inference

Infer:

- company name;
- country;
- region/city;
- language;
- business model;
- main offer;
- likely target customer;
- conversion goal.

Label each field with confidence and evidence.

### 5. Competitor Discovery

If web search API key is available, use it.
If not, create query plan and mark competitor discovery as not executed.

Do not fake search results.

### 6. Analysis

Generate structured analysis from extracted website and competitor evidence.

For v1, acceptable implementation:

- deterministic heuristics first;
- optional LLM call only if API key is present;
- no claim of full market coverage.

### 7. Report Rendering

Output:

```text
report.md
report.json
sources.json
```

Markdown report must follow the command output contract.

### 8. Logging

Log:

- input;
- sources attempted;
- sources succeeded/failed;
- assumptions;
- API usage if available;
- execution timestamp.

## Execution Mode

- Begin implementation immediately.
- Do not pause for optional clarification questions before starting work.
- Resolve minor, reversible ambiguity with the smallest reasonable implementation and record assumptions.
- Ask only if a real blocker prevents safe execution.

## Acceptance Criteria

- The MVP accepts a URL from the command line.
- It creates `report.md`, `report.json`, and `sources.json`.
- It does not fabricate executed web searches when no search connector/key exists.
- It infers at least company name, likely country/language when evidence exists, business model hypothesis, and conversion goal hypothesis.
- It produces a competitor query plan even when live competitor discovery is unavailable.
- It separates confirmed facts, assumptions, recommendations, and risks.
- It includes tests for model validation and confidence/source tagging.
- It includes `.env.example` with no secrets.
- README explains setup, run command, limitations, and next steps.

## Validation Commands / Checks

Run what applies:

```bash
python -m compileall src
pytest
python -m src.cli audit --url https://example.com --out reports/example --no-web
```

If network/API validation is unavailable, state that clearly in the execution report.

## Rollback Notes

The MVP should be removable by deleting:

```text
commercial-intelligence-mvp/
```

Do not couple it to global Project Execution OS runtime.

## Execution Report Contract

Return:

```text
EXECUTION REPORT

Status:
Files Changed:
Existing Solutions Checked:
Solution Reused Or Adapted:
Why Custom Implementation Was Necessary:
Validation Performed:
Validation Not Performed:
Blockers:
Assumptions Made:
Risks / Follow-Up:
Ready For Review: Yes / No
```
