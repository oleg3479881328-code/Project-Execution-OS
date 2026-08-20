# GLOBAL ENTITY DOSSIER STANDARD — One Entity, One Canonical Dossier

## Status

**GLOBAL / MANDATORY / CROSS-PROJECT**

This standard applies to every project, client, research domain, database, graph, CRM-like workflow, OSINT workflow, content system, automation and future agent workflow managed under Project Execution OS.

## Core Law

When an entity appears anywhere in the system, it must resolve to exactly **one canonical entity dossier**. The dossier is enriched over time. The same real-world entity must not be re-created as parallel records merely because it appears in a different project, event, source, table, report, workflow or conversation.

Default lifecycle:

`entity detected -> search existing canonical records -> identity resolution -> create/reuse one dossier -> enrich missing fields -> attach evidence -> attach relationships/events -> reuse everywhere`

## What Counts as an Entity

The rule is domain-agnostic. Examples include:

- person / contact / employee / public figure;
- company / business / vendor / client / competitor;
- venue / property / location / organization;
- product / service / software / tool / platform;
- project / repository / website / domain;
- publication / channel / account / profile;
- event / wedding / meeting / transaction when modeled as a reusable node;
- any other stable real-world or digital object that can recur across sources.

## Mandatory Identity-First Workflow

1. **Detect** the entity in any source or workflow.
2. **Search before creation** across the appropriate canonical registries, project databases, global knowledge base and known aliases.
3. **Resolve identity** using canonical name, aliases/former names, domain, phone, email, address, owner/contact person, social handles, IDs and other stable identifiers.
4. **Reuse or create exactly one canonical dossier.**
5. **Enrich the dossier** rather than opening a new parallel research record.
6. **Attach source/evidence** for material claims and keep verification state/date.
7. **Represent occurrences as relations/events/observations**, not duplicate entity rows.
8. **Reuse the canonical dossier** in downstream pages, graphs, CRM, SEO/AEO, outreach, reporting, automation and analysis.

## Canonical Dossier Field Families

### Identity

Canonical name; aliases/former names; entity type/category; stable internal ID; status; parent/child organization where relevant.

### Contact / Access

Website/domain; phone; email; address/service area; contact person/owner; official profiles; public contact routes.

### Social / Digital Identity

Instagram; Facebook; YouTube; TikTok; Pinterest; LinkedIn; Google Business; GitHub; X/Threads/other relevant platforms; platform-specific IDs/handles.

### Authority / Reputation

Reviews; ratings by source; publications; awards; associations; certifications; memberships; notable mentions; backlinks; public credits.

### Relationships / Graph

Projects; events; weddings; clients; vendors; employers; partnerships; preferred-vendor lists; recommendations; ownership; affiliations; repeat collaborations; referral relationships.

### Evidence / Provenance

Primary source; additional sources; evidence type; confidence; last verified; notes; contradictions; unresolved identity questions.

### Assets / Content

Images; logos; documents; media; relevant URLs; reusable descriptions; first-party notes.

### Operational / Publishability

Project relevance; SEO/AEO eligibility; outreach status; publishability; automation readiness; next enrichment step.

## Hard Rules

- **Search before create.** No new entity record until existing canonical records and aliases have been checked.
- **One real entity = one canonical dossier.**
- A new source, project, event or wedding is not a reason to create a second entity card.
- Missing fields trigger enrichment of the existing dossier.
- Occurrences belong in relations/events/observations, not duplicate entity records.
- Aliases and rebrands stay attached to one identity unless evidence proves separate entities.
- Unknown values remain unknown. Never invent contacts, owners, social URLs or relationships.
- Conflicting evidence is stored as a contradiction requiring resolution; do not silently overwrite it.
- Every material enrichment should retain source/provenance and verification date/status.
- Before external research, search our own accumulated system first to avoid researching the same entity repeatedly.

## Cross-Project Rule

Canonical identity may be global even when project-specific relationships are local. A company/person/tool should not be duplicated merely because it appears in different projects. Project-specific facts and relationships can remain in project layers while referencing the same canonical identity whenever architecture permits.

## Event / Relationship Rule

A shared event does not automatically imply a direct relationship between every participant. Model the event as its own node/observation and attach role-specific edges. Create direct entity-to-entity relationships only when evidence supports a direct relationship.

## Research Rule

The default research action changes from:

`question -> web search -> notes`

into:

`question -> identify entities -> resolve existing dossiers -> inspect already-known evidence -> enrich only missing/uncertain fields -> attach new evidence/relations`

This prevents repeated research, duplicated records, conflicting facts and wasted tokens/time.

## Agent Behavior

Every agent/chat operating under Project Execution OS must treat entity resolution as part of normal execution, not as a separate optional cleanup task. When new information about an existing entity appears, update the dossier during the work whenever practical.

## Migration / Legacy Handling

Legacy duplicate records are observations/evidence, not automatically deleted. During normalization:

1. identify the winning canonical entity;
2. merge unique verified fields/evidence;
3. move event/project-specific facts into relations/observations;
4. preserve source provenance;
5. mark/archive legacy duplicates only after their information is safely retained.

## Completion Criterion

For entity-heavy work, a task is not fully complete if useful new entity information remains stranded only in chat, a one-off report, or a duplicate project row. Material entity knowledge must be promoted to the canonical dossier/registry when the system supports it.

## Proven Origin

This global rule was promoted after the Olga/Cincinnati wedding ecosystem showed that the main bottleneck was not lack of research but duplicated and disconnected entity data across Wedding Master Inventory, Vendor Network, Venue DB, Cincinnati Wedding Ecosystem, Referral Graph and OSINT layers.
