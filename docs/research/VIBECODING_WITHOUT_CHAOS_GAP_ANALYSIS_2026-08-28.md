# Vibe Coding Without Chaos — Gap Analysis

Date: 2026-08-28
Status: reviewed donor reference
Donor: https://pimenov.ai/articles/vaybkoding-bez-bardaka/

## Purpose

Compare the donor workflow against current Project Execution OS rules and adopt only the useful gaps. The donor is a discovery/reference source, not system authority.

## Executive Result

Project Execution OS already covers the larger architecture: routed entrypoints, durable project memory, Existing Solution First, explicit harness design, review states, permissions, verification, rollback awareness, logs, handoff, and skill lifecycle.

The donor adds several useful execution-level rules that were either implicit or weaker in the OS:

1. every bounded implementation task should explicitly state `CHANGE / DO NOT TOUCH / VERIFY / ROLLBACK` when those fields matter;
2. any post-verification change invalidates prior verification for the affected behavior;
3. user-facing work needs behavioral verification, not only build/test success;
4. browser verification should cover success, at least one relevant failure state, persistence/refresh when applicable, critical console/network signals, and representative desktop/mobile sizes when applicable;
5. vague requests to “improve” working code must be converted into an observable defect/outcome and bounded scope before execution;
6. a reusable skill should be extracted from observed repetition, not invented as a universal framework before the workflow stabilizes.

These rules are accepted below as targeted additions to existing standards rather than a new parallel workflow.

## Rule-by-Rule Comparison

| Donor rule | OS status before review | Decision |
|---|---|---|
| Define user, problem, result, verification, non-goals | Mostly covered by project lifecycle, harness task shape, acceptance/review | Keep existing architecture; no duplicate standard |
| Durable project memory outside chat | Stronger in OS via entrypoint, project memory, transfer-ready state, logs | No change |
| `AGENTS.md` as concise recurring instructions | Already present in bootstrap/harness architecture | No change |
| Do not create documentation trees by ritual | Already explicit in Start New Project and Harness Engineering | No change |
| One bounded task package | Partially covered | Strengthen Harness Engineering with explicit task contract |
| Read state before changing | Already routed through entrypoint/context/state standards | No change |
| Machine checks plus real behavior check | Covered generally, but browser detail was weak | Strengthen Harness Engineering |
| Every later change invalidates affected verification | Missing as explicit law | Add to Harness Engineering and Review Standard |
| Browser success + failure + refresh + console/network + desktop/mobile | Not explicit centrally | Add as conditional UI verification baseline |
| Review `git diff` before checkpoint | General evidence/review exists; not explicit enough for code changes | Add to Harness Engineering |
| One completed change per checkpoint/commit | Compatible with bounded-change model | Add as preferred code checkpoint rule |
| Avoid vague “improve/refactor” prompts | Scope drift is reviewed, but prevention rule was weaker | Add explicit bounded-improvement rule |
| Skill only after repeated process stabilizes | Existing Skill Creator requires recurring need, but observed repetition criterion can be stronger | Strengthen Harness Engineering; Skill Creator already structurally compatible |
| Next step stored outside chat | Stronger OS continuity/logging already covers this | No change |

## Accepted Standard Changes

### A. Bounded Execution Contract

For non-trivial code/UI changes, the executor should know, before editing:

```text
GOAL
USER-OBSERVABLE RESULT
CONTEXT TO READ
CHANGE
DO NOT TOUCH
VERIFY
ROLLBACK / SAFE CHECKPOINT
```

Use only fields that materially reduce ambiguity; do not turn micro-tasks into paperwork.

### B. Verification Invalidation Law

```text
A change after verification invalidates the previous verification for every behavior that change could affect.
```

A task cannot remain `validated` merely because an earlier version passed.

### C. UI Behavioral Verification Baseline

When a change affects a user-facing interface and the environment allows behavioral verification, verify the relevant subset of:

- clean start/open;
- primary success path;
- one relevant error/empty/invalid state;
- refresh/persistence when persistence is part of the contract;
- critical console errors and network failures;
- representative desktop and mobile viewport when responsive behavior is in scope.

The subset must be driven by the actual contract. Do not run irrelevant checks by ritual.

### D. Bounded Improvement Rule

Do not execute an unbounded instruction such as “improve this screen” or “clean up the code” against a working system. Convert it to:

```text
observed defect or desired outcome
+ explicit boundary
+ non-goals
+ verification
```

Adjacent improvements become separate candidate tasks unless required to satisfy the current contract.

### E. Code Checkpoint Rule

For Git-backed implementation work, after successful validation:

- inspect the actual diff;
- confirm no unrelated files/behavior were changed;
- preserve a rollback path;
- prefer one coherent completed change per commit/checkpoint.

A commit is evidence of state, not evidence that behavior works.

### F. Skill Extraction Rule

Promote a workflow into a reusable skill only after real executions show a recurring, sufficiently stable sequence of inputs, checks, boundaries, stop conditions, and output evidence. If each execution still requires major instruction rewriting, keep collecting observations instead of hiding uncertainty in a skill.

## Rejected / Not Adopted As New Architecture

The donor’s suggested fixed file tree (`TODO.md`, `CHANGELOG.md`, `architecture.md`, etc.) is not adopted as a universal Project Execution OS bootstrap. The OS already deliberately expands memory only after meaningful work exists.

The donor’s “one-hour setup” is useful as an illustration but is not a standard SLA or mandatory sequence. Project Execution OS routing remains authoritative.

Browser tooling names such as Playwright or Chrome DevTools MCP are implementation options, not mandatory dependencies. The required thing is evidence appropriate to the contract.

## Final Decision

Do not create a new “vibe coding workflow.” Integrate the useful donor rules into the existing Harness Engineering and Review standards.

The Project Execution OS remains the authority; this donor improves execution precision inside the existing architecture.