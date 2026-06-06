# Project Execution OS Router

## Purpose

This is the live internal router for `Project Execution OS`.

`START_HERE.md` is the stable external entrypoint. It should remain minimal and durable.

This router may evolve as the internal system grows. Its job is to route an agent to the smallest relevant internal node for the current work.

## Routing Rule

Choose the narrowest route that fits the active request.

Do not read every standard by default.

Do not append an unrelated next-project question after answering the active request.

## Routes

- possible new project or new initiative -> `Start New Project.md`
- operating-mode uncertainty -> `docs/MODE_CLASSIFIER.md`
- explicit preservation intent such as save, capture, record, remember, add to library, add to project, or do not lose this -> `docs/AUTOMATIC_CAPTURE_STANDARD.md`
- idea or reference that should be preserved but is not yet a project -> `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- lifecycle or storage-layer decision -> `docs/PROJECT_LIFECYCLE_MODEL.md`
- website design, landing-page design, page structure, wireframe, UI system, responsive UI spec, or website design review -> `blocks/design/BLOCK.md`
- music generation, soundtrack design, adaptive music, real-time music, music-agent behavior, generated-music rights review, or music-tool evaluation -> `blocks/music/BLOCK.md`
- Telegram bots, Telegram Mini Apps, Telegram Business or Secretary Bots, Managed Bots, Telegram Login, Telegram Gateway, Telegram Stars, Bot API, TDLib, MTProto, or Telegram integrations -> `blocks/telegram/BLOCK.md`
- immigration law, USCIS, Form I-485, marriage-based adjustment of status, consular processing, immigration interviews, RFEs, NOIDs, immigration travel risk, or USCIS PM-602-0199 -> `blocks/us-law/immigration/BLOCK.md`
- United States law, federal or state legal research, statutes, regulations, court rules, case law, legal deadlines, legal-risk triage, attorney handoff preparation, or legal-source automation -> `blocks/us-law/BLOCK.md`
- indexing or repository catalog work -> `docs/INDEXING_STANDARD.md`
- current-project summary, status, orientation, or "where are we now?" question -> read the current project's entrypoint and only the minimum necessary current-state evidence; answer the question directly; stop after the answer; do not trigger `Start New Project.md` or ask which new project to create unless the owner explicitly requests a new project
- entry into a specific existing project -> that project's current entrypoint; prefer `PROJECT.md`, fall back to legacy `PROJECT_ENTRYPOINT.md` only during migration, and use `docs/PROJECT_ENTRYPOINT_STANDARD.md` if no project entrypoint exists
- transfer readiness, executor continuity, durable state maintenance, or handoff survivability -> `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- create, review, register, migrate, deprecate, or retire a reusable skill -> `blocks/skill-creator/BLOCK.md`
- multi-layer context assembly, selective knowledge loading, or API context/caching design -> `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- small bounded existing-project action -> `docs/MICRO_TASK_MODE.md`
- agent re-entry into an existing GitHub-backed project, handoff between agents, or request to inspect only changes since prior work -> `docs/INCREMENTAL_REENTRY_STANDARD.md`
- research task -> `docs/RESEARCH_STANDARD.md`
- review task -> `docs/REVIEW_STANDARD.md`
- already-decided Codex execution handoff -> `docs/CODEX_HANDOFF_ENTRYPOINT.md`
- communication channel, connected-agent communication, message transport, `01`, `02`, channel selection, or coordination-path uncertainty -> `blocks/communication-channel/BLOCK.md`
- stable ChatGPT system-layer configuration -> `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
- central knowledge capture, promotion, review, selective loading or retirement -> `docs/KNOWLEDGE_SYSTEM.md`
- repository-memory question for this system or a GitHub-backed project -> `docs/REPOSITORY_MEMORY_STANDARD.md`
- system-context profile identity, fingerprint or compatibility question -> `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- API token usage, cost or provider cache measurement -> `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`

## Boundary

This router stores navigation only.

Do not place detailed operating procedures, project state, implementation plans, tool commands, API credentials, logs or reusable knowledge content in this file.

## Final Rule

`START_HERE.md` is the stable door.

This file is the live internal map.

Choose the path, answer the active request, and stop unless the owner asked for another action.