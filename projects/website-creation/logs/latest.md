# Website Creator — latest log

## 2026-09-22 — Universal Site Fingerprint ONE PASS V2.2 — PROVEN LIVE

Owner-run proof target: https://venues.olgapoloweddings.com/

Accepted evidence:
- 4 responsive viewports completed;
- each viewport reported 59 links;
- raw anchor occurrences: 236 (=59×4);
- normalized Link Graph: 46 unique anchors;
- structured navigation items: 1;
- forms: 0;
- 8 motion samples completed;
- one 22-file ZIP built;
- ZIP bytes: 98,991,721;
- transfer chunks: 330;
- targetChanged=false;
- final marker: `UNIVERSAL SITE FINGERPRINT ONE-PASS V2.2: COMPLETE`.

Decision:
- V2.2 supersedes V2.1 as current accepted scanner.
- Links are first-class reconstruction evidence.
- Canonical package now includes `normalized/link-graph.json` in addition to raw per-viewport link evidence.
- Default translator input path: `URL → V2.2 fingerprint ZIP → Universal Page Recipe → editor adapter`.

Current V2.2 script:
https://docs.google.com/document/d/1me66NNjOsvO-0KXO7F8lgG490s-nKwWnUtMvVA-I-qk/edit

---

## 2026-09-21 — Showit Exact PW Route Binding

- Ingested the authoritative Showit exact-route registry supplied by the owner.
- Bound Universal Page Recipe operations to exact Dramaturg .pw route statuses.
- Added a conservative compiler that fails closed when an exact route is missing.
- Aperol result: all 17 sections currently have at least one missing exact route; no selector guessing is permitted.
- Selected Hero as first static proof candidate.
- Hero remaining exact routes: Canvas background/transparent fill, PonteLight font, text color. Page-trigger behavior is separate.
- Derived Drive binding: https://docs.google.com/document/d/1AKzgJUh2PWCirbYDmUb6cMUT1A1EumZ17rrW4nBKHTs/edit
- Bundle: https://drive.google.com/file/d/10Bo2-qO79pGfg4pQ81Wo1dIqiQiyWRx0/view

---

## 2026-09-21 — First Universal Page Recipe + Showit/Wix adapter artifacts

- Built reusable `fingerprint-to-page-recipe.py`.
- Generated a platform-neutral Recipe from Aperol Portfolio.
- Recipe inventory: 17 sections / 173 elements.
- Preserved exact Showit authored Desktop/Mobile geometry from exposed `init_data` and used DOM/computed style as verification.
- Generated compact machine Recipe for durable handoff.
- Generated Showit and Wix adapter plans.
- Showit translation: 165 exact / 7 approximate / 1 unsupported.
- Wix translation: 155 exact / 17 approximate / 1 unsupported.
- Explicitly separated translation support from automation execution proof.
- Marked old direct fingerprint→Showit translator as target-specific donor/compatibility knowledge rather than the preferred architecture.
- No target editor mutation occurred.

Durable folder:
https://drive.google.com/drive/folders/10oR140lzuXUK7eDq2nx77-oc6yBlb3Kc

---

## 2026-09-21 — Universal Site Fingerprint ONE PASS V2.1 — PROVEN LIVE

Owner-run proof target:
https://aperolspritz.tonicsiteshop.com/portfolio

Accepted evidence:
- four responsive viewports completed;
- desktop-1440: 416 nodes / 2 DOM img / 45 runtime image assets / 6 runtime font assets / 72 links;
- desktop-1200: 417 nodes / 2 DOM img / 45 runtime image assets / 6 runtime font assets / 72 links;
- tablet-1024: 417 nodes / 2 DOM img / 45 runtime image assets / 6 runtime font assets / 72 links;
- mobile-390: 398 nodes / 2 DOM img / 45 runtime image assets / 6 runtime font assets / 72 links;
- eight motion samples completed;
- one 21-file ZIP built;
- ZIP bytes: 45,216,413;
- transfer chunks: 151;
- targetChanged=false;
- final marker: `UNIVERSAL SITE FINGERPRINT ONE-PASS V2.1: COMPLETE`.

Decision:
- V2.1 is now `PROVEN LIVE / CURRENT ACCEPTED`.
- Default capture workflow is `URL → one V2.1 run → one ZIP`.
- V2 remains historical proof; separate static/motion passes remain fallback/recovery knowledge rather than the default path.

Current script:
https://docs.google.com/document/d/1VfcBW28jxc5SizUqW2AMjw7LxAiei3SKN2vGaSen2Oo/edit

---

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
