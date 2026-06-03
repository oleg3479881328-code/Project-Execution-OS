# AI Coordination Channel Standard

## Purpose

This standard defines how Oleg, ChatGPT, Codex and other explicitly connected AI agents communicate during project work without forcing every coordination message into GitHub.

Channel choice follows the active project layers defined in `docs/PROJECT_LIFECYCLE_MODEL.md`.

## Entry Block

For communication-channel selection, enter through:

`blocks/communication-channel/BLOCK.md`

The block is the single top-level route named `Канал связи`.

This document remains the detailed canonical policy and connected-agent channel registry.

Do not route to this document directly from `docs/ROUTER.md`.

## Core Rule

Use the lightest durable channel that fits the work and that is technically available to every participant in the exchange.

- `Chat` = live reasoning, decisions and instructions with Oleg.
- `Notion comments` = lightweight durable coordination, short statuses, questions, replies and links to larger artifacts, only when each participating agent can use native comments.
- `GitHub issue / pull request / review thread` = repository-bound technical execution, reviewable diffs, commit-linked decisions and implementation evidence; it is also the fallback bidirectional coordination transport when a participating agent cannot use the required Notion-comment path.

There is no universal rule that AI coordination must happen in a separate GitHub repository.

## Default Lightweight Coordination Channel

When available to every participant, use the Notion page `AI Coordination — ChatGPT` as the lightweight communication channel between Oleg, ChatGPT and connected execution/review agents.

Use native comments on that page for:

- short status messages;
- questions and responses;
- execution approvals;
- notifications that an artifact or report exists;
- links to repository-bound technical evidence.

Do not accumulate coordination messages, large reports, implementation packets or copied technical evidence in the page body merely to preserve a chat trail.

If an agent can only append page-body blocks but cannot use native comments, Notion is a readable status/reference layer for that agent, not the active bidirectional message transport.

## When To Use GitHub Instead

Use GitHub in the target repository when the message is directly tied to:

- a concrete file change;
- a commit, branch or pull request;
- code review;
- technical acceptance criteria;
- repository-specific execution evidence;
- an implementation task that should remain next to the technical source of truth.

When GitHub is selected for a ChatGPT / Codex collaboration loop, open:

`docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`

This is a nested channel-specific protocol inside `Канал связи`, not a separate top-level route.

Use the optional cross-repository hub when a durable direct agent-to-agent thread is required and the lightweight Notion-comments path is technically unavailable to one or more participants.

GitHub is an execution and review channel for GitHub-backed work, not the default home for all project communication.

## Compact Coordination State Snapshot

When a GitHub-backed project has a multi-step AI-to-AI execution or review loop, use a root-level file:

```text
AI_COORDINATION_STATE.md
```

This file is the compact operational snapshot.

The GitHub issue, pull request, or review thread remains the message transport and durable discussion trail.

The snapshot file stores only:

- the active channel;
- previous channels;
- active participants;
- the current task;
- latest reviewed repository state;
- accepted changes;
- open review items;
- one next step;
- required validation.

Do not copy the full discussion history into the file.

Update the snapshot only after a meaningful state transition:

- communication-channel migration;
- meaningful implementation commit;
- accepted review;
- new blocker;
- scope change;
- completed task.

Before processing `02` in an active GitHub-backed project, read in this order when the file exists:

```text
AI_COORDINATION_STATE.md
-> Active Channel
-> latest relevant comments
-> latest repository commit or PR state
-> Next Step
```

Use:

`docs/AI_COORDINATION_STATE_STANDARD.md`

for the canonical file format and migration rule.

## Optional Cross-Repository Hub

A dedicated GitHub coordination hub may exist as an optional transport for repository-oriented cross-project technical work when Notion is unavailable or a reviewable GitHub trail is specifically useful.

Current hub repository:

`oleg3479881328-code/AI-Coordination-Hub`

It does not replace Notion as a readable coordination layer or the target repository as the technical execution layer.

## Connected Agent Channel Registry

### DeepSeek

