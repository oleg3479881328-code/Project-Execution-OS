# Shared Web Platform Registry

## Purpose

This registry is the durable cross-project index for reusable web-platform solutions discovered in client projects.

It is not a code repository by itself. It records what is reusable, what evidence exists, what remains client-specific, and whether the item is only a candidate or already proven.

## Status Values

- `CANDIDATE` — appears reusable but is not yet cleared for shared adoption.
- `PROVEN` — reusable boundary reviewed; may be consumed by other projects.
- `DEPRECATED` — kept for history but should not be used for new work.

## Registry

### WEB-CMS-SOT-001 — Published CMS source of truth

- Status: `PROVEN`
- Origin: Olga Polo
- Cross-project evidence: Tusia uses the same editor-driven site architecture and is intentionally based on the Olga pattern.
- Invariant: fields editable by the client must resolve from the published CMS source everywhere they appear: hub/list, detail page, metadata, canonical/OG/schema projections where applicable.
- Failure mode: one render path reads current CMS content while another reads stale static registry values.
- Client-specific exclusions: venue names, content, brand assets, domains, secret/env names.
- Required checks: published source resolves consistently across all consuming surfaces; invalid published document fails loudly rather than silently using stale fallback.

### WEB-CMS-PARITY-001 — Published/fallback responsive parity

- Status: `PROVEN`
- Origin: Olga Polo mobile incident
- Invariant: CMS-published and fallback/non-published entity pages must satisfy the same responsive presentation contract even when their content renderer differs.
- Failure mode: edited/published entities use a separate shell/CSS path and break on mobile while untouched entities look correct.
- Required checks: at least one published entity and one fallback entity on desktop and mobile; no horizontal overflow; typography constrained to viewport; shared shell behavior verified.
- Exclusions: brand-specific pixel values and visual snapshots.

### WEB-ENTITY-ID-001 — Stable entity identity separate from slug/URL

- Status: `CANDIDATE`
- Origin: Olga Polo venue migration
- Cross-project relevance: Tusia has the same Venue/Wedding entity architecture.
- Invariant: content identity must not depend on the current public URL or slug; routing may migrate without losing editor/data bindings.
- Review still needed: code-level comparison against Tusia durable source before shared code extraction.

### WEB-PUBLISH-001 — Centralized one-click publish pipeline

- Status: `CANDIDATE`
- Origin: Olga Polo Puck editor
- Pattern: editor data/assets → durable published document/assets → versioned source → deployment → public-version verification.
- Proven concept: one client-facing Publish action; no manual second deployment step for the client.
- Current blocker for shared code: Olga implementation contains project-specific environment names, default repo/branch, actor/source strings, and project assumptions.
- Next action: extract a generic publish adapter contract only after Olga ↔ Tusia code-level comparison.

### WEB-SEO-STATE-001 — Preview/indexing state is explicit

- Status: `PROVEN`
- Origin: Olga + Tusia
- Invariant: preview/new layer remains `noindex,nofollow` until intentional SEO readiness/cutover; indexability must be a deliberate state, not an accidental side effect of deployment.
- Required checks: robots/meta state, canonical host/path, sitemap readiness before enabling indexability.

### WEB-BRAND-SHELL-001 — Engine shared, brand shell local

- Status: `PROVEN`
- Origin: Olga → Tusia
- Invariant: shared platform behavior may be common, but header/footer/menu/type system/crops/brand tokens remain project-specific unless a narrower reusable primitive is identified.
- Failure mode: copying one client's visual shell into another under the label of shared core.

### WEB-DESIGN-EVIDENCE-001 — Viewports are independent donor states

- Status: `PROVEN`
- Origin: Universal Site Design Extractor work across Olga/Tusia
- Invariant: mobile/tablet/desktop captures are independent evidence states; do not infer mobile from desktop.
- Required checks: suspicious geometry that exceeds viewport is flagged and reconciled against screenshots/other evidence before implementation.

## Current Shared-Code Extraction Gate

Do not create a shared npm/package implementation from Olga code yet.

Reason:

1. Olga has strong implementation evidence.
2. Tusia is a second real architectural consumer and the projects are intentionally near-identical.
3. However the currently discoverable Tusia project is represented by Notion + Vercel deployment evidence, while a separate durable GitHub repository was not found.
4. Therefore the knowledge-level invariants can be promoted now, but shared code must wait for a real code-level comparison or an owner-approved earlier extraction.

## Near-Identical Project Operating Rule

For Olga, Tusia, and future sites built from the same platform:

```text
furthest-ahead project
→ isolate generic improvement
→ independent review
→ promote to registry/shared layer
→ lagging projects consume it
```

Do not solve the same platform problem separately in each chat.

## Next Extraction Set

After Tusia durable code source is located or reconstructed into a durable repo:

1. compare entity contracts;
2. compare published content document shapes;
3. compare editor/publish lifecycle;
4. compare routing and public path resolution;
5. compare SEO/indexing state helpers;
6. compare responsive shell boundaries;
7. design the smallest client-neutral interfaces;
8. independently review them;
9. create shared code only after that review passes.

## Governance

Promotion follows `docs/SHARED_SOLUTION_PROMOTION_STANDARD.md`.

Project-specific exceptions must remain in the project and must not silently weaken a shared invariant.
