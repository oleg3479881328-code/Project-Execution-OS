# Project Entrypoint Standard

## Purpose

This standard defines the canonical entrypoint artifact for a specific project while preserving the Project Execution OS rule that AI interfaces enter the overall system through one global `START_HERE.md`.

A project entrypoint is a durable project node reached through routing. It is not a competing global door.

## Core Rule

Every meaningful project should have exactly one current canonical project entrypoint in its durable workspace.

Any AI/client interface should enter Project Execution OS through the global `START_HERE.md`, follow recursive routing, and only then reach the relevant project's canonical entrypoint.

```text
global START_HERE.md
→ router
→ router / registry / index ... as needed
→ canonical project entrypoint
→ project-local routing ... as needed
→ minimum current evidence
```

Routing depth is not fixed.

## Canonical Project Forms

Use the same project-entry contract in environment-specific durable forms:

- `GitHub / repository projects` -> `PROJECT.md`
- `Notion / workspace-first projects` -> `Project Entrypoint` or `START HERE` page
- another durable workspace -> one clearly identified canonical project entrypoint appropriate to that system

The medium may differ. The contract should stay the same.

## ChatGPT Projects

ChatGPT Project is an interface, not a durable project-entrypoint layer.

If stable user/system instructions already guarantee entry through global Project Execution OS `START_HERE.md`, no ChatGPT Project attachment is required.

When an attached bootstrap file is useful or required, use the generic optional `START_HERE.md` pointer defined by `docs/CHATGPT_PROJECT_START_HERE_TEMPLATE.md`. It points to the global Project Execution OS `START_HERE.md`, not directly to a specific project.

Do not create new project-specific ChatGPT attachment snapshots or parallel project-specific START_HERE contracts merely because work happens inside separate ChatGPT Projects.

Project identity is resolved through the live router tree and durable project registry/index nodes.

### Legacy ChatGPT Attachment Migration

Existing ChatGPT Projects may already contain project-specific START_HERE/pointer files created under the previous contract.

Migration is zero-touch by default:

- do not require the owner to open every ChatGPT Project;
- do not require re-uploading or replacing old attachments merely to adopt the new architecture;
- global `START_HERE.md` has precedence when stable client instructions require it;
- the live router path has precedence over a legacy interface pointer;
- the selected project's canonical durable entrypoint has precedence over a legacy interface pointer;
- current durable evidence has precedence over stale attachment content.

A legacy pointer may remain physically attached. Treat it as a non-authoritative compatibility artifact and ignore its direct project routing until the global router tree has selected that project.

Replace or remove a legacy attachment only during convenient maintenance or when it demonstrably causes ambiguity. Its presence alone is not a blocker.

## Recursive Navigation Contract

A navigation node may point to another router, project/domain registry, collection index, project entrypoint, specialized navigation node, or canonical content. Any navigation node may route onward again.

There is no artificial maximum routing depth. Use the depth required by the real information architecture while keeping each node narrow.

Navigation nodes should not duplicate detailed state or knowledge stored behind them.

## Required Questions The Project Entrypoint Must Answer

After reaching the canonical project entrypoint, a new human or AI should be able to answer:

1. What is this project?
2. Why does it exist?
3. What kind of project is it?
4. Where is the source of truth?
5. What has already been done?
6. What is the current state?
7. What is the next practical step?
8. Which decisions or constraints must not be ignored?
9. Where should I read next if I need deeper context?

If the entrypoint does not answer these clearly, it is incomplete.

## Required Sections

Every canonical live project entrypoint should include, in compact form: Project; Purpose; Source Of Truth; Source Trail; Current Status; Done So Far; Current Focus; Next Practical Step; Key Decisions And Constraints; Read Next.

Follow `docs/SOURCE_TRACEABILITY_STANDARD.md` for recoverable underlying sources and evidence. Unknown fields are allowed when truthful; invented fields are not.

## What The Project Entrypoint Must Not Become

The project entrypoint must not become the global system router, full project history, full rules document, transcript dump, research archive, or hidden second state database.

History belongs in logs/workflow runs/databases/supporting pages. Rules belong in standards/project rules. The project entrypoint remains the shortest reliable project-level front door after routing selects that project.

## Repository Legacy Migration Rule

For repository projects:

- if `PROJECT.md` exists, use it as the canonical project entrypoint;
- if `PROJECT.md` is absent but `PROJECT_ENTRYPOINT.md` exists, treat it as a legacy name;
- migrate it to `PROJECT.md` at the nearest safe opportunity;
- update links and references;
- do not keep both active at the same time.

This repository-file migration is separate from ChatGPT attachment migration: old repository entrypoint names should be cleaned up when safe, while old ChatGPT attachments may remain because they are non-authoritative interface artifacts.

## Maintenance Rule

Update the canonical project entrypoint whenever its source of truth, source trail, current mode, current focus, next practical step, or a major decision changes what a new participant must know first.

Do not update a generic ChatGPT attachment for ordinary project changes.

## Final Rule

One Project Execution OS has one global AI door: `START_HERE.md`.

One meaningful project has one canonical durable project entrypoint.

Stable global client instructions make per-project ChatGPT pointers unnecessary.

Recursive routers connect the global door to the correct project and may use as many navigation levels as the information architecture requires.