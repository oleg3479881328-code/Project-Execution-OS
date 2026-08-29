# Harness Engineering Standard v3

## Purpose

This standard defines how `Project Execution OS` designs the execution scaffold around AI agents and agentic workflows.

The goal is to make agents reliable by engineering the surrounding system, not by relying on prompt cleverness or model capability alone.

Use this standard to decide what context, tools, permissions, memory, verification, observability, and handoff artifacts an agent needs before it is treated as repeatable or operational.

## Source Trail

Primary donor references:

- `https://github.com/ai-boost/awesome-harness-engineering`
- `https://github.com/deepseek-ai/deepseek-harness`

Additional reviewed execution references:

- `https://pimenov.ai/articles/vaybkoding-bez-bardaka/`
- gap analysis: `docs/research/VIBECODING_WITHOUT_CHAOS_GAP_ANALYSIS_2026-08-28.md`
- DeepSeek extraction audit: `docs/research/DEEPSEEK_HARNESS_EXTRACTION_AUDIT_2026-08-29.md`

Donor references inform this standard but do not replace local OS architecture.

## Scope

Apply this standard when:

- creating or changing a reusable agent;
- creating or changing a repeated agentic workflow;
- giving an agent tools, files, APIs, browser access, repository access, Gmail, Calendar, Notion, Drive, GitHub, shell, or publishing access;
- moving a workflow from experiment toward operation;
- diagnosing repeated agent failure;
- preparing a Codex, Claude Code, Cursor, ChatGPT, local-model, or multi-agent handoff;
- deciding whether a task needs a single prompt, single agent, deterministic workflow, or multi-agent system.

Do not force this standard onto a disposable one-off chat task with no reuse, risk, durable artifact, external tool use, or future comparison value.

## Core Definition

```text
Agent harness = the controlled execution environment around an AI agent.
```

A harness may include entrypoint and routing, context, planning, tools, permissions, memory, sandbox, verification, observability, approval, and handoff state.

## Core Rule

```text
Do not start by adding more agents.
Start by making the smallest sufficient harness explicit.
```

Preferred progression:

```text
single answer
  -> single model call
  -> single agent with minimal tools
  -> deterministic workflow with checkpoints
  -> multi-agent workflow only when evidence justifies separation
```

## Runtime Reliability Invariants

Use the following rules when a workflow becomes durable, resumable, delegated, security-sensitive, or operational.

### Model-Visible Reconstruction Law

```text
If runtime state materially affects what the model sees, a durable runtime must be able to reconstruct that state when replay or resume matters.
```

This can include effective system instructions, injected context, model route/configuration, available tool schemas, user messages, assistant outputs, and tool results.

A human-readable transcript alone is not sufficient when it omits request state needed for faithful reconstruction.

Do not force event sourcing onto ordinary project documents. This law applies to reusable runtime/session implementations, not to every Project Execution OS file.

### Capability Seam Rule

When a reusable runtime capability can have more than one implementation, prefer three explicit roles:

```text
Service Definition
-> Provider
-> Consumer
```

- `Service Definition` owns the stable interface and obligations.
- `Provider` owns one implementation/backend.
- `Consumer` is the tool, workflow, or application that uses the capability.

Do not copy provider logic into consumers merely to avoid defining a seam.

This rule complements `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`; it does not replace the existing four-layer Project Execution OS architecture.

### Fail-Closed Runtime Law

```text
Unsupported or unavailable safety-critical behavior must not silently degrade into a weaker behavior.
```

Examples:

- required approval cannot be obtained -> deny;
- requested provider capability is unsupported -> reject explicitly;
- required confinement is unavailable -> do not silently run without confinement;
- durable state contains an event/format the runtime cannot faithfully interpret -> refuse replay or mark it unsupported;
- enforcement is partial -> report partial, never full.

Tool or provider errors should identify what failed rather than encourage the agent to invent an unverified workaround.

