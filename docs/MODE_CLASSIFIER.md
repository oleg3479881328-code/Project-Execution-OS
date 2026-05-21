# Mode Classifier

## Purpose

Use this classifier before expanding into workflow, repository creation, or deeper standards.

The goal is to decide the lightest correct operating mode as early as possible.

## Default Rule

Do not assume every request is a new project.

Classify first.
Expand second.

## Classifier

### Mode A — New Project

Use when:
- the user is clearly starting a new project;
- no durable project repository exists yet;
- the work should enter the operating system from zero.

### Mode B — Existing Project Work

Use when:
- the user points to an existing repository or project;
- the task is to continue, review, document, or implement inside that existing project.

### Mode C — Micro-Task

Use when:
- the task is tiny, safe, and bounded;
- the likely useful result fits in one short pass;
- a full workflow would be heavier than the work itself.

### Mode D — Discussion / Answer-Only

Use when:
- the user is asking for an opinion, explanation, comparison, translation, wording, or short analysis;
- no project memory needs to be created yet;
- the answer itself is the useful result.

### Mode E — Research-Only

Use when:
- the main need is investigation, comparison, source gathering, or pattern discovery;
- no project structure or implementation should be started yet.

### Mode F — Brainstorm-Only

Use when:
- the idea is still exploratory;
- the user wants options, framing, or direction before deciding whether a project should exist.

### Mode G — Legacy Project Normalization

Use when:
- the user gives an older repository or folder;
- the work is to bring it into the current operating model.

### Mode H — Codex Handoff

Use when:
- the reasoning is already sufficient;
- executor access is now the main missing step;
- the next correct artifact is a bounded packet for Codex.

## Fast Questions

If the mode is unclear, ask only the minimum needed:

1. Is this a new project, existing repo task, or just a quick answer?
2. Does this need durable project state, or is the answer itself enough?
3. Does this require Codex execution, or can it be completed directly?

## Escalation Rule

Start in the lightest plausible mode.

Escalate only when the task proves it needs:
- durable project state;
- richer review;
- broader research;
- structured handoff;
- future continuity.
