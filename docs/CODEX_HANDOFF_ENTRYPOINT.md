# Codex Handoff Entrypoint

## Purpose

Use this file whenever work is handed to Codex or another executor.

## Required Reading

Read both:

- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/CODEX_RESPONSE_CHANNEL.md`

For shorthand coordination commands, also read:

- `blocks/communication-channel/BLOCK.md`

## Short Command Safety Rule

The meanings of `01` and `02` are universal for all connected AI participants.

Never interpret `01` or `02` as numbered options, first-path selection, second-path selection, or permission to expand scope.

Their meanings come only from `blocks/communication-channel/BLOCK.md`:

- `01` = write / send the relevant current message through the registered active channel;
- `02` = read / check the latest relevant incoming message through the registered active channel and continue from its actual content.

## Bare GitHub Channel Shortcut

When the owner sends a bare positive integer as the entire message during an active GitHub-backed execution workflow, interpret it as a durable-channel shortcut.

Example:

```text
33
```

means:

```text
open pull request #33 if it exists
→ otherwise open issue #33
→ read the latest relevant incoming instruction
→ continue the already-authorized in-scope work immediately
→ do not stop to summarize the task
→ do not ask for routine confirmation
→ publish the updated commit and validation evidence in that channel
```

If `AI_COORDINATION_STATE.md` contains an explicit `Owner Shortcut`, that mapping takes precedence.

Do not use this shortcut interpretation when the surrounding conversation clearly presents numbered answer choices. In that case, treat the number as the selected option.

## Mandatory Outcome

Every GitHub-based execution handoff must contain:

`Response URL: <exact GitHub issue, pull request, or review-thread URL>`

The executor must post its execution report or blocker report as a new comment in that exact GitHub thread.

## Owner-Facing Rule

Keep the full execution packet inside GitHub.

Return to the owner only the shortest useful handoff, normally the single GitHub URL.
