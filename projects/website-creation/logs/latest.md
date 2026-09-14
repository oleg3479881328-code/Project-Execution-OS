# Website Creator — latest

Date: 2026-09-14

## Event

Owner clarified the execution objective after the speed review and Car Service Garage experiment:

**Website Creator must be our own fast reusable website-production system that any fresh chat/agent can enter and use without reconstructing the architecture, inventing one-off infrastructure, or silently introducing an arbitrary hosted platform.**

Canonical new standard:
`../OWN_SYSTEM_EXECUTION_STANDARD.md`

## Main Decision

Target pattern:

`ONE REUSABLE WEBSITE CREATOR ENGINE → MANY SITE INSTANCES`

Website Creator remains the global knowledge/control plane, but reusable execution is now explicitly part of the intended system boundary.

A new site should reuse the shared Site Model, component registry, editor, renderer, content/media model, QA and deployment adapters.

## Existing Solution First — Clarified

"Own system" does not mean building every primitive from scratch.

Prefer mature open-source/self-hostable/replaceable building blocks when they:

- reduce total build time;
- preserve canonical Site Model/data ownership;
- fit behind Website Creator contracts;
- can be replaced without rebuilding every Site Instance.

Custom-build only the verified missing reusable capability.

## No Silent Platform Rule

A fresh chat/executor must not silently introduce Replit, Wix, Framer, Webflow, a hosted CMS, a coding sandbox, a new deployment architecture or another external foundation merely because it is convenient.

External products may remain donors, benchmarks, optional adapters or explicitly accepted infrastructure. They are not allowed to redefine Website Creator architecture without an explicit decision.

The Replit prototype path introduced in chat is not canonical and must not be treated as Website Creator architecture.

## Fresh-Chat Contract

Every fresh chat working on a site must start through:

`PROJECT.md → PROJECT_STATE.md → OWN_SYSTEM_EXECUTION_STANDARD.md → SITE_MODEL_STANDARD.md → ROUTER.md → narrow task standards`

Then classify the work as:

1. `SITE INSTANCE WORK` — use existing shared engine capabilities; or
2. `WEBSITE CREATOR CORE WORK` — add one genuinely missing reusable capability.

No normal third path exists for one-off client infrastructure.

## Car Service Garage Role

Car Service Garage is the first validation case for the shared engine.

Use it to derive/prove:

- Site Model v0.1;
- first reusable component set;
- first shared renderer;
- first shared editor implementation;
- save/reload/publish loop;
- deterministic QA loop.

Do not make Car Service Garage itself the canonical engine and do not create a new client-specific editor/deploy stack around it.

## Current P0

1. Validate Car Service Garage as a Site Instance of the shared engine.
2. Derive real Site Model v0.1.
3. Establish first reusable components.
4. Bind one reusable editor to canonical site state.
5. Establish one reusable renderer.
6. Prove save → reload → publish → public render without manual frontend reconstruction.
7. Verify that the next site can start from the same engine instead of rebuilding generic plumbing.

## Core Principle

**Do not solve each website separately. Build and reuse the Website Creator system that solves websites.**