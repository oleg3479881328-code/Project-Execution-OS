# AI Coordination Log

Append meaningful coordination events at the bottom only. Do not rewrite history.

## 2026-06-08 — Active coordination snapshot created

Type: State initialization
Project: Project Execution OS
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/27

Event:
- Added `AI_COORDINATION_STATE.md` and this append-only log because both canonical root coordination files were missing.
- Recorded Issue #27 as the active reply surface.
- Recorded current review blocker: executor report referenced a commit SHA not resolvable through GitHub and expected prototype files were absent on the default branch.
- Recorded the accepted system-standard change that added mandatory start-now behavior to Codex handoff templates.

Next Step:
- For future `02`, open `AI_COORDINATION_STATE.md`, then read Issue #27 directly, then inspect repository evidence.

## 2026-06-08 — Clean integration branch required

Type: Review blocker
Project: Project Execution OS
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/27

Event:
- Verified correction commit `5298c32ef65884bb67ce9713b42c7e08830f8b44`.
- Accepted compact-context behavior for successful hybrid calls, bounded-evidence fallback, and explicit full-evidence debug mode.
- Applied README code-fence fix at `1ea0d29c769e142bddd4ad8976bdecc9010f021f`.
- Compared executor branch with `main` and found unrelated historical files in the diff.
- Requested a clean branch from current `main` with only Issue #27 changes.

Next Step:
- Review the next executor reply in Issue #27 and verify the clean diff before integration.

## 2026-06-08 — PR #30 review corrections requested

Type: Review blocker
Project: Project Execution OS
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/pull/30

Event:
- Published clean PR #30 from `codex/issue-27-hybrid-agent-clean`.
- Confirmed clean diff contains the intended hybrid-agent files only.
- Found open traceability review thread: compact-context source references require validation against bounded input evidence.
- Confirmed workflow failure occurs during system-context-manifest validation after `docs/CONTEXT_ASSEMBLY_STANDARD.md` changed.
- Posted an in-scope correction request in PR #30.
- Updated active channel to PR #30.

Next Step:
- On `02`, inspect PR #30 latest executor reply, new head SHA, checks, and review thread status.

## 2026-06-09 — Hybrid fallback hardening and model comparison opened

Type: Phase transition
Project: Project Execution OS
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/35

Event:
- Issue #34 benchmark completed with approximately 76% average measured context reduction and approximately 13.2 seconds average local preprocessing latency on `llama3.2:3b`.
- Observed reliability gaps: invalid local schema values, hallucinated paths, and timeout exceptions can propagate instead of degrading gracefully.
- Opened Issue #35 to harden fallback behavior, add explicit local-model selection, compare already-installed Ollama models, and publish a clean review PR.

Next Step:
- For future `02`, open Issue #35, inspect the latest executor report or blocker, and continue from actual repository evidence.

## 2026-06-09 — Mandatory executor progress heartbeat added

Type: System rule update
Project: Project Execution OS
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/35

Event:
- Updated `docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`.
- Added mandatory progress heartbeats for all executors during long-running tasks.
- Required first heartbeat after 20 minutes, then at least every 20 minutes until completion or blocker.
- Required immediate heartbeat on major phase completion, validation start, long benchmark start, PR creation, material ETA change, non-blocking fallback, or in-scope implementation-plan change.
- Required compact structured heartbeat fields and owner-visible linked receipt.

Next Step:
- Apply the heartbeat rule to all current and future bounded handoffs.

## 2026-06-09 — Durable interim checkpoint rule added

Type: System rule update
Project: Project Execution OS
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/35

Event:
- Updated `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`.
- Added mandatory durable interim checkpoints for long-running, multi-phase, benchmark-heavy, research-heavy, integration-heavy, and review-heavy work.
- Required preservation after meaningful phase completion, reusable partial results, provisional rankings, path-changing fallback decisions, implementation-complete / validation-pending state, validation-complete / publication-pending state, channel transitions, and in-scope reviewer corrections.
- Required checkpoints to remain repository-visible or channel-visible and linked from the active issue or PR when needed.
- Required new executors to be able to identify completed work, do-not-repeat steps, measured evidence, and the next safe action without reconstructing context from chat.

Next Step:
- Apply durable interim checkpoint preservation automatically whenever reconstruction cost becomes material.

## 2026-06-10 — Reels Factory AWS coordination moved to Issue #47

Type: Channel Transition
Project: Reels Factory MVP
Previous Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/46
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47

