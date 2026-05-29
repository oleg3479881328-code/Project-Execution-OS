# Decision Registry — Project Execution OS Architecture Review

## Purpose

This registry preserves accepted architecture decisions from the active review of `Project Execution OS` so that they are not lost inside chat before the relevant standards are implemented.

This is a decision record, not evidence that future documents, integrations, or runtime behavior have already been implemented.

## Context

- Date: 2026-05-29
- Scope: review and development direction for `Project Execution OS` as the central operating system for project-related AI work.
- Governing references:
  - `START_HERE.md`
  - `docs/PROJECT_LIFECYCLE_MODEL.md`
  - `docs/REPOSITORY_MEMORY_STANDARD.md`
  - `docs/DECISION_REGISTRY_STANDARD.md`
  - `docs/KNOWLEDGE_SYSTEM.md`
  - `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
  - `knowledge-library/README.md`

---

## Decision 001 — Keep Project Execution OS as the Central Brain for Project Work

### Decision

Develop `Project Execution OS` as the central operating brain for project-related AI work. Do not create a new upper-level system above it at this stage.

### Reason

The existing system already contains the central entrypoint, lifecycle routing, research and review standards, Codex handoff logic, AI coordination, agent/skill layers, and central reusable knowledge architecture. Creating another parent system now would add structure before a proven gap requires it.

### Evidence / Source

- `START_HERE.md` defines the single top-level entrypoint and routes into internal system nodes.
- `docs/PROJECT_LIFECYCLE_MODEL.md` defines project-layer roles and the reuse-first / MVP-first constraint.
- `PROJECT_INDEX.md` already describes the system model as including knowledge, skills, agents, governance, review and logging layers.

### Status

`accepted — recorded in repository; implementation implications still require later review`

### Consequences / Follow-Up

- Strengthen the existing system only where a real missing function is identified.
- Do not create a separate `Central AI System` or `Agent Network OS` repository as a parent layer unless later evidence requires it.

---

## Decision 002 — Approve a Future Context Assembly Standard

### Decision

A future `docs/CONTEXT_ASSEMBLY_STANDARD.md` is needed.

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

This standard must be model-agnostic. It is not a DeepSeek-only or API-caching document. Future API orchestration may use it to support stable prefixes, versioned context assembly and cost/cache measurement, but that is an extension rather than the main purpose.

### Evidence / Source

- `START_HERE.md` already requires routing to the smallest relevant internal node.
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` already requires a short reliable project front door rather than full history duplication.
- `docs/CODEX_HANDOFF_STANDARD.md` already defines a bounded execution-context packet for Codex.
- No existing dedicated context-assembly standard was identified during this review.

### Status

`accepted direction — standard not yet created`

### Consequences / Follow-Up

- Later draft and review `docs/CONTEXT_ASSEMBLY_STANDARD.md`.
- Link it to project entrypoint, research, review, Codex handoff and central knowledge selection rules without duplicating those standards.

---

## Decision 003 — Strengthen Existing Knowledge System; Do Not Create a Duplicate Knowledge Module Standard

### Decision

Do not create a separate `Knowledge Module Standard` as initially proposed. The required knowledge function already exists in:

```text
docs/REFERENCE_IDEA_CAPTURE_STANDARD.md
docs/KNOWLEDGE_SYSTEM.md
knowledge-library/README.md
```

### Reason

The current system already separates:

- raw references and ideas awaiting triage;
- project-specific knowledge that stays with its project layer;
- reviewed central reusable knowledge stored in `knowledge-library/`.

A new standard with overlapping purpose would increase duplication and ambiguity.

### Required Future Improvements

Later strengthen the existing knowledge system with:

1. an explicit lifecycle for reusable knowledge:

```text
captured → researched → candidate → reviewed → active → deprecated / replaced
```

2. relevance metadata supporting selective loading into context, such as:
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

4. integration with the future `CONTEXT_ASSEMBLY_STANDARD.md` so central knowledge is loaded only when relevant to the active task.

### Evidence / Source

- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md` defines the intake and promotion queue for uncommitted external references and ideas.
- `docs/KNOWLEDGE_SYSTEM.md` defines project-specific versus central reusable knowledge, promotion, review and anti-dump rules.
- `knowledge-library/README.md` defines the existing reviewed reusable knowledge store.

### Status

`accepted corrected direction — system amendments not yet made`

### Consequences / Follow-Up

- Preserve the existing knowledge architecture.
- Update `docs/KNOWLEDGE_SYSTEM.md` only after the required amendments have been fully specified and reviewed.
- Do not create a redundant knowledge-standard file.

---

## Next Open Direction For Review

### Direction 003 — System Version Manifest

Review whether `Project Execution OS` needs a formal manifest for system version, active core nodes, relevant hashes and agent/project compatibility with a specific system version.

Status: `not yet decided`.

## State Note

This file records accepted architectural directions. It does not by itself prove that the future standards or amendments described above have been implemented, validated or activated.