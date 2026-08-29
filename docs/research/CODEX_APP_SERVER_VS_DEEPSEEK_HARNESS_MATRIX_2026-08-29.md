# Codex App Server vs DeepSeek Harness — Execution-Plane Matrix — 2026-08-29

## Decision Summary

For the next practical Project Execution OS runtime experiment, prefer **Codex App Server first**.

DeepSeek Harness remains a high-value donor/reference and a possible later multi-provider execution layer, but Codex App Server is currently the closer fit for our existing Codex-centric worker model because it already exposes first-party thread lifecycle, streaming events, approvals, sandbox/permissions, interruption, persistence-backed thread history, project attachment, and external client control.

Project Execution OS remains the control plane in either case.

```text
Project Execution OS
= owner intent + routing + project memory + task contract + review + durable evidence

Codex App Server (first POC candidate)
= Codex execution runtime

DeepSeek Harness (secondary candidate / architecture donor)
= generic multi-provider harness and possible future runtime layer
```

## Primary Sources Reviewed

### OpenAI Codex

- `openai/codex/codex-rs/app-server/README.md`
- `openai/codex/codex-rs/app-server-client/README.md`
- current official `openai/codex` repository surfaces as of 2026-08-29

### DeepSeek Harness

- `deepseek-ai/deepseek-harness/docs/architecture.md`
- `docs/subsystems/session.md`
- `docs/subsystems/persistence.md`
- `docs/tool-execution-pipeline.md`
- `docs/subsystems/sandbox.md`
- `docs/subsystems/subagent.md`
- root `AGENTS.md`

## Comparison Matrix

| Concern | Codex App Server | DeepSeek Harness | Project Execution OS decision |
|---|---|---|---|
| External orchestrator control | First-class JSON-RPC app-server; stdio supported, unix socket supported, websocket experimental | SDK/headless/profile surfaces; plugin composition | Codex direct fit now |
| Task/session primitive | Thread -> Turn -> Item | Session -> Turn -> Step/Event | Either works; Codex maps more directly to current worker task lifecycle |
| Start new worker session | `thread/start` | create/start agent/session | Codex direct |
| Resume same session | `thread/resume` | persisted session resume | Both |
| Fork/branch work | `thread/fork`, bounded fork history | session fork/seed lineage | Both |
| Streaming progress | turn/item notifications and deltas | durable session events + live agent events | Both; Codex simpler for a Codex worker client |
| Interrupt/cancel | `turn/interrupt` | cancellation + subagent interrupt | Both |
| Durable history | stored threads, paginated turns/items, rollout/state persistence | append-only event log with pluggable JSONL/SQLite persistence | DeepSeek architecture is stronger/general; Codex is sufficient for first POC |
| Reconstructable runtime state | Thread/turn state and persisted items; exact effective surface depends on Codex protocol/version | explicit model-visible <-> logged invariant and request-header reconstruction | Adopt DeepSeek rule in OS; use Codex runtime where sufficient |
| Sandbox | Codex sandbox/permissions policy surfaced at thread/turn level | explicit sandbox seam; read-only/workspace-write/full; partial/full enforcement reporting | Codex first POC; retain OS verification because Codex policy propagation can vary by client/version |
| Approval policy | Built-in approval requests/policies/reviewer flows | approval seam in common tool pipeline | Codex direct for Codex execution |
| Tool execution | Built-in Codex tools + MCP/apps/plugins; app-server emits tool/item progress | generic tool registry + shared pre/guard/approval/execute/post pipeline | Codex execution; DeepSeek pipeline laws stay OS standard |
| Tool/provider replaceability | Primarily Codex-owned runtime surface; extensible via MCP/apps/plugins | core design: capability seams and replaceable plugins/providers | DeepSeek stronger for generic platform |
| Multi-agent/subagents | Current Codex runtime includes spawned child-thread/subagent concepts and parent/ancestor thread discovery; proactive behavior may be model/runtime controlled | explicit multi-provider subagent seam incl. Codex, Claude Code, in-process, ACP, DSH SDK | DeepSeek stronger as cross-provider orchestrator; Codex enough for first worker runtime POC |
| Child lineage | parent/ancestor thread relationships available on relevant subagent threads | explicit durable parent session + delegation depth | Adopt durable-lineage principle regardless of runtime |
| Provider diversity | Codex/OpenAI-centric | first-class multi-provider/adapters | DeepSeek wins if OS later needs one runtime for Codex + Claude + DeepSeek |
| Runtime profiles/composition | Codex config, permissions, projects, skills/plugins/apps/MCP | layered profiles/bundles/patches; every major subsystem replaceable | DeepSeek more composable; not needed for first POC |
| Project attachment | experimental project APIs + thread project assignment + cwd/runtime roots | workspace/session cwd plus custom composition | Codex closer to our project execution flow |
| Client integration | official app-server powers rich Codex interfaces; shared in-process client exists | TS/Python SDK and headless/web profiles | Both viable |
| Backpressure/lifecycle | bounded server queues; overload error; bounded client shutdown | plugin/runtime-specific lifecycle controls | Both; Codex already documents external client behavior |
| Fail-closed capability mismatch | Some behavior depends on protocol/config/client; runtime errors explicit, but effective capability proof is not universally atomic | explicit design rule: unsupported capabilities reject loudly; sandbox cannot silently bypass confinement | Keep OS fail-closed law above either runtime |
| Runtime maturity for our use case | First-party Codex execution surface in active official repo; some APIs experimental and changing | developer-preview harness, rapidly evolving | Codex wins for immediate bounded POC |
| Need to replace OS routing/memory/review | No | No | Never by default |

