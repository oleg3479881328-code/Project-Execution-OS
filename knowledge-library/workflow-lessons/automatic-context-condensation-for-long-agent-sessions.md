# Automatic Context Condensation For Long Agent Sessions

Type: workflow-lesson
Lifecycle status: candidate
Captured: 2026-06-05
Review status: preserved for review; not yet an active mandatory system rule

## Source And Evidence

The owner observed an actual long-running Cline session in which the agent reported context usage around `86K / 128K` tokens and later around `92K / 128K` tokens. The session had accumulated repeated large file reads, long terminal outputs from `gh` and `curl`, timeouts, and long GitHub Issue comments.

After condensation, the agent reported that the working context had been replaced by a compact summary and that subsequent growth should be slower.

The owner requested that this lesson be preserved centrally and used by default where applicable.

## Problem

Long agent sessions can accumulate unnecessary context from:

- repeated full reads of large source files;
- long terminal output and timeout traces;
- repeated API responses;
- historical issue comments;
- already-resolved debugging evidence;
- duplicated context that no longer helps the active task.

This can increase token use, cost, latency, and the risk that important live instructions become harder to distinguish from stale history.

Provider-side prompt caching may reduce billed cost for repeated prefixes, but it does not remove session-context bloat or replace deliberate context management.

## Reusable Lesson

For long-running agent sessions, proactively monitor context growth and preserve a compact handoff summary before history becomes oversized.

When the active interface supports condensation, use its built-in condensation mechanism. In Cline-like interfaces this may appear as a command such as `/compact` or `/smol`, but exact command names and behavior must be verified against the installed version before being treated as universal.

When automatic invocation is unavailable, the agent should proactively recommend a checkpoint, condensation, or new-session handoff packet before continuing expensive work.

## Default Operating Recommendation

When working in an agent interface that exposes context-window usage:

1. Watch for sustained context growth during long implementation or debugging sessions.
2. Treat repeated full-file reads, long logs, timeouts, and duplicated command output as context-bloat signals.
3. Before the context becomes oversized, create or refresh a compact durable handoff summary containing:
   - current objective;
   - completed work;
   - unresolved work;
   - relevant files only;
   - latest validation status;
   - commit, issue, or coordination references when applicable;
   - explicit next action.
4. Use the interface's verified condensation feature when available.
5. Start a fresh session when a bounded handoff is cheaper and safer than extending the current session.
6. Do not rely on prompt caching as a substitute for context reduction.

## Applies To

- Cline and similar coding-agent chats;
- Codex or executor sessions with bounded handoff packets;
- API-based orchestrators where token cost and context size matter;
- long debugging, implementation, review, and repository-maintenance sessions.

## Triggers

Load this lesson when one or more of the following is true:

- the interface shows high context-window utilization;
- the session contains repeated large file reads;
- terminal output or API logs have become long and repetitive;
- a task is complete and the project is being handed to another agent;
- the owner asks to reduce token consumption or make condensation automatic;
- prompt-cache savings are being discussed alongside session-context cost.

## Do Not Load When

- the task is small and bounded;
- the session is fresh;
- no agent context window is involved;
- the user only needs a standalone factual answer unrelated to project execution.

## Risks And Limits

- Exact commands such as `/compact` or `/smol` may be product-specific, version-specific, or unavailable in some interfaces.
- Condensation can omit important details if no durable project state or bounded handoff summary exists.
- A smaller context is not automatically a correct context; preserve current evidence and unresolved constraints.
- Provider-side prompt caching and session-context condensation are separate mechanisms.

## Related Standards

- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- `docs/INCREMENTAL_REENTRY_STANDARD.md`

## Review Needed Before Activation

Before promoting this candidate to an active standard:

1. verify the actual supported condensation commands and behavior in the installed Cline version;
2. decide whether a numeric warning threshold should be product-specific or general;
3. decide where any Cline-specific automatic instruction belongs, for example a global Cline rules layer rather than a project repository;
4. test whether the automatic rule reduces context growth without causing premature summaries or loss of critical state.
