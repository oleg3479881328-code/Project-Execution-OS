# Shared Project Capability Matrix

## Purpose

This matrix tracks which near-identical projects already implement each shared platform capability and which project is currently ahead.

It exists to prevent separate chats from treating each project as an isolated universe.

A project can be ahead in one capability and behind in another. The shared platform must therefore synchronize by capability, not by declaring one whole project the permanent master copy.

## Status Values

- `IMPLEMENTED` — capability exists in the project with real evidence.
- `PARTIAL` — some pieces exist but the shared invariant is not fully satisfied.
- `PLANNED` — accepted direction but not yet implemented.
- `UNKNOWN` — durable evidence not yet available.
- `N/A` — capability intentionally does not apply.

## Current Matrix — 2026-08-19

| Capability | Shared ID | Olga Polo | Tusia / Tasha | Current lead / note |
| --- | --- | --- | --- | --- |
| Shared Next.js/Vercel application pattern | — | IMPLEMENTED | IMPLEMENTED | both use same platform direction |
| Brand-preserving rebuild | WEB-BRAND-SHELL-001 | IMPLEMENTED | IMPLEMENTED | project-specific brand layer remains local |
| Preview/new-layer noindex state | WEB-SEO-STATE-001 | IMPLEMENTED | IMPLEMENTED | shared knowledge proven |
| Venue/Wedding entity architecture | WEB-ENTITY-ID-001 | IMPLEMENTED | PARTIAL | Olga has durable stable-ID implementation; Tusia architecture confirmed but code source not yet durable/located |
| Client visual editor | — | IMPLEMENTED | PLANNED/PARTIAL | Tusia migration explicitly adopts Olga Puck pattern; code-level state needs durable verification |
| Published CMS source of truth across surfaces | WEB-CMS-SOT-001 | IMPLEMENTED | UNKNOWN | Olga is current lead; Tusia must consume the promoted invariant rather than rediscover it |
| CMS/fallback responsive parity | WEB-CMS-PARITY-001 | IMPLEMENTED | UNKNOWN | Olga incident produced shared rule; Tusia should inherit rule immediately for new work |
| One-click centralized Publish | WEB-PUBLISH-001 | IMPLEMENTED | PLANNED/PARTIAL | Olga current implementation donor; generic adapter not extracted yet |
| Publish → live-version verification | WEB-PUBLISH-001 | IMPLEMENTED | UNKNOWN | shared acceptance contract candidate |
| Stable entity identity independent of URL | WEB-ENTITY-ID-001 | IMPLEMENTED | PARTIAL | Tusia needs code-level confirmation |
| Viewport-independent donor evidence | WEB-DESIGN-EVIDENCE-001 | IMPLEMENTED | IMPLEMENTED | extractor work confirms both |
| Independent implementation review | global OS | IMPLEMENTED process | IMPLEMENTED process | enforced by Project Execution OS / project manuals |

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
4. relevant global standards in Project Execution OS.

Project-specific visual/content work remains local and does not require reading unrelated client data.

## Current Evidence Limitation

Tusia has a real READY Vercel project and detailed Notion migration state, but a separate durable GitHub repository was not found through the connected GitHub source. Therefore Tusia code-level statuses remain conservative where implementation cannot be independently inspected.

## Related Nodes

- `docs/SHARED_SOLUTION_PROMOTION_STANDARD.md`
- `docs/SHARED_WEB_PLATFORM_REGISTRY.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/PROJECT_MEMORY_STANDARD.md`
