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

## 3. Universal Workflow Chain

Every meaningful project run must use this chain:

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

Finds reusable patterns, open-source examples, documentation, prior project artifacts, known risks, and similar systems.

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
