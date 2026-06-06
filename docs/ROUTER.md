# Project Execution OS Router

## Purpose

This is the live internal router for `Project Execution OS`.

`START_HERE.md` is the stable external entrypoint. It should remain minimal and durable.

This router may evolve as the internal system grows. Its job is to route an agent to the smallest relevant internal node for the current work.

## Routing Rule

Choose the narrowest route that fits the active request.

Do not read every standard by default.

When the active request enters an already active project rather than zero-state bootstrap, load the continuity rule early enough to preserve transfer-ready state during the same work step.

Do not append an unrelated next-project question after answering the active request.

## Routes

- possible new project or new initiative -> `Start New Project.md`
- operating-mode uncertainty -> `docs/MODE_CLASSIFIER.md`
- idea or reference that should be preserved but is not yet a project -> `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- lifecycle or storage-layer decision -> `docs/PROJECT_LIFECYCLE_MODEL.md`
- indexing, semantic retrieval, repository discovery layer, or index-first agent entry -> `docs/INDEXING_STANDARD.md`
- website design, landing-page design, page structure, wireframe, UI system, responsive UI spec, or website design review -> `blocks/design/BLOCK.md`
- deployment, hosting, publish, static site release, Cloudflare Pages, domain for static/frontend project -> `docs/DEPLOYMENT_STANDARD.md`
- current-project summary, status, orientation, or "where are we now?" question -> read the current project's entrypoint and only the minimum necessary current-state evidence; answer the question directly; stop after the answer; do not trigger `Start New Project.md` or ask which new project to create unless the owner explicitly requests a new project
- entry into a specific existing project -> that project's current entrypoint; prefer `PROJECT.md`, fall back to legacy `PROJECT_ENTRYPOINT.md` only during migration, and use `docs/PROJECT_ENTRYPOINT_STANDARD.md` if no project entrypoint exists; if the project already shows active execution evidence such as `PROJECT_STATE.md` or `logs/latest.md`, also read `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` before meaningful work
- transfer readiness, executor continuity, durable state maintenance, or handoff survivability -> `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- create, review, register, migrate, deprecate, or retire a reusable skill -> `blocks/skill-creator/BLOCK.md`
- multi-layer context assembly, selective knowledge loading, or API context/caching design -> `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- small bounded existing-project action -> `docs/MICRO_TASK_MODE.md`
- agent re-entry into an existing GitHub-backed project, handoff between agents, or request to inspect only changes since prior work -> `docs/INCREMENTAL_REENTRY_STANDARD.md`
- research task -> `docs/RESEARCH_STANDARD.md`
- review task -> `docs/REVIEW_STANDARD.md`
- already-decided Codex execution handoff -> `docs/CODEX_HANDOFF_STANDARD.md`
- communication channel, connected-agent communication, message transport, `01`, `02`, channel selection, or coordination-path uncertainty -> `blocks/communication-channel/BLOCK.md`
- stable ChatGPT system-layer configuration -> `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
- central knowledge capture, promotion, review, selective loading or retirement -> `docs/KNOWLEDGE_SYSTEM.md`
- repository-memory question for this system or a GitHub-backed project -> `docs/REPOSITORY_MEMORY_STANDARD.md`
- system-context profile identity, fingerprint or compatibility question -> `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- any API-based AI model integration, API token usage, cost analysis, prompt-cache design, or provider cache measurement -> `knowledge-library/execution-standards/api-model-runtime-cache-gate.md` -> `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`

## Boundary

This router stores navigation only.

Do not place detailed operating procedures, project state, implementation plans, tool commands, API credentials, logs or reusable knowledge content in this file.

## Final Rule

`START_HERE.md` is the stable door.

This file is the live internal map.

Choose the path, answer the active request, and stop unless the owner asked for another action.
