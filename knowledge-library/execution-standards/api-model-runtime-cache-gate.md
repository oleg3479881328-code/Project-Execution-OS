# API model runtime cache gate

- Type: `execution-standard`
- Lifecycle status: `active`
- Review status: `reviewed and accepted for selective reuse`
- Date: `2026-06-03`

## Purpose

Prevent API-based AI model integrations from silently omitting runtime usage, cost and provider-side prompt-cache checks.

## Applies To

Use this gate whenever an AI model is integrated, called, orchestrated or reviewed through an API.

Examples include DeepSeek, OpenAI, Anthropic and comparable model providers.

Do not apply this gate to ordinary chat use when runtime usage data is unavailable.

Do not apply it to ordinary non-model APIs such as weather, maps, payments or classical translation APIs unless comparable model-runtime fields exist.

## Mandatory Check

Every API-based AI model integration must answer this block before acceptance:

```text
API Model Runtime Check

Provider:
Model:
API-based AI model: Yes / No
Prompt caching supported: Yes / No / Unknown
Usage fields available:
Cache-hit fields available:
Cache-miss fields available:
Stable prefix ordering preserved: Yes / No / Not Applicable
Runtime logging implemented: Yes / No
If not implemented, blocker or reason:
```

## Rules

1. Record provider usage, token and billing fields when exposed.
2. Record prompt-cache hit and miss fields when exposed.
3. State explicitly when cache fields are unavailable. Do not invent values.
4. Check official provider documentation when support is unknown.
5. Block review acceptance while the check is unanswered.
6. If logging is deferred, record the reason and unresolved risk.

## Stable Prefix Pattern

For prefix-caching providers, keep reusable content before dynamic content where practical:

```text
stable system layer
-> stable routing layer
-> stable project orientation
-> selected reusable knowledge
-> current project evidence
-> live request or error
```

This ordering is a design hypothesis, not proof of cache reuse.

Measure provider-reported behavior.

## Runtime Fields

Record when available:

- `timestamp_utc`;
- `provider`;
- `model`;
- `request_id`;
- `project_id` or task identifier;
- `context_profile`;
- `context_fingerprint`;
- `selected_route`;
- `loaded_modules`;
- `input_tokens_total`;
- `input_tokens_cache_hit`;
- `input_tokens_cache_miss`;
- `output_tokens`;
- `total_tokens`;
- `estimated_cost_usd` or `billed_cost_usd`;
- `latency_ms`;
- `status`.

## DeepSeek Mapping

When available:

```text
prompt_cache_hit_tokens  -> input_tokens_cache_hit
prompt_cache_miss_tokens -> input_tokens_cache_miss
```

## Metric

When raw counts exist:

```text
cache_hit_share = input_tokens_cache_hit / (input_tokens_cache_hit + input_tokens_cache_miss)
```

## Handoff Rule

Any executor handoff for an API-based AI model integration must include the complete `API Model Runtime Check` block.

If the task is not an API-model integration, record:

```text
API Model Runtime Check: Not Applicable
```

## Review Rule

Block acceptance when:

- the check is omitted;
- provider support is unknown and official documentation was not checked;
- exposed cache fields are discarded silently;
- exposed usage or cost fields are discarded silently;
- stable prefix ordering was relevant but ignored;
- cache-efficiency claims are made without provider runtime evidence.

## Related Existing Standard

- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/REVIEW_STANDARD.md`

## Required Integration Follow-Up

Add references to this active gate from:

- `docs/ROUTER.md` for any API-based AI model integration or cache-measurement task;
- `docs/CODEX_HANDOFF_STANDARD.md` for API-model execution packets;
- `docs/REVIEW_STANDARD.md` for API-model acceptance review;
- `docs/CONTEXT_ASSEMBLY_STANDARD.md` beside its API and cache-aware section.

## Final Rule

Do not accept an API-based AI model integration while the runtime usage and cache gate is unanswered.
