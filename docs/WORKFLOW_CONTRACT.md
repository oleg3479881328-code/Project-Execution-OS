# Universal Workflow Contract v1

## 1. Purpose

This document defines the invariant workflow for Project Execution OS.

The workflow must be usable for:

- software projects;
- AI systems;
- websites;
- Telegram bots;
- OSINT tasks;
- business projects;
- learning projects;
- automation concepts;
- physical-world projects;
- any structured task that needs execution discipline.

The domain may change.
The workflow remains stable.

This workflow does not require every project to use every storage layer. Layer decisions are defined in `docs/PROJECT_LIFECYCLE_MODEL.md`.

## 2. Core Principle

Do not build giant architecture before the project has passed through a clear workflow.

Execution quality is more important than architectural fantasy.

Default operating gate:

`compact-first`

Default layer rule:

- use Chat for discussion, analysis and commands;
- use Notion when project context must persist in a readable management layer;
- attach GitHub only when versioned execution, code, durable technical files, or Codex work requires it;
- attach Google Drive only when heavy source files or non-versioned assets require it.

There is no universal rule that every project must have a GitHub repository.

## 3. Universal Workflow Chain

The full workflow is the reference model.

Compact mode is the default execution form.

Expand into the full stage chain only when scope, risk, review, handoff, or reuse requires it.

Reference chain:

```text
INPUT
→ CLARIFICATION
→ RESEARCH
→ PLAN
→ AGENT DESIGN only when needed
→ EXECUTION SPEC only when needed
→ REVIEW
→ RESULT
→ KNOWLEDGE EXTRACT only when reusable knowledge exists
→ LOG only when durable history is needed
```

For a GitHub-backed project or file-backed execution run, these stages may be represented as files such as:

```text
00_INPUT.md
01_CLARIFICATION.md
02_RESEARCH.md
03_PLAN.md
04_AGENT_DESIGN.md
05_EXECUTION_SPEC.md
06_REVIEW.md
07_RESULT.md
08_KNOWLEDGE_EXTRACT.md
09_LOG.md
```

Those filenames are an available artifact pattern, not mandatory bureaucracy for every project.

## 4. Stage Definitions

### INPUT

Stores the raw project idea, request, problem, goal, source material, or task when persistence is useful.

Must preserve original intent without over-interpreting it.

### CLARIFICATION

Clarifies ambiguity, constraints, success criteria, scope, risks, and missing context.

Must avoid endless questioning.

### RESEARCH

Finds reusable patterns, open-source examples, official documentation, publicly verifiable external sources, prior project artifacts, known risks, and similar systems.

Research must be reuse-first and evidence-backed when possible.

### PLAN

Converts clarified intent and research into a practical MVP-first plan.

The plan must define sequence, outputs, constraints, and stop conditions when a plan is actually required.

### AGENT DESIGN

Defines which task-specific agents are needed only when a real need exists.

Agents must not be created by default.

### EXECUTION SPEC

Defines what must be built, written, tested, purchased, researched, decided, or handed to an executor.

For software projects, this may become an implementation-ready specification.
For non-software projects, this may become an action-ready execution brief.

### REVIEW

Audits the relevant output, assumptions, evidence, risks, contradictions, and missing pieces.

Nothing important should become stable without appropriate review.

### RESULT

Records the result when durable result memory is needed.

The result may be a decision, document, specification, recommendation, design, or completed artifact.

### KNOWLEDGE EXTRACT

Extracts reusable lessons, patterns, anti-patterns, templates, and decisions only when the work produced reusable value.

Reusable knowledge must be separated from one-off project output.

### LOG

Records what happened, what changed, what was decided, what remains open, and what should happen next when durable operational history is useful.

## 5. State Separation

The system must distinguish:

- `generated` = proposed by AI or user but not written into an appropriate durable layer;
- `recorded` = written into the appropriate persistent layer, such as Notion or Google Drive metadata;
- `committed` = written to GitHub as a commit when a GitHub layer exists;
- `reviewed` = checked by a review process;
- `active` = approved for reuse;
- `archived` = preserved but no longer operational.

No agent may claim that something is executed, saved, recorded, committed, tested, reviewed, active, or complete without evidence appropriate to that layer.

## 6. Agent Rule

Agents are optional execution modules.

They may be created only when needed for:

- a workflow stage;
- a domain bottleneck;
- a quality bottleneck;
- a recurring project function.

The workflow contract is stable.
Agents are optional.

## 7. Knowledge Rule

A workflow run should produce a knowledge extract only when it creates a reusable lesson, pattern, anti-pattern, template, or verified solution.

Do not create empty knowledge artifacts by ritual.

Knowledge can stay local to the project or be promoted to the central knowledge library after review.

## 8. First Validation Rule

Before broad automation, runtime, or orchestration is built, complete real project runs using the smallest applicable workflow.

Automation is allowed only after repeated workflow evidence shows what should be automated.

## 9. Success Criteria

The workflow is acceptable only if it:

- works for many project types;
- keeps durable project state visible when durable state is needed;
- prevents fake execution claims;
- supports project-specific agents when useful;
- preserves reusable knowledge when it actually exists;
- keeps project-specific artifacts and central knowledge separate;
- produces one concrete next action per meaningful run.

## 10. Compact Mode

Compact mode is allowed for small or low-risk projects.

Compact mode is the default unless there is a concrete reason to expand into a heavier workflow.

Compact mode may use fewer artifacts than the full workflow reference chain, but it must preserve, when relevant:

- the appropriate durable source of truth for the project's active layers;
- explicit clarification when needed;
- bundled clarification when several answers belong to one package;
- evidence-backed research when research is required;
- review before stable acceptance;
- result and next action when durable tracking is useful;
- reusable knowledge extraction only when reusable knowledge exists.

Clarification rule:

When multiple user answers are needed to complete one coherent artifact, gather those answers in Chat first and then write one update to the appropriate durable layer unless the user explicitly asks for per-answer persistence.

## 11. Micro-Task Mode

Micro-task mode is allowed for tiny, safe, low-risk work that does not justify a full workflow run.

Use the minimal shape:

```text
goal -> action -> result -> short review note -> next action
```

Micro-task mode should prefer direct completion over ceremony.

## 12. Artifact Only When Useful

Do not create an artifact just because a workflow stage exists in theory.

Create an artifact when it will actually be useful for at least one of:

- future state recovery;
- review;
- evidence;
- reuse;
- decision memory;
- handoff.

If the artifact will not materially help later work, keep the task lighter.

## 13. Expansion Gate

Do not expand from compact or micro-task mode into a heavier workflow unless at least one condition is true:

- scope is genuinely broad;
- risk is non-trivial;
- review needs several distinct artifacts;
- handoff needs a structured packet;
- future reuse or continuation clearly depends on richer state.

If a useful result can be achieved through one message, one Notion update, one file, one issue, one packet, or one short artifact, that lighter path should win by default.

The full workflow is a map, not mandatory bureaucracy.
