# Harness Engineering Standard v2

## Purpose

This standard defines how `Project Execution OS` designs the execution scaffold around AI agents and agentic workflows.

The goal is to make agents reliable by engineering the surrounding system, not by relying on prompt cleverness or model capability alone.

Use this standard to decide what context, tools, permissions, memory, verification, observability, and handoff artifacts an agent needs before it is treated as repeatable or operational.

## Source Trail

Primary donor reference:

- `https://github.com/ai-boost/awesome-harness-engineering`

Additional reviewed execution reference:

- `https://pimenov.ai/articles/vaybkoding-bez-bardaka/`
- gap analysis: `docs/research/VIBECODING_WITHOUT_CHAOS_GAP_ANALYSIS_2026-08-28.md`

Donor references inform this standard but do not replace local OS architecture.

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

```text
Agent harness = the controlled execution environment around an AI agent.
```

A harness may include entrypoint and routing, context, planning, tools, permissions, memory, sandbox, verification, observability, approval, and handoff state.

## Core Rule

```text
Do not start by adding more agents.
Start by making the smallest sufficient harness explicit.
```

Preferred progression:

```text
single answer
  -> single model call
  -> single agent with minimal tools
  -> deterministic workflow with checkpoints
  -> multi-agent workflow only when evidence justifies separation
```

## Minimum Harness Questions

Before promoting an agent or workflow beyond one-off use, answer the smallest relevant subset.

### 1. Task Shape

- What repeated task is this harness for?
- Is the task bounded, long-running, risky, or multi-session?
- What is the successful outcome?
- What is explicitly out of scope?

### 2. Entrypoint And Route

- Where does the agent start?
- Which router or project entrypoint must be read first?
- Which deeper files are loaded only when needed?
- How does a new executor avoid stale chat memory?

### 3. Context Delivery

- What is always-on context?
- What is retrieved on demand?
- What must survive context compaction?
- What should never enter model context?

Use `docs/CONTEXT_ASSEMBLY_STANDARD.md`.

### 4. Planning And State

- Does the task need a durable plan?
- Where are decisions, deviations, and progress recorded?
- What state must survive handoff?

Use `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` for long or transferable work.

### 5. Tools

- Which tools are available?
- Which are actually needed?
- Are tool names and outputs unambiguous?
- Does each tool do one conceptual thing?
- Do tool errors tell the agent what to do next?

Do not expose broad tool sets merely because they exist.

### 6. Permissions

- Which actions are read-only, write-capable, destructive, external, financial, publishing, deployment, or communication actions?
- Which require explicit human approval?
- What is forbidden even if technically possible?

Default to least privilege.

### 7. Sandbox And Execution Boundary

- Where does code, shell, browser, or file execution happen?
- What files, network domains, credentials, and secrets are reachable?
- Can the agent modify its own rules, tools, hooks, or permission files?
- What is the rollback path?

An agent that can edit its own harness is higher risk.

### 8. Memory

- What should be remembered?
- Who approves memory writes that affect future behavior?
- How are stale or contradicted memories invalidated?
- Where is memory stored?

Prefer durable project files for project-specific state before inventing a global memory layer.

### 9. Verification

- What check proves the output works?
- Can the agent run it itself?
- What requires human review?
- Which failures should become regression cases?

Do not accept `it looked good once` as evidence for a repeated workflow.

### 10. Observability And Handoff

- What evidence explains what the agent did?
- Where are logs stored?
- What artifact proves completion?
- Can another executor resume without reading the chat transcript?

Use `logs/latest.md`, project state files, or the owning workflow log when the task must survive handoff.

## Bounded Execution Contract

For non-trivial implementation work, establish the smallest useful contract before editing:

```text
GOAL
USER-OBSERVABLE RESULT
CONTEXT TO READ
CHANGE
DO NOT TOUCH
VERIFY
ROLLBACK / SAFE CHECKPOINT
```

Omit fields that add no value for a micro-task. The purpose is to bound the decision space, not create paperwork.

If the instruction is vague, such as `improve this screen` or `clean up the code`, do not interpret it as permission for broad refactoring. Convert it into an observable defect or desired outcome, explicit boundaries, non-goals, and verification. Adjacent improvements become separate candidate tasks unless required by the current contract.

## Verification Invalidation Law

```text
Any change made after verification invalidates the previous verification for every behavior that the new change could affect.
```

Do not preserve a `validated` state merely because an earlier version passed. Re-run the relevant checks after the last affecting change.

## User-Facing Behavioral Verification

Machine checks are necessary when applicable, but they do not by themselves prove user-facing behavior.

For UI work, verify the relevant subset of:

- open from a clean/reproducible state;
- primary success path;
- one relevant error, invalid, empty, or failure state;
- refresh/persistence when persistence is part of the contract;
- critical console errors and network failures;
- representative desktop and mobile viewport when responsive behavior is in scope.

Choose checks from the actual contract. Do not perform irrelevant browser rituals merely to satisfy a checklist.

Browser tools such as Playwright or DevTools are implementation options, not mandatory dependencies. The requirement is observable evidence appropriate to the task.

## Code Checkpoint Rule

For Git-backed implementation work, after the final relevant verification:

1. inspect the actual diff;
2. confirm no unrelated files or behavior changed;
3. preserve a known rollback path;
4. prefer one coherent completed change per commit/checkpoint;
5. distinguish `committed` from `validated` and `reviewed`.

A commit proves a stored state. It does not prove the behavior works.

## Skill Extraction Rule

Do not create a reusable skill merely because a workflow can be imagined.

Promote a workflow into a skill only after real executions show a recurring, sufficiently stable sequence of inputs, boundaries, checks, stop conditions, and output evidence. If each run still requires major instruction rewriting, keep collecting observations instead of hiding uncertainty inside automation.

Use the Skill Creator block and lifecycle standards for the actual promotion decision.

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
7. Record what was reused, adapted, and remains custom.

Do not add empty templates, logs, agents, scorecards, memory files, or workflow layers by ritual.

## Relationship To Existing Standards

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
| Skill creation | `blocks/skill-creator/BLOCK.md` |

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
- adding another agent increases handoff failures;
- a task expands through undefined “improvements”;
- code is changed after verification without re-verifying affected behavior.

## Final Rule

Engineer the scaffold before blaming the model.

Use the smallest sufficient harness.

Make context, tools, permissions, boundaries, verification, rollback, and handoff explicit before treating an agent as reliable.