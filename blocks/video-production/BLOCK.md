# Video Production Block

## Purpose

Provide a reusable Project Execution OS domain layer for short-form and long-form video production, automated clipping, subtitle workflows, editing pipelines, AI voice/avatar integration, multilingual content factories, monetization, platform adaptation, and implementation handoff.

This block is for recurring video-production systems across projects, especially automated Reels, Shorts, TikTok, educational video, and media-factory workflows.

For YouTube-specific channel strategy, YPP, reused-content policy, playlists, analytics, uploads, or YouTube Data API workflows, use `blocks/youtube/BLOCK.md`.

For executable reusable media packages such as download, probe, transcription, or clipping, use `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md` and check `capability-library/REGISTRY.md`.

## Status

`candidate_v2`

This block is based on both prior owner experiments and external-tool research, but remains candidate until one automated production pipeline is validated end to end using reusable capability contracts.

## Core Principle

Video production should be treated as a repeatable pipeline, not as isolated manual editing.

Start from:

`source -> rights check -> download/import -> clip selection -> edit -> captions -> voice/visual layer -> platform adaptation -> publish package -> analytics -> iteration`

Technical operations that recur across applications should be implemented as capability blocks rather than copied into each project.

Initial capability chain:

```text
media.download
-> media.probe
-> media.extract_audio
-> media.transcribe
-> media.clip
```

The video-production domain block owns domain decisions and workflow patterns.

The capability blocks own bounded executable operations.

The target application owns product-specific selection logic, UI, customer data, and publishing decisions.

## When To Use

Use this block for:

- Reels, Shorts, or TikTok production;
- long-video-to-short-video clipping;
- yt-dlp and ffmpeg workflows;
- CapCut Desktop workflows;
- subtitle extraction and cleanup;
- AI voiceover;
- AI avatars;
- multilingual video factories;
- gadget, facts, cinema, educational, or language-learning content;
- QuizLight video-card creation workflows;
- automated media pipelines;
- monetization and scaling decisions for video projects;
- deciding which reusable media capabilities a project needs.

## When Not To Use

Do not use this block for:

- YouTube-specific channel strategy, YPP readiness, YouTube copyright/reused-content review, playlists, YouTube analytics, uploads, or YouTube Data API workflows; use `blocks/youtube/BLOCK.md`;
- claiming that a reusable executable block exists merely because the domain workflow is documented;
- piracy or copyright evasion;
- downloading or republishing content without rights or permission;
- bypassing platform controls;
- deceptive synthetic media;
- impersonation;
- hidden scraping of private media;
- medical, legal, political, or financial video claims without source verification.

## Required Reading Inside This Block

Smallest useful path:

1. `BLOCK.md`
2. `PRODUCT_SURFACES.md`
3. `READY_SOLUTIONS.md`
4. `TOOL_SELECTION_MATRIX.md`
5. `VIDEO_PIPELINES.md`
6. `CONTENT_FACTORY_PATTERNS.md`
7. `SHORT_FORM_PATTERNS.md`
8. `AUTOMATION_PATTERNS.md` when automation matters
9. `YT_DLP_AND_FFMPEG.md` for download/transcode work
10. `CAPCUT.md` for desktop editing workflows
11. `AI_VIDEO_STACKS.md` for AI-enhanced pipelines
12. `VOICE_AND_AVATAR.md` when voice or avatar layers matter
13. `PLATFORM_PATTERNS.md` before publication
14. `MONETIZATION.md` when business model matters
15. `IMPLEMENTATION_HANDOFF.md` before executor handoff
16. `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md` when functionality should be reusable across applications
17. `capability-library/REGISTRY.md` before assuming a reusable implementation is ready
18. `VALIDATION_BACKLOG.md` before treating research as verified
19. `REFERENCES.md` when freshness or authority matters
20. `blocks/youtube/BLOCK.md` when YouTube-specific platform decisions matter

Do not load every file by default. Load only the files relevant to the active workflow.

## Capability Reuse Rule

Before implementing video download, probing, audio extraction, transcription, clipping, captions, rendering, or publishing inside a project:

1. check `capability-library/REGISTRY.md`;
2. reuse a validated block when available;
3. extend a candidate block when its contract fits;
4. create a new capability block only when no adequate one exists;
5. keep application-specific orchestration outside the block.

## Typical Outputs

- video-factory architecture;
- source-to-publish pipeline;
- tool-selection decision;
- capability composition plan;
- yt-dlp/ffmpeg execution plan;
- CapCut workflow;
- AI voice/avatar stack;
- multilingual scaling plan;
- platform-specific adaptation plan;
- monetization model;
- implementation handoff;
- review checklist.

## Boundary

This domain block stores reusable domain knowledge and workflow decisions.

Executable reusable code belongs to the capability-block implementation layer and must be versioned and validated independently.

Do not store platform passwords, API keys, private creator data, unpublished confidential footage, or project-specific copyrighted source files in the central block.

Keep unstable platform rules, tool capabilities, and monetization requirements in dated research or references.

## Final Rule

Build pipelines that are repeatable, rights-aware, measurable, automatable, and composed from validated capability blocks.

Avoid one-off duplicated implementations unless they are intentionally used as bounded validation prototypes.