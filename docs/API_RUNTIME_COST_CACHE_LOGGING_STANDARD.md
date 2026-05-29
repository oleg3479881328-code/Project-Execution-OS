# API Runtime Cost And Cache Logging Standard v1

## Purpose

This standard defines how API-based AI execution records token usage, provider-side cache behavior and cost evidence for `Project Execution OS`.

The goal is to measure real economics instead of assuming that a context design is efficient merely because it looks stable.

## Scope

Apply this standard when an AI model is called through an API and runtime token or billing data is available.

Examples:

- DeepSeek API;
- OpenAI API;
- Anthropic API;
- other providers exposing comparable usage information.

This standard does not apply to ordinary chat use when no runtime usage data is available.

## Core Rule

Measure actual usage.

```text
Do not infer cache efficiency from prompt shape alone.
Record provider-reported token usage and cost evidence when available.
```

## Required Runtime Fields

Record these fields when the provider exposes them:

- `timestamp_utc`;
- `provider`;
- `model`;
- `request_id` or provider response identifier when available;
- `project_id` or task identifier when appropriate;
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
- `latency_ms` when available;
- `status`;
- `notes` only when a meaningful anomaly or interpretation is required.

If a provider uses different field names, preserve the provider-native values and map them into this common shape when practical.

## DeepSeek Mapping

When DeepSeek usage fields are available, record:

- `prompt_cache_hit_tokens` -> `input_tokens_cache_hit`;
- `prompt_cache_miss_tokens` -> `input_tokens_cache_miss`;
- prompt/input token total -> `input_tokens_total`;
- completion/output token total -> `output_tokens`;
- total token usage -> `total_tokens`.

Do not invent missing values.

## Cache Metrics

When cache-hit and cache-miss counts are present, calculate:

```text
cache_hit_share = input_tokens_cache_hit / (input_tokens_cache_hit + input_tokens_cache_miss)
```

Also calculate, when useful:

```text
cache_miss_share = input_tokens_cache_miss / (input_tokens_cache_hit + input_tokens_cache_miss)
```

Use percentages for reporting, but preserve raw token counts.

## Cost Metrics

Prefer billed cost when directly available.

If only pricing and usage are available, calculate an estimate and label it clearly:

```text
estimated_cost_usd
```

Do not label an estimate as billed cost.

## Context Identity Rule

When `SYSTEM_CONTEXT_MANIFEST.md` defines an active context profile, record:

- profile name;
- profile fingerprint;
- relevant repository commit or manifest version when useful.

This makes cost comparisons reproducible across context changes.

## Storage Rule

Runtime logs should live in the project layer that owns the API execution.

Examples:

- project-specific API workload -> the relevant project's log storage;
- central system experiment -> `logs/api-runtime/` inside `Project Execution OS`;
- external dashboard export -> preserve the export or screenshot reference in the relevant evidence layer.

Do not force every one-off call into a repository log when no durable comparison or debugging value exists.

## Aggregation Rule

For repeated workloads, summarize by useful windows such as:

- request;
- session;
- day;
- project;
- model;
- context profile;
- provider.

Useful aggregate fields include:

- request count;
- input cache-hit tokens;
- input cache-miss tokens;
- output tokens;
- total cost;
- average cost per request;
- average cache-hit share;
- p50 / p95 latency when available.

## Warning Conditions

Investigate when:

- cache-hit share drops sharply for a previously stable workload;
- a stable profile unexpectedly produces repeated cache misses;
- context fingerprint changes without an intentional profile update;
- input tokens grow materially without a clear task reason;
- cost per request rises materially;
- dynamic data appears before stable reusable prefix content;
- file ordering or formatting becomes non-deterministic.

Do not use a universal fixed threshold as an absolute failure rule. Compare against the workload's normal baseline.

## Evidence Example From Owner Usage

On 2026-05-29, the owner provided a DeepSeek Platform usage screenshot showing the following displayed daily values for `deepseek-v4-flash` on 2026-05-28:

```text
Input (Cache hit): 13,139,328 tokens
Input (Cache miss): 910,696 tokens
Output: 114,098 tokens
Input cache-hit share: approximately 93.5%
```

This is retained as practical evidence that cache-aware context design can materially affect real API economics.

It does not prove which exact content generated the cache hits and does not replace request-level runtime logging.

## Relationship To Context Assembly

Use `docs/CONTEXT_ASSEMBLY_STANDARD.md` to design the context package.

Use this standard to measure whether the runtime economics actually improved.

## Related Nodes

- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- `SYSTEM_CONTEXT_MANIFEST.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`

## Final Rule

Design for stable reusable context.

Measure actual provider behavior.

Do not confuse a good design hypothesis with verified runtime savings.