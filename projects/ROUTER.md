# Projects Router

## Purpose

This is the specialized project registry/router for projects stored inside `Project Execution OS`.

It is a navigation node, not project state.

Enter here only after the global `START_HERE.md` and `docs/ROUTER.md` have selected project navigation, unless a narrower direct route already identifies the exact project entrypoint.

## Routing Rule

Choose the narrowest matching project and open its canonical `PROJECT.md`.

Do not read every project by default.

A project may route onward through its own routers, registries, indexes, collections, entities, or task-specific evidence. There is no fixed maximum depth.

## Registered Projects

- Green Apple / `20260516-green-apple` -> `20260516-green-apple/PROJECT.md`
- AI Hands -> `ai-hands/PROJECT.md`
- ChatGPT Workspace Manager -> `chatgpt-workspace-manager/PROJECT.md`
- Codex -> `codex/PROJECT.md`
- Design Picker -> `design-picker/PROJECT.md`
- Personal Secretary OS / personal secretary / secretary / assistant mode -> `personal-secretary-os/PROJECT.md`
- Reels Factory MVP -> `reels-factory-mvp/PROJECT.md`
- SOFT / software umbrella -> `soft/PROJECT.md`
- SOLANA / Crypto-Web3 umbrella -> `https://github.com/oleg3479881328-code/SOLANA/blob/main/PROJECT.md`
- TikTok Research Sorter -> `tiktok-research-sorter/PROJECT.md`
- Tusia / Tasha Hurley Weddings -> `tusia-tasha-hurley/PROJECT.md`
- Циолковский / Есенин / Лермонтов archival research -> `tsiolkovsky-yesenin-lermontov-research/PROJECT.md`
- Visitor Analytics Control Plane -> `visitor-analytics-control-plane/PROJECT.md`

## External Project Rule

A project does not need to live physically under this directory to participate in the routing tree.

When an externally stored project needs central discovery, add a short registry route to its canonical durable entrypoint or to a smaller dedicated router. Do not copy the external project's changing state into this registry.

## Child Router Rule

When one project or project collection grows large enough that direct navigation becomes noisy, create the smallest useful child router/index inside that scope.

Examples may include:

```text
project
→ weddings router
→ wedding
→ vendors router
→ vendor dossier
```

or any other hierarchy justified by the real information architecture.

Do not create empty child routers merely in anticipation of possible future scale.

## Boundary

This file stores navigation only.

Do not place detailed project status, history, implementation plans, credentials, logs, task payloads, or reusable knowledge content here.

Each project's `PROJECT.md` and linked durable artifacts remain authoritative for that project's state.

## Maintenance Rule

Add, rename, move, or retire a route when the corresponding canonical project entrypoint changes.

Verify the target exists before registering it.

## Final Rule

`START_HERE.md` is the global door.

`docs/ROUTER.md` is the global live map.

This file is the projects-level map.

Select one project, continue recursively as needed, and load only the minimum context required for the active work.
