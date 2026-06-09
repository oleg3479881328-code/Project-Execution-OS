# Notion Agent Rules

## Purpose

Define how authorized agents may read and write Notion project spaces connected to Project Execution OS.

## Entry Rule

An agent must not begin from a random Notion page.

The valid entry sequence is:

1. Project Execution OS `START_HERE.md`.
2. `docs/ROUTER.md`.
3. Relevant project entrypoint or system block.
4. Matching Notion project page by `PROJECT_ID`.

## Read Rule

Read the smallest relevant Notion area:

- task work -> Tasks + linked project Current State;
- research -> Research + Links + relevant project Current State;
- decision work -> Decisions + evidence links;
- asset work -> Assets + linked task;
- handoff -> Current State + Tasks + Logs + attached durable-layer entrypoints.

Do not load the whole workspace by default.

## Write Rule

Write updates into the narrowest correct place:

- new work item -> Tasks;
- external source finding -> Research or Links;
- accepted architectural or product choice -> Decisions;
- file, reference, prompt, or media -> Assets;
- execution trace -> Logs;
- reusable insight -> Knowledge Extracted.

## Conflict Rule

If two durable layers disagree:

1. Do not silently overwrite either side.
2. Use the project's `Truth Map` to identify which layer owns that fact.
3. Create a reconciliation task.
4. Record the conflict in Logs.
5. Update the non-owning mirror only after the owning layer is confirmed.

## Agent Note Rule

Agents may add short operational notes, but must not use Notion as a hidden scratchpad for rules that belong in Project Execution OS or in a project repository.

## Secret Rule

Never store API keys, OAuth tokens, passwords, personal documents, or confidential case details in the reusable Notion layer.

Use credential pointers only, such as `stored in password manager`, when needed.

## MCP and API Rule

When using Notion MCP or API access:

- use the least powerful connection that can complete the work;
- prefer project-scoped access over workspace-wide access when supported;
- respect pagination and partial reads;
- validate exact available tools in the target agent environment;
- do not assume hosted MCP, local MCP, ChatGPT connector, Codex connector, and raw API expose identical capabilities.

## Sync Rule

Do not design uncontrolled two-way sync.

Allowed initial sync modes:

- GitHub -> Notion mirror for visibility;
- Notion -> GitHub issue creation for approved task intake;
- manual reconciliation for decisions and truth-map state;
- one-way export of reusable knowledge candidates for review.

Any two-way sync must define:

- owner layer per field;
- conflict behavior;
- rollback behavior;
- evidence trail;
- retry and duplicate handling.

## Final Rule

An agent using Notion must make the project clearer for the next agent, not create a second undocumented operating system.