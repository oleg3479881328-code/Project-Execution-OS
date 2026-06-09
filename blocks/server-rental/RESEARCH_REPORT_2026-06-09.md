# Server Rental Research Report — 2026-06-09

## Purpose

Explain why the Server Rental Block exists and preserve the initial architecture conclusion before deeper market research.

## Confirmed Internal Insight

The owner's workload spans AI video generation, open-source LLM evaluation, agent systems, coding workflows, research infrastructure, and Project Execution OS orchestration.

A local laptop or desktop should not be treated as the default compute ceiling.

The correct default question is:

`What compute profile is sufficient and cheapest for the workload?`

Not:

`What can be forced to fit on local hardware?`

## Initial Architecture Conclusion

Use a hybrid compute strategy:

- laptop as terminal and control surface;
- cheap always-on VPS for orchestration where useful;
- commercial APIs when they are economically justified;
- rented GPU workers for heavy open-source workloads;
- temporary parallel workers for batches;
- regional nodes when geography matters;
- automatic shutdown of expensive workers after use.

## Why This Matters

This model improves:

- flexibility;
- scaling;
- model choice;
- experimentation speed;
- cost control;
- avoidance of local-hardware lock-in;
- ability to swap GPU generations and providers;
- ability to choose compute by workload.

## Key Use Cases

### Video Generation

Compare:

- hosted SaaS generation;
- provider API generation;
- open-source model on rented GPU;
- parallel GPU workers for batch production.

Measure cost per generated minute and cost per finished hour.

### Open-Source LLM Cost Layer

Do not restrict candidate models to the owner's laptop.

Compare:

- local execution;
- direct API;
- owner-controlled model endpoint on rented GPU;
- hybrid routing with premium fallback.

### China Research

Use mainland China or Hong Kong nodes when local IP presence changes information visibility, access behavior, or market research quality.

## Important Correction

The system previously focused too narrowly on fitting open-source models to local hardware. That was an incomplete framing.

Future recommendations must proactively surface rented compute and hybrid routing whenever they may be materially better.

## Research Still Required

This report does not claim that any specific provider is best.

Current, cited research is still required for:

- provider pricing;
- GPU availability;
- billing granularity;
- storage costs;
- egress costs;
- stop and resume behavior;
- serverless GPU options;
- US provider comparison;
- mainland China provider comparison;
- Hong Kong comparison;
- account and payment restrictions;
- model requirements;
- model licenses;
- real deployment economics.

## Status

Initial architecture insight captured.

Deep external provider research and hands-on validation remain open.
