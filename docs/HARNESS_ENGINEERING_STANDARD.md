# Harness Engineering Standard v1

## Purpose

This standard defines how `Project Execution OS` designs the execution scaffold around AI agents and agentic workflows.

The goal is to make agents reliable by engineering the surrounding system, not by relying on prompt cleverness or model capability alone.

Use this standard to decide what context, tools, permissions, memory, verification, observability, and handoff artifacts an agent needs before it is treated as repeatable or operational.

## Source Trail

Primary donor reference:

- `https://github.com/ai-boost/awesome-harness-engineering`

This standard adapts the donor concept into the existing `Project Execution OS` architecture. It does not copy the donor list as a dependency or replace local OS standards.

## Scope

Apply this standard when:

- creating or changing a reusable agent;
- creating or changing a repeated agentic workflow;
- giving an agent tools, files, APIs, browser access, repository access, Gmail, Calendar, Notion, Drive, GitHub, shell, or publishing access;
- moving a workflow from experiment toward operation;
- diagnosing repeated agent failure;
- preparing a Codex, Claude Code, Cursor, ChatGPT, local-model, or multi-agent handoff;
- deciding whether a task needs a single prompt, single agent, deterministic workflow, or multi-agent system.

Do not force this standard onto a disposable one-off chat task with no reuse, risk, durable artifact, external tool use, or future comparison value.

## Core Definition

In this OS:

```text
Agent harness = the controlled execution environment around an AI agent.
```

A harness may include:

- entrypoint and routing;
- context package;
- planning artifact;
- tool interface;
- permission boundary;
- memory or state layer;
- sandbox or execution environment;
- verification loop;
- observability and logs;
- human approval or escalation path;
- handoff state.

## Core Rule

Use this operating rule:

```text
Do not start by adding more agents.
Start by making the smallest sufficient harness explicit.
```

The preferred progression is:

```text
single answer
  -> single model call
  -> single agent with minimal tools
  -> deterministic workflow with checkpoints
  -> multi-agent workflow only when evidence justifies separation
```

This mirrors `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`: useful, repeatable outcomes matter more than complexity.

## Minimum Harness Questions

Before promoting an agent or workflow beyond one-off use, answer the smallest relevant subset of these questions.

### 1. Task Shape

- What repeated task is this harness for?
- Is the task bounded, long-running, risky, or multi-session?
- What is the successful outcome?
- What should be explicitly out of scope?

### 2. Entrypoint And Route

- Where does the agent start?
- Which router or project entrypoint must be read first?
- Which deeper files are loaded only when needed?
- How does a new executor avoid using stale chat memory?

### 3. Context Delivery

- What is always-on context?
- What is retrieved on demand?
- What must survive context compaction?
- What should never enter the model context?

Use `docs/CONTEXT_ASSEMBLY_STANDARD.md` for routed context decisions.

### 4. Planning And State

- Does the task need a durable plan?
- Where are decisions, deviations, and progress recorded?
- What state must survive handoff to another agent?

For long or transferable work, use the active project continuity pattern from `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`.

### 5. Tools

- Which tools are available?
- Which tools are actually needed for this workflow?
- Are tool names and outputs unambiguous?
- Does each tool do one conceptual thing?
- Do tool errors tell the agent what to do next?

Do not expose broad tool sets merely because they exist.

### 6. Permissions

- Which actions are read-only?
- Which actions are write-capable?
- Which actions are destructive, external, financial, publishing, deployment, or communication actions?
- Which actions require explicit human approval?
- What is forbidden even if technically possible?

Default to least privilege.

### 7. Sandbox And Execution Boundary

- Where does code, shell, browser, or file execution happen?
- What files, network domains, credentials, and secrets are reachable?
- Can the agent modify its own rules, tools, hooks, or permission files?
- What is the rollback path if the agent makes a bad change?

An agent that can edit its own harness must be treated as a higher-risk system.

### 8. Memory

- What should be remembered?
- Who approves memory writes when the memory affects future behavior?
- How are stale, contradicted, or project-specific memories invalidated?
- Where is memory stored: project files, repository memory, external database, or platform memory?

Prefer durable project files for project-specific state before inventing a global memory layer.

### 9. Verification

- What check proves the output works?
- Can the agent run that check itself?
- What requires human review?
- Which failures must be recorded for future regression tests?

Do not accept `it looked good once` as evidence for a repeated workflow.

### 10. Observability And Handoff

- What evidence explains what the agent did?
- Where are logs stored?
- What artifact proves completion?
- Can another executor resume without reading the chat transcript?

Use `logs/latest.md`, project state files, or the owning workflow log when the task must survive handoff.

## Minimum Harness Package

For a reusable or repeated workflow, the minimum package should usually include:

```text
entrypoint
route
context rule
tool permissions
verification gate
state / log location
handoff instruction
```

For GitHub-backed projects, prefer:

```text
PROJECT.md
AGENTS.md or local agent instructions when useful
PROJECT_STATE.md after meaningful execution begins
logs/latest.md after meaningful execution begins
```

For central reusable standards inside this repository, prefer:

```text
START_HERE.md
→ docs/ROUTER.md
→ routed standard
→ PROJECT_STATE.md and logs/latest.md after meaningful changes
```

## Harness Change Protocol

When changing a harness:

1. Confirm the owner task and route.
2. Check for an existing adequate standard or donor pattern first.
3. Make the smallest useful change.
4. Keep the entrypoint and router consistent.
5. Add or update verification guidance.
6. Update transfer state when the change is meaningful.
7. Record what was reused, what was adapted, and what remains custom.

Do not add empty templates, logs, agents, scorecards, memory files, or workflow layers by ritual.

## Relationship To Existing Standards

Use this standard as the architecture wrapper. Then delegate specifics:

| Concern | Use |
|---|---|
| Existing solution search | `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` |
| Project entrypoint | `docs/PROJECT_ENTRYPOINT_STANDARD.md` |
| Context selection | `docs/CONTEXT_ASSEMBLY_STANDARD.md` |
| Transfer-ready state | `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` |
| Agent quality and metrics | `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` |
| API cost and cache evidence | `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md` |
| Research | `docs/RESEARCH_STANDARD.md` |
| Review | `docs/REVIEW_STANDARD.md` |
| Codex handoff | `docs/CODEX_HANDOFF_ENTRYPOINT.md` |

## Promotion Levels

### Level 0 — One-Off

No harness artifact is required unless the task has meaningful risk, write access, or durable project value.

### Level 1 — Repeated Experiment

Define the entrypoint, tool permissions, expected output, and one verification check.

### Level 2 — Operational Workflow

Add durable state, logs, regression examples, cost/latency evidence when available, and explicit approval rules for critical actions.

### Level 3 — High-Risk Or Business-Critical Workflow

Add stronger sandboxing, audit trail, adversarial cases, rollback procedure, permission tests, and human approval gates.

## Warning Conditions

Investigate and improve the harness when:

- the agent asks the same setup questions repeatedly;
- the agent loads too much context by default;
- the agent uses the wrong tool;
- the agent cannot explain what state is current;
- a new executor cannot resume the workflow;
- results vary wildly across runs;
- critical actions happen without approval evidence;
- tool errors lead to hallucinated workarounds;
- memory becomes stale or contradicts project files;
- cost grows without quality improvement;
- adding another agent increases handoff failures.

## Final Rule

Engineer the scaffold before blaming the model.

Use the smallest sufficient harness.

Make context, tools, permissions, verification, and handoff explicit before treating an agent as reliable.