### Per-Call Policy Resolution

When concurrent sessions, workers, tools, workspaces, or approved escalations can have different permissions, resolve execution policy per capability call rather than through mutable global state.

A resolved policy should carry the smallest relevant facts, for example:

- caller/session identity;
- workspace boundary;
- permission mode;
- explicitly approved escalation;
- provider enforcement status.

Defaults should be resolved explicitly at the owning boundary rather than hidden deep inside execution code.

### Interruption Recovery Law

```text
Incomplete durable work must not be recovered as successful work.
```

After a crash, aborted executor, incomplete persistence write, or lost worker:

- preserve trustworthy evidence already recorded;
- represent unfinished work as `interrupted`, `unknown`, `failed`, or another explicit non-success state;
- do not silently truncate inconvenient evidence merely to make the state look balanced;
- require fresh verification before promoting recovered work to completed/validated.

### Delegated Worker Lineage Rule

For resumable, recursive, or controllable child agents, persist the identities that affect authorization and reconstruction when the runtime supports them:

- parent worker/session identity;
- child identity;
- delegation depth;
- provider/preset identity when it changes tools or behavior.

Display labels and message metadata are attribution, not authority.

A requested child capability that its provider cannot support should fail loudly rather than be silently ignored.

## Common Tool Execution Pipeline

For a reusable runtime with multiple tools, prefer one shared execution pipeline rather than duplicating policy inside each tool.

Conceptual order:

```text
model requests tool
-> record/identify call
-> pre-execution hooks and policy
-> non-weakening guards
-> approval when required
-> execute with timeout/retry/metrics wrappers as appropriate
-> capability-specific checks
-> normalize/post-process result
-> freeze authoritative outcome
-> record result/evidence
-> expose result to model/UI
```

The exact implementation may differ by runtime.

Critical properties:

- a denied call should have an explicit observable outcome;
- approval cannot weaken a stronger invariant guard unless the policy explicitly defines a safe escalation path;
- post-processing must not disguise execution failure as success;
- tool identity must not change mid-pipeline;
- security policy should be able to span tool families without rewriting the agent loop.

## Sandbox Boundary Rules

Sandbox claims must name what is actually enforced.

Filesystem confinement does not automatically imply network isolation, process isolation, secret isolation, browser isolation, or credential isolation.

When the runtime can distinguish enforcement quality, record or surface the distinction, for example:

```text
full
partial
unavailable
```

Do not treat `partial` as equivalent to `full` for a task whose safety depends on the missing guarantee.

Prefer per-call sandbox policy when different sessions or executions can legitimately require different boundaries.

## Minimum Harness Questions

Before promoting an agent or workflow beyond one-off use, answer the smallest relevant subset.

### 1. Task Shape

- What repeated task is this harness for?
- Is the task bounded, long-running, risky, or multi-session?
- What is the successful outcome?
- What is explicitly out of scope?

### 2. Entrypoint And Route

- Where does the agent start?
- Which router or project entrypoint must be read first?
- Which deeper files are loaded only when needed?
- How does a new executor avoid stale chat memory?

### 3. Context Delivery

- What is always-on context?
- What is retrieved on demand?
- What must survive context compaction?
- What should never enter model context?

Use `docs/CONTEXT_ASSEMBLY_STANDARD.md`.

### 4. Planning And State

- Does the task need a durable plan?
- Where are decisions, deviations, and progress recorded?
- What state must survive handoff?

Use `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` for long or transferable work.

### 5. Tools

- Which tools are available?
- Which are actually needed?
- Are tool names and outputs unambiguous?
- Does each tool do one conceptual thing?
- Do tool errors tell the agent what to do next?
- Can shared policy be applied once through a common execution pipeline?

Do not expose broad tool sets merely because they exist.

### 6. Permissions

