# Cline + GLM-5.3-Flash Integration

Status: LOCALLY VALIDATED SECONDARY EXECUTOR
Last reviewed: 2026-09-06

## Purpose

Preserve a reusable low-cost secondary coding-agent route inside VS Code using Cline and GLM-5.3-Flash.

This route was first researched from:

`https://m.youtube.com/watch?v=QngK6ftj3Ug`

It was then installed and locally validated on the owner's Windows VS Code environment on 2026-09-06.

It remains a secondary execution path, not a replacement for the current Codex-centered workflow until comparative task evidence justifies a routing change.

## Canonical validated route

```text
VS Code
-> Cline
-> API Provider: Cline Usage-Billing
-> Models tab: Free
-> GLM-5.3-Flash
-> model ID: z-ai/glm-5.3-flash
```

No personal Z.AI API key and no paid Z.AI API setup are required for this validated route.

## Validated environment

- VS Code: `1.135.0`, Windows x64;
- official Cline Marketplace package: `saoudrizwan.claude-dev`;
- Cline version: `4.1.17`;
- official Cline device-authorization login completed;
- existing Codex, OpenAI/ChatGPT, Claude Code, Continue, Gemini, DeepSeek, Kimi, Qwen, and other extensions were not removed or reconfigured.

## Smoke-test evidence

The selected model returned:

`GLM_FREE_SMOKE_OK`

Observed runtime and billing evidence:

- VS Code route shown: `cline:z-ai/glm-5.3-flash`;
- smoke-test cost: `$0.00`;
- Cline Account -> Usage History model: `glm-5.3-flash`;
- Credits Used: `$0.0000`.

This is the validated evidence that the route was free at the time of testing.

## Billing UI rule

A Cline task header may show an estimated token cost such as `$0.0201`.

Do not use that estimate as proof of actual billing.

To verify whether the free route is still free, check:

`Cline Account -> Usage History`

A non-zero actual charge there is the relevant signal.

The account displayed a balance of `0.5000` during validation, but that balance alone does not prove a purchase. No purchase or personal Z.AI API key was created during this setup.

## Recovery procedure

1. Open Cline in VS Code.
2. Open Settings.
3. Select API Provider `Cline Usage-Billing`.
4. Open the `Free` models tab.
5. Select `GLM-5.3-Flash`.
6. Confirm model ID `z-ai/glm-5.3-flash`.
7. Run a small safe test.
8. Open Account -> Usage History and verify there is no non-zero charge for the model use.

## Do not use these routes when restoring the free setup

- do not click `Add Credits` unless paid mode is intentionally required;
- do not choose `ClinePass` merely to access GLM-5.3-Flash;
- do not connect the direct paid Z.AI API route;
- do not create a Z.AI API key for this setup;
- do not remove or replace existing AI extensions.

## Available Cline agent capabilities

The validated Cline setup exposes the normal Cline agent harness, including:

- workspace/file reading;
- file editing;
- terminal/commands;
- web fetch;
- MCP;
- workspace context.

At validation time, auto-approve was enabled for Read, Edit, Commands, Web Fetch, and MCP. Treat that as a security-sensitive local configuration and disable individual permissions when manual confirmation is preferred.

Image input was not separately validated by changing the workspace.

## Intended Project Execution OS role

Use as a locally validated secondary executor for:

- large-context repository reading;
- dependency and code-path discovery;
- preliminary refactor proposals;
- routine low-risk changes;
- second-pass code review;
- experiments where paid frontier inference is unnecessary.

Current primary executor remains Codex for established serious implementation/execution work until comparative evidence says otherwise.

## Important boundary

`No API key required` does not mean local inference.

Treat this as an external cloud provider path. Repository context, prompts, and files may leave the local machine according to current provider behavior and settings.

Never send credentials, secrets, private keys, or sensitive repository data unless the project's data policy permits the external provider.

## Availability rule

The route is locally verified, but free capacity remains provider-controlled.

Do not depend on it as critical infrastructure without rechecking current availability, rate limits, and billing behavior. Free access can change.

## Promotion test still pending

Installation/free-route validation is complete. Broader promotion requires a comparative real-task test under `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`:

1. run the same bounded repository task through Codex and Cline + GLM-5.3-Flash;
2. compare correctness;
3. compare elapsed time and retries;
4. compare context/tool behavior;
5. compare actual cost;
6. compare human correction/review burden;
7. record rate limits and failure modes.

## Canonical research and evidence note

`knowledge-library/verified-technical-solutions/cline-glm-5-3-flash-vscode-free-route-2026-09-05.md`

## Related nodes

- `docs/HARNESS_ENGINEERING_STANDARD.md`
- `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/integrations/codex/`

## Final rule

As of 2026-09-06, the canonical working setup is:

`VS Code -> Cline -> Cline Usage-Billing -> Free -> GLM-5.3-Flash (z-ai/glm-5.3-flash)`

Use Account -> Usage History to verify actual free billing status. Keep the route available as a secondary worker and do not replace Codex globally until measured comparative evidence supports that change.