- `Agent`: DeepSeek
- `Confirmed role`: execution / research / review
- `System entrypoint`: `START_HERE.md`
- `Connection confirmed`: 2026-05-25
- `Notion capability`: can read and append page-body blocks; native comments API is unavailable through its current MCP server.
- `Notion policy`: status/reference layer only for DeepSeek; do not use page-body blocks as the conversation thread.
- `Active bidirectional coordination transport`: GitHub issue `oleg3479881328-code/AI-Coordination-Hub#1`
- `Channel URL`: `https://github.com/oleg3479881328-code/AI-Coordination-Hub/issues/1`
- `Acknowledgement evidence`: DeepSeek accepted the GitHub channel in issue comment `#issuecomment-4536394458`.

For DeepSeek work that is tightly bound to a specific repository, move the execution/review thread to that target repository and use the hub issue only for routing or short cross-project coordination.

## Identity Format

When a durable coordination message is sent to Notion comments or GitHub, use a short explicit identity header when it materially improves continuation:

`FROM: <sender>`
`TO: <recipient>`
`TYPE: <message type>`
`PROJECT: <project>`

Recommended additional fields when a next action matters:

`STATUS: <short state>`
`NEXT STEP: <one next action>`

Do not require this ceremony for ordinary conversational replies where the participants and context are already obvious.

## Message Size Rule

Keep coordination messages short.

If material is substantial:

- store readable project management state in Notion when appropriate;
- store compact operational coordination state in `AI_COORDINATION_STATE.md` when a GitHub-backed project has a multi-step agent loop;
- store technical artifacts and execution evidence in the relevant GitHub repository when a GitHub layer exists;
- store heavy source files in Google Drive when a Drive layer exists;
- send only the short status and reference through the coordination channel.

## Execution Split

- ChatGPT performs analysis, research, comparison, architecture reasoning and decision preparation whenever it has adequate access.
- Codex performs bounded technical execution only after the decision and allowed scope are clear.
- DeepSeek may perform bounded execution, research or review only after routing through `START_HERE.md` and receiving clear scope.
- Do not spend executor limits on open-ended investigation that ChatGPT can perform directly.
- No execution agent may claim completion without evidence of performed work and required validation.

## Validated Working Examples

### GitHub Repository Inventory Cleanup

- Chat and ChatGPT established the project model and archive decisions;
- Notion comments served as the lightweight communication channel with Codex;
- Codex performed approved batch synchronization and batch repository archiving;
- Notion retained the readable catalogue;
- GitHub retained the executed repository state.

### DeepSeek Connection Activation

- ChatGPT routed the new agent through `START_HERE.md`;
- DeepSeek reported Notion native-comments unavailability through its MCP path;
- the Notion page remained a readable status/reference layer rather than a page-body message log;
- GitHub issue `AI-Coordination-Hub#1` became the active direct coordination transport;
- DeepSeek acknowledged that channel in the issue thread.

### QuizLight Channel Migration

- a GitHub issue became too long for reliable connector reading;
- a continuation issue became the new active transport;
- `AI_COORDINATION_STATE.md` was added at repository root;
- the file preserved accepted changes, open review items, validation checks and one next step;
- future coordination resumed from the snapshot instead of relying on the full old thread.

## Bidirectional Coordination Commands

These shorthand commands control communication only:

- `01` = send the relevant current message to the other AI through the active coordination channel.
- when Oleg sends `01` to `ChatGPT`, `ChatGPT` writes to the currently targeted connected agent through that agent's registered active channel.
- when Oleg sends `01` to `Codex` or `DeepSeek`, that agent writes to `ChatGPT` through its active registered channel.
- `02` = read the latest relevant incoming message from the other AI through the active coordination channel and respond based on its actual content.
- when Oleg sends `02` to `ChatGPT`, `ChatGPT` reads `AI_COORDINATION_STATE.md` first when it exists, then reads the targeted connected agent's message through the recorded active channel.
- when Oleg sends `02` to `Codex` or `DeepSeek`, that agent reads `AI_COORDINATION_STATE.md` first when it exists, then reads `ChatGPT`'s message through the recorded active channel.
- `01` and `02` do not by themselves approve destructive or scope-changing actions.

## Final Rule

Notion comments are the lightweight coordination path when readable ongoing communication is needed and every participant can use native comments.

GitHub is used when coordination is inseparable from repository execution or review, or when the required Notion-comments transport is unavailable to a participating agent.

Use `AI_COORDINATION_STATE.md` when a GitHub-backed multi-step agent loop needs compact resumable state.

Do not create or use a heavier communication structure unless real work proves it necessary.
