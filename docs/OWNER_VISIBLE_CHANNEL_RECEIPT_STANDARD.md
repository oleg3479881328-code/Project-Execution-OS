# Owner-Visible Channel Receipt Standard

Updated: 2026-06-06
Status: `active`

## Purpose

Make every inter-agent communication visible to the owner without requiring manual inspection of hidden or external channels.

## Core Rule

After sending any durable message to another agent, the sender must immediately report a short owner-visible receipt.

This applies to:

- acknowledgement;
- answer;
- request;
- clarification question;
- blocker report;
- status update;
- review instruction;
- execution report;
- artifact publication;
- draft pull-request publication;
- channel-transition notice.

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
```

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

## Example

```text
SENT: clarification request
MESSAGE TYPE: question
TO: Codex — Executor Agent
CHANNEL: GitHub issue #21
LINK: https://github.com/<owner>/<repo>/issues/21#issuecomment-<id>
CURRENT STATE: sent_blocked_waiting_for_answer
WAITING FOR: Codex clarification response
NEXT ACTION: read reply through 02 and continue inside approved scope
```

## Owner Visibility Rule

The sender must show the receipt to the owner immediately after sending the durable message.

Do not merely say `sent`.

Do not omit the link.

Do not make the owner inspect the external channel to discover whether a message was actually posted.

## Final Rule

Every durable inter-agent message must produce an owner-visible receipt with a direct link and a clear workflow state.