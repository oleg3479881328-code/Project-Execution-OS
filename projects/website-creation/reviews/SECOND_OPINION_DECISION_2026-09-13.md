# Website Creator — Second-Opinion Decision Review

Date: 2026-09-13
Status: ACCEPTED DECISION RECORD
Source review: independent second-opinion architecture/technical review delivered 2026-09-13.

## Purpose

This file records Website Creator's own decision on the independent review. The external review is evidence/input, not an automatic architecture authority.

Decision labels:
- `ACCEPT` — adopt the recommendation substantially as written.
- `MODIFY` — adopt the underlying idea with a different boundary, timing, or implementation.
- `REJECT` — do not adopt the recommendation as stated.

## Governing Boundary

Website Creator remains a **global PEOS website-production knowledge/control plane plus reusable capability system**. It is not required to become one monolithic website-builder runtime.

Execution capabilities may grow underneath it where repeated real work proves they are useful. Those capabilities should prefer stable contracts and adapters over bespoke per-site infrastructure.

---

## Decision Matrix

### 1. “Website Creator is a specification, not a system”
Decision: `MODIFY`.

Accepted observation: most Website Creator core artifacts are currently standards/contracts/routing, not an independent runtime.

Rejected implication: lack of a monolithic runtime is not itself a defect. PEOS intentionally allows document-first control planes. The real gap is only where repeated execution still has no reusable implementation/capability.

Action: keep knowledge/control plane separate from execution layer.

### 2. Canonical platform-independent Site Model
Decision: `MODIFY — HIGH PRIORITY`.

Accept the need for a versioned Site Model as the contract for reusable execution: renderers, editors, SEO, QA, deployment adapters and Site Instances should be able to depend on one stable representation.

Modification: do **not** design a universal giant schema in the abstract. Derive `Site Model v0.1` from the first real new-site validation, then test/generalize it against additional different sites before freezing broad requirements.

Canonical direction: `SITE_MODEL_STANDARD.md`.

### 3. Reference renderer
Decision: `MODIFY`.

A reference renderer is useful as proof that the Site Model can produce a real site and that editor/public output can agree.

Modification: create it together with the first real Site Model validation. Do not block all Website Creator work until a renderer exists.

### 4. Stop all further standards work until Site Model exists
Decision: `REJECT`.

Reason: routing, QA, release, security and tool-selection standards can improve independently. The Site Model is important, but should not become a new artificial bottleneck.

### 5. Visual editor build-vs-buy review
Decision: `ACCEPT WITH MODIFICATION`.

The Universal Visual Editor behavioral contract remains authoritative and should not be discarded. Existing internal implementation patterns remain valid evidence.

Before expanding implementation-specific editor infrastructure, run a real build-vs-buy/adapt comparison against current mature external visual editing/CMS options. Score every candidate against the same Website Creator acceptance contract.

No vendor wins by default. No existing internal solution wins merely because it already exists.

### 6. Freeze implementation-specific editor expansion until comparison
Decision: `MODIFY`.

Do not freeze the behavioral contract. Continue improving universal requirements when real production exposes a gap.

Avoid deeper vendor/library-specific architecture unless required by a real implementation or comparison spike.

### 7. Design duplication between Website Creator and PEOS Design Block
Decision: `ACCEPT`.

Website Creator should route design work to `../../blocks/design/BLOCK.md` and should not maintain a second abbreviated design pipeline that can drift.

Action: SOURCE_REGISTRY design section becomes a thin pointer/boundary, not a duplicate design standard.

### 8. Deterministic browser QA with Playwright
Decision: `ACCEPT`.

Playwright becomes the default browser-level deterministic QA layer for Website Creator where browser automation is applicable.

Visual-regression services/frameworks such as Percy/Chromatic remain conditional candidates, selected when the project actually needs baseline-diff infrastructure or a component catalogue.

Human visual/taste review remains separate from deterministic QA.

### 9. Website Factory: integrate provisioning/hosting/permissions instead of rebuilding by default
Decision: `ACCEPT WITH MODIFICATION`.

Keep proprietary value in research, qualification, dossier, strategy/design intelligence, content orchestration, QA and sales workflow.

Prefer ready-made infrastructure for generic provisioning, hosting, permissions and client editing when it meets acceptance criteria.

Modification: do not select Duda, 10Web, B12 or another platform as default from research alone. Run identical-input real comparisons first and record export/ownership/editor/permission/cost/quality evidence.

### 10. B12 as an additional factory comparison candidate
Decision: `ACCEPT AS RESEARCH CANDIDATE`.

Add it to the candidate set, but revalidate current capabilities/terms from official sources before any adoption decision.

### 11. Client isolation / multi-tenancy model
Decision: `ACCEPT`.

A reusable Site Instance architecture must define separation of content, media, credentials, domains, editor permissions and deployment authority.

