# Website Creator — SOURCE_REGISTRY.md

## Purpose

This is the global registry of reusable Website Creator standards, production contracts and capability families.

It intentionally does **not** index client projects. Website Creator stores promoted/generalized knowledge so a new site can be built without reopening the project where a technique was first discovered.

## Promotion Rule

A client/project-specific finding enters this registry only after:

`VERIFY → GENERALIZE → DE-IDENTIFY → DEFINE REUSABLE CONTRACT → STORE HERE OR IN A LINKED GLOBAL STANDARD`.

A client-project URL is not an acceptable substitute for a reusable standard.

---

## 1. Project Core

- Project entrypoint: `PROJECT.md`
- Current state: `PROJECT_STATE.md`
- Router: `ROUTER.md`
- Tool/donor registry: `TOOL_DONOR_REGISTRY.md`
- Site Model / Site Instance: `SITE_MODEL_STANDARD.md`
- Universal visual editor: `EDITOR_CREATION_STANDARD.md`
- Second-opinion decision record: `reviews/SECOND_OPINION_DECISION_2026-09-13.md`
- Design orchestrator: `../../blocks/design/BLOCK.md`
- Existing Solution First: `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- Project Drive root: https://drive.google.com/drive/folders/15DIWML8HiLSJrNfP5r7IyZu_YkrD2GTU

---

## 2. Research & Evidence

Reusable contract:

- confirm the real business/site/entity identity before generating public factual content;
- prefer first-party/official evidence for factual claims;
- preserve source/evidence/confidence where structured research is used;
- unknown remains unknown rather than being filled by plausible invention;
- audit an existing site before replacing/redesigning it;
- record current URLs, important assets, forms, integrations and SEO surfaces before migration;
- distinguish research candidates from approved production facts.

Related global PEOS standards:
- `../../docs/ENTITY_DOSSIER_STANDARD.md`
- `../../docs/PROJECT_KNOWLEDGE_DATABASE_STANDARD.md`

Existing internal capability family:
- Website Intelligence / Site Baseline Scanner — existing-site inspection/qualification; canonical packaging still subject to normalization.

---

## 3. Strategy & Information Architecture

Reusable contract:

1. define business goal;
2. define primary user action/conversion;
3. define primary user scenarios;
4. inventory required content/entities/services;
5. create sitemap/page families;
6. assign purpose + CTA to each page;
7. define internal-link/cluster strategy where useful;
8. define what must remain stable during migration/redesign.

Do not choose a frontend stack or visual style before the product/site problem is sufficiently defined.

---

## 4. Design / UI / Motion

Canonical authority:
- `../../blocks/design/BLOCK.md`

Website Creator **does not maintain a second abbreviated design pipeline**. Route design work into the PEOS Design Block and its narrower standards.

Website Creator only owns the integration boundary:

- design decisions/tokens/components must be representable by the concrete site implementation;
- where a Site Model is used, design-system binding should remain separable from vendor-specific renderer details where practical;
- deterministic correctness QA and human visual/taste QA remain different gates;
- Design Picker and Universal Site Design Extractor are reusable supporting tools, not replacement design authorities.

---

## 5. Site Model / Content & Data

Canonical Site Model contract:
- `SITE_MODEL_STANDARD.md`

Architecture direction:

- the Site Model is the platform-independent execution contract for one Site Instance;
- derive `v0.1` from a real new-site build rather than inventing an exhaustive universal schema;
- structured facts/content should remain separable from rendering when repeatability/editing/migration/scale requires it;
- renderer/platform/editor bindings consume the model or a deterministic mapped representation;
- secrets do not belong in the Site Model;
- Site Instances identify their model/schema version once versioning becomes concrete.

Reusable content/data rules:

- use stable IDs/slugs for reusable entities/page records where needed;
- preserve source/status/evidence metadata for factual production systems;
- reusable page templates/renderers consume approved structured records rather than performing hidden ad-hoc research;
- editorial content and factual fields should remain distinguishable;
- draft/staging/published states must be explicit;
- mass generation requires publishability/quality gates, not only available keywords.

Typical scalable chain:

`sources → identity/evidence → Site Model / structured record → renderer/editor/platform binding → QA gate → preview → release → measurement`.

---

## 6. Universal Visual Editor / CMS

Canonical:
- `EDITOR_CREATION_STANDARD.md`

Core contract:

- visual page editing in context;
- coordinated page/block structure, direct canvas manipulation and contextual inspector;
- selected image gets direct controls;
- visual crop/move/zoom workflow;
- non-destructive crop metadata;
- replace/remove/reset/shape/fill/whole-photo/size/alignment/text controls;
- bounded safe client permissions;
- editing state is not publication state;
- editor rendering and public rendering must agree;
- persistence across reload must be verified;
- production editing requires content history/rollback appropriate to the chosen storage/CMS architecture.

Golden visual acceptance references are stored in Website Creator Drive under the CMS/editor area and are treated as anonymous behavioral references. They are pending normalization into a durable version-addressable acceptance form.

Implementation-specific expansion is subject to a build-vs-buy/adapt comparison against the same behavioral contract.

---

## 7. Media

Reusable contract:

- original/master asset is not the same thing as a delivery derivative;
- preserve originals when transformations are required;
- transformations should be reproducible/traceable where practical;
- avoid unintentional upscaling;
- image crop/position/zoom should normally be non-destructive display metadata;
- delivery dimensions/compression should match target use;
- galleries need explicit selection/accounting rather than accidental duplication;
- filenames/alt/credit/caption must not invent unsupported facts.

For visual crop behavior see `EDITOR_CREATION_STANDARD.md`.

---

## 8. SEO & Discovery

Reusable technical contract:

- stable clean URLs/slugs;
- unique useful metadata where warranted;
- canonical correctness;
- robots/sitemap behavior verified;
- structured data aligned with visible supported content;
- crawlable useful internal links;
- existing public URLs treated as assets during migration;
- redirects/deprecations explicit;
- image SEO grounded in actual media/content;
- indexation/search evidence checked after release;
- page factories scale only after a smaller representative cluster proves quality/indexation/search value.

AEO/GEO principle:

Make real entities, relationships, services, expertise, geography and first-party evidence explicit and machine-understandable. Do not create invisible/fake authority signals.

Measurement chain where applicable:

`query → landing page → impression → click → conversion/inquiry`.

Useful platforms may include Google Search Console, analytics/event systems and schema validators.

Time-sensitive search/rich-result/schema claims must be revalidated from current official search-engine documentation before they are promoted into canonical rules. The 2026 independent review flagged changes that remain pending official revalidation.

---

## 9. Build & Release

Reusable release chain:

`IMPLEMENTED → LOCAL/BUILD CHECKS → VERSIONED CHANGE → PREVIEW/STAGING → QA → RELEASE APPROVAL → PRODUCTION DEPLOY → LIVE DESKTOP/MOBILE VERIFY → RELEASED`.

Rules:

- successful build != published;
- preview != production approval;
- keep source/change history for code-backed systems;
- use isolated changes/PRs when risk warrants it;
- identify known-good rollback target before risky release;
- verify the real deployed URL, not only localhost;
- domain/DNS changes require inventory of existing mail/forms/services and rollback;
- do not move a stable production surface merely because a new architecture is interesting;
- content stored outside code needs its own revision/history/rollback path.

Platforms are selected through `TOOL_DONOR_REGISTRY.md`, not hardcoded into this standard.

---

## 10. QA

Website acceptance can require multiple independent layers.

### Default browser-QA direction

Playwright is the default deterministic browser automation layer where browser-based QA is applicable. See `TOOL_DONOR_REGISTRY.md`.

Visual-regression services/frameworks may be added conditionally when baseline screenshot diffing/component-catalog workflows justify them.

### Deterministic / technical
- build/type/lint checks;
- broken asset/link detection;
- overflow/clipping checks;
- accessibility/contrast/focus/keyboard checks;
- responsive state checks;
- metadata/canonical/schema checks;
- expected media/content counts where applicable;
- Site Model/schema/reference validation when a Site Model is used.

### Visual / experiential
- desktop and mobile screenshots/live review;
- hierarchy/spacing/typography consistency;
- non-generic design quality;
- motion quality;
- design-system consistency;
- real interaction verification.

### Release/live
- HTTP/load success;
- images/assets load;
- forms/CTA paths work;
- no unexpected horizontal overflow;
- public rendering matches editor/preview intent;
- deployed state is actually the intended version.

Automated gates can prove correctness properties; they cannot alone prove taste.

---

## 11. Measurement & Optimization

Measure both production efficiency and website outcome.

Production:
- research time;
- design time;
- media-processing time;
- implementation time;
- build/deploy time;
- manual QA time;
- end-to-end wall-clock time;
- cost per preview/site.

Outcome:
- indexation/search visibility;
- page/query performance;
- behavior/engagement where useful;
- CTA/conversion/inquiry outcomes;
- client/editor usability;
- support/maintenance burden.

When a workflow feels slow, name the slow phase before redesigning the architecture.

---

## 12. Website Factory

Generic local-business factory model:

`prospect discovery → qualification → public-source research → business dossier → Site Model populated → content/IA/design direction → execution/platform binding → safe editor → QA → live preview → outreach/trial → purchase → domain/ownership transfer → support`.

Current architecture principle:

- keep research/design/content intelligence and QA under our control;
- use ready-made provisioning/editor/hosting/permissions/sales infrastructure when it meets quality/control/ownership/economics;
- build custom adapters/orchestration before building a generic platform from scratch;
- validate on real businesses with identical-input comparisons before declaring a vendor winner;
- do not use a fixed site-count threshold as a universal trigger for platform changes; measure cost/support/risk/complexity instead;
- before shared infrastructure operates multiple live client sites, define Site Instance isolation for content, media, credentials, permissions, deployment and domain authority.

Relevant external candidates/process donors are listed in `TOOL_DONOR_REGISTRY.md`.

---

## 13. Knowledge Maintenance

When a new reusable discovery appears:

1. verify it;
2. decide whether it is project-specific or universal;
3. if universal, generalize and de-identify it;
4. update the narrowest Website Creator standard/registry;
5. keep time-sensitive third-party facts marked for revalidation;
6. for adoption decisions that depend on external pricing/API/licensing/export/permissions/features, record the validation source/date and revalidate when the decision is executed or materially revisited;
7. avoid creating a parallel index unless scale truly requires it.

## Final Rule

Website Creator is a **production control/capability system**, not an archive of client projects and not automatically a monolithic builder runtime. Store reusable knowledge here in universal form and validate execution architecture through real site production.