## What Codex App Server Can Potentially Replace or Simplify

If a POC succeeds, the following custom execution plumbing becomes a deletion/simplification candidate:

1. manual creation of a Codex worker session;
2. manual prompt/task transport into that worker;
3. ad-hoc progress polling where app-server events can be consumed directly;
4. ad-hoc worker cancellation and continuation logic;
5. parts of the current bridge needed only to resume or steer a Codex session;
6. custom parsing of a worker's final chat response when authoritative turn/item events can be converted into OS evidence.

GitHub issues/comments may then become a durable coordination/audit surface rather than the primary live transport.

## What Must Remain Project Execution OS Owned

Do not delegate these responsibilities to either runtime:

- `START_HERE` and routing;
- project identity and canonical project memory;
- Existing Solution First;
- owner task interpretation;
- bounded execution contract;
- selection of what context the worker receives;
- policy deciding which actions require owner approval;
- independent review and verification standards;
- durable business/project evidence;
- cross-runtime registry and capability decisions;
- promotion/deprecation decisions for reusable capabilities;
- final status semantics (`completed`, `validated`, `reviewed`, etc.).

Runtime completion is not equivalent to OS validation.

## Why DeepSeek Harness Still Matters

DeepSeek Harness should not be discarded. It currently provides the stronger donor model for:

- generic Definition / Provider / Consumer capability seams;
- model-visible state reconstructability;
- event-sourced runtime history;
- shared tool policy pipeline;
- explicit fail-closed sandbox behavior;
- per-call policy resolution;
- explicit partial/full enforcement distinction;
- provider capability declarations;
- multi-provider child agents including Codex and Claude Code.

If Project Execution OS later needs one runtime spanning multiple agent products, DeepSeek Harness may become more valuable than a Codex-only runtime.

## Current Risks / Limitations

### Codex App Server

- several app-server capabilities are explicitly experimental;
- websocket listener is experimental/unsupported for production; stdio is the safest first POC transport;
- effective tool/sandbox/permission behavior can depend on version, client inputs, runtime configuration and platform;
- protocol schemas are version-specific and should be generated from the exact Codex binary used;
- external clients must handle asynchronous notifications and lifecycle ordering correctly;
- runtime completion does not prove the requested filesystem or user-visible effect actually happened.

### DeepSeek Harness

- developer-preview churn risk;
- adopting Cordis/runtime composition would add a second platform layer;
- using it only to launch Codex may add indirection without deleting enough OS code;
- broader surface means larger integration/maintenance cost.

## Recommended Architecture Now

```text
Project Execution OS
        |
        | bounded task contract + selected context + policy
        v
Codex App Server client adapter
        |
        v
Codex thread / turn / items
        |
        +--> sandbox / approvals / tools
        +--> streaming events
        +--> resume / fork / interrupt
        |
        v
OS evidence adapter
        |
        v
PROJECT_STATE / logs / GitHub audit surface / review gate
```

DeepSeek Harness stays outside this first path as a donor/reference and later optional provider-agnostic runtime candidate.

## Smallest Safe POC

Do **one isolated read-only Codex App Server POC** before any bridge deletion.

Contract:

```text
GOAL
Prove that Project Execution OS can programmatically start and control one Codex worker through the official app-server surface.

BOUNDARY
Disposable/local test workspace. Read-only task. No publishing, deployment, email, secrets mutation, or destructive writes.

FLOW
1. Launch exact pinned Codex binary with app-server over stdio.
2. Generate/version-pin the matching app-server schema.
3. Initialize a client.
4. thread/start with explicit cwd and restrictive permission/sandbox settings.
5. turn/start with one bounded repository-inspection task.
6. Capture thread/turn/item events.
7. Wait for authoritative turn completion.
8. thread/read or paginated history read to confirm durable state.
9. Resume the same thread and ask one follow-up question.
10. Interrupt a deliberately long harmless turn to verify cancellation.
11. Convert resulting events into one OS evidence artifact.

PASS
- start works;
- event stream is usable;
- durable read/resume works;
- interrupt works;
- no forbidden side effect occurs;
- another executor can understand result from OS evidence without reading raw chat.

FAIL
Any silent permission downgrade, missing authoritative state, non-resumable thread, uncontrolled side effect, or platform-specific failure that prevents a reliable bounded worker.
```

## Decision

**Primary POC candidate: Codex App Server.**

**DeepSeek Harness: retain as architecture donor and secondary multi-provider candidate.**

No current Prompt Bridge or worker transport is deleted until the POC proves an official Codex path can replace it with equal or better observability, control, recovery, and durable evidence.
