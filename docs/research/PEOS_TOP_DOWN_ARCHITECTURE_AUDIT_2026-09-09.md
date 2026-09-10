# PEOS Top-Down Architecture Audit — 2026-09-09

## Purpose

Review the overall structure of Project Execution OS without redesigning individual standards, workflows, tools, or projects.

The audit tests the current system against seven architectural concerns:

1. control plane;
2. domain / reusable knowledge;
3. executable capabilities;
4. workflow / composition;
5. applications / owner-facing interfaces;
6. canonical ownership of truth;
7. readiness / evidence state.

This is an audit artifact, not a competing architecture standard.

## Executive Verdict

**KEEP THE CURRENT ARCHITECTURE. STRENGTHEN TWO CROSS-CUTTING GOVERNANCE RULES.**

The current Project Execution OS structure is fundamentally sound and already contains the separation that a scalable project operating system needs.

No five-box rewrite, fixed-depth hierarchy, or new monolithic kernel is justified.

The strongest current model is:

```text
PROJECT EXECUTION OS — CONTROL PLANE
  owner intent
  routing
  context selection
  standards / policy
  project memory ownership
  approvals / review
  readiness / evidence rules
  transfer continuity

        ↓ selects / governs / verifies

DOMAIN KNOWLEDGE
        ↓
EXECUTABLE CAPABILITY
        ↓
WORKFLOW / APPLICATION ADAPTER
        ↓
OWNER-FACING UI / WORKING INTERFACE
```

External runtimes, models, SaaS tools, APIs, plugins, and harnesses may participate in execution, but they do not become the canonical control plane merely because they can execute work.

## Finding 1 — Control Plane

### Current state

Strong.

`START_HERE.md` is intentionally minimal and delegates to recursively composable routers. The routing hierarchy has no artificial depth limit and is designed to load the smallest sufficient context.

`HARNESS_ENGINEERING_STANDARD.md` already establishes the key architectural boundary:

```text
Project Execution OS = control plane
external harness/runtime = optional execution plane
```

### Decision

Do not create a larger central kernel.

The control plane is a **logical responsibility set**, not one giant file or service.

Canonical control-plane responsibilities are:

- owner intent and accepted scope;
- global and project routing;
- context-selection rules;
- operating standards and policies;
- canonical project-memory ownership;
- approval and review policy;
- evidence/readiness semantics;
- transfer-ready continuity.

Execution engines remain replaceable.

## Finding 2 — Domain / Reusable Knowledge

### Current state

Strong.

The Knowledge System already distinguishes:

```text
raw reference / idea
-> project-specific knowledge
-> central reusable knowledge
```

and central lifecycle:

```text
captured
-> researched
-> candidate
-> reviewed
-> active
-> deprecated / replaced
```

The important anti-duplication rule is already present: update the narrowest correct existing canonical artifact before creating a new one.

### Decision

No architectural change required.

Knowledge remains guidance and reusable truth; it must not be confused with executable availability.

## Finding 3 — Executable Capabilities

### Current state

Strong and more mature than the external-tool model.

Capability blocks already have stable contracts, provider separation, test requirements, versioning, manifests, and a canonical readiness registry.

Current lifecycle:

```text
idea
-> candidate
-> validated
-> production
-> deprecated
-> retired
```

This correctly prevents a specification or known tool from being mistaken for working capability.

### Decision

Keep `capability-library/REGISTRY.md` as canonical source of truth for internal reusable executable capability readiness.

Do not weaken `candidate`, `validated`, or `production` meanings.

## Finding 4 — Workflow / Composition

### Current state

Strong.

The capability standard correctly assigns sequencing and business decisions to workflows while keeping one bounded technical responsibility inside each capability.

### Decision

Keep orchestration outside capability cores.

A workflow may compose capabilities but must not silently absorb provider implementations or unrelated responsibilities.

## Finding 5 — Applications / Owner-Facing Interfaces

### Current state

Strong.

`apps/` is correctly defined as the application adapter / user-interface layer. Applications may orchestrate and present capabilities but may not copy reusable provider logic.

Block Studio is a valid first proof of this separation.

### Decision

No structural change required.

Owner-facing UI is an application surface, not canonical business memory and not the capability implementation layer.

## Finding 6 — Canonical Ownership Of Truth

### Current state

Mostly strong, but not explicit enough in one top-level architectural map.

The system already contains the necessary rules across Project, Knowledge, Review, Context Assembly, Tool Stack, and capability documents. The remaining risk is human/agent ambiguity when several surfaces contain related information.

### Canonical ownership rule

Every durable fact type must have one authoritative owner. Other surfaces may summarize, index, cache, render, or link to it, but must not silently become parallel truth.

Default ownership map:

