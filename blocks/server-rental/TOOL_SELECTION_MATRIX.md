# Tool Selection Matrix

## Purpose

Provide a reusable decision matrix for selecting rented compute.

## Selection Dimensions

Evaluate:

- workload type;
- required GPU VRAM;
- expected runtime;
- burst versus continuous usage;
- region;
- billing granularity;
- stop and resume behavior;
- persistent-volume cost;
- network egress cost;
- Docker support;
- API exposure;
- ComfyUI suitability;
- open-source LLM suitability;
- video-generation suitability;
- account and payment restrictions;
- compliance requirements;
- reliability and capacity risk.

## Workload Matrix

| Workload | Preferred Runtime Pattern | Primary Selection Metric |
|---|---|---|
| Lightweight orchestration | cheap always-on VPS | monthly baseline cost |
| Short open-source LLM tests | temporary GPU worker | cheapest sufficient VRAM |
| Persistent owner-controlled LLM API | persistent GPU endpoint or warm worker | cost per useful request plus uptime |
| Video generation experiments | temporary GPU worker | cost per generated minute |
| Video production batch | parallel temporary GPU workers | throughput per dollar |
| China-focused research | mainland China research node | local IP and access behavior |
| Cross-border China access | Hong Kong node | access balance and simplicity |
| Sensitive private workload | controlled private runtime | security and data handling |

## Economic Comparison Modes

Compare:

1. SaaS interface cost per generated unit;
2. provider API cost per generated unit;
3. rented-server compute cost per generated unit;
4. persistent storage cost;
5. data-transfer cost;
6. idle-time cost;
7. warm-start and setup overhead;
8. operational labor when relevant.

## Initial Provider Categories To Research

### Low-Cost GPU Marketplaces

- Vast.ai
- RunPod
- TensorDock
- similar marketplaces discovered during research

### GPU Clouds And Serverless GPU Providers

- Lambda
- Modal
- Replicate
- Baseten
- Beam
- Fal
- Hyperbolic
- similar providers discovered during research

### Major Clouds

- AWS
- Google Cloud
- Microsoft Azure
- Oracle Cloud

### Mainland China And China-Focused Options

- AutoDL
- Alibaba Cloud
- Tencent Cloud
- Huawei Cloud
- additional local providers discovered during research

### Regional Nodes

- mainland China
- Hong Kong
- United States
- Europe when useful

## Status

This matrix is a structural template. Provider pricing and availability must be filled through dated research artifacts and refreshed before purchase decisions.
