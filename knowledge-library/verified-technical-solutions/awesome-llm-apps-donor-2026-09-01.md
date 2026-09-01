# Awesome LLM Apps — reviewed donor catalog

Date reviewed: 2026-09-01
Status: VERIFIED EXTERNAL DONOR / SELECTIVE REUSE
Source: https://github.com/Shubhamsaboo/awesome-llm-apps
License: Apache-2.0
Detailed audit: `docs/research/AWESOME_LLM_APPS_DONOR_AUDIT_2026-09-01.md`

## Existing Solution First rule

Before building a new agent skill, multi-agent workflow, RAG pattern, MCP specialist, memory-backed app, always-on briefing agent, dependency monitor, or LLM context optimizer, check this donor catalog after checking existing Project Execution OS solutions and official platform references.

Do not import the repository wholesale. Reuse or adapt only the smallest adequate component.

## Highest-value reviewed donor patterns

- Advisor → Orchestrator → Worker for genuinely large parallel work, with strong-model review concentrated at commitment boundaries.
- Stateless workers receiving self-contained briefs rather than ambient project context.
- Per-subtask `PASS / FIX / ESCALATE` verification with retry/fallback evidence.
- Explicit execution and retry budgets for multi-model work.
- Eval-driven skill improvement: baseline -> scenarios/evals -> one targeted mutation -> re-run -> keep only if improved.
- Specialist MCP agents with only the tools required for their domain.
- Always-on monitoring separated into deterministic collection, ranking/noise filtering, rendering, scheduling, dry-run, and opt-in delivery.

## Executable pilot candidates

1. `agent_skills/scope-creep-detector` — offline/read-only diff-vs-intent classifier; strong fit with PEOS bounded execution and final-diff review.
2. `agent_skills/commit-archaeologist` — offline/read-only git-history intent reconstruction; useful before risky refactors.
3. `agent_skills/dependency-doctor` — bounded manifest diagnostics, offline by default.
4. `agent_skills/self-improving-agent-skills` — eval-based optimizer; candidate revisions only, never automatic promotion of active PEOS skills.
5. `always_on_agents/release_radar_agent` — dependency release monitor with impact filtering and guarded delivery, only if existing monitoring does not already cover the need.

## Explicit non-adoptions

- Do not replace PEOS routing with the donor Multi-MCP router.
- Do not replace canonical repository/project memory with Qdrant/vector conversational memory; vector memory may only be a retrieval/index layer.
- Do not make multi-agent execution the default; PEOS keeps smallest-sufficient-architecture rules.
- Do not adopt provider-specific model IDs as architecture.
- Do not auto-mutate or auto-promote active skills.
- Do not accept Headroom/TOON token-savings claims without PEOS-specific success/cost/latency benchmarks.
- Do not duplicate existing connectors, automations, or monitoring flows.

## Skill quality bar extracted

Future PEOS skill work should prefer:

```text
bounded capability
+ deterministic scripts for deterministic work
+ references loaded on demand
+ explicit network/security behavior
+ local/private default where possible
+ executable evals
+ real-input tests
+ evidence over claims
```

This is a donor quality pattern, not a replacement for `docs/SKILL_SPEC.md`, `docs/SKILL_REVIEW_STANDARD.md`, or the PEOS lifecycle registry.

## Architecture boundary

```text
Project Execution OS = control plane
reviewed donor component = optional bounded execution capability
```

PEOS retains ownership of startup/routing, durable state, canonical memory, approvals, review, lifecycle, evidence, and transfer readiness.

## License note

The upstream repository is Apache-2.0. If source is copied or modified for distribution, preserve required license/attribution notices and mark modified files as required by the license.

## Maintenance rule

This is a live upstream catalog. At execution time, inspect the current upstream implementation before reuse; this record stores the architectural decision and shortlist, not a frozen inventory.