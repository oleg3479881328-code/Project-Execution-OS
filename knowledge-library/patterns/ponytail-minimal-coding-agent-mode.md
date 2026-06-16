# Ponytail Minimal Coding Agent Mode

Type: pattern
Lifecycle status: candidate
Captured: 2026-06-16

## Source And Evidence

- External project: `DietrichGebert/ponytail` on GitHub.
- Captured from owner-requested research and discussion on 2026-06-16.
- Reported claims from the project README at capture time: roughly 80–94% less code, 3–6x faster, and 47–77% cheaper in benchmarked coding-agent tests across Haiku/Sonnet/Opus-style workflows.

## Problem

Coding agents often over-engineer small tasks: extra files, unnecessary abstractions, long explanations, custom helpers, and architecture that is not justified by the task. This increases token use, execution time, review cost, and maintenance burden.

## Reusable Pattern

Use a separate `Ponytail mode` for bounded coding tasks where the desired outcome is the smallest correct solution.

The useful lesson is not a magical token-reduction mechanism. The savings come mainly from forcing the coding agent to:

1. question whether code is needed at all;
2. prefer existing language/runtime features;
3. avoid unnecessary custom abstractions;
4. write fewer files;
5. write less explanatory noise;
6. avoid architecture unless the task genuinely needs architecture.

## Applies To

- Coding agents.
- Claude Code, Codex, Gemini CLI, Copilot CLI, OpenCode, and similar workflows.
- Small fixes, scripts, one-off tools, narrow refactors, quick prototypes, and cost-sensitive execution.
- Project Execution OS executor tasks where the instruction is implementation, not architecture design.

## Triggers

Load or consider this pattern when a task mentions:

- token cost reduction;
- coding-agent overengineering;
- minimal implementation;
- small bounded coding task;
- quick executor handoff;
- `Ponytail`;
- cheap/fast coding-agent run;
- avoid unnecessary architecture.

## Do Not Load When

Do not use as the default mode for:

- Project Execution OS architecture design;
- standards, protocols, safety models, or long-term system design;
- security-sensitive planning;
- repository-wide refactors that require analysis;
- tasks where explicit design reasoning and tradeoff review are required.

## When To Use

Use Ponytail-style constraints when the owner or system wants fast, cheap, minimal execution and the success condition is clear.

Recommended label:

`Ponytail mode = fast, cheap, minimal, no overengineering.`

## When Not To Use

Do not globally install Ponytail behavior into Project Execution OS. It may suppress necessary architecture, safety reasoning, context assembly, and future-proofing.

Recommended counter-mode:

`Normal/Architect mode = system design, protocols, safety, long-horizon architecture.`

## Adaptation Notes For Project Execution OS

Treat Ponytail as a mode or reusable executor constraint, not as a universal operating standard.

A future skill or executor instruction may reference this pattern when a coding task is already scoped and the expected output is a minimal change.

## Risks

- Under-designing tasks that actually need architecture.
- Cutting explanations that are needed for handoff or auditability.
- Treating benchmark claims as universal without local measurement.
- Confusing smaller code with better code.

## Review Status

Candidate. The idea is useful and researched enough to preserve, but it should not become active mandatory guidance until tested in actual Project Execution OS executor workflows.