- Which actions are read-only, write-capable, destructive, external, financial, publishing, deployment, or communication actions?
- Which require explicit human approval?
- What is forbidden even if technically possible?
- What happens when approval cannot be obtained?

Default to least privilege and fail closed for safety-critical actions.

### 7. Sandbox And Execution Boundary

- Where does code, shell, browser, or file execution happen?
- What files, network domains, credentials, and secrets are reachable?
- Which isolation properties are actually enforced?
- Is enforcement full, partial, or unavailable?
- Can the agent modify its own rules, tools, hooks, or permission files?
- What is the rollback path?

An agent that can edit its own harness is higher risk.

### 8. Memory

- What should be remembered?
- Who approves memory writes that affect future behavior?
- How are stale or contradicted memories invalidated?
- Where is memory stored?
- Can runtime-visible state needed for replay be reconstructed?

Prefer durable project files for project-specific state before inventing a global memory layer.

### 9. Verification

- What check proves the output works?
- Can the agent run it itself?
- What requires human review?
- Which failures should become regression cases?

Do not accept `it looked good once` as evidence for a repeated workflow.

### 10. Observability And Handoff

- What evidence explains what the agent did?
- Where are logs stored?
- What artifact proves completion?
- Can another executor resume without reading the chat transcript?
- Can interrupted work be distinguished from completed work?

Use `logs/latest.md`, project state files, or the owning workflow log when the task must survive handoff.

## Bounded Execution Contract

For non-trivial implementation work, establish the smallest useful contract before editing:

```text
GOAL
USER-OBSERVABLE RESULT
CONTEXT TO READ
CHANGE
DO NOT TOUCH
VERIFY
ROLLBACK / SAFE CHECKPOINT
```

Omit fields that add no value for a micro-task. The purpose is to bound the decision space, not create paperwork.

If the instruction is vague, such as `improve this screen` or `clean up the code`, do not interpret it as permission for broad refactoring. Convert it into an observable defect or desired outcome, explicit boundaries, non-goals, and verification. Adjacent improvements become separate candidate tasks unless required by the current contract.

## Verification Invalidation Law

```text
Any change made after verification invalidates the previous verification for every behavior that the new change could affect.
```

Do not preserve a `validated` state merely because an earlier version passed. Re-run the relevant checks after the last affecting change.

## User-Facing Behavioral Verification

Machine checks are necessary when applicable, but they do not by themselves prove user-facing behavior.

For UI work, verify the relevant subset of:

- open from a clean/reproducible state;
- primary success path;
- one relevant error, invalid, empty, or failure state;
- refresh/persistence when persistence is part of the contract;
- critical console errors and network failures;
- representative desktop and mobile viewport when responsive behavior is in scope.

Choose checks from the actual contract. Do not perform irrelevant browser rituals merely to satisfy a checklist.

Browser tools such as Playwright or DevTools are implementation options, not mandatory dependencies. The requirement is observable evidence appropriate to the task.

## Code Checkpoint Rule

For Git-backed implementation work, after the final relevant verification:

1. inspect the actual diff;
2. confirm no unrelated files or behavior changed;
3. preserve a known rollback path;
4. prefer one coherent completed change per commit/checkpoint;
5. distinguish `committed` from `validated` and `reviewed`.

A commit proves a stored state. It does not prove the behavior works.

## Skill Extraction Rule

Do not create a reusable skill merely because a workflow can be imagined.

Promote a workflow into a skill only after real executions show a recurring, sufficiently stable sequence of inputs, boundaries, checks, stop conditions, and output evidence. If each run still requires major instruction rewriting, keep collecting observations instead of hiding uncertainty inside automation.

Use the Skill Creator block and lifecycle standards for the actual promotion decision.

## Minimum Harness Package

For a reusable or repeated workflow, the minimum package should usually include:

```text
entrypoint
route
context rule
tool permissions
verification gate
state / log location
handoff instruction
```

For GitHub-backed projects, prefer:

