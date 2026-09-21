# Website Creator — PROJECT_STATE.md

## Status

- Project: `Website Creator`
- State: active
- Phase: **first shared engine runtime verified; reusable component/editor workflow validation next**
- Last updated: 2026-09-21

## Architecture Decision

Website Creator is a **global self-contained website-production knowledge/control plane plus reusable execution capability system**.

Owner intent is explicit:

**Website Creator must be our own fast reusable system that any fresh chat/agent can enter and use without reconstructing the architecture, inventing a new stack, or silently introducing an arbitrary hosted platform.**

Canonical own-system standard:
`OWN_SYSTEM_EXECUTION_STANDARD.md`

Technical path remains `projects/website-creation/` for compatibility; visible project name is `Website Creator`.

## Canonical Core

- `PROJECT.md` — global purpose and boundaries.
- `PROJECT_STATE.md` — current state and priorities.
- `OWN_SYSTEM_EXECUTION_STANDARD.md` — own-system, speed, reuse and no-silent-platform rules.
- `ROUTER.md` — narrow task routing.
- `SOURCE_REGISTRY.md` — global standards/capability registry.
- `TOOL_DONOR_REGISTRY.md` — reusable implementation building blocks/platforms/donors.
- `SITE_MODEL_STANDARD.md` — platform-independent Site Model / Site Instance execution contract.
- `EDITOR_CREATION_STANDARD.md` — universal visual editor contract.
- `engine/` — running shared Website Creator implementation.
- `engine/README.md` — implementation/local-run entrypoint.
- `engine/STATUS.md` — latest verified engine evidence and next implementation slice.
- `reviews/SECOND_OPINION_DECISION_2026-09-13.md` — accepted/modified/rejected decisions from the independent review.
- `reviews/SPEED_SYSTEM_REVIEW_2026-09-14.md` — speed bottleneck / ready-solution review; evidence, not automatic architecture authority.
- `logs/latest.md` — latest architecture decision/change.

Drive root:
https://drive.google.com/drive/folders/15DIWML8HiLSJrNfP5r7IyZu_YkrD2GTU

## System Boundary

Target pattern:

`ONE REUSABLE WEBSITE CREATOR ENGINE → MANY SITE INSTANCES`

Website Creator owns reusable:

1. Site Model / Site Instance contract.
2. Component registry.
3. Theme/design-token model.
4. Visual editor contract and implementation binding.
5. Content/media model.
6. Renderer.
7. QA gates.
8. Release/deploy adapters.
9. Agent/fresh-chat entrypoint and routing.

Site Instances contain site-specific data/configuration/content/assets and deployment references, not new copies of generic infrastructure.

## First Engine — Verified 2026-09-14

A real shared engine now exists at `engine/`.

Current implementation binding:

- Next.js / React renderer;
- Payload CMS self-hosted backend;
- PostgreSQL;
- Puck visual editing through the MIT `@delmaredigital/payload-puck` integration;
- Playwright deterministic browser QA;
- Docker Compose local PostgreSQL;
- no Puck Cloud, Payload Cloud, Replit, Wix, Framer or other hosted-builder dependency.

Verified GitHub Actions runtime path:

`install → TypeScript check → seed Car Service Garage Site Instance into PostgreSQL/Payload → production build → start production server → HTTP root check → Playwright desktop/mobile render checks`.

All of those steps passed on Website Creator Engine workflow run `34869753523` for commit `87a7a3db5b16526f6832343df062f5d0de0e64de`.

Desktop/mobile screenshots were captured as workflow evidence. See `engine/STATUS.md`.

This validates the plumbing/runtime, not yet the final visual component system or full editor acceptance contract.

## No Silent Platform Rule

A new chat/executor must not silently introduce Replit, Wix, Framer, Webflow, a hosted CMS, a coding sandbox, a new deployment system or another external execution foundation merely because it is convenient.

External products may be:

- donors/benchmarks;
- optional replaceable adapters;
- explicitly accepted infrastructure;
- sources of mature open-source/self-hostable building blocks.

They are not allowed to redefine Website Creator architecture without an explicit architecture decision.

## Existing Solution First — Current Interpretation

"Own system" does not mean writing every primitive from scratch.

Use mature open-source/self-hostable/replaceable components when they:

- reduce total build time;
- preserve our Site Model/data ownership;
- fit behind our contracts;
- can be replaced without rebuilding all Site Instances.

Custom-build only the missing reusable layer.

## Site Model State

`SITE_MODEL_STANDARD.md` defines the platform-independent architecture boundary.

Status:
- direction accepted;
- first concrete `0.1-draft` TypeScript Site Instance shape now exists in `engine/src/site-model/types.ts`;
- Car Service Garage is represented as the first fixture/Site Instance in `engine/src/sites/car-service-garage.ts`;
- the draft model is successfully consumed by a real seed → Payload/Puck state → renderer → browser QA path;
- **v0.1 is not frozen yet**;
- next different Site Instances must determine what belongs in the universal core vs extensions;
- machine-readable JSON Schema/equivalent remains a later promotion after the shape survives more than one site.

