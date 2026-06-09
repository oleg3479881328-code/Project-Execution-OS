# Cloud Compute On-Demand Strategy

Status: captured architecture insight
Date: 2026-06-09

## Context

The owner identified a major architectural correction for AI-heavy project work: do not design around the limits of local laptop or desktop hardware by default. For many workloads, local hardware should be treated as a terminal and control surface, while compute is rented on demand.

This insight applies across video generation, open-source LLM testing, agent orchestration, coding assistants, research infrastructure, and Project Execution OS cost optimization.

## Core Decision

Default to evaluating cloud compute on demand before adapting a solution to local hardware.

Do not begin with:

`What model fits on the owner's laptop?`

Begin with:

`What model best fits the task, and what rented compute profile is cheapest and sufficient for running it?`

## Strategic Model

The owner's laptop or desktop can primarily serve as:

- browser and terminal;
- VS Code workstation;
- remote-control surface;
- result-review interface;
- orchestration console.

Heavy compute can be externalized to:

- commercial APIs;
- rented GPU instances;
- temporary servers with open-source models;
- cheap always-on control servers;
- geographically specialized nodes, such as mainland China research nodes.

## Compute Ladder

Use a layered routing model:

1. commercial SaaS interface when speed of validation matters;
2. provider API when automation matters;
3. rented GPU with an open-source model when lower marginal cost or control matters;
4. cheap always-on control server for orchestration;
5. larger or multiple GPU instances only when the workload requires them;
6. shut down expensive GPU capacity immediately after the workload completes.

## Scaling Principle

Cloud compute is elastic in both directions.

Use:

- a cheap small server for lightweight text processing and orchestration;
- a larger GPU for a temporary heavy model test;
- multiple parallel GPU workers for a video batch;
- a different GPU generation when a specific model requires it;
- no active GPU at all when there is no heavy workload.

This avoids fixed-capacity lock-in.

## Video Generation Implication

For AI video production, compare three paths as separate economic modes:

1. hosted generation service such as Kling-like products;
2. direct video-generation API;
3. open-source video model deployed on a rented GPU server.

Evaluate the cost per generated minute and per finished hour. Do not assume the hosted service is automatically the correct default for scale.

## Open-Source LLM Implication

For cost-saving layers between premium APIs and coding agents, do not restrict the model search to what fits on the owner's local hardware.

Evaluate:

- local deployment only when it is genuinely advantageous;
- rented GPU inference for larger open models;
- an owner-controlled API endpoint backed by a rented model;
- workload routing so cheap operations are handled by lower-cost models and premium APIs are reserved for tasks that justify them.

The correct abstraction is not necessarily `local model`.

It is often:

`owner-controlled model endpoint on rented compute`.

## Operational Principle

Treat compute as a selectable runtime resource, not as a permanent hardware constraint.

Build and maintain a reusable catalogue containing:

- provider;
- region;
- GPU type;
- VRAM;
- hourly rate;
- billing granularity;
- stop and resume behavior;
- persistent-storage cost;
- Docker support;
- ComfyUI suitability;
- open-source LLM suitability;
- video-generation suitability;
- API exposure options;
- payment and account restrictions;
- geographic-access value.

## Research Direction

Perform a dedicated infrastructure comparison across:

- United States and international GPU-rental providers;
- mainland China providers;
- Hong Kong options;
- major clouds;
- low-cost GPU marketplaces;
- serverless GPU providers;
- open-source video-model deployment patterns;
- open-source LLM deployment patterns.

## Decision Rule For Future Recommendations

Whenever the owner is evaluating an AI workload, proactively compare:

- local execution;
- provider API;
- rented server execution;
- hybrid routing.

Do not silently assume local hardware is the baseline.

## Lesson Learned

The system failed to surface this option early enough during local-model discussions. Future recommendations must actively flag a better infrastructure path when one is visible, even when the owner initially asks about a narrower implementation route.

## Next Research Task

Create a current, cited provider and model matrix for:

- video generation;
- open-source LLM inference;
- agent workloads;
- China research nodes;
- hybrid Project Execution OS compute routing.
