# Website Creator — PROJECT.md

## Project

- Name: `Website Creator`
- Technical path: `projects/website-creation/` (kept stable for routing compatibility)
- Type: global website-production knowledge/control plane + reusable capability system
- Status: active
- Operating system: Project Execution OS
- Created: 2026-09-13

## Purpose

`Website Creator` is the canonical, client-agnostic system for designing, building, editing, optimizing, deploying and maintaining websites.

It contains reusable website-production knowledge as **its own standards, contracts, capabilities, tools and acceptance gates**. A fresh chat must be able to build a new site from this project without opening any client project or reconstructing prior work from memory.

Website Creator is not a dispatcher that chooses a different hosted website-builder product for every site. The target is **our own reusable Website Creator engine**, assembled from replaceable proven building blocks where useful, and consumed by many Site Instances.

Canonical own-system rule: `OWN_SYSTEM_EXECUTION_STANDARD.md`.

## Own System Rule

`ONE REUSABLE WEBSITE CREATOR ENGINE → MANY SITE INSTANCES`.

A new website should reuse the shared Site Model, component registry, editor, renderer, content/media model, QA and deployment adapters.

A new chat must not silently introduce a hosted builder, coding sandbox, new editor, new deployment architecture or client-specific infrastructure merely because it is convenient.

If a reusable capability is missing, improve the shared Website Creator engine once and then reuse it.

"Own system" does not mean writing every primitive from scratch. Existing Solution First still applies: prefer mature open-source/self-hostable/replaceable building blocks when they fit our contracts and preserve ownership of canonical site state.

## No Client Dependency Rule

Website Creator must not depend on, route through, or cite client-specific projects as part of its operating architecture.

Knowledge learned during client work may enter Website Creator only after it is:

1. generalized;
2. de-identified;
3. separated from client-specific facts and URLs;
4. expressed as a reusable standard, component, algorithm, contract, test or tool;
5. independently usable without the source client project.

Once promoted, the generalized knowledge belongs to Website Creator. The client project is not a runtime or knowledge dependency.

## Scope

Website Creator covers the complete website lifecycle:

- business/site research and evidence;
- existing-site audit and baseline capture;
- goals, conversion paths, information architecture and sitemap planning;
- platform-independent Site Model and Site Instance contracts;
- donor-first visual research and design extraction;
- design systems, tokens, sections, components, responsive behavior and motion;
- structured content and content/data separation;
- visual editor / CMS / safe client authoring;
- image/media handling, crop, move, zoom, sizing, galleries and delivery assets;
- SEO, local SEO, pSEO, AEO/GEO, schema, canonical, sitemap and indexing;
- frontend implementation and reusable renderers/adapters;
- Git/change control, preview/staging, QA, release and rollback;
- deployment platforms and domain/DNS/ownership workflows;
- analytics, search validation and conversion measurement;
- AI-assisted and agentic website production;
- automated local-business website factory workflows;
- cost, speed, quality and repeatability improvement.

## Canonical Storage

- Project entrypoint: this file.
- Current state: `PROJECT_STATE.md`.
- Own-system execution rule: `OWN_SYSTEM_EXECUTION_STANDARD.md`.
- Task router: `ROUTER.md`.
- Global capability/standards registry: `SOURCE_REGISTRY.md`.
- Website tool/donor registry: `TOOL_DONOR_REGISTRY.md`.
- Site Model / Site Instance contract: `SITE_MODEL_STANDARD.md`.
- Universal visual editor standard: `EDITOR_CREATION_STANDARD.md`.
- **Running shared engine implementation:** `engine/`.
- Engine entrypoint / local-run contract: `engine/README.md`.
- Engine verification state / evidence: `engine/STATUS.md`.
- Second-opinion decision record: `reviews/SECOND_OPINION_DECISION_2026-09-13.md`.
- Project Drive root: https://drive.google.com/drive/folders/15DIWML8HiLSJrNfP5r7IyZu_YkrD2GTU
- GitHub/PEOS remains canonical for reusable standards, routing and shared engine code.

