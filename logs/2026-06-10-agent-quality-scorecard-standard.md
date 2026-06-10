# Agent Quality Scorecard Standard Added

Date: 2026-06-10

## Purpose

Record the addition of a reusable system-wide standard for evaluating AI agents, agentic workflows and model-backed automations by measurable outcomes.

## Trigger

The owner approved durable capture after reviewing an external argument about professional versus amateur use of AI agents.

## Executed Changes

- created `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`;
- routed agent-quality, evaluation, regression-protection, observability, tool-use-quality and orchestration-complexity questions through `docs/ROUTER.md`;
- linked scorecard economics to `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`;
- defined minimum scorecard evidence for repeated operational workflows;
- defined the least-complex-architecture rule;
- defined staged promotion levels from one-off use to high-risk or business-critical workflows.

## Key Decision

Agent quality must not be judged by prompt cleverness, token count per request, number of tools, number of agents, or subjective impressions.

The preferred metric is useful, repeatable and explainable outcome quality, followed by cost, latency, retries, human correction effort, context efficiency, tool-use quality, regression protection, safety and transferability.

## Deferred Maintenance

`PROJECT_INDEX.md` should include `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` in its canonical-documents list when the next safe index-maintenance pass updates the large root index file.

## Related Files

- `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`
- `docs/ROUTER.md`
- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- `docs/INDEXING_STANDARD.md`
