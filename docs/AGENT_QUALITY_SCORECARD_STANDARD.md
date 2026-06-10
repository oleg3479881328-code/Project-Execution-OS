# Agent Quality Scorecard Standard v1

## Purpose

This standard defines how `Project Execution OS` evaluates AI agents, agentic workflows and model-backed automations.

The goal is to measure useful, repeatable outcomes instead of judging quality by prompt cleverness, token count per request, number of tools, number of agents, or subjective impressions.

## Scope

Apply this standard when:

- an agent or agentic workflow is intended for repeated use;
- a prompt, model, tool set, context package or orchestration flow is being changed;
- an API-backed execution path is being optimized;
- an agent is moving from experiment toward operational use;
- a regression, cost increase or reliability issue must be investigated;
- two agent designs, providers or context profiles are being compared.

Do not force a full scorecard onto a disposable one-off chat task with no reuse, risk or comparison value.

## Core Principle

Measure the smallest sufficient architecture against successful outcomes.

```text
Do not optimize tokens per request in isolation.
Optimize cost, latency, reliability and human effort per successful outcome.
Do not add agents, tools or context unless measured evidence justifies the added complexity.
```

## Architecture Rule

Use the least complex design that reliably satisfies the task.

Preferred progression:

```text
single model call
  -> single agent with a minimal tool set
  -> deterministic workflow with checkpoints
  -> multi-agent workflow only when measured failure patterns justify separation
```

Multi-agent architecture is not an automatic sign of maturity.

Add another specialized agent only when evidence shows that it improves at least one important outcome without causing unacceptable cost, latency, transfer-loss or debugging overhead.

## Scorecard Dimensions

### 1. Outcome Quality

Measure whether the useful result was actually produced.

Recommended fields:

- `task_id`;
- `task_type`;
- `success`;
- `accepted_without_manual_rework`;
- `quality_score` when a rubric exists;
- `failure_category` when unsuccessful;
- `artifact_reference` when a durable output exists.

Primary metrics:

- `success_rate`;
- `accepted_without_manual_rework_rate`;
- rubric score distribution when applicable.

### 2. Cost And Latency

Measure economics per successful result, not only per request.

Recommended metrics:

- `total_cost_usd`;
- `cost_per_request`;
- `cost_per_successful_outcome`;
- `latency_ms`;
- `p50_latency_ms`;
- `p95_latency_ms`;
- `retry_count`;
- `retry_rate`;
- `human_correction_minutes` when practical.

Token and cache evidence follows:

`docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`

### 3. Context Efficiency

Measure whether the agent receives the smallest sufficient context package.

Recommended fields:

- `context_profile`;
- `context_fingerprint`;
- `selected_route`;
- `loaded_modules`;
- `input_tokens_total`;
- `input_tokens_cache_hit`;
- `input_tokens_cache_miss`;
- `cache_hit_share` when available;
- meaningful context-growth anomalies.

Do not interpret a larger context as automatically worse when it materially improves outcome quality.

Context design follows:

`docs/CONTEXT_ASSEMBLY_STANDARD.md`

### 4. Tool Use

Measure whether tools are minimal, distinct and correctly selected.

Recommended metrics:

- available tool count;
- invoked tool count;
- successful tool calls;
- failed tool calls;
- unnecessary tool calls;
- wrong-tool selections;
- permission violations;
- human approvals requested for critical actions.

Do not optimize for an arbitrary universal tool-count limit.

A smaller tool set is usually easier to control, but tool overlap and unclear boundaries are often more dangerous than raw count.

### 5. Reliability And Regression Protection

Maintain a representative evaluation set for repeated workflows.

The set should contain:

- normal cases;
- edge cases;
- previously observed failures;
- safety-sensitive cases where applicable;
- format and artifact checks;
- cost and latency baselines when practical.

Before promoting a meaningful change to an operational agent, compare it against the current baseline.

Track:

- passed checks;
- failed checks;
- regressions introduced;
- regressions fixed;
- expected behavior changes;
- unexpected behavior changes.