## Universal Visual Editor State

The editor remains defined first by its client-neutral behavior/acceptance contract.

The first embedded implementation is now wired through Puck + Payload and compiles/runs inside the shared engine.

Still to prove through real editor interaction tests:

- save/reload persistence through the UI;
- explicit draft vs publish behavior from the editor;
- image replace/crop/move/zoom/size behavior;
- toolbar/inspector parity;
- editor/public-render parity after interactive changes;
- history/rollback path.

Do not build those separately in a client project. Extend the shared engine and test once.

## Car Service Garage Validation

Car Service Garage is the first validation case for the shared-engine architecture.

It is evidence/input, not the canonical engine.

Verified so far:

`Car Service Garage Site Instance → seed into canonical page state → shared renderer → production server → Playwright desktop/mobile QA`.

The current rendered evidence intentionally uses the integration's basic components; it proves reusable plumbing, not pixel-perfect parity with the earlier Car Service Garage visual design.

Next Car Service Garage slice:

`reusable generic component set → stronger visual parity → editor interaction/save/publish tests → media editing acceptance`.

## Fresh-Chat Contract

Every fresh chat working on Website Creator or a new site must start with:

1. `PROJECT.md`
2. `PROJECT_STATE.md`
3. `OWN_SYSTEM_EXECUTION_STANDARD.md`
4. `engine/STATUS.md` when implementation/runtime state matters
5. `SITE_MODEL_STANDARD.md`
6. `ROUTER.md`
7. only the narrow task standards needed

Then classify the work as exactly one of:

- `SITE INSTANCE WORK` — use existing engine capabilities;
- `WEBSITE CREATOR CORE WORK` — add a genuinely missing reusable capability.

There is no normal third path of one-off client infrastructure.

## Knowledge Promotion Rule

When useful learning appears in any external/client project:

`PROJECT-SPECIFIC FINDING → VERIFY → GENERALIZE → DE-IDENTIFY → DEFINE CONTRACT / ALGORITHM / COMPONENT / TEST → STORE IN WEBSITE CREATOR → USE WITHOUT SOURCE PROJECT`

Do not store a client-project link as a substitute for the generalized knowledge.

## Current Default Production Model

`research/evidence → Site Model draft → design/content decisions → populate shared components → shared renderer/editor binding → SEO/technical QA → responsive/visual QA → preview → release → production → live verification → measurement`

The key speed rule is reuse: do not rebuild generic infrastructure inside a site task.

## Current Priorities

### P0 — current
- build the first **generic reusable component set** inside the shared engine;
- move Car Service Garage from primitive Puck blocks to those reusable components without putting client-specific assumptions in core;
- prove editor UI `edit → save → reload → draft/publish → public render`;
- implement/test the media interaction subset required by `EDITOR_CREATION_STANDARD.md`;
- keep browser evidence for desktop/mobile after each accepted slice.

### P0 — verified
- shared engine repository path exists;
- Payload + PostgreSQL persistence path initializes;
- Car Service Garage seed succeeds;
- TypeScript check succeeds;
- production build succeeds;
- production server starts and serves canonical Site Instance content;
- Playwright verifies desktop/mobile render path.

### P1
- define a stable deployment adapter path rather than deployment probing;
- measure wall-clock time by phase;
- ensure a second Site Instance can start without rebuilding generic plumbing.

### P2
- multi-client isolation for shared live operation;
- content history/rollback requirements;
- version/hash golden references;
- revalidate current official SEO/AEO/search facts before changing canonical search rules.

## Final Boundary

Website Creator may know **what works**. It should not need to know **which client originally taught us that it works**.

And a fresh chat should not need to invent **how to build a website system** before it can build **a website**.

## 2026-09-21 — Universal Website Translator Direction

A second reusable execution path is now under active evaluation:

`source website → capture/fingerprint → normalize → universal recipe → editor adapter → automated build → verify`.

This does not replace the shared Website Creator engine. It adds a platform/editor translation path for cases where sites must be recreated or operated inside browser-based editors such as Showit or Wix.

Current execution candidate: Dramaturg / playwright-repl + Stagecraft, with native `.pw` as the default for linear UI workflows and JavaScript as an escape hatch.

Do not fork Dramaturg first. Prove one existing Showit PW operation as a parameterized Stagecraft skill against the real authenticated browser, then test a representative Wix operation set.

Canonical architecture:
`UNIVERSAL_WEBSITE_TRANSLATOR_ARCHITECTURE.md`

Detailed Drive record:
https://docs.google.com/document/d/1RmTaj0rH7J-VV3mTgOJRl_J09rs5J8UI6L0HuKH3H6k/edit

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