| Truth type | Canonical owner |
| --- | --- |
| global system entry | `START_HERE.md` |
| live global navigation | `docs/ROUTER.md` and child routers |
| high-level PEOS architecture and boundaries | `PROJECT.md` |
| current PEOS execution continuity | `PROJECT_STATE.md` + `logs/latest.md` |
| project identity / local entry | that project's canonical `PROJECT.md` or approved entrypoint |
| current project status / blocker / next action | that project's state/log |
| mandatory operating rule | owning standard |
| reusable knowledge | owning project knowledge or central `knowledge-library/` entry |
| reusable executable capability readiness | `capability-library/REGISTRY.md` |
| external tool / stack adoption status | `docs/TOOL_STACK_AUDIT.md` |
| application-specific UI / orchestration | owning application/project |
| external source files / heavy binary assets | approved durable storage layer for that project |

### Decision

Promote this ownership map into the high-level project architecture.

Do not create duplicate prose solely to make information easier to find; improve routing/indexing instead.

## Finding 7 — Readiness / Evidence State

### Current state

Internal capabilities: strong.

Reusable knowledge: strong.

External tools / integrations: weaker.

`TOOL_STACK_AUDIT.md` already identifies this as a gap. Its current adoption labels (`CORE`, `ACTIVE`, `PROJECT-SPECIFIC`, `CANDIDATE`, `LEGACY`) describe architectural role but do not always answer the separate evidence question:

```text
Do we merely know about this tool?
Can we access it now?
Has its connection been technically tested?
Has it succeeded in a real workflow?
Has the owner accepted it for continued use?
```

### Decision

Do **not** replace adoption status with one overloaded lifecycle.

Use two independent dimensions for external tools when evidence matters:

```text
ADOPTION ROLE
core | active | project-specific | candidate | legacy

EVIDENCE STATE
known
-> researched
-> accessible / connected
-> technically proven
-> workflow proven
-> owner confirmed
```

Not every inventory row needs every evidence field. Add evidence state when the difference can affect routing, execution, cost, security, or claims of readiness.

A tool must never be described as operational merely because it was researched or saved.

## Architecture Risks Ranked

### P0 — None requiring structural rewrite

No evidence supports replacing the current recursive routed architecture or four-layer execution model.

### P1 — Canonical ownership visibility

The rules exist, but the top-level project entrypoint should expose the ownership map so agents do not rediscover it from several standards.

### P1 — External tool readiness ambiguity

Tool role and proof level need to be distinguishable. This is already foreshadowed by `TOOL_STACK_AUDIT.md` GAP-1 and GAP-8.

### P2 — Control-plane visualization

A visual architecture map can improve orientation, but it remains a derived view. It must not become a source of truth and must not invent topology.

Archify remains suitable only under its existing validation boundary.

## Rejected Changes

The audit explicitly rejects the following as unnecessary or harmful now:

- replacing PEOS with a fixed five-part folder architecture;
- forcing all projects into one storage system;
- making ChatGPT, Codex, Notion, GitHub, or another interface the canonical memory for all project types;
- putting all control-plane rules into one giant kernel file;
- loading the entire OS or project for routine tasks;
- converting every donor/tool into an internal capability;
- creating a new lifecycle standard when existing knowledge, capability, review, and tool artifacts already own most of the behavior;
- creating new registries merely for symmetry.

## Accepted Architecture

```text
                         OWNER
                           │
                           ▼
                PROJECT EXECUTION OS
                    CONTROL PLANE
       intent / routing / context / policy / memory
        approval / review / evidence / continuity
                           │
          ┌────────────────┼─────────────────┐
          │                │                 │
          ▼                ▼                 ▼
   project state      reusable knowledge   tool/provider
   and decisions       + standards         selection/evidence
          │                │                 │
          └────────────────┼─────────────────┘
                           ▼
                    DOMAIN KNOWLEDGE
                           │
                           ▼
                  EXECUTABLE CAPABILITY
                           │
                           ▼
               WORKFLOW / APP ADAPTER
                           │
                           ▼
                  OWNER-FACING UI
                           │
                           ▼
                    VERIFIED RESULT
```

The side branches are sources of governed context and state, not extra execution layers.

## Acceptance Criteria From This Audit

1. High-level PEOS entry documentation explicitly shows the control plane plus four application/execution layers.
2. High-level documentation names canonical owners for major truth types.
3. Capability readiness remains governed by the capability registry.
4. Knowledge lifecycle remains governed by the Knowledge System.
5. External tool role is kept separate from external tool evidence/readiness.
6. No competing startup workflow, architecture tree, or parallel standard is introduced.
7. Project remains transfer-ready after the change.

## Final Verdict

Project Execution OS does not need an architectural rewrite.

Its current architecture should be treated as:

```text
small recursively routed control plane
+ selectively loaded durable knowledge/state
+ contract-driven executable capabilities
+ composable workflows/adapters
+ replaceable owner-facing interfaces
```

The next maturity gain comes from making **canonical ownership** and **evidence/readiness** impossible to confuse, not from adding more layers.