Event:
- Created Issue #47 as the single active reply surface for the AWS ComfyUI + Wan Image-to-Video smoke-test execution phase.
- Posted redirect notice in Issue #46.
- Posted origin notice in Issue #47.
- Updated `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md` to Issue #47.
- Updated `AI_COORDINATION_STATE.md` to the Reels Factory MVP execution phase.
- Canonical execution kit commit is `3f7a245605a3afed5f7cd0c6c3758e68d3a8f282`.
- Accepted route: `g5.xlarge` + `Wan2.1-I2V-14B-480P` FP16 Diffusers + `wanvideo_2_1_14B_I2V_example_03.json` + `100 GB gp3` + source-IP-only security.

Next Step:
- Wait for executor acknowledgement and explicit AWS access status in Issue #47.
- Do not launch AWS resources until owner explicitly authorizes runtime execution.

## 2026-06-11 — MarkItDown adapter coordination moved to Issue #51

Type: Channel Transition
Project: Project Execution OS / MarkItDown Intake Adapter
Previous Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51

Event:
- Confirmed the mailbox-dispatcher v3 publication checkpoint from `coordination/FROM_EXECUTOR.md` with reported SHA `aed415635ec277dc3737fa6d13553b3b17d614c4`.
- Created Issue #51 as the dedicated bounded reply surface for the MarkItDown local document intake adapter MVP.
- Posted origin notice in Issue #51 and redirect notice in Issue #49.
- Updated `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md` to Issue #51.
- Updated `coordination/TO_EXECUTOR.md` to sequence `5` with the new handoff.
- Updated `AI_COORDINATION_STATE.md` to the MarkItDown adapter execution phase.
- Required immediate executor `ACK` in Issue #51 and matching inbound mailbox update.

Next Step:
- Read `coordination/FROM_EXECUTOR.md`, then Issue #51, and verify the executor `ACK` before reviewing implementation evidence.

## 2026-06-12 — Restored Issue #51 mailbox after dispatcher v4 route clobber

Type: Coordination recovery and review blocker
Project: Project Execution OS
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51
Queued Follow-Up: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52

Event:
- Verified published Mailbox Dispatcher v4 commit `b893038c222a4926ac37ae55d67254b0dc14e683`.
- Rejected v4 after code review because commit/push failures remain unchecked, SHA publication remains misleading, runtime dirty-tree policy remains too permissive, and trust-boundary documentation remains inaccurate.
- Detected that the dispatcher-development commit overwrote `coordination/TO_EXECUTOR.md` for Issue #52 while `ACTIVE_CHANNEL_ROUTE.md` and `AI_COORDINATION_STATE.md` still identified Issue #51 as the active task.
- Restored the active Issue #51 outbound mailbox with sequence `6` in commit `e5e9baf10b7d752f68e5d002efb7138615ac1f98`.
- Posted Issue #51 recovery notice: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51#issuecomment-4690906540
- Queued Mailbox Dispatcher v5 correction in Issue #52 without overwriting the active route: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52#issuecomment-4690902781
- Updated `AI_COORDINATION_STATE.md` and `logs/latest.md` to preserve the recovered route and queued follow-up.

Next Step:
- Wait for Codex `ACK` in Issue #51 for outbound mailbox sequence `6`.
- Keep Mailbox Dispatcher v5 queued in Issue #52 until Issue #51 completes and the route is intentionally migrated.

## 2026-07-10 — TikTok Research Sorter coordination moved to Issue #72

Type: Channel Transition
Project: TikTok Research Sorter 0.2.0
Previous Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/57
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/72

Event:
- Created Issue #72 as the dedicated bounded execution surface for autonomous stabilization and delivery of TikTok Research Sorter 0.2.0.
- Posted a signed origin notice in Issue #72 and a signed redirect notice in Issue #57.
- Updated `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md` to Issue #72.
- Created the reviewer-owned project mailbox `projects/tiktok-research-sorter/coordination/TO_EXECUTOR.md` with sequence `1`.
- Updated `AI_COORDINATION_STATE.md` to the TikTok Research Sorter task.
- Required immediate Codex ACK, creation of the executor-owned `FROM_EXECUTOR.md`, branch reconciliation, reproducible dependency lock, Linux and Windows CI, automated extension/updater artifacts, profile-card validation, updater hardening, and signed completion evidence.
- Preserved PR #71 as the related code-review surface while Issue #72 remains the active coordination channel.
- Explicitly removed the owner from routine courier, installation, testing, and evidence-relay duties.

Next Step:
- Read `projects/tiktok-research-sorter/coordination/FROM_EXECUTOR.md` when created, then Issue #72, then reported branch, CI, artifact, and PR evidence.
- Continue automatically from the executor ACK, HEARTBEAT, BLOCKER, or COMPLETE state.
