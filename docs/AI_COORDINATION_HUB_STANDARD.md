# AI Coordination Channel Standard

## Purpose

This standard defines how Oleg, ChatGPT and Codex communicate during project work without forcing every coordination message into GitHub.

Channel choice follows the active project layers defined in `docs/PROJECT_LIFECYCLE_MODEL.md`.

## Core Rule

Use the lightest durable channel that fits the work.

- `Chat` = live reasoning, decisions and instructions with Oleg.
- `Notion comments` = lightweight durable coordination, short statuses, questions, replies and links to larger artifacts.
- `GitHub issue / pull request / review thread` = repository-bound technical execution, reviewable diffs, commit-linked decisions and implementation evidence.

There is no universal rule that AI coordination must happen in a separate GitHub repository.

## Default Lightweight Coordination Channel

When available, use the Notion page `AI Coordination — ChatGPT` as the lightweight communication channel between Oleg, ChatGPT and Codex.

Use comments on that page for:

- short status messages;
- questions and responses;
- execution approvals;
- notifications that an artifact or report exists;
- links to repository-bound technical evidence.

Do not accumulate large reports, implementation packets or copied technical evidence in the page body merely to preserve a chat trail.

## When To Use GitHub Instead

Use GitHub in the target repository when the message is directly tied to:

- a concrete file change;
- a commit, branch or pull request;
- code review;
- technical acceptance criteria;
- repository-specific execution evidence;
- an implementation task that should remain next to the technical source of truth.

GitHub is an execution and review channel for GitHub-backed work, not the default home for all project communication.

## Optional Cross-Repository Hub

A dedicated GitHub coordination hub may exist as an optional transport for repository-oriented cross-project technical work when Notion is unavailable or a reviewable GitHub trail is specifically useful.

It is not mandatory and does not replace Notion as a readable coordination layer or the target repository as the technical execution layer.

## Identity Format

When a durable coordination message is sent to Notion comments or GitHub, use a short explicit identity header when it materially improves continuation:

`FROM: <sender>`
`TO: <recipient>`
`TYPE: <message type>`
`PROJECT: <project>`

Do not require this ceremony for ordinary conversational replies where the participants and context are already obvious.

## Message Size Rule

Keep coordination messages short.

If material is substantial:

- store readable project management state in Notion when appropriate;
- store technical artifacts and execution evidence in the relevant GitHub repository when a GitHub layer exists;
- store heavy source files in Google Drive when a Drive layer exists;
- send only the short status and reference through the coordination channel.

## Execution Split

- ChatGPT performs analysis, research, comparison, architecture reasoning and decision preparation whenever it has adequate access.
- Codex performs bounded technical execution only after the decision and allowed scope are clear.
- Do not spend Codex limits on open-ended investigation that ChatGPT can perform directly.

## Validated Working Example

During GitHub Repository Inventory Cleanup:

- Chat and ChatGPT established the project model and archive decisions;
- Notion comments served as the lightweight communication channel with Codex;
- Codex performed approved batch synchronization and batch repository archiving;
- Notion retained the readable catalogue;
- GitHub retained the executed repository state.

This is the current proven coordination pattern.

## Final Rule

Notion comments are the lightweight coordination path when readable ongoing communication is needed.

GitHub is used when coordination is inseparable from repository execution or review.

Do not create or use a heavier communication structure unless real work proves it necessary.

## Bidirectional Coordination Commands

These shorthand commands control communication only:

- `01` = send the relevant current message to the other AI through the active coordination channel
- when Oleg sends `01` to `ChatGPT`, `ChatGPT` writes to `Codex`
- when Oleg sends `01` to `Codex`, `Codex` writes to `ChatGPT`
- `02` = read the latest relevant incoming message from the other AI through the active coordination channel and respond based on its actual content
- when Oleg sends `02` to `ChatGPT`, `ChatGPT` reads `Codex`'s message
- when Oleg sends `02` to `Codex`, `Codex` reads `ChatGPT`'s message
- `01` and `02` do not by themselves approve destructive or scope-changing actions
