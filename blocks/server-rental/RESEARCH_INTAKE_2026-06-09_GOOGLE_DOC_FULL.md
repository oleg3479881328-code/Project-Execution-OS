# Server Rental Research Intake — Google Doc Full — 2026-06-09

## Source

Uploaded Google Docs snapshot: `Облачные GPU для AI: Стратегия Аренды`

Original document ID: `1M8Ihfg0iFB6H4HvZtxiDJ8uuJzmYYsDBhnbBmpDdUXI`

## Intake Status

`full text extracted from uploaded snapshot`

This intake preserves the second external research report for comparison and later verification. It is not yet canonical provider truth.

## Strong Findings Worth Preserving

### Hybrid Runtime Architecture

The report independently converges on the same architecture:

- laptop as thin terminal;
- cheap always-on VPS as orchestration node;
- API routing for low-volume or latency-sensitive jobs;
- temporary GPU workers for batch workloads;
- external object storage;
- automatic shutdown after idle time;
- per-job cost logging;
- provider and GPU selection by workload.

### Useful Provider Shortlist

International and US-facing:

- RunPod
- Vast.ai
- Lambda Labs
- TensorDock
- Modal
- Spheron
- Replicate
- Baseten
- Fal
- Beam
- Hyperbolic
- AWS
- Google Cloud
- Azure
- Oracle

China and Asia track:

- AutoDL
- Alibaba Cloud
- Tencent Cloud
- Huawei Cloud
- Hong Kong as a separate operational region

### Useful GPU Profiles

The report identifies these profiles as worth testing:

- RTX 4090: cheap media worker and small-model inference
- RTX 5090: stronger single-card media worker
- RTX A6000: 48GB compatibility worker
- L40S: 48GB inference-focused worker
- A100 80GB: heavy compatibility worker
- H100 SXM: premium throughput worker
- H200 SXM: very large-model worker
- B200: frontier-only worker
- H20: China-specific memory-heavy profile

### Useful Video Model Shortlist

- Wan 2.1 14B
- Wan 2.1 1.3B
- Hunyuan Video
- LTX Video
- SkyReels
- JoyAI-Echo
- Mochi 1
- CogVideoX
- Stable Video Diffusion

### Useful LLM Routing Idea

Use three model classes:

- lightweight router/parser model;
- midrange agent and coding model;
- premium API for frontier reasoning or very large MoE models.

The report correctly reinforces that a self-hosted endpoint is a routing layer, not a universal replacement for APIs.

## Practical Stack Suggested By The Report

Potential implementation stack:

- Docker
- NVIDIA Container Toolkit
- ComfyUI CLI or Comfy API
- FFmpeg
- vLLM
- Celery
- Redis
- Cloudflare R2 or another S3-compatible object store
- Prometheus
- Grafana
- nvidia-smi exporter
- provider API lifecycle controller
- per-job cost logger

## Important Errors And Caution Flags

Do not treat the following as canonical without primary-source verification:

### Provider Pricing

All provider prices are volatile. Marketplace values, spot values, on-demand values, and serverless effective prices must be separated.

### AWS H100 Figure

The report cites `AWS P5 H100: $12.29/hour` without clarifying whether this is per GPU or per instance. AWS P5 instances commonly bundle multiple GPUs, so the unit must be verified before comparison.

### Cloudflare R2 Wording

The report states `$0 Egress Fee` as an absolute. Verify current storage, request, and egress rules before treating R2 as the default.

### China Compliance Wording

The report overstates the rule as if any public API in mainland China necessarily requires ICP filing and as if ICP filing is available only to Chinese legal entities. Actual applicability depends on hosting model, domain, provider, account type, and public-web usage. Verify official Alibaba, Tencent, and Huawei documentation.

### Hugging Face In Mainland China

The report says Hugging Face is blocked. Treat this as an operational hypothesis requiring testing, not as a universal permanent fact.

### Video Economics

The report gives exact costs per generated minute for multiple models. These are not reliable until benchmark conditions are recorded:

- model revision;
- precision or quantization;
- GPU;
- resolution;
- frame count;
- steps;
- text-to-video or image-to-video;
- cold or warm start;
- interpolation;
- upscale;
- audio generation;
- post-processing.

### JoyAI-Echo Economics

The report states JoyAI-Echo can cost `$0.054/minute` and `$3.24/hour`. This is not supported by an absolute official generation-speed benchmark. Preserve only as an unverified estimate.

### JoyAI-Echo License

The report labels JoyAI-Echo as requiring commercial authorization from LTX. The official JoyAI-Echo README must remain the authoritative source. The available public release is constrained for non-commercial research use unless permissions are obtained.

### Wan Repository Path

The report references `Wan-Video/Wan2.1`. Verify the official current repository and model-card path before canonical storage.

### LTX Video Version And License

The report references `LTX-2.3` and a paid commercial-license requirement. Verify exact current version and license text against the official repository before use.

### SkyReels Version

The report references SkyReels V3 and links a general repository. Verify the exact current release, model card, license, and infrastructure requirements.

### Qwen 3.5 And DeepSeek V3.2

The report references Qwen 3.5 and DeepSeek V3.2. These are temporally unstable and must be verified from official sources before entering the canonical LLM shortlist.

### vLLM Version

The report cites vLLM `0.7+`. Version recommendations must be refreshed from official vLLM documentation before implementation.

### Autoscaling Logic

The idle-shutdown rule based only on `nvidia-smi` at 0% for 10 minutes is insufficient by itself. It must also check:

- queue state;
- active job state;
- upload state;
- retry state;
- model-loading state;
- provider billing granularity.

## Economic Simulation Preserved As Hypothesis

The report models:

- SaaS: `$1.80/minute`
- commercial API: `$0.60/minute`
- rented GPU: approximately `$0.14/minute`

This is useful as a scenario model, but not a verified market comparison. It should be re-run with current official SaaS/API prices and measured rented-GPU benchmarks.

## Canonical Lessons To Merge

- Build provider-agnostic orchestration.
- Separate head node, GPU workers, and object storage.
- Add lifecycle automation and cost logging from day one.
- Route low-volume work to API and batch work to rented GPU when economics support it.
- Maintain separate US/international and mainland-China/Hong-Kong tracks.
- Benchmark cost per generated minute instead of guessing from hourly rates.
- Keep provider prices in dated research artifacts, not permanent block prose.

## Next Validation Work

1. Verify provider pricing from official pages.
2. Verify current GPU inventory and billing units.
3. Verify official model repositories and licenses.
4. Run one measured Wan-family video benchmark on a rented GPU.
5. Run one measured open-source LLM endpoint benchmark with vLLM.
6. Test one head-node plus worker lifecycle flow.
7. Verify mainland-China signup, payment, and public-hosting rules from official provider documentation.
