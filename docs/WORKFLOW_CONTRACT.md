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

## 2. Core Principle

Do not build giant architecture before the project has passed through a clear workflow.

Execution quality is more important than architectural fantasy.

Default operating gate:

`compact-first`

Default project-location rule:

Each project should use its own dedicated private GitHub repository unless there is an explicit reason to use compact or internal mode.

## 3. Universal Workflow Chain

The full workflow is the reference model.

Compact mode is the default execution form.

Expand into the full file chain only when scope, risk, review, handoff, or reuse requires it.

Reference chain:

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

## 4. Stage Definitions

### 00_INPUT.md

Stores the raw project idea, request, problem, goal, source material, or task.

Must preserve original intent without over-interpreting it.

### 01_CLARIFICATION.md

Clarifies ambiguity, constraints, success criteria, scope, risks, and missing context.

Must avoid endless questioning.

### 02_RESEARCH.md

Finds reusable patterns, open-source examples, official documentation, publicly verifiable external sources, prior project artifacts, known risks, and similar systems.

Research must be reuse-first and evidence-backed when possible.

### 03_PLAN.md

Converts clarified intent and research into a practical MVP-first plan.

The plan must define sequence, outputs, constraints, and stop conditions.

### 04_AGENT_DESIGN.md

Defines which task-specific agents are needed for this project.

If no specialized agent is needed, this file must say so.

Agents must not be created by default.

### 05_EXECUTION_SPEC.md

Defines what must be built, written, tested, purchased, researched, decided, or handed to a coder.

For software projects, this becomes implementation-ready specification.
For non-software projects, this becomes action-ready execution brief.

### 06_REVIEW.md

Audits the plan, execution spec, agent design, assumptions, evidence, risks, contradictions, and missing pieces.

Nothing important should become stable without review.

### 07_RESULT.md

Records the result of the workflow run.

The result may be a decision, document, specification, recommendation, design, or completed artifact.

### 08_KNOWLEDGE_EXTRACT.md

Extracts reusable lessons, patterns, anti-patterns, templates, and decisions.

Reusable knowledge must be separated from one-off project output.

### 09_LOG.md

Records what happened, what changed, what was decided, what remains open, and what should happen next.

## 5. State Separation

The system must distinguish:

- generated state: proposed by AI or user but not committed;
- committed state: written to repository;
- reviewed state: checked by review;
- active state: approved for reuse.

No agent may claim that something is executed, saved, committed, tested, reviewed, active, or complete without evidence.

## 6. Agent Rule

Agents are replaceable execution modules.

They may be created only when needed for:

- a workflow stage;
- a domain bottleneck;
- a quality bottleneck;
- a recurring project function.

The workflow contract is stable.
Agents are optional.

## 7. Knowledge Rule

Every workflow run must produce `08_KNOWLEDGE_EXTRACT.md`.

Knowledge can stay local to the project or be promoted to the central knowledge library after review.

## 8. First Validation Rule

Before automation, runtime, or orchestration is built, complete manual project runs using this workflow.

Automation is allowed only after repeated workflow evidence shows what should be automated.

## 9. Success Criteria

The workflow is acceptable only if it:

- works for many project types;
- keeps project state visible;
- prevents fake execution claims;
- supports project-specific agents;
- preserves reusable knowledge;
- keeps project libraries and central knowledge separate;
- produces one concrete next action per run.

## 10. Compact Mode

Compact mode is allowed for small or low-risk projects.

Compact mode is the default unless there is a concrete reason to expand into a heavier workflow.

Compact mode may use fewer files than the full workflow reference chain, but it must preserve:

- source-of-truth repository artifacts;
- explicit clarification when needed;
- bundled clarification when several answers belong to one package;
- evidence-backed research when research is required;
- review before stable acceptance;
- logging of result and next action;
- reusable knowledge extraction when relevant.

Clarification rule:

When multiple user answers are needed to complete one coherent artifact such as an AI-ready package, gather those answers in chat first and then write one repository update for the completed package unless the user explicitly asks for per-answer persistence.

## 11. Micro-Task Mode

Micro-task mode is allowed for tiny, safe, low-risk work that does not justify a full workflow run.

Use the minimal shape:

```text
goal -> action -> result -> short review note -> next action
```

Micro-task mode should prefer direct completion over ceremony.

## 12. Artifact Only When Useful

Do not create a file artifact just because a workflow stage exists in theory.

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

If a useful result can be achieved through `1 file`, `1 issue`, `1 packet`, or `1 short artifact`, that lighter path should win by default.

The full workflow is a map, not mandatory bureaucracy.
