# Start New Project

## CONTRACT

Purpose: canonical boot-router for starting a project through Project Execution OS.

This file is not the full operating system.

Language:
- respond in Russian by default;
- keep useful technical English terms with short Russian explanations;
- follow explicit user language requests.

## BOOT DECISION

First classify the user request.

Use `docs/MODE_CLASSIFIER.md` when the mode is unclear.

If the request is not a new project start, do not ask the project startup questions.

Allowed non-start modes:
- discussion / answer-only;
- micro-task;
- research-only;
- brainstorm-only;
- idea capture / reference triage;
- existing project work;
- legacy project normalization;
- Codex handoff.

If the user asks to create a project but gives no project idea, do not infer the idea.

Ask `Question 1` and wait.

If the user changes intent during startup and says they want only to discuss the idea, stop the startup sequence immediately and switch to the lightest correct non-start mode.

## NEW PROJECT START

### Question 1

Какую идею или проект разрабатываем?

After the user answers Question 1, ask:

### Question 2

Где должен жить этот проект?

Options:
- A) создать новый private GitHub repository (приватный репозиторий GitHub)
- B) использовать existing repository (существующий репозиторий)
- C) создать folder (папку) внутри Project Execution OS только как исключение
- D) brainstorm-only mode (режим брейншторма) без создания проекта
- E) не знаю
- F) свой вариант

## MUST

- default to `compact-first`;
- use the smallest useful workflow;
- create a short `STARTUP STATE` after Question 1 and Question 2;
- use repository artifacts as durable source of truth when state must persist;
- create artifacts only when they will actually be useful later;
- ask only necessary clarification;
- route into deeper standards only with a concrete reason.

## MUST NOT

- invent a startup workflow;
- skip this file for a new project start;
- replace this file with interpretation;
- guess the project idea;
- design architecture before startup state exists;
- write code before the task is classified;
- create agents before they are needed;
- start backend, frontend, runtime, database, or automation layers before a first useful result exists;
- expand into full workflow when `1 file`, `1 issue`, `1 packet`, or `1 short artifact` is enough;
- read deeper standards just because they exist.

## STARTUP STATE FORMAT

```text
STARTUP STATE

Project idea:
Project mode:
Storage decision:
Current next action:
Forbidden now:
```

## DEFAULT PROJECT RULES

- one project = one dedicated private GitHub repository by default;
- public repositories are an explicit user choice;
- every new repository gets a short bilingual GitHub description;
- Russian comes first, English second;
- Project Execution OS is the central brain, not the default storage place for all project history.

## WHEN

- if user wants idea exploration only -> use `brainstorm-only mode`;
- if user wants to discuss an idea and avoid losing it without starting a project -> use `reference idea capture`;
- if user points to an older non-standard repo -> use `legacy-project-normalization mode`;
- if project-bound GitHub issue, PR, or review thread already exists -> use it first;
- if no direct Codex runtime bridge exists but GitHub coordination exists -> use GitHub as Codex transport;
- if Codex execution is next -> next artifact is `Implementation Handoff Packet`.

## ROUTING TRIGGERS

- mode unclear -> `docs/MODE_CLASSIFIER.md`
- workflow weight unclear -> `docs/WORKFLOW_DECISION_TABLE.md`
- small safe task -> `docs/MICRO_TASK_MODE.md`
- workflow or compact mode needed -> `docs/WORKFLOW_CONTRACT.md`
- project structure needed -> `docs/PROJECT_STRUCTURE_STANDARD.md`
- memory recovery needed -> `docs/REPOSITORY_MEMORY_STANDARD.md`
- graph navigation needed -> `docs/GRAPHIFY_STANDARD.md`
- research needed -> `docs/RESEARCH_STANDARD.md`
- review needed -> `docs/REVIEW_STANDARD.md`
- idea should not be lost but is not yet a project -> `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- Codex execution next -> `docs/CODEX_HANDOFF_STANDARD.md`
- GitHub coordination needed -> `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`
- coordination hub needed -> `docs/AI_COORDINATION_HUB_STANDARD.md`
- agent creation needed -> `docs/AGENT_CREATION_STANDARD.md`
- central reusable agents needed -> `agent-library/PROJECT_INDEX.md`
- central reusable skills needed -> `skills/PROJECT_INDEX.md`
- deferred system idea appears -> `docs/DEFERRED_SYSTEM_IDEAS.md`

## OUTPUT FORMAT

For a new project start, respond with only the next required startup question until Question 1 and Question 2 are answered.

After Question 1 and Question 2, output the short `STARTUP STATE` and the next action.

For non-start modes, answer or act in the lightest correct mode.

Do not re-announce that you are re-checking the startup entrypoint after the mode has already switched away from project start.

Do not format a simple idea-discussion prompt as `Question 1 of 1`.

Prefer natural phrasing such as:

`В чем идея, которую хочешь обсудить?`

## FINAL RULE

Classify first.

Start small.

Expand only when the task proves it needs more structure.
