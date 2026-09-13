# Website Creator — PROJECT_STATE.md

## Status

- Project: `Website Creator`
- State: active
- Phase: second-opinion integrated; execution-contract validation next
- Last updated: 2026-09-13

## Architecture Decision

Website Creator is a **global self-contained website-production knowledge/control plane plus reusable capability system**.

It must not use client projects as canonical knowledge dependencies. Client-derived learning is allowed only after promotion into generalized Website Creator standards/capabilities with client names, client URLs and project-specific assumptions removed.

Technical path remains `projects/website-creation/` for compatibility; visible project name is `Website Creator`.

Website Creator is not required to become one monolithic builder/runtime. Reusable execution may be implemented beneath it through Site Models, renderers, editor/CMS bindings, platform adapters and deterministic QA capabilities.

## Canonical Core

- `PROJECT.md` — global purpose and boundaries.
- `PROJECT_STATE.md` — current state and priorities.
- `ROUTER.md` — narrow task routing.
- `SOURCE_REGISTRY.md` — global standards/capability registry.
- `TOOL_DONOR_REGISTRY.md` — reusable tools/platforms/donors.
- `SITE_MODEL_STANDARD.md` — platform-independent Site Model / Site Instance execution contract.
- `EDITOR_CREATION_STANDARD.md` — universal visual editor contract.
- `reviews/SECOND_OPINION_DECISION_2026-09-13.md` — accepted/modified/rejected decisions from the independent review.
- `logs/latest.md` — latest architecture decision/change.

Drive root:
https://drive.google.com/drive/folders/15DIWML8HiLSJrNfP5r7IyZu_YkrD2GTU

## Global Capability Layers

1. Research / evidence / site baseline.
2. Strategy / conversion / information architecture.
3. Platform-independent Site Model / Site Instance.
4. Design / UI / motion / design-system extraction.
5. Structured content and page-data models.
6. Universal visual editor / CMS / safe authoring.
7. Media and image manipulation.
8. SEO / AEO / pSEO / structured data / indexing.
9. Build / deployment / preview / release / rollback.
10. Browser QA / accessibility / responsive / visual QA.
11. Analytics / search / conversion validation.
12. AI-assisted implementation and automation.
13. Automatic local-business website factory workflows.

## Independent Review Decision

The 2026-09-13 independent review was processed through an explicit decision record rather than applied wholesale.

Core accepted conclusions:

- Website Creator should gain a canonical platform-independent Site Model for execution.
- The Site Model is **not** the identity of Website Creator and does not replace the knowledge/control plane.
- `Site Model v0.1` must be derived from a real new-site build, not designed exhaustively in advance.
- a first reference renderer should be built alongside that real v0.1 validation;
- PEOS Design Block remains the single authority for design workflow; Website Creator should route there rather than duplicate it;
- Playwright is the default deterministic browser-QA direction where applicable;
- editor architecture requires a real build-vs-buy/adapt comparison before major new implementation-specific expansion;
- Website Factory should prefer ready-made generic provisioning/hosting/permissions infrastructure when it passes real acceptance tests;
- no factory vendor is selected by research alone; use identical-input comparisons;
- client isolation, content rollback and versioned golden references are real requirements;
- no deeper Website Creator OS/runtime layer is justified yet.

Canonical decision record:
`reviews/SECOND_OPINION_DECISION_2026-09-13.md`

## Site Model State

`SITE_MODEL_STANDARD.md` now defines the architecture boundary.

Status:
- direction accepted;
- `v0.1` schema not frozen;
- first concrete schema must be derived from the next real new-site production;
- machine-readable TypeScript types + JSON Schema (or equivalent) are the target once concrete fields exist;
- one real renderer/adapter must consume the model before v0.1 can be considered validated;
- subsequent different sites must test what belongs in the universal core vs extensions.

## Universal Visual Editor State

The editor remains defined first by its client-neutral behavior/acceptance contract.

Core interaction contract:

- visual page canvas, not only property forms;
- block/page structure + direct manipulation + right inspector;
- selected image gets visible selection state, floating toolbar and contextual inspector;
- crop/move is a visual modal with drag + zoom, not numeric focal coordinates as the primary UX;
- non-destructive crop metadata stored in resolution-independent percentages;
- shape, fill/whole-photo, replace, remove, reset, width/alignment, alt and caption behavior;
- optional direct resize handles persisting percentage width;
- shared state between toolbar and inspector;
- editor/public-render parity;
- deterministic reload persistence;
- golden visual references as acceptance evidence.

Current internal implementation options such as Puck, `react-easy-crop` and `react-moveable` remain proven implementation candidates, but no stack is a universal default until a documented build-vs-buy/adapt comparison is complete.

## Knowledge Promotion Rule

When useful learning appears in any external/client project:

`PROJECT-SPECIFIC FINDING → VERIFY → GENERALIZE → DE-IDENTIFY → DEFINE CONTRACT / ALGORITHM / COMPONENT / TEST → STORE IN WEBSITE CREATOR → USE WITHOUT SOURCE PROJECT`

Do not store a client-project link as a substitute for the generalized knowledge.

## Current Default Production Model

`research → Site Model draft → strategy/IA → donor/design system → structured content/data → renderer/platform binding → editor when needed → SEO/technical QA → responsive/visual QA → preview → release → production → live verification → measurement`

This may iterate during real production; the important requirement is convergence on a reusable machine-readable site contract instead of separate hidden page state in every layer.

## Current Priorities

### P0
- derive `Site Model v0.1` from the first real new-site validation;
- create the first reference renderer/adapter as part of that validation;
- perform editor build-vs-buy/adapt comparison before major new custom editor infrastructure.

### P1
- keep Design Block as the single design workflow authority;
- use Playwright as default browser QA where applicable;
- run identical-input factory-platform comparison before choosing a default backend.

### P2
- define multi-client Site Instance isolation before shared live multi-client operation;
- require content revision/history/rollback for production editing;
- version/hash golden visual references;
- revalidate current official SEO/AEO/search facts before changing canonical search rules.

### Evidence-triggered
- add task-loading manifests only if real context-loading failures appear;
- create a deeper Website Creator runtime/OS only if repeated production proves PEOS + current capability boundaries insufficient.

## Final Boundary

Website Creator may know **what works**. It should not need to know **which client originally taught us that it works**.

The next architecture improvements should come from real site production evidence, not further abstraction for its own sake.