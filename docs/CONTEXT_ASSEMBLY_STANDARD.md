# Context Assembly Standard v3

## Purpose

This standard defines how a human or AI participant assembles the minimum sufficient, trustworthy context needed for a specific action through `Project Execution OS`.

The architecture is model- and interface-agnostic: one stable global entrypoint, recursively composable navigation, durable external sources of truth, and smallest-sufficient context loading.

## Core Rule

```text
Enter through the one global stable door.
Follow the live router tree as deeply as necessary.
Load only what the route and active task require.
Do not load the whole system or whole project by default.
```

## Universal Entry Sequence

```text
0. Stable client/system instruction, if needed
1. global START_HERE.md
2. first live router: docs/ROUTER.md
3. zero or more additional routers / registries / indexes
4. relevant system standard/block and/or canonical project entrypoint
5. zero or more project/domain/collection routers or indexes
6. minimum task-specific durable evidence
7. relevant reusable knowledge/skills only when triggered
8. current user instruction, error, log or execution input
```

The number of routing layers is intentionally unbounded.

A route can be one hop or one hundred hops if the real information architecture requires it. Depth itself is not a problem; unnecessary context expansion is.

## Recursive Router Rule

A router is a navigation pattern, not one privileged file.

A navigation node may be a router, registry, index, directory map, project catalogue, wedding catalogue, vendor catalogue, capability catalogue or another bounded map.

It may point to another navigation node or to canonical content.

Each navigation level should expose only enough information to choose the next relevant path. It should not duplicate all content behind that path.

Example:

```text
START_HERE
→ global ROUTER
→ Projects registry
→ Olga Polo project
→ Weddings router
→ specific wedding
→ Vendors router
→ specific vendor dossier
→ evidence required for the active task
```

This example is illustrative, not a required fixed hierarchy.

## Client / Interface Rule

ChatGPT Projects, Codex, Claude, DeepSeek, local models and future agents are execution interfaces.

They may contain a minimal stable bootstrap instruction or pointer, but they should not become canonical project-memory stores merely because work happens there.

When a client can reach the global Project Execution OS entrypoint, its bootstrap should direct it to global `START_HERE.md`.

Do not create a separate navigation architecture for each AI client.

## Project Context Rule

When routing reaches a specific project, read that project's canonical durable entrypoint first.

The intended shape is:

```text
global START_HERE.md
→ router tree
→ PROJECT.md / durable project entrypoint
→ project index/router if useful
→ minimum additional files needed for the task
```

Do not replace project-entrypoint use by indiscriminately reading an entire repository, complete Drive tree, full chat history or log archive.

## Context Selection Rule

Before loading an additional artifact, answer:

1. Does the active route require it?
2. Does the current navigation/project entrypoint point to it?
3. Is it needed for correctness, evidence or execution?
4. Does a reviewed reusable solution apply?

If none is true, do not load it.

## Anti-Bloat Rule

Do not create context packages made of entire repositories, complete historical chats, every standard, all project records, every knowledge item, or stale files merely because they exist.

A deep router tree is compatible with a small context window because each step can discard irrelevant sibling branches.

## Project Index Rule

Before mass scanning a project or collection, check whether a useful index/router already exists.

If a collection has grown enough that navigation is becoming expensive or ambiguous, create the smallest useful router/index at that level.

Examples may include projects, weddings, vendors, venues, knowledge domains or capabilities.

Do not create empty hierarchy for hypothetical future scale.

## Reusable Knowledge Rule

Use central reusable knowledge only when the current task may benefit from a reviewed cross-project solution or pattern.

Do not load complete knowledge, skills, agent or block trees into routine work.

## Executor Context Rule

When execution is already decided, provide the executor with a bounded payload: objective, allowed scope, forbidden changes, relevant evidence, acceptance criteria and validation requirements.

Do not make an executor rediscover an open-ended router tree unless discovery itself is the task.

## API / Cache-Aware Rule

For API-based orchestration, keep stable content toward the front where practical:

```text
stable client instruction
→ global START_HERE
→ selected router path
→ stable project orientation
→ selected standards/knowledge
→ current evidence
→ live instruction/error/log
```

Caching is an optimization, not memory. Preserve runtime usage/cost logging where provider data is available.

## Review Rule

Review context assembly for:

- missing required context;
- unnecessary loaded context;
- stale/unreviewed guidance treated as active truth;
- router nodes that have accumulated content instead of navigation;
- duplicate interface-specific entry architectures;
- hard-coded routing-depth assumptions;
- project/collection scale that now deserves a smaller child router/index.

## Related Nodes

- `START_HERE.md`
- `docs/ROUTER.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/CHATGPT_PROJECT_START_HERE_TEMPLATE.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`

## Final Rule

The system must not depend on an AI reading everything or knowing in advance which project it is inside.

It must enable any compatible AI to know one stable global door, recursively navigate to the correct canonical node, and load the smallest trustworthy context sufficient for the active action.