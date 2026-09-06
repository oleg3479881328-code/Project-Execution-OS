# Cline + GLM-5.3-Flash in VS Code — free no-own-API-key route

Status: VERIFIED / LOCALLY VALIDATED
Initial research date: 2026-09-05
Local validation date: 2026-09-06
Source video: https://m.youtube.com/watch?v=QngK6ftj3Ug
Video title returned by transcription provider: `Use GLM 5.3 Flash FREE in VS Code — No API Key Required`

## Why this was captured

This route provides a working low-cost secondary coding agent inside VS Code: GLM-5.3-Flash through Cline without supplying a personal Z.AI API key or buying API credits.

It is relevant to Project Execution OS as a secondary worker for repository inspection, routine code changes, preliminary refactors, large-context reading, independent review, and other bounded coding-agent work.

## Canonical validated route

```text
VS Code
-> Cline
-> API Provider: Cline Usage-Billing
-> Models tab: Free
-> GLM-5.3-Flash
-> model ID: z-ai/glm-5.3-flash
```

This was locally validated on 2026-09-06.

The important distinction is that this is not a local model and not a direct self-hosted Z.AI API setup. The user does not supply their own Z.AI API key for this Cline-hosted route, but inference still occurs through external cloud infrastructure.

## Locally validated environment

Validation environment:

- VS Code: `1.135.0`, Windows x64;
- official Cline Marketplace package: `saoudrizwan.claude-dev`;
- installed Cline version: `4.1.17`;
- existing Codex, OpenAI/ChatGPT, Claude Code, Continue, Gemini, DeepSeek, Kimi, Qwen, and other AI extensions were left in place and were not reconfigured.

Cline account access was completed through the official device-authorization login flow.

## Free-route evidence

The selected model was:

- API Provider: `Cline Usage-Billing`;
- tab: `Free`;
- display name: `GLM-5.3-Flash`;
- model ID: `z-ai/glm-5.3-flash`;
- runtime route shown in VS Code: `cline:z-ai/glm-5.3-flash`.

A real smoke test returned the exact response:

`GLM_FREE_SMOKE_OK`

Observed usage evidence:

- smoke-test usage cost: `$0.00`;
- Cline Account -> Usage History showed model `glm-5.3-flash`;
- Credits Used: `$0.0000`.

This is the operational evidence to use when checking whether the route is still free.

## Important billing UI nuance

Cline may show a token-cost estimate in a task header, for example `$0.0201`.

Do not treat that estimate as proof of actual credit deduction.

For this route, verify actual billing through:

`Cline Account -> Usage History`

The locally validated GLM-5.3-Flash run showed `$0.0000` credits used.

The Cline account also displayed a balance of `0.5000`. That balance alone does not prove that it was purchased, and no purchase or personal API key was created as part of this setup.

## Recovery procedure

If the setting is lost or changed:

1. Open Cline in VS Code.
2. Open Cline Settings.
3. Set API Provider to `Cline Usage-Billing`.
4. Open the `Free` models tab.
5. Select `GLM-5.3-Flash`.
6. Confirm model ID `z-ai/glm-5.3-flash`.
7. Run a small safe test.
8. Open Account -> Usage History and verify there is no non-zero charge for that GLM-5.3-Flash use.

## What not to do for the free route

- do not click `Add Credits` unless paid mode is intentionally required;
- do not select `ClinePass` merely to access this model;
- do not connect the paid Z.AI API route;
- do not create a Z.AI API key for this setup;
- do not remove or replace existing AI extensions or VS Code settings just to use GLM-5.3-Flash.

## Cline capabilities available to this route

Cline provides agentic access to:

- workspace/file reading;
- file editing;
- terminal/commands;
- web fetch;
- MCP;
- workspace context.

At validation time, auto-approve was enabled for Read, Edit, Commands, Web Fetch, and MCP. This is a security-sensitive setting and can be disabled when manual confirmation is preferred.

Image input was not separately validated by modifying the workspace.

## GLM-5.3-Flash characteristics captured from the 2026-09-05 research pass

The research pass recorded these freshness-sensitive characteristics:

