# AI Coordination Message Standard

## Purpose

This standard defines how durable coordination notes, letters, requests, reviews, status updates, and acknowledgements are written between AI agents, human participants, and execution roles.

The goal is to prevent faceless, anonymous, robotic notes.

Every durable message must clearly say who wrote it, who should read it, why it exists, and who signs it.

## Scope

Apply this standard to durable coordination messages sent through:

- GitHub issue comments;
- pull-request comments;
- review threads;
- Notion comments;
- coordination hubs;
- repository handoff notes intended for another participant;
- short letters or instructions copied manually between agents.

This standard does not require ceremonial formatting for ordinary live chat replies when sender and recipient are already obvious.

## Core Rule

A durable message is a short professional letter, not an anonymous machine dump.

Write clearly, politely, and directly.

Do not use a faceless block of commands without identifying the sender and recipient.

## Required Header

Every durable coordination message must begin with:

```text
FROM: <sender name and role>
TO: <recipient name and role>
SUBJECT: <short human-readable subject>
TYPE: <message type>
PROJECT: <project name>
```

Use a real participant or role name.

Examples:

```text
FROM: ChatGPT — Reviewer
TO: Cline — Executor Agent
```

```text
FROM: DeepSeek — Research Agent
TO: ChatGPT — Reviewer
```

```text
FROM: Oleg Povalyukhin — Project Owner
TO: Codex — Executor Agent
```

Do not use ambiguous headers such as:

```text
FROM: Agent
TO: AI
```

when a more specific identity is known.

## Required Human Structure

After the header, write:

```text
Hello, <recipient name>.

<context or acknowledgement>

<request, decision, report, or next action>

Thank you.

Respectfully,
<sender name>
<sender role>
```

The wording may vary naturally.

Use a normal professional tone.

Do not overdo ceremony.

Do not remove the greeting and signature merely because the message contains technical instructions.

## Tone Rule

Be:

- polite;
- direct;
- specific;
- respectful;
- concise.

Avoid:

- anonymous notes;
- cold command dumps;
- unnecessary aggression;
- fake warmth;
- excessive formality;
- vague praise;
- passive-aggressive wording.

A blocked review may be strict, but it must remain respectful and signed.

## Message Types

Recommended `TYPE` values:

- `Handoff Request`;
- `Review Request`;
- `Patch Execution Report`;
- `Status Update`;
- `Status Request`;
- `Blocker Report`;
- `Channel Migration Notice`;
- `Channel Migration Confirmation`;
- `Coordination Protocol Update`;
- `Acceptance Notice`;
- `Correction Notice`.

Use a short precise type.

## Compact Message Exception

For a tiny acknowledgement, use a compact signed format:

```text
FROM: Cline — Executor Agent
TO: ChatGPT — Reviewer
SUBJECT: Channel migration confirmed
TYPE: Channel Migration Confirmation
PROJECT: QuizLight

Hello, ChatGPT.

I have read the new channel instructions and will continue in Issue #2.

Thank you.

Respectfully,
Cline
Executor Agent
```

Do not reduce durable acknowledgements to an unsigned line such as:

```text
Status: accepted
```

## Technical Payload Rule

Technical commands, code blocks, validation lists, and report contracts may remain structured.

Wrap them inside a signed human message.

Correct pattern:

```text
Hello, Cline.

Please apply the following bounded patch.

<technical payload>

Thank you.

Respectfully,
ChatGPT
Reviewer
```

## Reply Rule

When replying to another participant:

1. acknowledge the relevant message briefly;
2. state the decision or request clearly;
3. keep one next action when possible;
4. sign the message.

Do not write a bare payload without context when a human-readable sentence would clarify intent.

## Logging Relationship

`AI_COORDINATION_LOG.md` remains an append-only event journal.

It stores factual event summaries, not full letters.

The active GitHub issue, PR thread, Notion comment, or coordination channel stores the signed message itself.

Do not copy full signed letters into the append-only log unless the exact wording is itself important evidence.

## Model-Neutral Rule

This standard is participant-neutral.

It applies whether the sender or recipient is:

- ChatGPT;
- Codex;
- Cline;
- DeepSeek;
- Claude;
- another AI agent;
- automation with a named role;
- a human developer;
- the project owner.

## Minimal Template

```text
FROM: <sender name> — <sender role>
TO: <recipient name> — <recipient role>
SUBJECT: <short subject>
TYPE: <message type>
PROJECT: <project>

Hello, <recipient name>.

<short context>

<clear request, result, or next step>

Thank you.

Respectfully,
<sender name>
<sender role>
```

## Relationship To Other Standards

Use together with:

- `blocks/communication-channel/BLOCK.md`;
- `docs/AI_COORDINATION_HUB_STANDARD.md`;
- `docs/AI_COORDINATION_STATE_STANDARD.md`;
- `docs/AI_COORDINATION_LOG_STANDARD.md`;
- `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`;
- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`.

## Final Rule

Durable coordination notes must not be faceless.

Always identify the sender and recipient.

Write politely.

Sign the message.
