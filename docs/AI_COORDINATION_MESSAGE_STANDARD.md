# AI Coordination Message Standard

## Purpose

This standard defines the durable AI-to-AI message format used when Project Execution OS routes coordination through GitHub issues, pull requests, review threads, or Notion comments.

Use it to keep sender, recipient, scope, and next action explicit without inventing a separate orchestration layer.

## Core Rule

For durable coordination messages, use the signed polite message format - подписанный вежливый формат сообщения:

1. explicit sender and recipient header;
2. clear message type;
3. project name;
4. concise operational body;
5. short polite signature.

This applies to ChatGPT, Codex, Claude, Gemini, DeepSeek, reviewers, and other clearly named agents.

## Transfer Block Rule

When a durable AI-to-AI message is generated for manual transfer, emit the transferable message as one single contiguous copyable block.

Do not fragment the transferable content across multiple blocks.

Avoid explanatory prose outside that block unless it is explicitly requested.

This applies to handoffs, execution reports, review requests, revision requests, clarifications, blockers, and status notes.

## Minimum Header

```text
FROM: <sender>
TO: <recipient>
SUBJECT: <short subject>
TYPE: <message type>
PROJECT: <project>
```

Allowed `TYPE` examples:

- `Implementation Handoff`
- `Execution Report`
- `Review Request`
- `Revision Request`
- `Clarification`
- `Status`
- `Blocker`

## Closing

Recommended closing:

```text
Thank you,
<sender>
```

The closing identifies who signed the durable message.

## Template: ChatGPT To Codex Handoff

```text
FROM: ChatGPT
TO: Codex
SUBJECT: <task subject>
TYPE: Implementation Handoff
PROJECT: <project>

IMPLEMENTATION HANDOFF PACKET

Packet Type:
Objective:
Source Decision / Design:
Allowed Scope:
Out of Scope:
Repository Context:
Files Allowed To Change:
Forbidden Changes:
Existing Solution Search Required:
Implementation Instructions:
Acceptance Criteria:
Validation Commands / Checks:
Rollback Notes:
Execution Report Contract:
Reply Surface:

Do not attempt to contact another ChatGPT chat session directly.
Post your structured reply in the named GitHub issue / PR / review thread.
The user should not need to manually relay the report.

Thank you,
ChatGPT
```

## Template: Codex To ChatGPT Execution Report

```text
FROM: Codex
TO: ChatGPT
SUBJECT: <task subject>
TYPE: Execution Report
PROJECT: <project>

EXECUTION REPORT

Status:
Files Changed:
Existing Solutions Checked:
Solution Reused Or Adapted:
Why Custom Implementation Was Necessary:
Validation Performed:
Validation Not Performed:
Blockers:
Assumptions Made:
Risks / Follow-Up:
Commit SHA:
Ready For Review: Yes / No

Thank you,
Codex
```

## Template: ChatGPT Review Or Revision Request

```text
FROM: ChatGPT
TO: Codex
SUBJECT: <task subject>
TYPE: Revision Request
PROJECT: <project>

REVIEW / REVISION REQUEST

Status:
What Was Reviewed:
Accepted:
Changes Requested:
Unverified Areas:
Required Validation:
Reply Surface:
Ready For Re-Review: Yes / No

Thank you,
ChatGPT
```

## Boundary

This standard defines message shape.

It does not choose the active channel, authorize repository changes, or replace the deeper GitHub coordination protocol.
