# Archify Integration — Project Execution OS

## Status

`CANDIDATE`

Reviewed: `2026-08-30`

Upstream:

- Repository: `https://github.com/tt-a1i/archify`
- Reviewed stable version: `v2.16.0`
- License: MIT

## Purpose

Use Archify as an external architecture-visualization and architecture-evidence tool for Project Execution OS and its projects when a verified interactive system map is useful.

Archify is not a Project Execution OS capability block and must not be represented in `capability-library/REGISTRY.md` unless Project Execution OS later implements and verifies its own bounded capability contract around it.

Current role:

```text
Project Execution OS
        |
        | architecture description / repository evidence
        v
Archify agent skill + deterministic renderer/validator
        |
        v
validated typed JSON IR
        |
        v
self-contained architecture/workflow/sequence/data-flow/lifecycle artifact
```

## Existing Solution First Decision

Do not build a custom architecture-map renderer before testing Archify.

Archify already provides the relevant finished mechanism:

- typed JSON intermediate representation;
- deterministic HTML/SVG compilation;
- architecture, workflow, sequence, data-flow, and lifecycle views;
- schema/layout/output validation;
- exact-route and authored upstream/downstream exploration;
- optional revision-verified source evidence;
- Before / Delta / After architecture comparison;
- self-contained HTML and export formats;
- Codex CLI support;
- DeepSeek Harness community integration path.

Therefore the default experiment is adoption/integration, not reimplementation.

## Truth Boundary

Archify output is a communication/evidence artifact, not an independent source of architectural truth.

Project Execution OS remains authoritative for:

- owner intent;
- routing;
- standards;
- durable project memory;
- approvals and review policy;
- capability readiness;
- verified project state.

Archify may visualize only relationships supported by authored structure or source evidence. It must not be used to manufacture topology, impact, risk, merge safety, runtime reachability, or ownership facts that were not established.

## Installation / Invocation Candidates

Global skill install:

```bash
npx skills add tt-a1i/archify -g
```

Try with Codex without permanent install:

```bash
npx skills use tt-a1i/archify@archify --agent codex
```

DeepSeek Harness community opt-in reported upstream:

```bash
dsh plugin --profile web add @tt-a1i/archify-dsh@0.1.0
```

The DeepSeek Harness adapter is not automatically approved by this document; it must be evaluated together with the existing execution-plane research before adoption.

## Network / Privacy Note

Upstream documents an optional stable-manifest update reminder. It does not install updates automatically. For a no-update-check test environment, use:

```bash
ARCHIFY_UPDATE_CHECK_DISABLED=1
```

Project data, prompts, credentials, secrets, or private repository contents must not be intentionally transmitted outside the approved local/agent execution path merely to generate a diagram.

## Pilot — Project Execution OS Self Map

The first pilot target is this repository itself.

### Goal

Generate a high-level interactive map that helps an owner or new executor understand Project Execution OS without replacing the canonical entrypoint/router.

### Scope

Map the smallest useful control-plane path:

```text
START_HERE.md
-> docs/ROUTER.md
-> project entrypoint / state restoration
-> standards / domain knowledge
-> reusable capability path
-> application adapter
-> worker / Codex execution handoff
-> review
-> durable evidence / knowledge promotion
```

Also show the four intended layers:

```text
domain knowledge
-> executable capability
-> workflow / application adapter
-> owner-facing UI
```

### Required Evidence Mode

Where Archify supports source-backed architecture nodes, pin evidence to one repository revision and include only verified file/line references.

If exact evidence cannot be established, the relationship must be labelled as authored/conceptual rather than source-proven.

### Acceptance Criteria

The pilot passes only if all are true:

1. Archify runs successfully through a supported Codex path without requiring a custom renderer.
2. The generated JSON IR validates successfully.
3. The delivered HTML artifact validates successfully under Archify's own checks.
4. The map contains the canonical `START_HERE.md -> docs/ROUTER.md` entry path.
5. The four Project Execution OS layers are visually distinguishable.
6. The map does not present speculative relationships as source-proven facts.
7. At least one exact authored route can be traced interactively.
8. The artifact remains self-contained and can be opened locally.
9. No production secret is stored in the artifact or committed output.
10. A human review confirms the map reduces orientation time rather than adding misleading complexity.

## Pilot Outputs

Keep generated pilot artifacts under a bounded repository-local test location such as:

```text
docs/architecture/archify/
```

Expected artifacts:

```text
project-execution-os.architecture.json
project-execution-os.architecture.html
VALIDATION.md
```

Do not commit large derivative exports (PNG/WebM/etc.) unless they serve a specific documentation need.

## Promotion Gate

Remain `CANDIDATE` until the pilot passes.

Promote to `ACTIVE` in the central tool inventory only after evidence records:

- exact Archify version;
- exact Project Execution OS revision mapped;
- install/invocation path used;
- validation command/results;
- artifact path;
- human review result;
- known limitations;
- rollback/removal path.

Promotion does not make Archify mandatory for every project.

## Use When

Archify is a good candidate when the task is:

- system orientation;
- architecture communication;
- workflow/sequence explanation;
- source-backed architecture review;
- architecture delta review before merge;
- route/reach exploration;
- durable visual documentation of a sufficiently stable system.

## Do Not Use When

Do not require Archify for:

- trivial repositories;
- rapidly changing throwaway experiments;
- diagrams whose truth cannot be grounded;
- replacing `START_HERE.md`, `docs/ROUTER.md`, project state, or canonical standards;
- claiming runtime behavior solely from a diagram;
- avoiding direct source inspection during a technical review.

## Exit / Replacement Path

Archify has no authority over canonical project state. Removing it must leave Project Execution OS fully operable.

Removal is therefore:

```text
remove/uninstall Archify skill or plugin
-> retain canonical repository docs/state
-> delete optional generated visualization artifacts if no longer useful
```

No migration of core Project Execution OS memory or routing should be required.

## Decision

```text
ADOPT FOR PILOT
DO NOT REIMPLEMENT
DO NOT PROMOTE TO ACTIVE UNTIL VERIFIED
DO NOT REGISTER AS AN INTERNAL CAPABILITY YET
```