```text
PROJECT.md
AGENTS.md or local agent instructions when useful
PROJECT_STATE.md after meaningful execution begins
logs/latest.md after meaningful execution begins
```

For central reusable standards inside this repository, prefer:

```text
START_HERE.md
→ docs/ROUTER.md
→ routed standard
→ PROJECT_STATE.md and logs/latest.md after meaningful changes
```

## Harness Change Protocol

When changing a harness:

1. Confirm the owner task and route.
2. Check for an existing adequate standard or donor pattern first.
3. Make the smallest useful change.
4. Keep the entrypoint and router consistent.
5. Add or update verification guidance.
6. Update transfer state when the change is meaningful.
7. Record what was reused, adapted, integrated experimentally, rejected, and remains custom.

Do not add empty templates, logs, agents, scorecards, memory files, or workflow layers by ritual.

Do not replace a working Project Execution OS control-plane responsibility merely because a donor runtime implements a similar lower-level mechanism.

## Runtime Integration Boundary

Project Execution OS may use an external harness/runtime as an execution plane while keeping the OS as the control plane.

Preferred ownership split:

```text
Project Execution OS
  -> owner intent
  -> routing
  -> project standards
  -> durable project memory
  -> approvals/review policy
  -> business evidence

Optional runtime
  -> model calls
  -> tool execution
  -> runtime session log
  -> sandbox enforcement
  -> child-agent execution
```

Before replacing an existing mechanism with an external runtime, require evidence that integration removes meaningful custom complexity without weakening ownership, evidence, security, or transfer readiness.

## Relationship To Existing Standards

| Concern | Use |
|---|---|
| Existing solution search | `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` |
| Project entrypoint | `docs/PROJECT_ENTRYPOINT_STANDARD.md` |
| Context selection | `docs/CONTEXT_ASSEMBLY_STANDARD.md` |
| Transfer-ready state | `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` |
| Agent quality and metrics | `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` |
| API cost and cache evidence | `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md` |
| Research | `docs/RESEARCH_STANDARD.md` |
| Review | `docs/REVIEW_STANDARD.md` |
| Codex handoff | `docs/CODEX_HANDOFF_ENTRYPOINT.md` |
| Capability blocks | `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md` |
| Skill creation | `blocks/skill-creator/BLOCK.md` |

## Promotion Levels

### Level 0 — One-Off

No harness artifact is required unless the task has meaningful risk, write access, or durable project value.

### Level 1 — Repeated Experiment

Define the entrypoint, tool permissions, expected output, and one verification check.

### Level 2 — Operational Workflow

Add durable state, logs, regression examples, cost/latency evidence when available, explicit approval rules for critical actions, and interruption/recovery semantics when needed.

### Level 3 — High-Risk Or Business-Critical Workflow

Add stronger sandboxing, audit trail, adversarial cases, rollback procedure, permission tests, fail-closed behavior tests, and human approval gates.

## Warning Conditions

Investigate and improve the harness when:

- the agent asks the same setup questions repeatedly;
- the agent loads too much context by default;
- the agent uses the wrong tool;
- the agent cannot explain what state is current;
- a new executor cannot resume the workflow;
- results vary wildly across runs;
- critical actions happen without approval evidence;
- unavailable approval or sandboxing silently becomes weaker execution;
- provider capability gaps are silently ignored;
- tool errors lead to hallucinated workarounds;
- memory becomes stale or contradicts project files;
- model-visible runtime state cannot be reconstructed when replay is required;
- interrupted execution looks indistinguishable from success;
- cost grows without quality improvement;
- adding another agent increases handoff failures;
- a task expands through undefined “improvements”;
- code is changed after verification without re-verifying affected behavior.

## Final Rule

Engineer the scaffold before blaming the model.

Use the smallest sufficient harness.

Make context, tools, permissions, boundaries, verification, rollback, evidence, reconstruction, and handoff explicit before treating an agent as reliable.
