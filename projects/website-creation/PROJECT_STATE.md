# Website Creator — PROJECT_STATE.md

## Status

- Project: `Website Creator`
- State: active
- Phase: own-system execution direction fixed; first shared-engine validation next
- Last updated: 2026-09-14

## Architecture Decision

Website Creator is a **global self-contained website-production knowledge/control plane plus reusable execution capability system**.

Owner intent is now explicit:

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
- `v0.1` schema not frozen;
- first concrete schema should be derived from the Car Service Garage validation case rather than abstract completeness planning;
- machine-readable TypeScript types + JSON Schema (or equivalent) remain the target;
- one real reusable renderer/adapter must consume the model before v0.1 is validated;
- later different Site Instances must test what belongs in universal core vs extensions.

## Universal Visual Editor State

The editor remains defined first by its client-neutral behavior/acceptance contract.

Core interaction contract:

- visual page canvas, not only property forms;
- block/page structure + direct manipulation + right inspector;
- selected image gets visible selection state, floating toolbar and contextual inspector;
- crop/move is a visual modal with drag + zoom, not numeric focal coordinates as primary UX;
- non-destructive crop metadata stored in resolution-independent percentages;
- shape, fill/whole-photo, replace, remove, reset, width/alignment, alt and caption behavior;
- optional direct resize handles persisting percentage width;
- shared state between toolbar and inspector;
- editor/public-render parity;
- deterministic reload persistence;
- golden visual references as acceptance evidence.

Implementation must prefer an embedded/open/self-hostable reusable building block when it meets this contract. The editor itself must be built once as Website Creator capability, not separately for each site.

## Car Service Garage Validation

Car Service Garage is the first validation case for the shared-engine architecture.

It is evidence/input, not the canonical engine.

Validation goal:

`Car Service Garage data/content/assets → Site Model v0.1 → shared components → shared editor → shared renderer → QA → deploy adapter`

Success requires that another site can then start from the same engine without rebuilding editor/renderer/deploy plumbing.

Do not create a new client-specific editor or a collection of disposable probe projects as the normal implementation path.

## Fresh-Chat Contract

Every fresh chat working on Website Creator or a new site must start with:

1. `PROJECT.md`
2. `PROJECT_STATE.md`
3. `OWN_SYSTEM_EXECUTION_STANDARD.md`
4. `SITE_MODEL_STANDARD.md`
5. `ROUTER.md`
6. only the narrow task standards needed

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

### P0
- validate the shared-engine pattern on Car Service Garage;
- derive real `Site Model v0.1` from that validation;
- establish the first reusable component set;
- establish one reusable renderer;
- bind one reusable editor implementation to canonical site state;
- prove save/reload/publish without manual frontend reconstruction.

### P1
- use Playwright as default deterministic browser QA where applicable;
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