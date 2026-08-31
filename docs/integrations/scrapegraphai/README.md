# ScrapeGraphAI Integration Review

Last verified: 2026-08-31

## Status

`CANDIDATE / project-specific` — useful and sufficiently mature for a bounded pilot, but not yet promoted to a global default dependency.

## Why this exists

ScrapeGraphAI was already present in the Project Execution OS tool audit as a candidate for structured web/entity extraction. This note records the current verified capabilities and the delta that matters for our workflows.

## Existing internal use case

Primary fit already identified:

- wedding-industry entity graph and enrichment;
- website -> entities / venues / vendors / contacts / social links -> structured records;
- competitor/site research;
- repeatable extraction where hand-written selectors would be brittle;
- monitoring selected public pages for meaningful changes.

Canonical structured outputs should continue to follow the owning project's data architecture (for example Sheets / project datastore). ScrapeGraphAI is an extraction capability, not canonical project memory.

## Verified current upstream capabilities

Official upstream repositories/documentation verified on 2026-08-31:

- open-source ScrapeGraphAI Python project;
- official Python API SDK;
- official `scrapegraph-mcp` MCP server;
- official `just-scrape` CLI;
- ScrapeGraph API v2 support in MCP;
- scrape / extract / search;
- asynchronous multi-page crawl with start/status/stop/resume;
- JSON Schema generation;
- monitor create/list/get/pause/resume/delete;
- monitor activity history including whether a page changed and diffs;
- credits/history inspection;
- hosted remote MCP endpoint as well as local MCP operation.

## Important delta from our earlier evaluation

### 1. Codex can use ScrapeGraphAI through MCP

ScrapeGraphAI now documents a direct OpenAI Codex integration using Codex's native Streamable HTTP MCP support. This removes the need to build a custom Codex-to-scraper adapter for the pilot.

Practical consequence: a bounded Codex worker can receive live scrape/extract/search/crawl tools and use structured extraction results directly during execution.

### 2. Monitoring is now a first-class capability

The MCP exposes monitor lifecycle operations and monitor activity/diff history. The `just-scrape` CLI also advertises scheduled page-change monitoring with webhook alerts.

Practical consequence: before creating another custom competitor/page monitor, test the existing monitor implementation.

### 3. Crawl + extract should be separated deliberately

Use crawl for discovering/collecting multiple pages and links. Use extract with a defined prompt/schema for structured records. Do not assume a crawl result alone is a normalized entity database.

## Proposed architecture

```text
Codex / approved agent
        |
        v
ScrapeGraphAI MCP
  | scrape
  | extract
  | search
  | crawl
  | monitor
        |
        v
validation / provenance checks
        |
        v
project-owned structured store
(Sheets or project datastore)
        |
        v
Notion / websites / graph / other consumers
```

## Existing Solution First decision

Do **not** build a custom general-purpose scraper or page-change monitoring service before this candidate is tested.

Preferred order for relevant tasks:

1. normal supported web/API/connector access when it already solves the task;
2. ScrapeGraphAI bounded pilot for AI-assisted extraction/crawl/monitoring;
3. only build custom extraction code when the pilot proves a concrete missing requirement, unacceptable cost/reliability, provenance problem, or site-specific blocker.

## Pilot acceptance test

Run one representative wedding-industry target through the current MCP/API and require all of the following:

1. discover relevant internal pages/links;
2. extract a fixed schema: entity name, entity type, website, location, contact fields if public, social URLs, source URL;
3. preserve source/provenance per extracted record;
4. distinguish missing values from inferred values;
5. detect duplicates/aliases before writing downstream;
6. run the same target again and measure stability;
7. create one page monitor and verify an activity record/diff cycle;
8. record credits/cost and elapsed time;
9. compare result quality and operational effort with our current extraction route.

## Promotion gate

Promote from `CANDIDATE` only if the pilot demonstrates:

- acceptable extraction accuracy;
- usable provenance;
- repeatable output;
- acceptable cost/latency;
- meaningful reduction in custom scraper maintenance;
- acceptable handling of JS-heavy targets relevant to us;
- reliable MCP operation with the chosen executor;
- clear credential/secrets handling and rollback path.

If those conditions fail, retain it as a project-specific fallback rather than forcing adoption.

## Current recommendation

**Pilot MCP + monitor first. Do not build a replacement.**

The highest-value new capability relative to our earlier internal note is the combination of direct Codex MCP access and first-class monitoring/diff operations. This should be tested against the existing wedding-industry graph/enrichment workflow before any broader adoption.

## Upstream references

- https://github.com/ScrapeGraphAI/Scrapegraph-ai
- https://github.com/ScrapeGraphAI/scrapegraph-mcp
- https://github.com/ScrapeGraphAI/just-scrape
- https://scrapegraphai.com/blog/scrapegraphai-mcp-codex
