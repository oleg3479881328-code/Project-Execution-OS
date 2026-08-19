# Shared Project Capability Matrix

## Purpose

This matrix tracks which near-identical projects already implement each shared platform capability and which project is currently ahead.

It exists to prevent separate chats from treating each project as an isolated universe.

A project can be ahead in one capability and behind in another. The shared platform must therefore synchronize by capability, not by declaring one whole project the permanent master copy.

## Status Values

Implementation status:
- `IMPLEMENTED` — capability exists in the project with real evidence.
- `PARTIAL` — some pieces exist but the shared invariant is not fully satisfied.
- `PLANNED` — accepted direction but not yet implemented.
- `UNKNOWN` — durable evidence not yet available.
- `N/A` — capability intentionally does not apply.

Adoption status against the current family target:
- `ADOPTED` — project satisfies the current reviewed family target.
- `PENDING` — family target is known and should be consumed when this capability is touched.
- `BLOCKED` — adoption needs a prerequisite/evidence source.
- `EXCEPTION` — intentional project-specific deviation is documented.

## Current Matrix — 2026-08-19

| Capability | Shared ID | Current family target | Olga Polo | Tusia / Tasha | Adoption note |
| --- | --- | --- | --- | --- | --- |
| Shared Next.js/Vercel application pattern | — | Next.js App Router + TypeScript + Vercel, independent client deploy lifecycle | IMPLEMENTED / ADOPTED | IMPLEMENTED / ADOPTED | common platform baseline |
| Brand-preserving rebuild | WEB-BRAND-SHELL-001 | shared engine, client-local brand shell | IMPLEMENTED / ADOPTED | IMPLEMENTED / ADOPTED | do not copy brand CSS/assets across clients |
| Preview/new-layer noindex state | WEB-SEO-STATE-001 | preview/new layer `noindex,nofollow` until intentional SEO readiness | IMPLEMENTED / ADOPTED | IMPLEMENTED / ADOPTED | shared knowledge proven |
| Venue/Wedding entity architecture | WEB-ENTITY-ID-001 | stable entity identity separated from public slug/URL; Venue ↔ Wedding relationships | IMPLEMENTED / ADOPTED | PARTIAL / PENDING | Olga has durable stable-ID implementation; Tusia should converge when entity code is touched |
| Client visual editor | — | branded Puck editor with constrained client-facing blocks | IMPLEMENTED / ADOPTED | PLANNED/PARTIAL / PENDING | Tusia migration explicitly adopts Olga pattern |
| Published CMS source of truth across surfaces | WEB-CMS-SOT-001 | published client-edited data resolves consistently across hub/detail/SEO projections; invalid published doc fails loudly | IMPLEMENTED / ADOPTED | UNKNOWN / PENDING | **do not rediscover in Tusia**; inherit family rule immediately |
| CMS/fallback responsive parity | WEB-CMS-PARITY-001 | published and fallback paths satisfy one responsive presentation contract | IMPLEMENTED / ADOPTED | UNKNOWN / PENDING | Olga incident produced proven family rule; Tusia must not repeat the bug |
| One-click centralized Publish | WEB-PUBLISH-001 | one client action → durable published data/assets → versioned source → deploy → public-version verification | IMPLEMENTED / ADOPTED | PLANNED/PARTIAL / PENDING | Olga is implementation donor; generic adapter still not extracted |
| Publish → live-version verification | WEB-PUBLISH-001 | success only after exact published version is visible publicly | IMPLEMENTED / ADOPTED | UNKNOWN / PENDING | acceptance contract should be inherited |
| Stable entity identity independent of URL | WEB-ENTITY-ID-001 | entity ID remains stable across route/slug migrations | IMPLEMENTED / ADOPTED | PARTIAL / PENDING | code-level confirmation still needed in Tusia |
| Viewport-independent donor evidence | WEB-DESIGN-EVIDENCE-001 | desktop/tablet/mobile are independent donor states; suspicious geometry blocked/reconciled | IMPLEMENTED / ADOPTED | IMPLEMENTED / ADOPTED | extractor work confirms both |
| Independent implementation review | global OS | separate review pass against fresh evidence before handoff | IMPLEMENTED / ADOPTED | IMPLEMENTED / ADOPTED | enforced by Project Execution OS/project manuals |

## Current Convergence Queue

### Tusia should consume from Olga/shared layer
1. `WEB-CMS-SOT-001` — published CMS source-of-truth contract.
2. `WEB-CMS-PARITY-001` — CMS/fallback responsive parity.
3. `WEB-PUBLISH-001` — one-click Publish + exact public-version verification.
4. `WEB-ENTITY-ID-001` — stable identity independent of route/slug.

These are not open architecture questions in Tusia. They are current family targets. If Tusia work reaches one of these areas, the executor must adapt the family target rather than restart solution design.

### Shared layer should consume from Tusia when it advances
Tusia is already strong evidence for:
- brand-shell separation;
- multi-viewport donor capture;
- brand-preserving rebuild against a different photographer visual system.

Any stronger generic design-capture, mobile-shell, or editor usability rule discovered there should be promoted upward and become available to Olga in the same way.

## Synchronization Rule

For every substantive platform change in a near-identical project:

1. identify the capability affected;
2. check this matrix and the shared registry before inventing anything;
3. if another project already has a reviewed stronger implementation, reuse/adapt that solution;
4. if the current project discovers a stronger generic solution, promote it upward under `SHARED_SOLUTION_PROMOTION_STANDARD`;
5. update this matrix after adoption or after a capability meaningfully changes;
6. do not require both projects to move simultaneously — synchronize by reviewed capability when each project reaches that point.

## Important Consequence

There is no single permanent `master client project`.

Instead there is a shared platform whose capabilities may temporarily be led by different projects:

```text
CMS capability       → Olga may lead today
Design capture       → Tusia may expose the next better rule tomorrow
SEO capability       → another client may lead later

all reviewed improvements
        ↓
Shared Platform Registry
        ↓
all sibling projects can consume them
```

This is the mechanism that prevents chat-to-chat drift while allowing projects to progress at different speeds.

## Chat Entry Requirement

When a new chat works on Olga, Tusia, or another project in this platform family, it should not rely only on that project's local migration snapshot.

Before proposing platform architecture or solving a repeated platform problem, the executor must consult:

1. the current project entrypoint/state;
2. `docs/SHARED_WEB_PLATFORM_REGISTRY.md`;
3. this capability matrix;
4. `docs/PLATFORM_FAMILY_SYNC_STANDARD.md`;
5. relevant global standards in Project Execution OS.

Project-specific visual/content work remains local and does not require reading unrelated client data.

## Current Evidence Limitation

Tusia has a real READY Vercel project and detailed Notion migration state, but a separate durable GitHub repository was not found through the connected GitHub source. Therefore Tusia code-level statuses remain conservative where implementation cannot be independently inspected.

This limitation **does not reopen already-proven family architecture decisions**. It only blocks code-level extraction/comparison where source inspection is actually required.

## Related Nodes

- `docs/PLATFORM_FAMILY_SYNC_STANDARD.md`
- `docs/SHARED_SOLUTION_PROMOTION_STANDARD.md`
- `docs/SHARED_WEB_PLATFORM_REGISTRY.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/PROJECT_MEMORY_STANDARD.md`
