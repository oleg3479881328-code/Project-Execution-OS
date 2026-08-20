# GLOBAL PROJECT KNOWLEDGE DATABASE STANDARD

## Status

**GLOBAL / MANDATORY / CROSS-PROJECT**

This standard applies to Olga Polo, Tusia/Tasha Hurley and every future photographer/site/market project built under Project Execution OS. The architecture is reusable beyond photography whenever a project has material structured entities, relationships, evidence, media and production output.

## Core Law

Each project with material structured research/content must have **one central operational Knowledge Database** that acts as the structured project source of truth.

Do not scatter canonical structured data across ad-hoc Sheets, Notion tables, chat, repo JSON and one-off research files without a defined ingestion/crosswalk path.

Default production flow:

`internal sources -> identity resolution -> Project Knowledge Database -> Page Queue -> QA gates -> Page Factory/application -> publish -> verification -> feedback into Knowledge Database`

## Separation of Responsibilities

### Project Knowledge Database

Use for structured operational truth that must drive code, graphs, SEO/AEO, pages, automation and QA. For current photographer projects this may be a Google Sheet or other structured datastore.

Typical layers:

- `Entities Master`
- `ID Crosswalk`
- category/entity source tables
- `People`
- `Events`
- `Relationships`
- `Evidence`
- `Reviews`
- `Geography`
- `Media`
- `SEO Publishability` / scoring
- `Page Queue`
- `Redirects / URLs`
- `QA`
- `Change Log`
- `Dashboard`

### Notion

Human-readable project memory, decisions, research dossiers, architecture, audits, handoffs, explanations and deep entity dossiers. Notion is not automatically the best operational source for high-volume structured production data.

### GitHub

Committed reusable standards, schemas/contracts, code, application adapters, generators, QA logic and implementation evidence. GitHub is the executable/standards layer, not the client-specific research warehouse.

### Chat

Temporary execution context. Material structured knowledge must not remain stranded only in chat.

## Project Database vs Global Identity

One central project database does **not** mean one giant global client database.

Each photographer/client/market may have its own Project Knowledge Database because project relevance, publishability, local relationships, media rights and production state are project-specific.

Identity resolution still follows `docs/ENTITY_DOSSIER_STANDARD.md`: the same real entity must not be conceptually duplicated merely because it appears in several projects. Preserve cross-project/global identity and source-system IDs through crosswalks where architecture permits.

## Mandatory Entity Architecture

The central database must support stable IDs and graph relations. Typical photographer model:

`Photographer <-> Wedding/Event <-> Venue <-> Vendor/Partner <-> Person <-> City/Region <-> Publication/Review <-> Media`

A shared event is represented by event-role edges. It does not automatically create direct business-to-business relationships. Direct relationships such as `REPEATED_COLLABORATION`, `RECOMMENDS`, `PREFERRED_VENDOR`, `AFFILIATED_WITH` or `PUBLICATION_CO_CREDIT` require direct evidence.

## Search-Before-Research Rule

Before external web research or creation of a new entity:

1. search the Project Knowledge Database;
2. search Google Drive / Google Sheets and existing project inventories;
3. search Notion project memory/dossiers/audits;
4. search GitHub/data stores where relevant;
5. resolve aliases/source-system IDs through `ID Crosswalk`;
6. use external research only for unresolved gaps, stale fields or verification.

## Master Registry Rule

`Entities Master` is the project-wide operational index, not a second manually maintained copy of every source table.

Where possible it should derive or aggregate:

- canonical/source ID;
- entity name/class/source layer;
- alias/merge status;
- relationship count;
- evidence count;
- review count;
- direct-client relationship flag;
- publishability;
- publish priority;
- dossier status;
- QA status.

Detailed category-specific fields may remain in source/category tables. Avoid duplicating hundreds of fields into the master index unless the master truly owns them.

## ID Crosswalk Rule

Never destroy old IDs simply because a canonical record changes.

Use an explicit crosswalk for:

- legacy ID -> canonical ID;
- source-system ID -> project operational ID;
- aliases/rebrands;
- merged brands/businesses;
- historical records.

Pattern:

`legacy/source ID <-> canonical project ID <-> global dossier identity`

## Media Rule

Media is a first-class data layer, not an afterthought. A public SEO page should not be marked production-ready merely because entity text exists.

Track at minimum:

- media/source ID;
- related entity/event;
- source URL or asset pointer;
- first-party/third-party provenance;
- media type;
- rights/usage status where relevant;
- page suitability/readiness;
- verification state.

## Page Queue Rule

No direct jump from research notes to code-generated public pages.

Every candidate page passes through `Page Queue`, recording at minimum:

