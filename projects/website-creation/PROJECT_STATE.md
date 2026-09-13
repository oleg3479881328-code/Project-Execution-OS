# Website Creator — PROJECT_STATE.md

## Status

- Project: `Website Creator`
- State: active
- Phase: global system normalization
- Last updated: 2026-09-13

## Architecture Decision

Website Creator is a **global self-contained website-production system**.

It must not use client projects as canonical knowledge dependencies. Client-derived learning is allowed only after promotion into generalized Website Creator standards/capabilities with client names, client URLs and project-specific assumptions removed.

Technical path remains `projects/website-creation/` for compatibility; visible project name is `Website Creator`.

## Canonical Core

- `PROJECT.md` — global purpose and boundaries.
- `ROUTER.md` — narrow task routing.
- `SOURCE_REGISTRY.md` — global standards/capability registry.
- `TOOL_DONOR_REGISTRY.md` — reusable tools/platforms/donors.
- `EDITOR_CREATION_STANDARD.md` — universal visual editor contract.
- `logs/latest.md` — latest architecture decision/change.

Drive root:
https://drive.google.com/drive/folders/15DIWML8HiLSJrNfP5r7IyZu_YkrD2GTU

## Global Capability Layers

1. Research / evidence / site baseline.
2. Strategy / conversion / information architecture.
3. Design / UI / motion / design-system extraction.
4. Structured content and page-data models.
5. Universal visual editor / CMS / safe authoring.
6. Media and image manipulation.
7. SEO / AEO / pSEO / structured data / indexing.
8. Build / deployment / preview / release / rollback.
9. Browser QA / accessibility / responsive / visual QA.
10. Analytics / search / conversion validation.
11. AI-assisted implementation and automation.
12. Automatic local-business website factory workflows.

## Universal Visual Editor State

The image/editor work has been promoted into a client-neutral contract. Website Creator owns the behavior now.

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
- golden visual references stored inside Website Creator Drive as anonymous acceptance evidence.

Implementation choices currently accepted as useful reusable solutions include Puck, `react-easy-crop` and `react-moveable`, but the behavioral contract is authoritative; a different stack may satisfy the same contract.

## Knowledge Promotion Rule

When useful learning appears in any external/client project:

`PROJECT-SPECIFIC FINDING → VERIFY → GENERALIZE → DE-IDENTIFY → DEFINE CONTRACT / ALGORITHM / COMPONENT / TEST → STORE IN WEBSITE CREATOR → USE WITHOUT SOURCE PROJECT`

Do not store a client-project link as a substitute for the generalized knowledge.

## Current Default Production Model

`research → strategy/IA → donor/design system → structured content/data → implementation → editor when needed → SEO/technical QA → responsive/visual QA → preview → release → production → live verification → measurement`

## Current Work Remaining

- remove remaining client-specific wording/links from Website Creator registries and Drive indexes;
- rename Drive surfaces from `Website Creation` to `Website Creator`;
- normalize the production-standards folder so it is not named after a client;
- keep long-tail historical material outside the core unless it is promoted into a global reusable artifact.

## Final Boundary

Website Creator may know **what works**. It should not need to know **which client originally taught us that it works**.