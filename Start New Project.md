# Start New Project

## BOOT MODE

This file is the only canonical startup entrypoint for a new project in Project Execution OS.

Language rule:
- respond to the user in Russian by default;
- keep technical English terms when useful, but add a Russian explanation next to them;
- if the user explicitly requests another language, follow the user request.

## HARD STOP

Do not invent your own startup workflow.
Do not skip this file.
Do not replace it with your own interpretation.
Do not design architecture yet.
Do not write code yet.
Do not create agents yet.
Do not start backend, frontend, runtime, database, or automation work yet.

Ask only this first question now:

### Question 1

Какую идею или проект разрабатываем?

After the user answers Question 1, ask in Russian:

### Question 2

Где должен жить этот проект?

Options:
- A) создать новый private GitHub repository (приватный репозиторий GitHub)
- B) использовать existing repository (существующий репозиторий)
- C) создать folder (папку) внутри Project Execution OS только как исключение
- D) brainstorm-only mode (режим брейншторма) без создания проекта
- E) не знаю
- F) свой вариант

After Question 2 is answered:
- create or use repository artifacts as the source of truth;
- use the smallest useful workflow;
- ask only necessary clarification;
- avoid overengineering;
- route into the deeper standards listed below only when needed.

## DEFAULT PROJECT RULES

- one project = one dedicated private GitHub repository by default;
- public repositories are an explicit user choice, not the default;
- every new repository gets a short clear bilingual GitHub description at creation time;
- in that description, Russian comes first and English second;
- Project Execution OS is the central brain, not the default storage place for project execution history.

If the user wants brainstorming only, use `brainstorm-only mode`.

If the user points to an older non-standard repository or folder, use `legacy-project-normalization mode`.

If the work is project-bound and already has a suitable GitHub issue, PR, or review thread, use the existing coordination channel first instead of creating a new one.

If a direct runtime bridge to Codex does not exist but a GitHub coordination surface exists, use GitHub as the transport layer to Codex.

## ROUTING INTO THE BRAIN

Read deeper rules only when they are actually needed:

- project modes: `docs/PROJECT_ENTRY_MODES.md`
- workflow chain and compact mode: `docs/WORKFLOW_CONTRACT.md`
- project location and structure: `docs/PROJECT_STRUCTURE_STANDARD.md`
- repository memory and project memory: `docs/REPOSITORY_MEMORY_STANDARD.md`
- graph memory: `docs/GRAPHIFY_STANDARD.md`
- research rules: `docs/RESEARCH_STANDARD.md`
- review rules: `docs/REVIEW_STANDARD.md`
- Codex handoff and packet formats: `docs/CODEX_HANDOFF_STANDARD.md`
- GitHub coordination with Codex: `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`
- coordination hub policy: `docs/AI_COORDINATION_HUB_STANDARD.md`
- agent creation rules: `docs/AGENT_CREATION_STANDARD.md`
- central reusable agents: `agent-library/PROJECT_INDEX.md`
- central reusable skills: `skills/PROJECT_INDEX.md`
- deferred future-system ideas: `docs/DEFERRED_SYSTEM_IDEAS.md`

## RESPONSE BEHAVIOR

For a new project:
- ask Question 1;
- ask Question 2;
- choose the smallest useful workflow;
- preserve the idea in repository artifacts;
- move into deeper standards only when the task truly requires them.

Do not turn the startup into ceremony.

Do not force the full workflow when compact mode or brainstorming mode is enough.

Do not use Codex for small safe reasoning, drafting, or documentation tasks that can be completed directly without executor access.

## FINAL RULE

This file is a boot-router, not the full operating system.

Use it to start correctly.
Use Project Execution OS to go deeper.
