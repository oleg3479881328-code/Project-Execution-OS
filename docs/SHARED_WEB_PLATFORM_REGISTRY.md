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
- Shared-code status: represented in `packages/shared-web-core-v0.1/src/contracts.ts`; production dependency adoption still pending real client canary.

### WEB-PUBLISH-001 — Centralized one-click publish pipeline

- Status: `CANDIDATE`
- Origin: Olga Polo Puck editor
- Pattern: editor data/assets → durable published document/assets → versioned source → deployment → public-version verification.
- Proven concept: one client-facing Publish action; no manual second deployment step for the client.
- Shared-code status: generic `PublishAdapter`, `PublishReceipt` and public-version verification contracts now exist in `packages/shared-web-core-v0.1/src/contracts.ts`; no Olga repo/branch/env defaults were copied.
- Remaining gate: production canary integration and review.

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

## Shared Web Core v0.1 — current state

Owner approved early extraction because Olga and Tusia are intentionally near-identical project instances and the goal is to stop chat-to-chat architectural drift.

Created candidate contract layer:

- `packages/shared-web-core-v0.1/src/contracts.ts`
- `packages/shared-web-core-v0.1/canaries/tusia-runtime-canary.json`
- `packages/shared-web-core-v0.1/scripts/validate-canary.mjs`
- `.github/workflows/shared-web-core-canary.yml`

Important boundary:

- this is a **contract canary**, not a full shared UI/CMS implementation;
- the Tusia canary is a durable runtime-recovery artifact and does not pretend to be original source code;
- unknown Tusia internals remain explicitly `unknown`;
- production projects are not yet automatically migrated to this package.

## Current Shared-Code Promotion Gate

v0.1 stays `CANDIDATE` until:

1. independent review confirms the contracts contain no hidden Olga-specific assumptions;
2. a real client canary consumes the contracts in its codebase;
3. build/runtime regression passes;
4. the capability matrix is updated with adoption evidence.

Tusia is preferred as first real integration canary once its durable source is located or reconstructed as an actual maintainable source tree.

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

1. production canary integration of stable entity identity;
2. production canary integration of published-content resolver contract;
3. publish adapter implementation behind client-specific configuration;
4. hostname-aware indexing/publication helper;
5. shared responsive parity test harness without brand snapshots;
6. independent review;
7. only then version/publish as a true reusable package consumed by sibling projects.

## Governance

Promotion follows `docs/SHARED_SOLUTION_PROMOTION_STANDARD.md`.

Project-specific exceptions must remain in the project and must not silently weaken a shared invariant.
