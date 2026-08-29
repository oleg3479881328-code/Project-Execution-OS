# DeepSeek Harness Extraction Audit — 2026-08-29

## Decision

Treat `deepseek-ai/deepseek-harness` as a donor/reference implementation for Project Execution OS, not as a replacement.

Primary extraction targets:

- reconstructable model-visible state;
- replaceable capability seams;
- one common tool execution pipeline;
- fail-closed behavior rather than silent degradation;
- per-call execution policy;
- explicit enforcement quality;
- durable worker lineage;
- interruption-aware recovery;
- provider capability declarations;
- optional runtime integration for session persistence, sandboxing, and subagents.

## Adopt Now

1. Model-visible runtime inputs must be reconstructable from durable state when replay/resume matters.
2. Reusable runtime capabilities should separate stable definition, provider implementation, and consumer.
3. Tool execution should pass through a shared policy/guard/approval/execute/post-process/result-record pipeline.
4. Unsupported or unavailable security/runtime capabilities must fail explicitly rather than silently degrade.
5. Execution policy should be resolved per call when sessions or concurrent workers can have different boundaries.
6. Partial enforcement must never be reported as full enforcement.
7. Crash recovery must preserve evidence and represent unfinished work as interrupted or unknown rather than successful.
8. Delegated workers should have durable parent/child identity and recursion/delegation depth when continuation is supported.
9. Provider-specific feature gaps must be declared and rejected loudly when requested.

## Adapt Later

- append-only event-sourced runtime sessions;
- request-envelope snapshots for replay;
- continuable child agents;
- child tool filtering;
- layered runtime profiles and overrides;
- replay/snapshot regression fixtures;
- durable architecture decision notes.

## Experimental Integration Candidates

- DeepSeek Harness headless/SDK runtime surfaces;
- built-in session persistence;
- built-in sandbox providers;
- Codex and Claude Code subagent providers.

These should be evaluated only as lower execution-plane components. Project Execution OS remains the control plane for routing, owner intent, project memory, approvals, review, standards, and durable project evidence.

## Do Not Copy By Default

- Cordis as a mandatory Project Execution OS framework;
- DeepSeek-specific package topology and naming;
- repository-specific coverage/documentation conventions;
- self-modifying runtime behavior;
- pre-release compatibility refusal as an OS-wide policy.

## Extraction Matrix

| Pattern | Decision |
|---|---|
| all-plugin runtime composition | ADAPT |
| Definition / Provider / Consumer seam | ADOPT |
| append-only runtime event log | ADAPT |
| model-visible state is reconstructable | ADOPT |
| persistence separate from session model | ADOPT |
| common tool execution pipeline | ADOPT |
| fail-closed approval and policy | ADOPT |
| per-call policy resolution | ADOPT |
| explicit partial/full enforcement | ADOPT |
| durable worker lineage | ADOPT |
| provider capability declarations | ADOPT |
| continuable subagents | ADAPT / INTEGRATE |
| runtime profiles/overlays | ADAPT |
| headless / SDK runtime | INTEGRATE experimentally |
| Codex / Claude Code providers | INTEGRATE experimentally |
| Cordis-specific implementation rules | IGNORE |
| self-modification | IGNORE by default |
| immediate replacement of current OS components | REPLACE: none |

## Smallest Future Proof Of Concept

If later approved, test one isolated read-only task through a DeepSeek Harness runtime surface, verify durable replay, verify denial behavior, delegate one bounded child task, and confirm that Project Execution OS still owns the task contract and durable result evidence. Measure failure mode, recovery behavior, latency, and maintenance cost before considering broader adoption.

## Sources

- https://github.com/deepseek-ai/deepseek-harness
- `docs/architecture.md`
- `docs/subsystems/session.md`
- `docs/subsystems/persistence.md`
- `docs/tool-execution-pipeline.md`
- `docs/subsystems/sandbox.md`
- `docs/subsystems/subagent.md`
- root `AGENTS.md`

## Final Decision

Immediate action is standards extraction, not migration. No current Project Execution OS component is deleted or replaced on the basis of this audit alone.
