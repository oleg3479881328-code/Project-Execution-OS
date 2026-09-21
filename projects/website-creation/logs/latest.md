# Website Creator — latest log

## 2026-09-21 — Universal Website Translator / Dramaturg PW-first direction

### Captured

- Generalized the current Showit/Dramaturg learning into a cross-editor architecture.
- Recorded the chain `Capture → Normalize → Recipe → Editor Adapter → Build → Verify`.
- Selected Dramaturg / playwright-repl + Stagecraft as the primary existing-solution candidate for the browser execution/skill layers.
- Recorded PW-first rule: linear UI flows use native `.pw`; JS remains an escape hatch for real program logic.
- Recorded that Stagecraft already provides much of the proposed brick model: SKILL.md, .pw/.js skills, variables, recording/replay and user skill discovery.
- Defined Showit as first proof and Wix as second generic-editor proof candidate.
- Explicitly rejected a premature Dramaturg fork or a second custom DSL/browser engine.
- Preserved the boundary: capture/fingerprint, normalized recipe, and target editor implementation are separate layers.

### Durable locations

- Architecture: https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/projects/website-creation/UNIVERSAL_WEBSITE_TRANSLATOR_ARCHITECTURE.md
- Detailed Drive record: https://docs.google.com/document/d/1RmTaj0rH7J-VV3mTgOJRl_J09rs5J8UI6L0HuKH3H6k/edit
- SOFT Master Software Inventory updated.
- SOFT Third-Party Software Index updated.
- Website Creator Automatic Website Factory README updated.
- Website Creator Tools & Extractors README updated.

### Next proof

Known working Showit PW operation → Stagecraft skill → parameter → real Chrome replay/run → deterministic verification; then repeat with a small representative Wix operation set.

---

# Website Creator — latest

Date: 2026-09-14

## Event

The first real reusable Website Creator Engine implementation was created and runtime-verified.

Engine path:
`../engine/`

Verification state:
`../engine/STATUS.md`

## Main Result

The architecture is no longer only prose.

A real self-hostable execution path now exists:

`Site Instance → Payload/Puck canonical page state → shared Next.js renderer → production server → Playwright QA`

Current implementation binding:

- Payload CMS;
- PostgreSQL;
- Puck via the MIT `@delmaredigital/payload-puck` integration;
- Next.js / React;
- Playwright;
- Docker Compose for local PostgreSQL.

No Puck Cloud, Payload Cloud, Replit, Wix, Framer or other hosted website builder is required.

## Existing Solution First Applied

Instead of writing our own Payload↔Puck bridge, Website Creator uses the existing MIT `@delmaredigital/payload-puck` integration and follows its proven Payload App Router patterns.

The binding remains replaceable. Website Creator Site Model, contracts and Site Instances remain ours.

## Car Service Garage Validation — Slice 1

Car Service Garage was converted into the first `0.1-draft` Site Instance fixture and seeded into the shared engine.

Verified workflow run:
- Website Creator Engine run: `34869753523`
- source commit: `87a7a3db5b16526f6832343df062f5d0de0e64de`

Passed:

1. dependency installation;
2. TypeScript check;
3. PostgreSQL/Payload initialization;
4. Car Service Garage seed;
5. production Next.js build;
6. production server start;
7. HTTP request to the public renderer;
8. Playwright desktop render assertions;
9. Playwright mobile render assertions;
10. desktop/mobile screenshot evidence upload.

The first build-only workflow had already passed on commit `aa9c389c0e2e48595b133592ef579b1e5a439cff`; the second run extended verification through real seed + runtime + browser QA.

## What This Does Not Yet Prove

Do not overstate this milestone.

The current public evidence is intentionally primitive visually. It validates the shared plumbing and canonical render path, not yet:

- pixel-level Car Service Garage design parity;
- reusable branded section components;
- full visual-editor save/reload/publish interaction through browser UI;
- image crop/move/zoom/resize acceptance;
- history/rollback acceptance;
- second unrelated Site Instance reuse.

## Current P0

1. Build the first generic reusable section/component set in `engine/`.
2. Recompose Car Service Garage from those components without client-specific core assumptions.
3. Prove Puck editor interaction against the same canonical state.
4. Prove save → reload → draft/publish → public render.
5. Add media editing behavior required by `EDITOR_CREATION_STANDARD.md`.
6. Keep deterministic desktop/mobile browser evidence.

## Core Principle

**Do not solve each website separately. Build and reuse the Website Creator system that solves websites.**
