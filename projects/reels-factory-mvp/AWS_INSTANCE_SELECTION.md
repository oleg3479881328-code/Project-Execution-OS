# AWS Instance Selection — Reels Factory MVP Smoke Test

Date: 2026-06-10 (corrected)
Region: us-east-2 (Ohio)
Author: Infrastructure executor

## Constraint Summary

| Constraint | Value |
|---|---|
| Max vCPU (G and VT quota) | 4 |
| Available AWS credits | $74.57 |
| Credit expiration | 2026-10-04 |
| Workload | Single 3-second 480p Wan I2V generation |
| Wan I2V model | **Wan2.1-I2V-14B-480P** (only I2V variant available) |

## Important Correction: No I2V-1.3B Model Exists

After verifying the official Wan2.1 repository (https://github.com/Wan-Video/Wan2.1), the available models are:

| Model | Type | VRAM Estimate |
|---|---|---|
| T2V-1.3B | Text-to-Video | ~8 GB |
| T2V-14B | Text-to-Video | ~20+ GB |
| **I2V-14B-480P** | **Image-to-Video** | **~18-22 GB** |
| I2V-14B-720P | Image-to-Video | ~22-26 GB |
| FLF2V-14B | First-Last-Frame-to-Video | ~20+ GB |

**There is no I2V-1.3B model.** The smallest I2V model is 14B. This changes the instance selection calculus significantly.

## Candidates Compared

| Instance | vCPU | GPU | GPU VRAM | RAM | Local Storage | On-Demand Price (us-east-2) |
|---|---|---|---|---|---|---|
| **g4dn.xlarge** | 4 | T4 | **16 GB** | 16 GB | 125 GB NVMe | **$0.526/hr** |
| g5.xlarge | 4 | A10G | 24 GB | 16 GB | 250 GB NVMe | $1.006/hr |
| g6.xlarge | 4 | L4 | 24 GB | 16 GB | EBS only | ~$0.70/hr (est.) |

## VRAM Analysis for I2V-14B-480P

The I2V-14B model requires approximately 18-22 GB VRAM at FP16 for 480p generation.

**g4dn.xlarge (16 GB VRAM):**
- ❌ Insufficient for FP16 I2V-14B at full precision
- ⚠️ **May work with FP8 quantized models** — the ComfyUI-WanVideoWrapper supports FP8 scaled models from Kijai (https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled)
- ⚠️ **May work with block swapping** — the wrapper supports offloading blocks to system RAM. With 20/40 blocks offloaded, VRAM usage drops to ~12-14 GB
- **Verdict:** Possible but unvalidated. Risk of OOM or very slow generation due to swapping.

**g5.xlarge (24 GB VRAM):**
- ✅ Sufficient for FP16 I2V-14B-480P
- ✅ A10G is ~1.5-2x faster than T4 for inference
- ❌ Costs $1.006/hr — nearly 2x g4dn
- **Verdict:** Safe choice, but expensive for a smoke test.

**g6.xlarge (24 GB VRAM):**
- ✅ Sufficient VRAM
- ✅ L4 is more power-efficient than A10G
- ❌ No local NVMe storage (EBS only)
- **Verdict:** Good middle ground if available.

## Recommendation

### First Launch Candidate: g5.xlarge

**Why:** The I2V-14B model is the only I2V option. g4dn.xlarge (16 GB VRAM) may not be sufficient for reliable FP16 inference. g5.xlarge (24 GB VRAM) provides headroom and is the safest first choice.

**Cost impact:** At $1.006/hr, a 2-hour test costs ~$2.01 — still well within the $74.57 credit budget.

### Alternative: Try g4dn.xlarge with FP8 first

If the owner wants to minimize cost, try g4dn.xlarge with:
- FP8 quantized model from Kijai (https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled)
- Block swapping enabled (offload 20-30 blocks to RAM)
- Reduced resolution (640x360 instead of 854x480)

If this fails (OOM or too slow), terminate and relaunch on g5.xlarge.

## Quota Validation

- Quota name: `Running On-Demand G and VT instances`
- Quota code: `L-DB2E81BA`
- Applied limit: **4 vCPU**
- g4dn.xlarge / g5.xlarge / g6.xlarge all use: **4 vCPU**
- Utilization after launch: **4 / 4 (100%)**
- Result: **Fits exactly.** No other G-family instances can run simultaneously.

## Pricing Breakdown

| Instance | Compute/hr | EBS/hr | IPv4/hr | Total/hr | 2hr test |
|---|---|---|---|---|---|
| g4dn.xlarge | $0.526 | $0.0033 | $0.005 | ~$0.534 | ~$1.07 |
| **g5.xlarge** | **$1.006** | **$0.0033** | **$0.005** | **~$1.014** | **~$2.03** |
| g6.xlarge | ~$0.70 | $0.0033 | $0.005 | ~$0.708 | ~$1.42 |

## Charges After Stop/Terminate

| Resource | After Stop | After Terminate |
|---|---|---|
| Compute | Stopped (no charge) | Removed |
| EBS root volume | Charged (~$2.40/month for 30GB) | Removed (if DeleteOnTermination=true) |
| Public IPv4 | Released (no charge) | Released |
| Local NVMe storage | Data persists (charged via instance) | Lost |

## Storage Recommendation

**Minimum: 50 GB gp3 root volume** (not 30 GB)

The Deep Learning AMI GPU PyTorch (~15 GB) + ComfyUI + dependencies + pip caches + model weights (I2V-14B is ~30 GB) + temporary output files can easily exceed 30 GB.

Recommended: **50 GB gp3** (costs ~$4/month or $0.0055/hr — negligible).

## Direct Links

- EC2 Launch: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- g4dn.xlarge pricing: https://aws.amazon.com/ec2/pricing/on-demand/
- g5.xlarge pricing: https://aws.amazon.com/ec2/pricing/on-demand/
- ComfyUI: https://github.com/comfyanonymous/ComfyUI
- ComfyUI-WanVideoWrapper: https://github.com/kijai/ComfyUI-WanVideoWrapper
- Wan2.1 GitHub: https://github.com/Wan-Video/Wan2.1
- Wan models (official): https://huggingface.co/Wan-AI
- WanVideo ComfyUI models (Kijai): https://huggingface.co/Kijai/WanVideo_comfy
- WanVideo FP8 scaled (Kijai): https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
