# Tusia Runtime Recovery and Olga Comparison

## Purpose

This document creates a durable, evidence-based snapshot of the currently deployed Tusia/Tasha prototype and compares its observable platform capabilities against the durable Olga implementation.

Important: the original Tusia source repository was not found in GitHub, Google Drive, or File Library. Therefore this is **not claimed to be the original source code**. It is a durable runtime recovery record based on the deployed Vercel artifact plus project memory. It is sufficient for capability-level synchronization, but it does not replace a true source-level diff.

## Current deployed Tusia evidence

Vercel project:
- project: `tasha-hurley-weddings-preview`
- project ID: `prj_0jyr5Ue9rSjJQS6q6hJneSrwgOnr`
- framework: Next.js
- latest inspected deployment: `dpl_957sk9KPvXH2zoTM1dd2b4vQBRUC`
- state: `READY`
- route inspected: `/venues`

Observable runtime facts from the rendered HTML:
- Next.js App Router runtime;
- `meta viewport=width=device-width, initial-scale=1`;
- `robots: noindex,nofollow` and `x-robots-tag: noindex`;
- separate desktop and mobile header structures;
- mobile shell uses `logo + MENU + CONNECT`;
- venue hub contains seven linked entities;
- links resolve through `/venues/<slug>`;
- imagery is currently sourced from `tashah.sg-host.com/wp-content/uploads/...`;
- several shell links still point to the staging WordPress host;
- hub content is statically rendered/prerendered by Next.js;
- no runtime evidence on the inspected page of a client-facing CMS resolver, stable entity IDs, one-click publish lifecycle, or exact public publish-version verification.

Observed venue slugs on the current hub:
1. `elizabeth-house`
2. `kalmia-garden-gastler-farm`
3. `adena-orchard-vine`
4. `brooklyn-grange`
5. `central-park`
6. `garner-historic-district`
7. `locust-hill-barn`

## Olga durable implementation reference

Olga has inspectable GitHub source in `oleg3479881328-code/olga-polo-weddings-web` and currently provides stronger evidence for shared platform capabilities including:
- stable entity IDs separate from slug/URL;
- published CMS source-of-truth projection;
- fail-loud validation for malformed published documents;
- editor-managed JSON/assets as protected production data;
- one-click Publish into durable versioned source;
- deployment followed by exact `publishId` live verification;
- CMS/fallback responsive parity rule;
- build-time consistency checks;
- clean venue hierarchy with Venue → Wedding direction.

## Capability comparison

| Capability | Olga | Tusia deployed evidence | Family decision |
| --- | --- | --- | --- |
| Next.js + Vercel | implemented | implemented | shared baseline |
| Brand-local shell | implemented | implemented | keep local per client |
| Preview noindex | implemented | implemented | shared rule proven |
| Venue entity pages | implemented | implemented at runtime | shared concept |
| Venue/Wedding relationship model | implemented | project direction exists, runtime proof incomplete | Olga target should be adopted |
| Stable entity ID independent of slug | implemented | not observable | adopt Olga/shared target; do not redesign |
| Published CMS source of truth | implemented | not observable | adopt `WEB-CMS-SOT-001` |
| CMS/fallback responsive parity | implemented after real incident | not observable | adopt `WEB-CMS-PARITY-001` before editor rollout |
| Client visual editor | implemented | project direction says Puck, runtime proof incomplete | use Olga pattern as donor |
| One-click Publish | implemented | not observable | adopt `WEB-PUBLISH-001` |
| Exact live publish-version verification | implemented | not observable | adopt shared target |
| Client-local brand CSS/header/footer | implemented | implemented with different brand | never move brand shell into core |
| External/staging-host dependency | limited/production-oriented | still visible in shell/assets | Tusia cleanup required before production cutover |

## What is already settled for Tusia

The following are no longer open architecture questions:

1. **Stable identity** — entity identity must be independent of public slug/URL.
2. **CMS source of truth** — once content is client-editable, hub/detail/metadata/schema projections must resolve from the same published source.
3. **Fail loudly** — malformed published content must not silently fall back to stale static content.
4. **Responsive parity** — CMS-published and fallback pages must satisfy one mobile/desktop presentation contract.
5. **Publish contract** — one client action → durable published data/assets → versioned source → deploy → exact public version verification.
6. **Preview state** — remain noindex until intentional SEO readiness.
7. **Brand boundary** — Tusia visual shell remains Tusia-specific even if engine behavior is shared.

## What cannot yet be claimed

Until original or reconstructed durable Tusia source exists, do not claim:
- file-by-file source parity with Olga;
- that Tusia already implements Olga's CMS/publish internals;
- that a shared npm package has been proven by two source-level consumers;
- that current deployed Tusia detail pages use stable IDs or a published-content resolver.

## Shared Core extraction consequence

This comparison is enough to design **interfaces/contracts** for Shared Core v0.1, but not enough to extract Olga implementation wholesale as a proven shared package.

Safe first extraction design targets:
- `EntityIdentity` contract;
- `PublishedDocument<T>` contract;
- published-source resolver interface;
- publication-state/indexing helper;
- publish adapter interface;
- validation/consistency contracts;
- responsive parity acceptance contract.

Do not extract:
- brand shell;
- client content;
- domains/routes that are client-specific;
- Olga env names/default repo/branch strings;
- Tusia staging host links/assets.

## Independent review verdict

**PASS for capability-level convergence.**

Reasoning:
- Tusia runtime independently confirms the shared Next.js/Vercel + brand-local-shell + venue-layer direction.
- Olga has stronger durable evidence for CMS/publish/entity contracts.
- Therefore Tusia should consume those reviewed family targets instead of re-solving them.
- Runtime evidence is explicitly distinguished from source evidence, so no false code-parity claim is made.

**BLOCKED for final Shared Core package extraction** until there is a durable source representation of the Tusia application (original source found, or a deliberate reconstructed implementation committed and reviewed).

## Next action

Create a durable Tusia source repository or reconstruction target, then implement the already-settled family contracts there as the canary. After independent review passes, extract/normalize the smallest client-neutral modules into Shared Core v0.1 and only then consider Olga adoption of the shared package.