- model family: GLM-5.3-Flash;
- associated with the earlier `Ox Alpha` naming/reference;
- Mixture-of-Experts architecture;
- approximately 320B total parameters with approximately 18B active parameters per token;
- up to 1M-token context window in referenced provider descriptions;
- multimodal positioning;
- MIT-licensed weights according to public model/provider material reviewed in the session;
- aimed at coding and agentic workloads as well as general use.

Recheck these provider/model facts before making future deployment or cost commitments.

## Benchmark interpretation rule

Do **not** convert one coding/agent benchmark into the claim that GLM-5.3-Flash is globally better than Claude Opus or another frontier model.

Correct interpretation:

- GLM-5.3-Flash appears highly competitive on some coding/agentic benchmarks;
- benchmark leadership can be harness-specific and task-specific;
- model quality and agent quality are separate variables;
- vendor benchmarks are useful evidence, not universal truth.

## Harness matters

The same base model can perform materially differently depending on the agent harness around it.

System implication:

```text
model quality != final agent quality

final outcome depends on:
model
+ harness
+ tool use
+ context assembly
+ permissions
+ retry/verification behavior
```

This aligns with Project Execution OS harness-engineering principles.

## Recommended internal role

Current routing:

```text
Codex
-> primary serious implementation/execution path when reliability and existing workflow integration matter

Cline + GLM-5.3-Flash
-> locally validated secondary / inexpensive worker
-> large-repository reading
-> dependency discovery
-> preliminary refactor proposals
-> repetitive low-risk edits
-> second independent code review
-> experiments where paid frontier inference is unnecessary
```

Local installation and free-route validation are complete.

Do not replace Codex globally until a real comparative task is run through both paths and evaluated under `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`.

## Security and privacy boundary

`No API key required` does **not** mean local, offline, or private.

For the Cline-provider route:

- prompts and repository context may be sent to external provider infrastructure;
- do not expose secrets, tokens, passwords, private keys, or confidential project material without an approved data boundary;
- inspect current provider privacy/data-retention terms before using it on sensitive repositories.

This route should be treated as a cloud execution path.

## Cost and availability boundary

The free model route is operationally verified, but free access is still provider-controlled and should be treated as opportunistic capacity rather than guaranteed infrastructure.

Possible future changes include:

- free model removal;
- rate limits;
- queueing;
- provider/model substitution;
- provider policy changes;
- paid usage requirements later.

Therefore Project Execution OS should not make critical production execution depend solely on temporary free inference.

## Existing Solution First conclusion

Do not build a custom VS Code agent or direct GLM integration merely to obtain this capability.

The maintained existing solution is now locally proven:

```text
Cline extension
+ Cline Usage-Billing
+ Free
+ GLM-5.3-Flash
```

Only build or adapt a custom route if a demonstrated gap remains, such as privacy, deterministic provider control, automation/API access, rate limits, unsupported tool behavior, or deeper integration with Project Execution OS worker contracts.

## Adoption status

`LOCALLY VALIDATED SECONDARY EXECUTOR`.

Completed evidence:

1. Cline installation verified;
2. GLM-5.3-Flash confirmed in the Free provider list;
3. official Cline account login completed;
4. real model smoke test passed;
5. actual Usage History showed `$0.0000` credits used;
6. existing VS Code AI extensions remained intact.

Still pending before any broader promotion above secondary-worker status:

1. run the same bounded real repository task through Codex and Cline + GLM-5.3-Flash;
2. compare correctness, elapsed time, context use, tool behavior, cost, retries, and human review burden;
3. record rate limits and failure modes under repeated use;
4. inspect current privacy/data controls for sensitive repositories.

## Related nodes

- `docs/integrations/cline-glm-5-3-flash/README.md`
- `docs/HARNESS_ENGINEERING_STANDARD.md`
- `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/research/CODEX_APP_SERVER_VS_DEEPSEEK_HARNESS_MATRIX_2026-08-29.md`
- `knowledge-library/verified-technical-solutions/vscode-chat-custom-endpoint-deepseek-v4-pro.md`

## Final rule

Treat `VS Code -> Cline -> Cline Usage-Billing -> Free -> GLM-5.3-Flash` as a verified working secondary coding-agent route as of 2026-09-06. Verify actual free status from Usage History, not from estimated task cost shown in the UI, and keep Codex as the primary executor until comparative evidence supports a routing change.