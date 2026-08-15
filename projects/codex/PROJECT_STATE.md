# Codex — PROJECT_STATE.md

## Current Mode

`active monitoring + knowledge consolidation`

## Current Objective

Maintain one durable Codex project that captures important public developments and our own operational experience, then turns worthwhile findings into concrete tests, integrations, or reusable project practices.

## Active Inputs

- Reddit monitoring: https://www.reddit.com/r/codex/
- Official OpenAI/Codex sources when a claim needs verification.
- Existing Project Execution OS Codex standards and integration docs.
- Our own Codex, GitHub, MCP, n8n and executor experiments.

## Current Monitoring Rules

Surface and preserve only meaningful findings in these categories:

- Codex product updates and new features;
- new tools and execution capabilities;
- MCP and external integrations;
- automation and agent workflows;
- long-running / remote execution patterns;
- limits, usage behavior and pricing changes;
- bugs, regressions and verified fixes/workarounds;
- reusable ideas applicable to current projects.

For each durable finding, preserve:

1. date observed;
2. source URL;
3. concise claim/finding;
4. verification status;
5. why it matters;
6. possible application in our system;
7. next test/action if warranted.

## Existing Monitoring

An hourly condition-watch task for `r/codex` is active. It is configured to notify only when new posts are materially useful or important.

## Initial Findings To Preserve

The recent monitoring conversation surfaced several themes worth retaining as leads. Treat them as community-reported until revalidated against original sources before operational adoption:

- remote / always-on Codex CLI execution patterns using a persistent machine plus SSH/Tailscale;
- live-device execution loops where Codex acts, observes runtime state and validates results;
- reports about usage/reset behavior and paid reset options;
- risk of usage waste when an agent loops on a UI action it cannot perform;
- support escalation may be relevant when anomalous usage is caused by a stuck workflow.

## Existing Internal Codex Assets

Reuse these instead of recreating their contracts:

- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`
- `docs/integrations/codex/CODEX_PROJECT_BOOTSTRAP_ADAPTER.md`
- `skills/coordination/chatgpt-codex-github-communication/`

## Current Risks / Unknowns

- Reddit reports may be anecdotal, stale, account-specific, or incomplete.
- Product limits/pricing can change quickly and must be verified at time of use.
- Some useful Codex material already exists elsewhere in Project Execution OS; duplication must be avoided.

## Next Safe Actions

- Continue Reddit condition monitoring.
- Revalidate high-value community findings before turning them into project decisions.
- When new Codex work occurs elsewhere in our projects, link or promote the reusable result here instead of leaving it only in chat.
- Expand deeper knowledge files only when there is enough confirmed material to justify them.