## Existing Solution First

Before inventing a new website mechanism:

1. Check Website Creator standards, components and tool registry.
2. Check the running shared engine in `engine/`.
3. Check reusable PEOS standards/blocks.
4. Check generic internal tools and SOFT inventory.
5. Check current official documentation and proven external solutions.
6. Prefer a mature open-source/self-hostable/replaceable building block when it can live inside our architecture and preserve our canonical Site Model/data ownership.
7. Adapt/integrate first.
8. Custom-build only the verified gap.

A third-party hosted platform must not silently become the Website Creator foundation. Hosted services may be optional adapters or temporary infrastructure only when explicitly selected and replaceable.

Canonical standards:
- `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `OWN_SYSTEM_EXECUTION_STANDARD.md`

## Default Production Chain

`RESEARCH READY → SITE MODEL DRAFT → STRATEGY / IA READY → DESIGN SYSTEM READY → CONTENT / DATA READY → SHARED ENGINE / RENDERER BOUND → EDITOR READY (when needed) → SEO / TECHNICAL QA → VISUAL / RESPONSIVE QA → PREVIEW / STAGING → RELEASE GATES → PRODUCTION DEPLOY → LIVE VERIFY → MEASURE / IMPROVE`

The exact ordering between Site Model, strategy, design and content may iterate during a real build; the important rule is that reusable execution must converge on a machine-readable site contract instead of leaving every layer to invent its own page state.

For automated local-business sales workflows:

`DISCOVERY → QUALIFICATION → DOSSIER → SITE MODEL POPULATED → SHARED WEBSITE CREATOR ENGINE → SAFE EDITOR → QA → PREVIEW → OUTREACH / TRIAL → SALE → DOMAIN / OWNERSHIP TRANSFER → SUPPORT`

## Core Principles

- Generated code is not a finished website.
- A successful build is not a published website.
- A preview URL is not production approval.
- Website Creator is the global knowledge/control plane plus reusable execution system; the Site Model is the reusable execution contract for a concrete site.
- New sites consume shared capabilities; they do not rebuild generic infrastructure.
- Structured facts/content should be separable from rendering when scale/reuse requires it.
- Media transformations should be traceable and non-destructive where practical.
- Editing and publishing are distinct states.
- Deterministic QA and visual QA solve different problems; both may be required.
- Live deployed behavior is part of acceptance.
- Repeated successful work should be promoted into deterministic reusable capabilities.
- Open-source/self-hostable components are preferred when they reduce build time without owning canonical site state.
- Do not introduce arbitrary hosted execution dependencies without explicit architecture justification.
- Do not create a deeper runtime/OS layer merely in anticipation of future scale; require production evidence.

## Architecture Review Rule

External reviews and vendor research are inputs, not automatic authority.

For architecture changes:

`READ → RESEARCH → REVIEW → ACCEPT / MODIFY / REJECT → IMPLEMENT ACCEPTED CHANGES → VERIFY`.

Do not rebuild Website Creator around a review without an explicit decision record.

## Read Next

1. `PROJECT_STATE.md`
2. `OWN_SYSTEM_EXECUTION_STANDARD.md`
3. `engine/STATUS.md` when implementation/runtime state matters
4. `SITE_MODEL_STANDARD.md`
5. `ROUTER.md`
6. the narrow standard selected by the router
7. `engine/README.md` for shared-engine implementation work
8. `SOURCE_REGISTRY.md` when locating a reusable capability
9. `TOOL_DONOR_REGISTRY.md` when selecting implementation building blocks
10. `../../blocks/design/BLOCK.md` for website design/UI work

## Success Condition

A fresh chat can enter Website Creator and create or update a site by using the shared Website Creator engine, contracts and reusable capabilities, without needing a client project, rebuilding editor/renderer/deploy plumbing, inventing a new architecture, or introducing an arbitrary execution platform.

As real sites are produced, reusable execution state should converge on a validated Site Model + shared component/editor/renderer/QA/adapters pattern rather than repeated per-site reinvention.
