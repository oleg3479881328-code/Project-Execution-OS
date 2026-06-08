# Owner-Visible Channel Receipt Standard

Updated: 2026-06-08
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
OWNER ACTION REQUIRED:
NEXT ACTION:
```

## Owner Action Rule

`OWNER ACTION REQUIRED` is mandatory.

Use exactly one of these shapes:

```text
OWNER ACTION REQUIRED: none
```

or:

```text
OWNER ACTION REQUIRED: send `02` to the executor now
```

or another equally explicit single action.

Do not tell the owner that nothing is required when a manual trigger, relay, click, approval, or UI action is still necessary.

If the workflow cannot continue until the owner sends `02`, say that directly.

If the owner must click Merge, approve access, paste a token, open a link, or relay a one-line trigger, state that exact action.

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
SENT: review correction request
MESSAGE TYPE: review instruction
TO: Codex — Executor Agent
CHANNEL: GitHub pull request #30
LINK: https://github.com/<owner>/<repo>/pull/30
CURRENT STATE: sent_execution_continues
WAITING FOR: Codex correction commit and validation report
OWNER ACTION REQUIRED: send `02` to the executor now
NEXT ACTION: Codex reads PR #30 and continues inside approved scope
```

## Owner Visibility Rule

The sender must show the receipt to the owner immediately after sending the durable message.

Do not merely say `sent`.

Do not omit the link.

Do not make the owner inspect the external channel to discover whether a message was actually posted.

Do not hide a required owner trigger behind wording such as `nothing to do` or `wait for the executor`.

## Final Rule

Every durable inter-agent message must produce an owner-visible receipt with a direct link, a clear workflow state, and an explicit statement of whether the owner must do anything next.