- page candidate ID;
- entity/event ID;
- page type;
- publishability;
- priority;
- stage;
- proposed slug;
- canonical URL;
- media readiness;
- relationship readiness;
- evidence readiness;
- technical QA;
- blocker/notes.

This separates **knowledge readiness** from **page generation**.

## Publishability Gate

A page may enter public production only when required conditions for that page type are satisfied. For SEO-v3 photographer pages this normally includes:

- identity resolved;
- key factual fields supported;
- useful unique user value;
- real media/source material;
- meaningful graph relation(s);
- first-party or otherwise verified context;
- canonical/robots/schema decision;
- no invented facts;
- reciprocal/internal linking plan where applicable;
- conversion path.

## URL / Redirect Preservation Law

Existing public URLs are assets. Page Factory must not silently replace them.

Maintain a central `Redirects / URLs` registry for:

- existing URL;
- proposed/new URL;
- canonical target;
- keep/redirect/deprecate decision;
- 301 mapping;
- sitemap state;
- verification status.

Changed public URLs require explicit mapping and QA. Preserve useful existing URLs unless there is a documented reason to change them.

## QA Layer

The central database must make data defects visible before production. QA checks should include, as relevant:

- duplicate canonical IDs;
- unmapped legacy IDs;
- orphan relation targets;
- publish-now rows with missing technical QA;
- pages without media/evidence/relations;
- unresolved redirects/canonical conflicts;
- stale/unverified evidence;
- contradictions;
- missing reciprocal links;
- project-specific publishability violations.

QA failures are blockers, not cosmetic warnings, when they affect identity, evidence, indexing, rights or production correctness.

## Dashboard Rule

Every serious Project Knowledge Database should expose a compact operational dashboard. Useful metrics include:

- unique entities;
- events;
- relationships;
- evidence records;
- reviews;
- media records;
- publish-now count;
- enrich count;
- priority queue count;
- duplicate IDs;
- crosswalk rows;
- URL/redirect rows;
- open QA items.

The dashboard is for operational visibility, not a second manual reporting system.

## Change Log Rule

Major schema changes, migrations, bulk normalizations, merge decisions, recovered stranded evidence, page-gate changes and URL mapping decisions must be recorded in `Change Log` with date and short reason.

## Page Factory Contract

Page Factory consumes **approved structured data**, not arbitrary chat prose or unverified research notes.

Expected direction:

`Knowledge Database adapters -> normalized entity/event/page model -> templates/components -> structured data/schema/internal links -> preview -> technical QA -> explicit production release`

Preview/staging remains `noindex,nofollow` until explicit production approval where this project rule applies.

## Photographer-Project Default

For photographer ecosystems, start with:

1. Photographer/client identity.
2. Weddings/events.
3. Venues.
4. Vendors/partners/people.
5. Geography.
6. Publications/reviews/authority.
7. Media.
8. Relationships/evidence.
9. Page Queue and URL mapping.
10. QA and publishing feedback.

Do not begin by generating hundreds of thin pages. Build a Knowledge Engine first, then generate only candidates that pass publishability gates.

## Migration Rule for Existing Projects

Do not throw away useful existing category tabs/databases simply to make the architecture look cleaner.

Migration sequence:

1. inventory existing sources;
2. choose the central Project Knowledge Database;
3. create `Entities Master` and `ID Crosswalk`;
4. retain useful category/source tables as subordinate layers;
5. connect `Events / Relationships / Evidence / Reviews / People`;
6. add `Geography / Media / Page Queue / Redirects / QA / Change Log / Dashboard` as needed;
7. recover stranded evidence and missing edges;
8. verify counts and QA;
9. only then connect Page Factory.

## Completion Criterion

A structured-data project is not architecturally complete if:

- multiple conflicting operational sources of truth remain without a declared winner;
- source-system IDs are discarded instead of crosswalked;
- material evidence/media/relationships are stranded outside the central database;
- Page Factory can publish without passing the queue and QA gates;
- existing public URLs can be replaced without mapping and verification;
- new agents cannot discover the central database and its role from the project entrypoint/global router.

## Proven Origin

This standard was proven during the 2026-08-20 Olga Polo Cincinnati consolidation. The existing `Cincinnati Wedding Ecosystem` workbook was retained under the same file ID and evolved into `Olga Knowledge Database v1 — Cincinnati Wedding Ecosystem` rather than replaced.

The implementation added a live master entity registry, ID crosswalk, geography/media/page-production layers, URL preservation, QA, change log and dashboard while preserving useful existing category, event, relationship, evidence, review and people tables.

The globally reusable lesson is architectural, not client-specific:

**centralize structured operational truth, preserve provenance and IDs, gate generation through QA, and keep human memory/code standards in their proper systems.**
