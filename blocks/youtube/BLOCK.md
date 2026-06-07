# YouTube Block

## Purpose

Provide a reusable Project Execution OS domain layer for YouTube channel strategy, Shorts and long-form publishing, monetization, originality and rights review, analytics, multilingual scaling, YouTube Data API workflows, channel operations, and implementation handoff.

This block is the platform-specific YouTube layer. Reusable editing and rendering workflows belong in `blocks/video-production/`.

## Status

`candidate_v2`

This block is based on official YouTube documentation, prior owner discussions, and existing Video Production Block knowledge. It remains candidate until validated on a real YouTube channel workflow.

## Core Principle

Treat YouTube as a content system and business channel, not just a place to upload videos.

Start from:

`channel goal -> audience -> niche -> content system -> originality/rights -> Shorts + long-form role -> publish package -> analytics -> monetization -> iteration`

Automation may reduce labor, but it must not create repetitive mass-produced output with minimal variation.

## When To Use

Use this block for:

- YouTube channel creation and strategy;
- YouTube Shorts;
- long-form YouTube videos;
- channel monetization planning;
- YouTube Partner Program readiness;
- copyright, reused-content, and inauthentic-content review;
- channel analytics;
- playlist, metadata, and publishing structure;
- YouTube Data API automation;
- upload workflows;
- multilingual YouTube channels;
- faceless/anonymous YouTube channels;
- YouTube as an acquisition channel for SaaS, affiliate, education, or media projects;
- QuizLight YouTube learning workflows.

## When Not To Use

Do not use this block for:

- general editing workflows that are platform-neutral; use `blocks/video-production/`;
- piracy, copyright evasion, or repost factories;
- deceptive thumbnails or misleading metadata;
- fake engagement, spam, or view manipulation;
- mass-produced low-variation content;
- impersonation;
- evading channel restrictions or demonetization;
- political, medical, legal, or financial claims without source verification.

## Required Reading Inside This Block

Smallest useful path:

1. `BLOCK.md`
2. `READY_SOLUTIONS.md`
3. `PRODUCT_SURFACES.md`
4. `CHANNEL_STRATEGY.md`
5. `SHORTS_AND_LONG_FORM.md`
6. `CONTENT_AND_COPYRIGHT.md`
7. `PUBLISHING_AND_METADATA.md`
8. `MONETIZATION.md` when business model matters
9. `ANALYTICS_AND_EXPERIMENTS.md` when growth or review matters
10. `AUTOMATION_AND_API.md` when uploads, playlists, metadata, or channel tooling matter
11. `MULTILINGUAL_SCALING.md` when language networks matter
12. `PLATFORM_OPERATIONS.md` for ongoing channel workflows
13. `IMPLEMENTATION_HANDOFF.md` before executor handoff
14. `CURRENT_PLATFORM_SNAPSHOT_2026-06-07.md` for freshness-sensitive current facts
15. `VALIDATION_BACKLOG.md` before treating recommendations as verified
16. `REFERENCES.md` when source freshness or policy authority matters
17. `../video-production/BLOCK.md` when editing, clipping, captions, ffmpeg, CapCut, AI voice, or multilingual rendering matter

Do not load every file by default. Load the smallest path that fits the task.

## Typical Outputs

- YouTube channel concept;
- niche and audience decision;
- Shorts vs long-form role split;
- content calendar structure;
- originality and copyright review;
- monetization map;
- metadata and playlist plan;
- publish package;
- multilingual scaling plan;
- analytics experiment plan;
- API automation plan;
- implementation handoff;
- review report.

## Boundary

This block stores reusable YouTube platform knowledge only.

Do not store channel passwords, private creator data, OAuth tokens, API secrets, AdSense details, unpublished confidential footage, or project-specific copyrighted source files in this central block.

Keep unstable platform rules and monetization thresholds in dated research reports or current-platform snapshots.

## Final Rule

Build channels around original value, clear audience fit, repeatable formats, truthful metadata, measurable iteration, and policy-aware scaling.