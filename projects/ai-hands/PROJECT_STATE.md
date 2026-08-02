# AI Hands — Project State

## State Snapshot

- Date: `2026-08-02`
- Status: `active`
- Mode: `execution`
- Phase: `MVP 1 bootstrap and environment discovery`
- Health: `green with unverified local-environment dependency`

## Objective

Prove that a local model can execute a bounded task prepared by ChatGPT against an approved local repository and return a verifiable result.

## Confirmed Decisions

- Project name: `AI Hands`.
- Project ID: `ai-hands`.
- Project location: `projects/ai-hands/` inside `Project-Execution-OS`.
- Durable layers: GitHub and Notion.
- MVP architecture: controller task -> local executor -> approved workspace -> isolated Git branch -> validation -> diff/report.
- Existing-solution candidates: Goose, OpenHands, Cline CLI/SDK; custom adapter only if these are inadequate.
- Automatic merge and unrestricted shell access are outside MVP 1.

## Unknowns To Verify

- Operating system and local development environment.
- CPU, RAM, GPU, and available VRAM.
- Installed local model servers.
- Exact installed models and quantizations.
- Docker and WSL availability.
- Which candidate executor is already installed or easiest to adapt.
- Which model produces reliable tool calls on the actual machine.

## Active Work Package

### WP-001 — Local environment inventory

Collect verified machine and software facts without changing the environment.

Required output:

- system inventory;
- installed runtimes and model servers;
- installed model list;
- candidate executor availability;
- constraints and recommended first donor path.

### WP-002 — Executor donor smoke test

After WP-001, test the smallest adequate existing executor against a disposable repository with one harmless file-edit task.

Required output:

- setup steps;
- task packet used;
- commands run;
- file diff;
- validation result;
- failures and limitations;
- go/no-go decision.

## Risks

- Small local models may produce malformed or unreliable tool calls.
- Large context or model memory requirements may exceed the machine's resources.
- Agent shells may claim local-provider support but fail in multi-step execution.
- Unsafe command access could damage unrelated files without strict workspace and command boundaries.

## Next Practical Step

Prepare and execute WP-001 on the owner's computer, then update this file and `logs/latest.md` with verified findings.
