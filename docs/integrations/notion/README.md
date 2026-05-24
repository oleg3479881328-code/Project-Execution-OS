# Notion Integration Standard

## Purpose

This document defines the role of `Notion` inside `Project Execution OS`.

`Notion` is not a temporary adapter beneath GitHub. It is the readable memory and management layer for projects that need durable context, status, decisions, catalogue visibility or coordination.

Layer selection is governed by `docs/PROJECT_LIFECYCLE_MODEL.md`.

## Core Position

A project uses only the layers it needs.

- `Chat` = thinking, discussion, decisions and commands during active conversation.
- `Notion` = readable memory, project catalogue, status, high-level decisions and lightweight coordination when context must persist.
- `GitHub` = versioned execution, code, technical artifacts and Codex implementation when required.
- `Google Drive` = optional storage for heavy files and source assets when required.

There is no rule that a Notion-managed project must later move into GitHub.

## When Notion Is the Durable Layer

Use Notion as the durable management layer when a project needs:

- a readable project record;
- status and next action;
- decisions and links;
- cataloguing and review;
- idea development that must not be lost;
- non-technical project management;
- lightweight coordination between Oleg, ChatGPT and Codex.

Examples include research, life projects, organization, product decisions, inventories, writing projects and project coordination.

## When GitHub Is Added

Add GitHub only when a project requires:

- code or executable artifacts;
- technical files whose version history matters;
- committed technical documentation;
- scripts, batch execution or Codex file changes;
- issues, commits or pull requests as execution evidence.

When both Notion and GitHub exist, neither automatically replaces the other:

- Notion stores readable project management state and high-level decisions;
- GitHub stores technical/versioned execution state.

A project entrypoint should state the active layers and what truth belongs to each one.

## When Google Drive Is Added

Add Google Drive only when a project requires heavy or non-versioned source materials such as images, scans, audio, video, PDFs, archives or large exports.

Notion may store the link to the relevant Drive folder.

Google Drive is an assets layer, not the project brain and not the source of operational decisions.

## Coordination Channel

Notion may be used as a lightweight human-readable coordination channel.

For the current operating model, the page `AI Coordination — ChatGPT` uses comments for short messages, status updates and links to larger artifacts.

Large technical execution packets, committed documents and repository-specific evidence should remain in the appropriate GitHub-backed layer when a repository is involved.

## Evidence Rule

Evidence must match the layer:

- a Notion update can prove that a status, decision or catalogue record was written in Notion;
- a GitHub commit or pull request can prove that a technical repository change exists;
- a Google Drive file or folder reference can prove that an asset exists in Drive;
- none of these alone proves that the entire project is correct or complete.

Do not force Notion decisions into GitHub merely to create ceremony, and do not claim GitHub execution based only on a Notion status note.

## Sync and Automation Rule

Use synchronization only when it removes real manual friction.

Validated example:

- GitHub repository inventory was batch-synchronized into Notion for readable review;
- GitHub archive actions were executed only after dry-run and explicit approval;
- Notion retained the readable inventory while GitHub recorded the repository execution state.

Do not build broad synchronization or webhook automation before repeated use proves it necessary.

## Final Rule

Notion is the readable management and coordination layer when a project needs it.

GitHub is added for versioned technical execution when a project needs it.

Google Drive is added for heavy assets when a project needs it.

No layer is mandatory merely because another layer exists.