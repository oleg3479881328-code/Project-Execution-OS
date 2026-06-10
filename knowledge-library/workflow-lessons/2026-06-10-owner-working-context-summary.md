# Owner Working Context Summary — Oleg Povalyukhin

- Type: workflow-lesson
- Lifecycle status: captured
- Date: 2026-06-10
- Source: accumulated conversations with the owner
- Review status: not yet reviewed for promotion to active reusable guidance

## Purpose

Preserve a structured working-context summary so future agents can understand the owner's recurring projects, preferences, operating style, and active lines of work without relying on chat memory alone.

## Owner Profile

Oleg uses ChatGPT as an execution partner across technical, operational, research, and business projects. He prefers directness, practical implementation, and durable capture of useful decisions. He frequently works from a phone while driving or away from a desk, so instructions should be easy to execute step by step.

## Communication Preferences

- Prefer Russian by default unless the owner switches language.
- When giving an English definition, also provide the Russian translation.
- For step-by-step work, use one question, one answer, one action at a time.
- Avoid unnecessary softening. State clearly when an idea is weak, risky, or inefficient.
- When offering multiple options, add a clear recommendation.
- For terminal commands, provide copy-ready commands.
- Preserve useful decisions and reusable lessons durably when asked; chat-only summaries are insufficient.

## Project Execution OS Preferences

- Use `START_HERE.md` as the canonical top-level entrypoint for project-related work.
- Follow the route selected by `docs/ROUTER.md`; do not invent a parallel workflow.
- The owner expects durable capture into the correct knowledge or project layer whenever he asks to save, record, preserve, remember, add to the library, or avoid losing information.
- The owner values transfer-ready project state so a new agent can continue work without rereading entire chat histories.

## Active And Recurring Workstreams

### 1. Project Execution OS

The owner is building a reusable project operating system for agent-assisted execution. Important themes:

- repository-first source of truth;
- explicit routing from a single top-level entrypoint;
- domain blocks and reusable skills;
- transfer-ready state;
- selective context loading rather than reading everything;
- central knowledge library for reusable lessons;
- project-specific storage when knowledge belongs to one project;
- Codex handoff only after planning and decisions are ready.

### 2. AI Agent Quality And Cost Control

The owner is interested in evaluating agents with engineering metrics rather than prompt aesthetics. Topics discussed include:

- cost per successful outcome;
- token usage and cache efficiency;
- latency;
- retry count;
- correctness and hallucination rate;
- tool-use quality;
- observability;
- regression protection;
- orchestration complexity.

### 3. Server Rental And Compute Strategy

The owner is researching server rental, including China and Hong Kong, for AI workloads and possible video-factory infrastructure. Relevant topics:

- VPS and GPU rental;
- pay-as-you-go compute;
- serverless GPU;
- hybrid compute routing;
- open-source LLM hosting;
- ComfyUI hosting;
- cost comparison between providers;
- whether rented infrastructure is preferable to buying hardware.

### 4. Video Factory / Reels Factory

The owner is exploring a scalable short-form video production system for Facebook Reels, TikTok, and YouTube Shorts. Key themes:

- multilingual production;
- AI voiceover and possible avatars;
- automated clipping;
- CapCut, ffmpeg, and yt-dlp workflows;
- testing short videos quickly;
- large-scale publishing and monetization;
- affiliate marketing;
- reuse of content across languages;
- possible server-based automation.

The owner prefers anonymity and does not want to use his own voice or appear on camera by default.

### 5. Telegram Products

The owner is exploring Telegram bots and mini-apps, including:

- news-digest bots with AI summarization;
- mini-app builders;
- SaaS products for Telegram;
- channel analytics;
- integration and monetization opportunities.

### 6. QuizLight / Language Learning By Video

The owner proposed a separate module for learning languages from video:

- watch a video or series in a normal player;
- switch into card-creation mode;
- open transcript;
- click a timestamp or phrase;
- generate a multimedia context card;
- include phrase, translation, image, nearby transcript context, meaning block, and start/end playback.

This idea should remain available for future QuizLight work.

### 7. Chrome Extension Block

The owner requested a reusable Chrome Extension domain block. Important expectations:

- include search for existing solutions;
- include useful libraries;
- include monetization options;
- include payment-system considerations;
- produce a plan before Codex execution handoff.

### 8. Design Catalog / Design Block

The owner wants a design-selection workflow where he can browse a catalog and point to preferred styles. This should support concrete visual references and easier design decisions before implementation.

### 9. Notion Agent Re-entry System

The owner wants a Notion-oriented system analogous to Project Execution OS, so agents can enter any project, understand state, and continue work consistently.

### 10. DoorDash And Gig-Economy Operations

The owner has explored delivery work strategy in the Cincinnati / Ohio area. Topics include:

- profitable zones and dead zones;
- restaurant database;
- acceptance rules;
- dollars per mile and dollars per hour;
- waiting-time reduction;
- local mapping;
- equipment;
- multi-platform expansion such as Uber Eats and Instacart.

### 11. Immigration And USCIS Research

The owner has asked for practical U.S. immigration research and preparation, especially around adjustment of status, marriage-related cases, interviews, attorney presence, RFEs, consular processing, and current policy changes. This is high-stakes work and should be handled with current primary-source research and clear uncertainty boundaries.

## English Learning Preferences

The owner wants English learning at approximately a 10-year-old native-speaker level by default. Relevant preferences:

- simple, natural phrases;
- Russian translation whenever English definitions are used;
- IPA and Russian-style phonetic transcription for new phrases when useful;
- Quizlet-style formatting when requested;
- compact learning cards;
- vintage pin-up educational poster style for visual vocabulary materials;
- Russian explanation text on educational posters, while the target word or phrase remains in English.

## Technical Context

The owner works primarily on Windows 11 and has used:

- VS Code;
- PowerShell;
- CapCut Desktop;
- ffmpeg;
- yt-dlp;
- AI media-generation tools;
- GitHub repositories;
- mobile access from Android.

Remote-control and session-continuity workflows are relevant because the owner may need to control a desktop session from a phone.

## Operational Rules For Future Agents

- Start project-related work from `START_HERE.md` and follow the smallest relevant router path.
- Do not treat chat memory as the source of truth when repository evidence exists.
- Use current web research for unstable facts, prices, policies, software changes, laws, immigration topics, and product recommendations.
- Prefer primary sources for technical and high-stakes research.
- For implementation guidance, provide practical next actions rather than abstract commentary.
- Preserve new project decisions in the appropriate durable layer when the owner explicitly requests capture.
- Keep system-wide lessons separate from project-only details.

## Risks And Limitations

- This entry summarizes prior conversations and may contain stale operational details.
- It is a captured context document, not an active system rule.
- Sensitive personal details should not be expanded unless necessary for the active task.
- Project-specific state should be checked in each project's own entrypoint before execution.

## Applies To

- owner-context orientation;
- agent re-entry;
- project handoff;
- communication style adaptation;
- selecting which project route to open first.

## Triggers

Load this entry when:

- a new agent needs orientation about the owner;
- a task spans multiple known workstreams;
- the owner refers to prior discussions but the active chat lacks context;
- communication style or execution format materially affects correctness.

## Do Not Load When

Do not load this entry for:

- isolated factual questions unrelated to the owner's projects;
- narrow tasks where the current project entrypoint already provides all needed context;
- situations where personal context is unnecessary.

## Related Standards

- `START_HERE.md`
- `docs/ROUTER.md`
- `docs/AUTOMATIC_CAPTURE_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
