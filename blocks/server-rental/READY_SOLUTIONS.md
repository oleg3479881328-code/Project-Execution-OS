# Ready Solutions

## Purpose

Store reusable deployment routes for server-rental decisions.

## Route A: Cheap Always-On Control Node

Use when a lightweight server must stay online continuously.

Typical duties:

- queues;
- schedulers;
- routing;
- webhooks;
- monitoring;
- API gateway;
- agent coordination;
- job dispatch to temporary workers.

Preferred shape:

- low-cost VPS;
- modest CPU and RAM;
- persistent disk;
- Docker;
- secure remote access;
- no expensive GPU unless continuously justified.

## Route B: Temporary GPU Worker

Use when a heavy model is needed only for a bounded task.

Typical duties:

- video generation;
- open-source LLM inference;
- image generation;
- benchmarks;
- batch jobs;
- experimentation.

Preferred shape:

- pay-as-you-go GPU instance;
- persistent volume when model weights are reused;
- containerized environment;
- automatic shutdown after queue completion;
- cost logging per job.

## Route C: Video Generation Worker

Use for open-source video models.

Preferred shape:

- GPU selected by VRAM and model requirements;
- NVMe storage for model weights and temporary media;
- FFmpeg;
- ComfyUI or model-specific API server when useful;
- queue-based execution;
- output export to durable storage;
- worker shutdown after batch completion.

## Route D: Owner-Controlled LLM Endpoint

Use when an open-source model should sit between premium APIs and low-value workloads.

Preferred shape:

- rented GPU;
- open-source inference server;
- authenticated private endpoint;
- routing rules by task type;
- fallback to premium APIs;
- cost and quality logging;
- ability to swap model and GPU profile independently.

## Route E: Parallel Batch Pool

Use when throughput matters.

Preferred shape:

- multiple temporary workers;
- queue;
- idempotent jobs;
- per-worker health checks;
- result collection;
- automatic scale-down after queue exhaustion.

## Route F: Mainland China Research Node

Use when Chinese IP presence and local information visibility matter.

Preferred shape:

- mainland China region when local-network visibility is required;
- Hong Kong only when mainland presence is not necessary;
- browser and automation tooling;
- translation layer;
- Baidu, Bilibili, Gitee, and local-service research workflows;
- explicit compliance review before public hosting.

## Route G: Hybrid Project Execution OS Compute Routing

Use as the long-term system pattern.

Preferred shape:

`laptop terminal -> control node -> task router -> API or temporary worker -> durable result store -> shutdown`

Routing logic should compare:

- latency;
- price;
- model quality;
- data sensitivity;
- workload size;
- region;
- setup reuse;
- expected runtime.
