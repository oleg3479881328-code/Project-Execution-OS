# Decision Registry — Project Execution OS Architecture Review

## Purpose

This registry preserves accepted architecture decisions from the active review of `Project Execution OS` so that they are not lost inside chat and can be distinguished from implemented repository state.

## Context

- Date: 2026-05-29
- Scope: review and development direction for `Project Execution OS` as the central operating system for project-related AI work.
- Governing references:
  - `START_HERE.md`
  - `docs/PROJECT_LIFECYCLE_MODEL.md`
  - `docs/REPOSITORY_MEMORY_STANDARD.md`
  - `docs/DECISION_REGISTRY_STANDARD.md`
  - `docs/CONTEXT_ASSEMBLY_STANDARD.md`
  - `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
  - `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
  - `SYSTEM_CONTEXT_MANIFEST.md`
  - `docs/KNOWLEDGE_SYSTEM.md`
  - `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
  - `knowledge-library/README.md`

---

## Decision 001 — Keep Project Execution OS as the Central Brain for Project Work

### Decision

Develop `Project Execution OS` as the central operating brain for project-related AI work. Do not create a new upper-level system above it at this stage.

### Reason

The existing system already contains the central entrypoint, lifecycle routing, research and review standards, Codex handoff logic, AI coordination, agent/skill layers, central reusable knowledge architecture, context assembly, context versioning and API economics measurement rules. Creating another parent system now would add structure before a proven gap requires it.

### Evidence / Source

- `START_HERE.md` defines the single top-level entrypoint and routes into internal system nodes.
- `docs/PROJECT_LIFECYCLE_MODEL.md` defines project-layer roles and the reuse-first / MVP-first constraint.
- `PROJECT_INDEX.md` describes the system model and canonical artifacts.

### Status

`accepted — recorded and reflected in committed repository architecture`

### Consequences / Follow-Up

- Strengthen the existing system only where a real missing function is identified.
- Do not create a separate `Central AI System` or `Agent Network OS` repository as a parent layer unless later evidence requires it.

---

## Decision 002 — Implement Context Assembly Standard

### Decision

Create and route through `docs/CONTEXT_ASSEMBLY_STANDARD.md`.

### Purpose

Define how a human or AI participant obtains the minimal sufficient and trustworthy context for a specific action inside `Project Execution OS`.

### Core Principle

Do not load the entire central system or entire project by default. Assemble only the context necessary for the current task.

Expected context sequence when applicable:

```text
CORE_SYSTEM_PROMPT
→ START_HERE.md
→ relevant system standard selected by route
→ PROJECT_ENTRYPOINT.md for a specific project, when applicable
→ minimum task-relevant files/evidence
→ relevant reusable knowledge only when needed
→ current instruction, error, log or live input
```

### Boundary

The standard is model-agnostic. It is not a DeepSeek-only or API-caching document. API orchestration may use it to support stable prefixes, versioned context assembly and cost/cache measurement, but that is an extension rather than the main purpose.

### Evidence / Source

- `START_HERE.md` routes to the smallest relevant internal node.
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` requires a short reliable project front door rather than full history duplication.
- `docs/CODEX_HANDOFF_STANDARD.md` defines a bounded execution-context packet for Codex.
- Owner-provided DeepSeek Platform usage screenshot showed approximately 93.5% input cache-hit share for the displayed 2026-05-28 workload.

### Status

`implemented — committed and routed from START_HERE.md`

### Implementation Evidence

- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- commit: `3cfe8306d7030a75ed38cd846765ccf538b3c7c1`
- `START_HERE.md` route update
- commit: `f56ed776b528b28a0736d729f2938aa4c61f01fc`

### Consequences / Follow-Up

- Validate the standard through bounded review and real project use.
- Use it as the basis for future API orchestration work.

---

## Decision 003 — Strengthen Existing Knowledge System; Do Not Create Duplicate Knowledge Module Standard

### Decision

Do not create a separate `Knowledge Module Standard`. Strengthen the existing knowledge architecture in:

```text
docs/REFERENCE_IDEA_CAPTURE_STANDARD.md
docs/KNOWLEDGE_SYSTEM.md
knowledge-library/README.md
```

### Reason

The system already separates:

- raw references and ideas awaiting triage;
- project-specific knowledge that stays with its project layer;
- reviewed central reusable knowledge stored in `knowledge-library/`.

A new overlapping standard would increase duplication and ambiguity.

### Implemented Improvements

`docs/KNOWLEDGE_SYSTEM.md` now includes:

1. explicit lifecycle:

```text
captured → researched → candidate → reviewed → active → deprecated / replaced
```

2. relevance metadata supporting selective loading into context:
   - `Applies To`;
   - `Triggers`;
   - `Do Not Load When`;
   - `Related Standards`;
   - `Status`;
   - `Replaced By`.

3. explicit distinctions among:
   - `reference`;
   - `knowledge entry`;
   - `standard`;
   - `skill/plugin`;
   - `agent`;
   - `project artifact`.

4. integration with `docs/CONTEXT_ASSEMBLY_STANDARD.md` so central knowledge is loaded only when relevant to the active task.

### Status

`implemented — committed as Knowledge System v2`

### Implementation Evidence

- `docs/KNOWLEDGE_SYSTEM.md`
- commit: `d95a2d6aadfa2200406dc7f12fc1df9e1daf668e`

---

## Decision 004 — Implement System Context Versioning

### Decision

Create a versioned manifest for stable reusable central context profiles.

### Purpose

Make context changes visible, reproducible and measurable without treating provider-side cache behavior as guaranteed memory.

### Implemented Artifacts

- `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- `SYSTEM_CONTEXT_MANIFEST.md`

Initial profile:

```text
knowledge-aware-core-v1
```

Initial fingerprint:

```text
160c2650b5658d5d977b16063c71c96d694055fb2b92be7b5d2430f33624c579
```

### Status

`implemented — initial profile committed`

### Implementation Evidence

- `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- commit: `4fb3ee2dca0c05e197dcc9c29287a2eb9511ddd3`
- `SYSTEM_CONTEXT_MANIFEST.md`
- commit: `a92109e12ebed9841cdb001529043884146a3c52`

---

## Decision 005 — Implement API Runtime Cost And Cache Logging Standard

### Decision

Create a provider-neutral runtime logging standard for token usage, cache behavior and cost evidence.

### Purpose

Measure actual economics instead of assuming context efficiency from prompt structure alone.

### Implemented Artifact

- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`

### Status

`implemented — committed standard; runtime automation not yet built`

### Implementation Evidence

- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- commit: `fd6790384b38c7bd607f0afeab5cc195e2a688b8`

### Consequences / Follow-Up

- Future API adapters should emit runtime logs using the common shape.
- Automatic log ingestion, dashboards and provider adapters remain separate future execution work.

---

## Implementation Log

Executed changes are summarized in:

`logs/2026-05-29-context-cache-implementation.md`

Commit:

`8354ba3c203a215a62bddccfe80b3face43a24e8`

## Central Index Update

The central map now includes the new standards and manifest:

`PROJECT_INDEX.md`

Commit:

`a213806e1fec70b13088607f604c82908d2574da`

## State Note

Committed repository artifacts exist.

Not yet implemented:

- API orchestrator runtime;
- automatic manifest regeneration;
- automatic request-level log ingestion;
- cost dashboard;
- provider-specific adapters;
- validation through repeated real project use.

Do not claim those runtime capabilities as active until execution and validation evidence exists.

## Next Required Action

Run a bounded review pass over the newly committed context-assembly, context-versioning and API-economics artifacts before building runtime automation.