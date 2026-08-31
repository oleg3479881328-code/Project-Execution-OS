# Latest Executor Status

Date: 2026-08-30
Marker: SYSTEM_HYGIENE_V2_DATA_QUALITY_VERIFIED
Task-ID: peos-system-hygiene-v2-data-quality
Status: Hygiene v2 was hardened against shallow-clone activity distortion and its persistence-to-ACTION_REQUIRED behavior was verified deterministically in CI.

Implemented:
- `scripts/audit_system_hygiene.py` now checks `git rev-parse --is-shallow-repository` before treating Git-history activity telemetry as trustworthy;
- a shallow repository produces an explicit data-quality warning instead of silently presenting incomplete `last_touched`, `commits_30d`, and `commits_90d` values as reliable;
- snapshots now record `git_history_shallow` and `activity_metrics_reliable`;
- GitHub Actions summary surfaces Git-history completeness;
- structural hygiene checks still run in shallow clones because their validity does not depend on complete Git history;
- added `scripts/test_hygiene_persistence.py` as a deterministic regression test for warning persistence and shallow-history detection;
- wired the regression test into the existing integrity workflow before the live hygiene audit.

Verified Persistence Behavior:
- two prior consecutive history rows containing the same warning ID plus the current occurrence produce count 3 and meet the `ACTION_REQUIRED` threshold;
- a history row without that warning ID breaks the consecutive chain;
- three prior consecutive rows plus the current occurrence produce count 4;
- the production history file is not polluted with synthetic test rows.

Verified History-Quality Behavior:
- `is_shallow_repository()` explicitly distinguishes shallow and full-history states;
- shallow history is treated as an execution/data-quality limitation, not as a repository hygiene defect and not as an automatic lifecycle signal;
- the production CI checkout remains `fetch-depth: 0`, so scheduled/push activity telemetry is calculated from full Git history.

Verified CI Run:
- GitHub Actions run: https://github.com/oleg3479881328-code/Project-Execution-OS/actions/runs/33344486124
- validated commit: `afd5754ee368ef7d5c8b1c13a947e5b222b3cab9`
- project structure: PASS;
- router integrity: PASS;
- system context manifest: PASS;
- completion contract: PASS;
- hygiene persistence/history-quality regression test: PASS;
- system hygiene audit: PASS.

Durable Lesson:
Never interpret Git-history-derived hygiene telemetry from a shallow clone as complete repository activity evidence. Structural checks may still be valid, but activity metrics require full history or an explicit incompleteness warning.

Next-Safe-Action: let real scheduled history accumulate while keeping the deterministic persistence regression test in CI; if production hygiene is later adapted to project repositories, preserve the same distinction between structural truth and history-dependent telemetry.
