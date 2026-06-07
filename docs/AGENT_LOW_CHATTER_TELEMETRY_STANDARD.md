# Agent Low-Chatter Telemetry Standard

Updated: 2026-06-06
Status: `active`

## Purpose

Reduce token waste, context pollution, and owner distraction during agent execution.

## Core Rule

Agents may reason deeply internally, but must not publish a running stream of internal reasoning by default.

External messages should contain only the minimum information needed to keep the owner and other agents oriented.

## Allowed Outbound Status Types

Use short telemetry messages such as:

```text
STARTED:
CHECKING:
SENT:
BLOCKED:
READY FOR REVIEW:
DONE:
```

When a durable inter-agent message was sent, include the owner-visible linked receipt required by:

`docs/OWNER_VISIBLE_CHANNEL_RECEIPT_STANDARD.md`

## Default Message Contents

A routine status should contain only:

```text
STATE:
CURRENT ACTION:
LINK:                # when a durable message or artifact exists
WAITING FOR:
NEXT ACTION:
```

## Prohibited By Default

Do not publish:

- hidden chain-of-thought style narration;
- step-by-step internal deliberation;
- speculative branches that do not affect the owner;
- repeated restatement of the task;
- long terminal-output summaries when a link or short evidence note is enough;
- verbose commentary for routine tool use;
- repeated progress messages with no state change.

## When More Detail Is Allowed

Provide a fuller explanation only when:

- the owner explicitly asks for reasoning or an explanation;
- a blocker requires a decision;
- a material risk must be surfaced;
- a review report needs evidence;
- the task is complete and a concise final summary is useful.

Even then, give a concise decision summary rather than a raw reasoning dump.

## Tool Output Rule

Do not paste large command outputs or logs into chat unless they are necessary for a decision.

Prefer:

- a short summary;
- the exact failing line;
- a direct link to the durable artifact or log;
- the next action.

## Frequency Rule

Send a status only when one of these changes:

- execution started;
- active action changed materially;
- a durable message was sent;
- a blocker appeared;
- a blocker was resolved;
- a reviewable artifact became available;
- the task completed.

## Owner Visibility Example

```text
STATE: sent_waiting_for_reply
CURRENT ACTION: clarification sent to executor
LINK: https://github.com/<owner>/<repo>/issues/<id>#issuecomment-<id>
WAITING FOR: executor response
NEXT ACTION: read the reply and continue inside approved scope
```

## Final Rule

Think deeply inside. Report briefly outside. Show links and state changes, not a running monologue.