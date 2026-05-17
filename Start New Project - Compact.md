# Start New Project — Compact

## Purpose

This file is the minimal bootstrap for starting a new project with any AI system.

This is NOT a request to redesign Project Execution OS.

This is a request to START a new project using the workflow system.

## Immediate Behavior

The AI must first do only this:

### Question 1

What idea or project are we developing?

### Question 2

Where should this project live?

Options:
- A) create a new GitHub repository
- B) use an existing repository
- C) create a folder inside Project Execution OS
- D) I do not know yet
- E) other

Do not:
- design architecture yet;
- write code yet;
- create agents yet;
- create runtime/backend/frontend yet;
- create automation systems yet.

## Core Model

Repository is the source of truth.

Chat is temporary.

Important work must become repository artifacts.

## Workflow

Use the smallest useful workflow.

Default workflow:

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

Small tasks may use a compact workflow.

## Core Rules

The AI must:
- use MVP-first thinking;
- ask one question at a time when clarification is needed;
- prefer reuse before building from scratch;
- separate facts from assumptions;
- review before important execution;
- verify execution before accepting it;
- extract reusable knowledge after meaningful work.

The AI must not:
- overengineer;
- jump directly into coding;
- create giant architectures too early;
- invent repository state;
- claim execution without evidence;
- mass-generate files without reason.

## Codex Interaction Model

Reasoning model thinks.
Codex executes.
Reviewer verifies.
Repository memory persists.

Bad Codex prompt:

```text
Improve the project.
```

Good Codex prompt:

```text
Read these files.
Modify only these paths.
Do not redesign architecture.
Follow acceptance criteria.
Return execution report.
```

## Skills

Skills are reusable workflow instructions.

Skills live in:

```text
skills/
```

Use only the smallest useful set of skills.

Core useful skills:
- repository research;
- brainstorming;
- design review;
- implementation handoff;
- execution review;
- repository memory update.

## Knowledge Library

Reusable knowledge lives in:

```text
knowledge-library/
```

Extract reusable patterns after meaningful work.

## Agent Rules

Agents are optional.

Do not create agents by default.

Create agents only if:
- specialized repeated work exists;
- quality improves from role separation;
- workflow complexity justifies it.

## MVP Rule

A simple working workflow is better than a perfect unfinished system.

Do not add abstraction layers unless real workflow evidence proves they are needed.

## Default Response

After reading this file, respond with:

```text
I understand this is a new project start.

Question 1:
What idea or project are we developing?
```
