# Owner-Visible Channel Receipt Standard

Updated: 2026-06-08
Status: `active`

## Purpose

Make every inter-agent communication visible to the owner without requiring manual inspection of hidden or external channels.

## Core Rule

After sending any durable message to another agent, the sender must immediately report a short owner-visible receipt.

This applies to acknowledgement, answer, request, clarification question, blocker report, status update, review instruction, execution report, artifact publication, draft pull-request publication, and channel-transition notice.

## Required Receipt Fields

Every receipt must include:

```text
SENT:
MESSAGE TYPE:
TO:
CHANNEL:
LINK:
CURRENT STATE:
WAITING FOR:
NEXT ACTION:
OWNER ACTION REQUIRED:
```

## Owner Action Rule

`OWNER ACTION REQUIRED` is mandatory and must be the final line of the entire owner-facing response.

Use exactly one of these shapes:

```text
OWNER ACTION REQUIRED: none
```

or one explicit, self-contained instruction.

The instruction must still work if the owner reads only the last line and sends it to an executor who has not seen the previous chat.

For a GitHub-backed handoff, include the direct URL and the required action in the final line.

Good:

```text
OWNER ACTION REQUIRED: send any executor this exact message: `Open https://github.com/<owner>/<repo>/issues/34 and execute the handoff packet now. Post the report in that issue.`
```

Bad:

```text
OWNER ACTION REQUIRED: send `34`
```

A bare number is allowed only when the target executor is known to share the same registered GitHub-backed coordination state and has already acknowledged that shortcut mapping in the active channel.

Do not tell the owner that nothing is required when a manual trigger, relay, click, approval, or UI action is still necessary.

If the owner must click Merge, approve access, paste a token, open a link, or relay a one-line trigger, state that exact action.

## Final Placement Rule

`OWNER ACTION REQUIRED` must be the last line of the receipt and the last line of the whole response.

Do not place commentary, explanation, or a second follow-up suggestion after it.

## Link Rule

`LINK` is mandatory.

Use the direct URL of the durable message, issue comment, pull-request comment, Notion comment, artifact, or other registered reply-surface item whenever the transport provides one.

If the transport does not provide a deep link, use the narrowest available durable channel URL and state that a direct message link is unavailable.

## Current State Values

Use one of:

- `sent_waiting_for_reply`;
- `sent_execution_continues`;
- `sent_blocked_waiting_for_answer`;
- `sent_ready_for_review`;
- `sent_channel_transition_pending_ack`;
- `sent_completed`.

## Owner Visibility Rule

The sender must show the receipt to the owner immediately after sending the durable message.

Do not merely say `sent`.

Do not omit the link.

Do not make the owner inspect the external channel to discover whether a message was actually posted.

Do not hide a required owner trigger behind wording such as `nothing to do`, `wait for the executor`, or an unexplained bare number.

## Final Rule

Every durable inter-agent message must produce an owner-visible receipt with a direct link, a clear workflow state, and an explicit self-contained final-line owner action.
