# Patterns

## Terminal-First Pattern

Treat the owner's laptop as a control surface rather than a fixed compute ceiling.

Use:

`laptop -> secure remote access -> rented runtime -> result review`

## Burst GPU Pattern

Use for workloads that occur intermittently.

Sequence:

`prepare job -> start GPU worker -> process queue -> export results -> shut down worker`

## Warm Storage Pattern

Use when model weights are large and reused frequently.

Keep:

- persistent storage;
- cached model weights;
- reproducible container image;
- lightweight control metadata.

Avoid paying for an idle GPU when only storage is needed.

## Routing Layer Pattern

Use a small always-on control node to select execution mode:

- SaaS;
- provider API;
- owner-controlled model endpoint;
- local execution;
- temporary GPU worker;
- regional research node.

## Scale-Out Pattern

When a batch is parallelizable, compare one large worker against several smaller workers.

Do not assume the most expensive GPU is automatically the cheapest path per completed batch.

## Region-Specific Node Pattern

Use a region-specific server when IP geography affects access, search visibility, latency, or compliance.

Keep this separate from the compute-optimization decision when possible.

## Evidence-First Pricing Pattern

Before recommending a provider, record:

- date checked;
- GPU model;
- VRAM;
- hourly rate;
- billing minimum;
- storage cost;
- egress cost;
- stop behavior;
- capacity availability;
- signup and payment restrictions.

## Swap-Friendly Model Pattern

Separate:

- model choice;
- inference server;
- GPU profile;
- provider;
- region.

This allows changing one layer without rebuilding the whole system.
