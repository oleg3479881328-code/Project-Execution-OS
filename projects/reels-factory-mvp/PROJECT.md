# PROJECT — Reels Factory MVP

## 1. Project

- Project name: Reels Factory MVP
- Short description: Validate a minimal repeatable pipeline for creating one original short-form animated reel using temporary rented GPU compute only.
- Project type: video-production / server-rental / AI media MVP

## 2. Purpose

This project exists to test whether Oleg can produce a short original animated visual reel without buying hardware, without permanent GPU rental, and without expensive SaaS video-generation platforms.

Current-stage success means producing one complete MVP video and recording the practical workflow, cost, time, and quality outcome.

## 3. Source Of Truth

Durable source of truth: this GitHub repository under:

`projects/reels-factory-mvp/`

The project operates under Project Execution OS.

## 4. Current Status

- Status: active / initialized
- Current mode: MVP validation
- Current phase: define and execute first visual-only animated video test
- Confidence: concept approved; technical stack not yet selected

## 5. Done So Far

Confirmed decisions:

- Build a real Project Execution OS project for the Reels Factory MVP.
- Start with a visual-only animated short, not voice-first content.
- Use a 15-second MVP before attempting a 30-second version.
- Treat compute as temporary rented runtime only.

## 6. Current Focus

Create one short original vertical animated video:

- duration: 15 seconds;
- structure: 3 scenes x 5 seconds;
- format: vertical 9:16;
- style: animated / cartoon;
- content type: visual scenes only;
- voiceover: not required for MVP;
- publishing: not required for MVP.

## 7. Next Practical Step

Select the first test concept and visual style, then choose the simplest open-source AI video generation route that can run on temporary rented GPU compute.

## 8. Key Decisions And Constraints

Hard constraints:

- Do not consider buying owned hardware.
- Do not consider permanent rental of expensive GPU servers.
- Do not use SaaS video-generation platforms for the MVP.
- Use temporary rented GPU only when needed.
- Shut down rented GPU runtime after the generation job.
- Track real generation cost and time.
- Avoid copyright-dependent source footage for the MVP.

Architecture assumption for this MVP:

`concept -> 3-scene visual plan -> temporary GPU generation -> download outputs -> assemble/export -> record cost/time/quality`

## 9. Read Next

Minimum relevant Project Execution OS nodes:

- `START_HERE.md`
- `docs/ROUTER.md`
- `blocks/video-production/BLOCK.md`
- `blocks/server-rental/BLOCK.md`

No additional project artifacts exist yet. Create `PROJECT_STATE.md` and `logs/latest.md` only after the first meaningful execution step begins.
