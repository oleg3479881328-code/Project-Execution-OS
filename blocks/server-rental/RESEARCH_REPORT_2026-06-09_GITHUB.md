# Server Rental GitHub Research Report — 2026-06-09

## Scope

This report covers GitHub-based research for reusable server-rental and cloud-GPU infrastructure patterns relevant to Project Execution OS.

The goal is not to identify current prices. GitHub is suitable for discovering implementation donors, official SDKs, deployment templates, and reusable architectural patterns.

## Confirmed Official Donors

### 1. RunPod Official ComfyUI Serverless Worker

Repository:

- `runpod-workers/worker-comfyui`
- https://github.com/runpod-workers/worker-comfyui

Confirmed capabilities from the official README:

- runs ComfyUI workflows as a RunPod serverless API endpoint;
- accepts workflow JSON through API calls;
- supports synchronous and asynchronous execution;
- exposes standard endpoints such as `/run`, `/runsync`, and `/health`;
- supports result return as base64 or S3 URLs;
- supports S3 upload through environment variables;
- provides Docker images;
- provides deployment, configuration, customization, development, and CI/CD guides;
- allows SSH access when configured;
- accepts ComfyUI workflow export in API JSON format.

Implication:

For image and video pipelines built in ComfyUI, Project Execution OS does not need to invent a serverless worker from scratch. This repository is the strongest implementation donor found for the media path.

### 2. RunPod Official Python SDK

Repository:

- `runpod/runpod-python`
- https://github.com/runpod/runpod-python

Confirmed capabilities from the official README:

- official RunPod API and SDK library;
- custom serverless worker creation;
- local worker testing;
- startup fitness checks;
- endpoint execution through sync and async methods;
- GraphQL wrapper;
- pod lifecycle control;
- create pod;
- stop pod;
- resume pod;
- terminate pod.

Implication:

The minimal orchestration layer can be built using the official SDK. The system can dispatch jobs and control GPU lifecycle without implementing low-level provider integration from scratch.

### 3. vLLM Official Repository

Repository:

- `vllm-project/vllm`
- https://github.com/vllm-project/vllm

Confirmed capabilities from the official README:

- LLM inference and serving library;
- OpenAI-compatible API server;
- Anthropic Messages API and gRPC support;
- continuous batching;
- prefix caching;
- chunked prefill;
- quantization support including FP8, INT8, INT4, GPTQ, AWQ, GGUF, and others;
- distributed inference parallelism;
- streaming output;
- tool calling and reasoning parsers;
- support for 200+ model architectures;
- support for model families including Llama, Qwen, Gemma, Mixtral, DeepSeek-V3, Qwen-MoE, Qwen3.5, multimodal models, embedding models, and more;
- support for NVIDIA, AMD, CPU, and additional hardware plugins including Huawei Ascend.

Implication:

For the LLM savings layer, vLLM is the primary reusable serving donor. An owner-controlled open-source model endpoint can expose an OpenAI-compatible interface and sit between Project Execution OS and premium APIs.

### 4. Modal Official Examples

Repository:

- `modal-labs/modal-examples`
- https://github.com/modal-labs/modal-examples

Confirmed capabilities from the official README:

- official examples for Modal;
- local scripts communicate with Modal and spawn serverless containers on demand in the cloud;
- guided examples across multiple capability categories;
- Python-oriented execution model.

Implication:

Modal is a strong donor for ephemeral serverless execution patterns. It is particularly relevant when custom Python workloads should scale from zero without operating a persistent GPU VM.

## Secondary Donors And Community Repositories

### RunPod ComfyUI Community Templates

Search results identified additional repositories such as:

- `ashleykleynhans/runpod-worker-comfyui`
- `Dekita/runpod-serverless-comfyui-worker`
- `Weixuanf/runpod-ns-worker-comfyui`
- `artokun/comfyui-runpod-serverless`
- `metebalci/ComfyUI-RunOnRunpod`

Use these only as supplementary donors. Prefer the official `runpod-workers/worker-comfyui` repository as the default reference implementation.

### Vast.ai Community Clients

Search results identified several community clients and automation stubs, including:

- `eldjarn/vastai_client`
- `Barahlush/vastai_client` archived
- `HammadRafique29/vastai_automate`

No equally mature official Vast.ai orchestration donor was identified through the available GitHub search.

Implication:

Vast.ai remains attractive as a low-cost compute marketplace candidate, but its automation path should be treated as a separate integration task. It is not the preferred first orchestration donor.

## Architecture Result

### Recommended Media Path

`client -> head node or direct request -> RunPod serverless endpoint -> official worker-comfyui -> ComfyUI workflow -> S3-compatible output storage`

Use when:

- image generation;
- video generation through ComfyUI nodes;
- media batch processing;
- API-driven workflows;
- serverless economics are preferable to persistent pods.

### Recommended LLM Path

`client or Project Execution OS -> authenticated endpoint -> rented GPU worker -> vLLM -> open-source model -> OpenAI-compatible response`

Use when:

- routing cheap tasks away from premium APIs;
- hosting private open-source models;
- model swapping;
- continuous batching matters;
- OpenAI-compatible integration reduces application changes.

### Recommended Provider-Lifecycle Path

`head node -> provider SDK -> create pod or serverless request -> fitness checks -> execute job -> upload output -> stop or terminate worker -> log cost`

Use the official RunPod SDK as the first implementation donor.

### Recommended Serverless Experiment Path

`local terminal -> Modal script -> serverless cloud container -> result`

Use Modal as a parallel experiment for custom Python jobs where zero-to-one deployment speed matters.

## Decision: What To Build First

### Phase 1: Video Validation

Use:

- RunPod;
- official `runpod-workers/worker-comfyui`;
- one selected ComfyUI-compatible open-source video model;
- S3-compatible storage;
- one benchmark workload;
- per-job cost logging.

Do not build custom pod orchestration first if the serverless worker is sufficient.

### Phase 2: LLM Savings Endpoint

Use:

- rented GPU;
- official vLLM;
- OpenAI-compatible endpoint;
- one open-source model;
- authenticated private access;
- benchmark against DeepSeek API and premium APIs.

### Phase 3: Hybrid Head Node

Build only after Phase 1 and Phase 2 validate economics.

Responsibilities:

- queue jobs;
- route between commercial API, RunPod serverless, persistent pod, and vLLM endpoint;
- collect cost logs;
- shut down idle workers;
- preserve output metadata;
- maintain provider-agnostic interfaces.

## What Not To Build Yet

Do not prematurely build:

- a full multi-provider abstraction layer;
- custom Vast.ai orchestration;
- Kubernetes;
- complex Celery clusters;
- multi-region deployment;
- China production hosting;
- custom autoscaling beyond one validated workflow.

## Provider Research Boundary

GitHub research cannot establish current provider pricing, billing granularity, or regional availability. Those values must come from official pricing pages or live provider consoles.

## Canonical Recommendation

The strongest immediate implementation route is:

`RunPod Serverless + official worker-comfyui + ComfyUI workflow + S3-compatible storage`

for media experiments, and:

`rented GPU + vLLM OpenAI-compatible server`

for the LLM savings layer.

These are proven donor-first routes and should be preferred over designing new infrastructure from scratch.