Do not accept `it worked once` as sufficient evidence for a repeated workflow.

### 6. Observability

Preserve enough evidence to explain the execution path.

Record when practical:

- selected route;
- model and provider;
- context profile and fingerprint;
- loaded modules;
- agent or workflow version;
- tool calls;
- retries;
- result status;
- failure category;
- cost and latency;
- durable artifact references.

Do not log secrets, credentials or unnecessary personal data.

### 7. Safety And Permissions

Use minimum necessary permissions.

Track:

- read-only versus write-capable tools;
- critical actions requiring human approval;
- attempted permission violations;
- blocked unsafe actions;
- audit trail availability;
- external-content prompt-injection risks when applicable.

Write access, deletion, payment, publication, deployment and outbound communication should receive explicit review appropriate to their risk.

### 8. Transferability

A repeated workflow is not mature if it works only with one human operator or one chat history.

Check whether a new executor can determine:

- where the entrypoint is;
- what state is current;
- which context is required;
- which tools are allowed;
- what the acceptance checks are;
- where logs and artifacts live;
- what failed previously;
- what action is safe to take next.

## Required Minimum Scorecard

For a repeated operational workflow, record at least:

| Category | Minimum required evidence |
|---|---|
| Outcome | success or failure, acceptance status, failure category when relevant |
| Economics | total cost when available, latency when available, retries |
| Context | route, profile or loaded modules when the workflow uses routed context |
| Tools | invoked tools and tool-call failures when tools are used |
| Reliability | evaluation or verification result appropriate to the task |
| Safety | approval evidence for critical write actions when applicable |
| Transferability | durable state or artifact reference for work that must survive handoff |

## Comparison Rule

When comparing two designs, models or context profiles:

1. use the same representative task set where practical;
2. preserve the version or fingerprint of each compared configuration;
3. compare successful outcomes first;
4. compare cost, latency, retries and human corrections after quality is acceptable;
5. record material trade-offs;
6. reject improvements that only move cost or speed while causing unacceptable reliability or safety loss.

## Promotion Levels

Use the lightest level that fits the workflow.

### Level 0 — One-Off

No durable scorecard required unless the task has meaningful risk or future comparison value.

### Level 1 — Repeated Experiment

Keep a small task set, result notes, token and latency evidence when available, and known failure examples.

### Level 2 — Operational Workflow

Maintain repeatable evaluations, versioned configuration, runtime logging, failure classification and regression checks.

### Level 3 — High-Risk Or Business-Critical Workflow

Add explicit approval gates, stronger audit trails, adversarial cases, permission testing, rollback procedures and monitored baselines.

## Relationship To MCP

`MCP` means `Model Context Protocol`.

Use MCP where it reduces custom connector duplication and improves portability.

Do not treat MCP as a substitute for:

- permission design;
- tool schema quality;
- validation;
- error handling;
- audit logging;
- security review;
- workflow-specific evaluation.

## Storage Rule

Store scorecard evidence in the layer that owns the workflow.

Examples:

- project-specific workflow -> the relevant project evidence or logs layer;
- central system experiment -> `logs/agent-quality/` inside `Project Execution OS` when durable evidence is useful;
- reusable operational agent -> its versioned agent, workflow or project layer;
- external dashboard export -> preserve the export or a durable reference in the owning evidence layer.

Do not create empty scorecard artifacts by ritual.

## Warning Conditions

Investigate when:

- success rate drops after a prompt, model, tool or context change;
- retries increase materially;
- cost per successful outcome increases materially;
- human correction time increases;
- context size grows without a quality benefit;
- cache-hit share drops unexpectedly for a stable workload;
- wrong-tool selections increase;
- a multi-agent workflow adds handoff failures;
- critical actions occur without the expected approval trail;
- a new executor cannot reproduce the intended workflow.

Compare against the workflow's baseline rather than applying a universal fixed threshold.

## Related Nodes

- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`

## Final Rule

Judge agents by useful, repeatable and explainable outcomes.

Use the smallest sufficient architecture.

Measure quality before optimizing cost.

Do not confuse complexity with professionalism.