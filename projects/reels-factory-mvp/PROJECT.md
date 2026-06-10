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
- Include storyboard-oriented scene control.
- Include donor-video analysis as a future factory capability.

## 6. Current Focus

Create one short original vertical animated video:

- duration: 15 seconds;
- structure: 3 scenes x 5 seconds;
- format: vertical 9:16;
- style: animated / cartoon;
- content type: visual scenes only;
- voiceover: not required for MVP;
- publishing: not required for MVP.

## 7. Functional Requirements

### 7.1 Storyboard Mode

Each generated scene should be representable as a controllable storyboard unit:

`start frame -> textual scene description -> end frame`

For each scene, the pipeline should be able to store:

- scene ID;
- intended duration;
- start frame reference;
- end frame reference;
- textual description of what happens between the frames;
- subject and character continuity notes;
- camera movement notes;
- motion intensity;
- visual style notes;
- seed and model metadata;
- generation result and accept/reject decision.

The purpose is to reduce random generation and improve repeatability, visual continuity, and cost control.

### 7.2 Donor Video Analysis Mode

The future factory should support automated analysis of a donor or reference video.

Allowed purpose:

- extract production mechanics;
- understand why a video holds attention;
- generate a reusable structural blueprint for a new original video.

The analysis should be able to extract:

- total duration;
- scene boundaries and shot lengths;
- opening hook;
- pacing pattern;
- visual composition;
- camera movement;
- subject movement;
- transitions;
- text overlays and captions;
- audio events when relevant;
- recurring visual motifs;
- probable retention triggers;
- scene-by-scene storyboard draft;
- reusable structural pattern.

Required boundary:

`donor video -> structural analysis -> abstract blueprint -> new original concept -> original assets -> original output`

Do not use this mode to republish, clone, or closely recreate protected source footage.

## 8. Next Practical Step

Select the first test concept and visual style, then choose the simplest open-source AI video generation route that can run on temporary rented GPU compute.

For the first MVP, prepare three storyboard units with:

- one start frame;
- one scene description;
- one end frame;
- one five-second generated clip.

## 9. Key Decisions And Constraints

Hard constraints:

- Do not consider buying owned hardware.
- Do not consider permanent rental of expensive GPU servers.
- Do not use SaaS video-generation platforms for the MVP.
- Use temporary rented GPU only when needed.
- Shut down rented GPU runtime after the generation job.
- Track real generation cost and time.
- Avoid copyright-dependent source footage for the MVP.
- Donor-video analysis must produce an abstract production blueprint, not a clone.

Architecture assumption for this MVP:

`concept -> 3 storyboard units -> temporary GPU generation -> download outputs -> assemble/export -> record cost/time/quality`

Future donor-analysis extension:

`donor video -> automated structural analysis -> storyboard blueprint -> new original concept -> original storyboard units -> original generated reel`

## 10. Read Next

Minimum relevant Project Execution OS nodes:

- `START_HERE.md`
- `docs/ROUTER.md`
- `blocks/video-production/BLOCK.md`
- `blocks/server-rental/BLOCK.md`

No additional project artifacts exist yet. Create `PROJECT_STATE.md` and `logs/latest.md` only after the first meaningful execution step begins.
