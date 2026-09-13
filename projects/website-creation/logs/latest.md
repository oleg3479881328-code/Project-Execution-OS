# Website Creator — latest

Date: 2026-09-13

## Event

Independent architecture/technical second-opinion review completed and was processed through Website Creator's own decision pass.

The review was **not** applied wholesale.

Canonical decision record:
`../reviews/SECOND_OPINION_DECISION_2026-09-13.md`

## Main Decision

Keep Website Creator as a **global PEOS website-production knowledge/control plane plus reusable capability system**.

Do not turn it immediately into one monolithic website-builder runtime.

Add a reusable execution contract beneath it:

`Website Creator standards → Site Model / Site Instance → renderer/editor/platform adapters → QA/release/deploy`.

## Accepted / Modified Changes

- created `SITE_MODEL_STANDARD.md`;
- Site Model is accepted as the platform-independent execution contract for a concrete site;
- `Site Model v0.1` must be derived from the first real new-site build, not from an abstract universal schema exercise;
- first reference renderer/adapter should be built alongside that v0.1 validation;
- PEOS Design Block is the single design workflow authority; Website Creator no longer repeats a second design pipeline in `SOURCE_REGISTRY.md`;
- Playwright promoted to default deterministic browser-QA direction where applicable;
- editor behavioral contract preserved, but major new implementation-specific editor work now requires build-vs-buy/adapt comparison;
- Storyblok, Sanity Visual Editing and Builder.io added only as editor research/comparison candidates, not defaults;
- Website Factory keeps research/design/content/QA intelligence under our control while preferring ready-made generic provisioning/hosting/permissions when real comparison proves fit;
- Duda and 10Web remain candidates; B12 added as a research candidate; no winner selected;
- content history/rollback added as a production editing requirement;
- multi-client Site Instance isolation accepted as a requirement before shared live multi-client operation;
- golden editor references must become version-addressable/hash/revision-backed;
- time-sensitive third-party adoption facts require source/date revalidation;
- time-sensitive SEO/AEO claims from the review remain pending official revalidation before canonical update.

## Explicit Rejections

- do not treat “no monolithic runtime yet” as proof Website Creator is architecturally invalid;
- do not halt all standards work until Site Model exists;
- do not select an editor/CMS/factory vendor from research alone;
- do not create a deeper Website Creator OS/runtime layer by anticipation;
- do not use a fixed site-count breakpoint as a universal scaling rule;
- do not simplify the tool registry taxonomy unless real operational confusion proves it necessary.

## Current P0

1. Use the next real new-site build to derive the concrete `Site Model v0.1`.
2. Build the first real renderer/adapter against it.
3. Before major new editor infrastructure, run a real internal-vs-external editor comparison against `EDITOR_CREATION_STANDARD.md`.

## Current P1

- Playwright browser QA;
- identical-input Website Factory candidate comparison;
- keep all design-process evolution in `blocks/design/` rather than duplicating it here.

## Core Principle

**Architecture now moves forward through real production evidence.**

Do not add abstract layers merely because they sound scalable. Promote what repeated real work proves reusable.