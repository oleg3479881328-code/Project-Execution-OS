# Website Creator — OWN SYSTEM EXECUTION STANDARD

## Status

- Decision: CANONICAL
- Date: 2026-09-14
- Scope: all Website Creator implementation work

## Owner Intent

Website Creator must become **our own fast reusable website-production system** that any fresh chat/agent can enter and use without reconstructing the architecture, inventing a new stack, or introducing an arbitrary SaaS dependency.

The goal is not to choose a different third-party website builder for every site.

The goal is:

`ONE REUSABLE WEBSITE CREATOR ENGINE → MANY SITE INSTANCES`

## Core Rule

A new site must consume the existing Website Creator engine and contracts.

A new chat must **not**:

- invent a new editor;
- invent a new renderer architecture;
- invent a new deployment workflow;
- create ad-hoc probe projects as the normal development method;
- silently introduce Replit, Wix, Framer, Webflow or another hosted builder as the execution foundation;
- create a client-specific replacement for a capability that belongs in Website Creator core.

If a reusable capability is missing, improve the shared engine once and then reuse it.

## Ownership Boundary

Website Creator should own the durable system state:

- Site Model / Site Instance contract;
- component registry;
- renderer contract;
- visual-editor contract and implementation binding;
- content/media model;
- theme/design-token model;
- QA gates;
- release/deploy adapters;
- project bootstrapping rules;
- agent/chats entrypoint and task routing.

Client/site instances contain only project-specific state such as:

- business facts;
- pages/content;
- media;
- theme/token values;
- chosen reusable components;
- site-specific configuration;
- deployment/domain references.

## Existing Solution First — Correct Interpretation

"Own system" does **not** mean writing every primitive from scratch.

Prefer mature reusable building blocks, especially open-source/self-hostable libraries, when they can live inside our architecture and remain replaceable.

Allowed pattern:

`OUR SYSTEM + REPLACEABLE OPEN-SOURCE/INFRASTRUCTURE COMPONENTS`

Examples of acceptable categories:

- embedded visual-editor library;
- self-hosted CMS/backend;
- PostgreSQL;
- image/crop libraries;
- Playwright;
- Docker;
- replaceable hosting/deployment adapters.

The external component must not become the definition of the site or the canonical project knowledge.

## No Silent Platform Rule

No executor/chat may introduce a hosted platform, coding sandbox, builder, CMS cloud or deployment system merely because it is convenient.

Before adding an execution dependency, it must answer:

1. Is this already solved inside Website Creator?
2. Is there a mature self-hostable/open-source building block?
3. Does it preserve our Site Model/data ownership?
4. Can it be replaced without rebuilding every site?
5. Does the dependency materially reduce total build time?

If the answer is unclear, do not silently add the dependency.

## Target Execution Architecture

```text
WEBSITE CREATOR
│
├── Site Model
├── Component Registry
├── Theme / Tokens
├── Visual Editor
├── Content / Media Backend
├── Renderer
├── QA
└── Deployment Adapters

        ↓

SITE INSTANCE
├── site data
├── pages/content
├── assets
├── theme values
├── selected components
└── deployment/domain refs
```

The engine is reusable. Site instances are data/configuration/content, not independent re-inventions of the engine.

## Speed Principle

Speed comes from reuse, not from skipping quality.

For every new site:

1. reuse existing engine;
2. reuse existing components;
3. reuse existing editor;
4. reuse existing renderer;
5. reuse existing QA;
6. add only genuinely new reusable capability;
7. promote that capability back into Website Creator when it is general.

Do not rebuild generic infrastructure inside a client task.

## Fresh-Chat Contract

A fresh chat working on a website must enter through:

1. `PROJECT.md`
2. `PROJECT_STATE.md`
3. `OWN_SYSTEM_EXECUTION_STANDARD.md`
4. `SITE_MODEL_STANDARD.md`
5. `ROUTER.md`
6. only the narrow task-specific standards required

The chat must then determine whether it is:

- creating/updating a Site Instance using existing capabilities; or
- adding a missing reusable capability to Website Creator core.

It must not invent a third path consisting of one-off client infrastructure.

## Car Service Garage Validation Rule

Car Service Garage is the first validation case for this architecture.

Use it to discover the minimum real engine needed for:

- Site Model v0.1;
- first reusable component set;
- first reusable renderer;
- first visual-editor implementation;
- save/reload/publish loop;
- first deterministic QA loop.

Do not turn Car Service Garage itself into the canonical engine. Promote only generalized, de-identified capabilities into Website Creator.

## Acceptance Gate

The first engine validation succeeds when:

1. Car Service Garage can be represented as a Site Instance;
2. the public site renders from canonical site state;
3. the visual editor edits that same state or a deterministic mapped representation;
4. text/media/section changes survive reload;
5. draft and publish are distinct where required;
6. a published change reaches the public renderer without manual frontend reconstruction;
7. Playwright can verify the main user paths;
8. a second new site can start from the same engine without rebuilding editor/renderer/deploy plumbing.

## Final Rule

**Do not solve each website. Build and reuse the Website Creator system that solves websites.**

**Do not invent one-off infrastructure. Improve the shared engine once.**