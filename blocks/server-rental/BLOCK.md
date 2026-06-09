# Server Rental Block

## Purpose

Provide a reusable Project Execution OS domain layer for renting servers and cloud compute on demand, with special focus on GPU workloads, AI video generation, open-source LLM inference, agent workloads, hybrid routing, geographic-region selection, and cost optimization.

This block exists to prevent local hardware from becoming an accidental architectural constraint.

## Status

`candidate`

This block has been created from a captured architectural insight and must now be expanded through current, cited market research and validation.

## Core Principle

Treat compute as a selectable runtime resource, not as a permanent local-hardware constraint.

Start from:

`task -> workload profile -> required compute -> provider/region selection -> rented runtime -> shutdown after use`

Do not start from:

`what fits on the owner's laptop`

## When To Use

Use this block for:

- server rental;
- VPS and cloud server selection;
- GPU instance rental;
- pay-as-you-go compute;
- serverless GPU;
- AI video generation infrastructure;
- open-source LLM inference hosting;
- owner-controlled API endpoints;
- ComfyUI deployment;
- temporary high-powered compute;
- always-on low-cost orchestration nodes;
- mainland China, Hong Kong, United States, or international server-region selection;
- cost comparison between SaaS, API, and rented infrastructure;
- workload routing between local, API, and rented compute;
- elastic scaling up, down, and sideways;
- Project Execution OS infrastructure decisions.

## When Not To Use

Do not use this block for:

- buying laptops, desktops, or physical GPU rigs unless explicitly comparing ownership versus rental;
- application-level product architecture unrelated to hosting;
- unsafe, unlawful, abusive, or evasive infrastructure usage;
- credential storage;
- private API keys;
- provider-account secrets.

## Default Decision Model

Evaluate at least these execution modes:

1. commercial SaaS interface;
2. direct provider API;
3. open-source model on rented GPU;
4. cheap always-on control server plus temporary GPU workers;
5. local execution only when it is genuinely advantageous.

## Compute Profiles

### Lightweight Control Node

Use for:

- orchestration;
- queues;
- scheduling;
- monitoring;
- routing;
- low-cost text processing;
- API gateway duties.

### Temporary GPU Worker

Use for:

- open-source LLM inference;
- video generation;
- image generation;
- batch processing;
- model evaluation;
- temporary heavy workloads.

### Parallel Worker Pool

Use when throughput matters more than single-machine power.

Examples:

- multiple video clips in parallel;
- bulk prompt execution;
- batch inference;
- model benchmarking.

### Geographic Research Node

Use when local IP or regional internet visibility matters.

Examples:

- mainland China research;
- Hong Kong cross-border access;
- US-region access;
- provider-specific or market-specific testing.

## Required Reading Inside This Block

Smallest useful path:

1. `BLOCK.md`
2. `READY_SOLUTIONS.md`
3. `TOOL_SELECTION_MATRIX.md`
4. `PATTERNS.md`
5. `SECURITY_AND_COMPLIANCE.md`
6. `VALIDATION_BACKLOG.md`
7. `REFERENCES.md`
8. latest `RESEARCH_REPORT_<date>.md`

Do not load every file by default. Load only the files relevant to the active workload.

## Typical Outputs

- provider shortlist;
- server-selection decision;
- GPU-instance recommendation;
- US versus China versus Hong Kong comparison;
- SaaS versus API versus rented-server economics;
- open-source video deployment route;
- open-source LLM deployment route;
- owner-controlled API route;
- hybrid orchestration architecture;
- cost model;
- validation plan;
- implementation handoff.

## Boundary

This block stores reusable infrastructure knowledge only.

Do not store API keys, passwords, billing credentials, private SSH keys, or provider-account secrets.

Keep unstable provider pricing, GPU availability, platform restrictions, sanctions exposure, and payment limitations in dated research artifacts and references.

## Final Rule

Select compute for the workload. Do not distort the workload to fit accidental local constraints.
