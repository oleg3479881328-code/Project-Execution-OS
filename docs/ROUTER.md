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

- project knowledge database, central operational database, structured source of truth, photographer knowledge engine, SEO knowledge database, Page Queue, Media registry, Geography layer, Redirects/URLs registry, QA dashboard, ID Crosswalk architecture, Knowledge Database to Page Factory, structured website production pipeline, or migration from scattered project tables into one production datastore -> `docs/PROJECT_KNOWLEDGE_DATABASE_STANDARD.md`
- entity, business, person, vendor, venue, organization, tool, platform, website/domain, publication/profile, reusable node, identity resolution, deduplication, entity enrichment, dossier, canonical card, aliases/rebrands, repeated research prevention, or cross-project entity reuse -> `docs/ENTITY_DOSSIER_STANDARD.md`
- possible new project or new initiative -> `Start New Project.md`
- `личный секретарь`, `секретарь`, `режим секретаря`, `режим личного секретаря`, `личный помощник`, `помощник`, `режим помощника`, personal secretary, or personal assistant -> `projects/personal-secretary-os/PROJECT.md`
- operating-mode uncertainty -> `docs/MODE_CLASSIFIER.md`
- `03`, explicit START_HERE re-entry, instruction to look up repository rules by active topic, or correction that the agent should not rely on chat memory -> `docs/COMMAND_03_START_HERE_LOOKUP_STANDARD.md`
- explicit preservation intent such as save, capture, record, remember, add to library, add to project, or do not lose this -> `docs/AUTOMATIC_CAPTURE_STANDARD.md`
- idea or reference that should be preserved but is not yet a project -> `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- durable file creation, artifact storage destination, folder placement, cleanup, import, upload, export, backup, or concern about scattered files -> `docs/FILE_ORGANIZATION_STANDARD.md`
- lifecycle or storage-layer decision -> `docs/PROJECT_LIFECYCLE_MODEL.md`
- website design, landing-page design, page structure, wireframe, UI system, responsive UI spec, or website design review -> `blocks/design/BLOCK.md`
- Impeccable, AI-coded frontend design QA, AI-slop review, frontend design detector, UI polish/audit after AI coding, or design quality gate for coded web UI -> `blocks/design/IMPECCABLE_DESIGN_QA_GATE.md`
- Chrome Extension, browser extension, Manifest V3, extension content scripts, extension service workers, Chrome Web Store publishing, extension monetization, or extension payments -> `blocks/chrome-extension/BLOCK.md`
- YouTube channel strategy, YouTube Shorts publishing strategy, YouTube long-form strategy, YouTube Partner Program, YPP, YouTube monetization, YouTube copyright, reused content, Content ID, YouTube analytics, YouTube playlists, YouTube Data API, YouTube uploads, or multilingual YouTube channels -> `blocks/youtube/BLOCK.md`
- Video Production, video factory, reels factory, short-form editing, TikTok videos, yt-dlp, ffmpeg, CapCut, automated clipping, multilingual video production, AI voice, AI avatar, or QuizLight video-card extraction -> `blocks/video-production/BLOCK.md`
- reusable executable block, capability block, plug-in functionality, portable code module, shared transcription module, shared download module, shared clipping module, composable application capability, or request to build functionality once and reuse it across applications -> `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`
- server rental, VPS, cloud server, GPU rental, pay-as-you-go compute, serverless GPU, rented AI infrastructure, China server, Hong Kong server, GPU instance selection, ComfyUI hosting, open-source LLM endpoint hosting, or hybrid compute routing -> `blocks/server-rental/BLOCK.md`
- Solana, Solana dApp, wallet-connected app, Anchor program, SPL Token, Token Extensions, Solana payments, Solana NFT, Solana DeFi, Solana marketplace, Solana RPC, or Solana program security -> `blocks/solana/BLOCK.md`
- logic concepts, argument structure, cause-and-effect analysis, fallacy detection, assumption review, contradiction check, or decision-quality reasoning review -> `blocks/logic/BLOCK.md`
- music generation, soundtrack design, adaptive music, real-time music, music-agent behavior, generated-music rights review, or music-tool evaluation -> `blocks/music/BLOCK.md`
- Telegram bots, Telegram Mini Apps, Telegram Business or Secretary Bots, Managed Bots, Telegram Login, Telegram Gateway, Telegram Stars, Bot API, TDLib, MTProto, or Telegram integrations -> `blocks/telegram/BLOCK.md`
- Notion workspace architecture, Notion project registry, Notion project template, PROJECT_ID routing, Notion agent re-entry, Notion MCP, Notion API, Notion database schema, Notion and GitHub coordination, or Notion synchronization design -> `blocks/notion/BLOCK.md`
- OSINT, open-source intelligence, public-source investigation, публичная разведка, расследовательский поиск, investigative research, проверка компании, проверка подрядчика, проверка сайта, проверка домена, due diligence, репутационная проверка, scam risk review, fraud risk review, evidence log, source verification, timeline reconstruction -> `blocks/osint/BLOCK.md`
- Ohio taxes, Ohio municipal income tax, RITA, CCA, Ohio gig-economy income, Ohio DoorDash income, Ohio LLC, Ohio small-business tax routing, Ohio payroll, Ohio unemployment tax, Ohio sales tax, or Ohio tax deadlines -> `blocks/us-tax-accounting/ohio/BLOCK.md`
- United States taxation, bookkeeping, accounting operations, self-employment income, gig-economy income, estimated taxes, LLC tax classification, payroll, contractors, W-2, 1099, sales tax, monthly close, year-end close, CPA handoff, EA handoff, or tax-accounting tool selection -> `blocks/us-tax-accounting/BLOCK.md`
- immigration law, USCIS, Form I-485, marriage-based adjustment of status, consular processing, immigration interviews, RFEs, NOIDs, immigration travel risk, or USCIS PM-602-0199 -> `blocks/us-law/immigration/BLOCK.md`
- United States law, federal or state legal research, statutes, regulations, court rules, case law, legal-risk triage, attorney handoff preparation, or legal-source automation -> `blocks/us-law/BLOCK.md`
- indexing or repository catalog work -> `docs/INDEXING_STANDARD.md`
- create, expand, review, or formalize a reusable domain block -> `skills/orchestration/domain-block-creation/SKILL.md`
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
- `0.2`, `02`, check executor reply, check executor answer, проверить ответ исполнителя, or status check of an executor handoff -> `docs/COMMAND_02_EXECUTOR_REPLY_CHECK_STANDARD.md`
- communication channel, connected-agent communication, message transport, `01`, `10`, channel selection, route recovery, or coordination-path uncertainty -> `blocks/communication-channel/BLOCK.md`
- stable ChatGPT system-layer configuration -> `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
- central knowledge capture, promotion, review, selective loading or retirement -> `docs/KNOWLEDGE_SYSTEM.md`
- repository-memory question for this system or a GitHub-backed project -> `docs/REPOSITORY_MEMORY_STANDARD.md`
- system-context profile identity, fingerprint or compatibility question -> `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- API token usage, cost or provider cache measurement -> `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- harness engineering, agent harness, agent runtime scaffold, agent tool/context/permission design, sandbox/memory/verification scaffold, or reliability architecture before agent operation -> `docs/HARNESS_ENGINEERING_STANDARD.md`
- agent quality, cost per successful outcome, evals, regression protection, observability, tool-use quality, orchestration complexity, or agent comparison -> `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`

## Boundary

This router stores navigation only.

Do not place detailed operating procedures, project state, implementation plans, tool commands, API credentials, logs or reusable knowledge content in this file.

## Final Rule

`START_HERE.md` is the stable door.

This file is the live internal map.

Choose the path, answer the active request, and stop unless the owner asked for another action.