Gate: this must be explicit before Website Factory operates multiple live client sites through shared infrastructure.

Do not place secrets inside the Site Model.

### 12. Content history / rollback separate from code rollback
Decision: `ACCEPT`.

Editing/publishing infrastructure must provide content revision/history and rollback semantics appropriate to the chosen CMS/editor. Git rollback alone is insufficient when content is stored outside code.

### 13. Version the golden editor references
Decision: `ACCEPT`.

Golden visual acceptance evidence must be durable and version-addressable. The behavioral contract should identify the exact accepted reference version/hash/revision rather than depend on an unversioned replaceable image link.

Current Drive references remain temporary until normalized.

### 14. Per-task loading manifest / mechanical routing enforcement
Decision: `MODIFY / DEFER`.

The problem is real, but Website Creator is not yet large enough to justify another routing subsystem automatically.

Keep the narrow-loading rule now. Add task manifests only when repeated evidence shows agents are overloading context or choosing wrong routes.

### 15. Revalidation governance for third-party facts
Decision: `ACCEPT`.

Every adoption decision involving external pricing, API behavior, licensing, export, permissions or product features must record the validation date/source and be revalidated when the decision is executed or materially revisited.

Do not invent a fixed calendar interval unless operational evidence justifies one.

### 16. SEO/AEO 2026 corrections from the review
Decision: `ACCEPT PENDING OFFICIAL REVALIDATION`.

The review flags current search-result/schema changes. Because these are time-sensitive external facts, update the canonical SEO standard only after checking current official Google documentation. Do not promote a second-opinion claim directly into canonical truth.

### 17. Simplify tool status taxonomy to DECIDED/CANDIDATE/REJECTED
Decision: `REJECT FOR NOW`.

The current registry distinguishes internal capabilities, proven options, donors and conditional external tools, which remains useful.

Improvement accepted: make decision uncertainty explicit in individual entries (for example, proven implementation option but default platform decision still pending).

### 18. Website Creator should grow a deeper internal OS now
Decision: `REJECT FOR NOW`.

Do not create another operating-system layer by anticipation.

Re-evaluate after multiple real sites reveal repeated execution/state-management needs that cannot be represented cleanly by PEOS + Website Creator standards/capabilities.

### 19. Website Creator → Site Instance model
Decision: `ACCEPT WITH MODIFICATION`.

A Site Instance should be a project-specific population of the canonical Site Model plus assets, selected renderer/editor/platform bindings, QA/release state and deployment references.

It should not automatically mean a bespoke per-client codebase.

### 20. Fixed scaling breakpoint (for example “switch around 20 sites”)
Decision: `REJECT AS UNIVERSAL RULE`.

Scale transitions depend on support load, platform economics, editor requirements, site complexity, traffic, automation quality and ownership constraints. Use measured operational thresholds rather than a borrowed fixed number.

---

## Accepted Target Architecture

Website Creator remains the control/knowledge plane.

Reusable execution evolves toward:

`RESEARCH / EVIDENCE`
→ `SITE MODEL DRAFT`
→ `DESIGN SYSTEM (PEOS Design Block)`
→ `CONTENT + MEDIA POPULATION`
→ `EDITOR / CMS BINDING WHEN NEEDED`
→ `RENDERER / EXECUTION ADAPTER`
→ `SEO / DISCOVERY PASS`
→ `DETERMINISTIC QA`
→ `VISUAL / HUMAN QA`
→ `PREVIEW / RELEASE GATES`
→ `PRODUCTION DEPLOY`
→ `LIVE VERIFY`
→ `MEASURE / IMPROVE`

The Site Model is the execution contract, not a replacement for Website Creator's knowledge/control plane.

## Accepted Priority Order

### P0
- establish `SITE_MODEL_STANDARD.md` and derive v0.1 from the first real new-site validation;
- require editor build-vs-buy/adapt comparison before major new editor infrastructure.

### P1
- make Design Block the single design-process authority;
- use Playwright as default browser QA where applicable;
- run identical-input Website Factory platform comparison without pre-selecting a winner;
- establish a first reference renderer alongside Site Model v0.1.

### P2
- define Site Instance/client isolation rules before shared multi-client live operation;
- add content rollback/version history requirements;
- version/hash golden visual references;
- revalidate and then update time-sensitive SEO/AEO rules.

### P3 / Evidence-triggered
- task-specific loading manifests if context-routing failures appear;
- deeper Website Creator runtime/OS only if repeated execution proves the need;
- taxonomy simplification only if current statuses cause operational confusion.

## Final Decision

Do not rebuild Website Creator around the review. Use the review to close concrete gaps while preserving the project boundary:

**Website Creator = global reusable website-production control plane.**

**Site Model + renderers + editor/platform adapters + QA = reusable execution layer beneath it.**

Architecture changes should now be validated through real site production rather than increasingly abstract design.