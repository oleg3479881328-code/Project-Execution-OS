# Sources — Commercial Intelligence Agent

Inspected date: 2026-06-20
Status: candidate evidence, not validation evidence

## Project Execution OS standards used

### Start New Project

URL: https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/Start%20New%20Project.md

Pattern used:

- classify the work before expanding into a project;
- do not restart a questionnaire when the idea is already clear;
- route into the lightest correct path.

### Project Lifecycle Model

URL: https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/PROJECT_LIFECYCLE_MODEL.md

Pattern used:

- ChatGPT performs research, comparison, classification, architecture reasoning, and decision preparation;
- Codex performs bounded technical execution only after the decision is clear;
- do not spend Codex on open-ended thinking.

### Existing Solution First Standard

URL: https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/EXISTING_SOLUTION_FIRST_STANDARD.md

Pattern used:

- search before invention;
- adapt before rebuilding;
- build from scratch only when no adequate donor exists or adaptation is worse.

### Research Standard

URL: https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/RESEARCH_STANDARD.md

Pattern used:

- separate confirmed facts, donor solutions, assumptions, recommendations, custom work, and risks;
- use publicly verifiable external sources before new synthesis.

### Agent Module Format Standard

URL: https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/AGENT_MODULE_FORMAT_STANDARD.md

Pattern used:

- file-based reusable module;
- manifest + README + skills + commands + connectors + references + handoff contracts;
- candidate status until real validation.

## Donor repositories checked

### asadcs/ai-competitor-analysis-agent-workflow

URL: https://github.com/asadcs/ai-competitor-analysis-agent-workflow

Observed pattern:

- modular architecture for competitor research;
- competitor discovery;
- positioning, pricing, and messaging analysis;
- opportunity and gap identification;
- branded report generation;
- monthly monitoring idea;
- WAT separation: Workflows, Agents, Tools.

Adapted:

- WAT-style separation into workflow/skill/command/tool responsibilities;
- branded report as an optional later output;
- competitor discovery and opportunity/gap sections.

Not copied:

- exact wording;
- project-specific structure;
- branding implementation details;
- any unvalidated execution claims.

### sneha1012/prospector-ai

URL: https://github.com/sneha1012/prospector-ai

Observed pattern:

- end-to-end B2B sales intelligence pipeline;
- scrape -> store -> enrich -> serve architecture;
- SQLite storage;
- FastAPI dashboard;
- structured lead scoring and recommended actions;
- demo mode and audit trail concepts.

Adapted:

- pipeline stages as a future MVP architecture;
- structured lead scoring and insight schema;
- store/enrich/report loop;
- separation between data acquisition and AI enrichment.

Not copied:

- contractor-specific data model;
- stealth scraping assumptions;
- industry-specific prompts;
- implementation claims without local validation.

### GURPREETKAURJETHRA/AI-Lead-Generation-Agent

URL: https://github.com/GURPREETKAURJETHRA/AI-Lead-Generation-Agent

Observed pattern:

- lead generation from public discussions;
- Firecrawl extraction;
- agent orchestration;
- Google Sheets output;
- lead qualification with LLM.

Adapted:

- public-discussion lead discovery pattern;
- structured lead output;
- Google Sheets as optional lightweight output;
- qualification criteria concept.

Not copied:

- Quora-only source assumption;
- autonomous lead contacting;
- any spam workflow;
- API key setup details.

### aman-ali65/AURA-SEO-Intelligence-Agent

URL: https://github.com/aman-ali65/AURA-SEO-Intelligence-Agent

Observed pattern:

- website SEO audit from URL;
- title/meta/headings/link/image extraction;
- competitor-style search discovery;
- PageSpeed/performance checks;
- PDF reporting.

Adapted:

- website audit coverage;
- SEO + competitor discovery combination;
- report export as optional future capability.

Not copied:

- exact code stack;
- Gemini-specific dependency;
- CLI-only behavior;
- PDF generation implementation.

## Tool/platform donors checked

### Firecrawl

URL: https://docs.firecrawl.dev/introduction

Observed capability:

- search the web;
- scrape pages into markdown/HTML/structured JSON;
- interact with pages;
- map/crawl websites;
- agent and MCP support;
- LLM-ready output, JS rendering, dynamic content handling.

Candidate use:

- customer website extraction;
- competitor page extraction;
- search + scrape pipeline;
- dynamic page inspection when simple scraping fails.

### Tavily

URL: https://docs.tavily.com/welcome

Observed capability:

- web search;
- extract webpages;
- crawl webpages;
- map webpages;
- create research tasks;
- Python and JavaScript SDKs.

Candidate use:

- competitor discovery;
- customer voice research;
- topic/market research;
- quick search-to-evidence pipeline.

### Apify Actors

URL: https://docs.apify.com/platform/actors

Observed capability:

- serverless programs for workflow automation, scraping, browser automation, and data processing;
- structured JSON input/output;
- manual, API, scheduled, and composed runs;
- storage, schemas, and Actor Store.

Candidate use:

- reusable scraping/extraction actors;
- scheduled monitoring;
- marketplace/directory crawling;
- future packaged scraping tools.

### LangGraph

URL: https://docs.langchain.com/oss/python/langgraph/overview

Observed capability:

- low-level orchestration framework for long-running, stateful agents;
- durable execution;
- streaming;
- human-in-the-loop;
- memory and persistence;
- observability with LangSmith.

Candidate use:

- stateful research workflow;
- resumable multi-step commercial intelligence runs;
- human review gates before risky lead/outreach steps.

### CrewAI

URL: https://docs.crewai.com/

Observed capability:

- collaborative AI agents, crews, and flows;
- guardrails, memory, knowledge, observability;
- agents, tasks, processes, human-in-the-loop triggers;
- enterprise integrations.

Candidate use:

- simpler multi-agent prototype;
- role-based specialist agents: market researcher, competitor analyst, offer doctor, funnel auditor, lead strategist.

## Adaptation decision

Do not copy a full donor repo directly.

Recommended architecture:

```text
Commercial Intelligence Agent Module
→ explicit audit command
→ commercial research skill
→ deterministic extraction/storage/reporting tools later
→ Codex handoff only after module shape is accepted
```

Future implementation should borrow:

- WAT separation from `ai-competitor-analysis-agent-workflow`;
- scrape/store/enrich/serve pipeline from `prospector-ai`;
- lead qualification and Google Sheets output pattern from `AI-Lead-Generation-Agent`;
- SEO audit coverage from `AURA-SEO-Intelligence-Agent`;
- extraction/crawl/search capabilities from Firecrawl/Tavily/Apify;
- stateful orchestration from LangGraph or simpler role orchestration from CrewAI.

## Risks

- Search and scraping results can become stale.
- Competitor discovery quality depends on geography inference.
- Minimal input can create false assumptions; confidence tagging is mandatory.
- Lead research can become spammy if not bounded; no auto-contact by default.
- Some sites prohibit scraping; tool use must respect applicable terms and law.
- Paid APIs may create hidden cost; MVP must include cost logging.
- LLM reports can sound confident without evidence; all claims need source tagging.

## Next validation target

Use one real customer website and produce a complete first report.
Record:

- what was inferred correctly;
- what was wrong or low confidence;
- which sources were actually useful;
- what sections of the report produced action-ready insight;
- what should be removed from the module as bloat.
