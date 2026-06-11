# AWS Instance Selection — Reels Factory MVP Smoke Test

Date: 2026-06-10
Region: us-east-2 (Ohio)
Author: Infrastructure executor

## Constraint Summary

| Constraint | Value |
|---|---|
| Max vCPU (G and VT quota) | 4 |
| Available AWS credits | $74.57 |
| Credit expiration | 2026-10-04 |
| Workload | Single 3-second 480p Wan I2V generation |
| GPU VRAM required (Wan I2V 1.3B 480p) | ~6-8 GB |
| GPU VRAM required (Wan I2V 14B 480p) | ~18-20 GB |

## Candidates Compared

| Instance | vCPU | GPU | GPU VRAM | RAM | Local Storage | On-Demand Price (us-east-2) |
|---|---|---|---|---|---|---|
| **g4dn.xlarge** | 4 | T4 | **16 GB** | 16 GB | 125 GB NVMe | **$0.526/hr** |
| g5.xlarge | 4 | A10G | 24 GB | 16 GB | 250 GB NVMe | $1.006/hr |
| g6.xlarge | 4 | L4 | 24 GB | 16 GB | EBS only | ~$0.70/hr (est.) |

## Recommendation: g4dn.xlarge

**Why g4dn.xlarge is the best choice for the first smoke test:**

1. **Fits the 4 vCPU quota** — all three candidates fit, but g4dn is cheapest.
2. **16 GB VRAM is sufficient** — Wan I2V 1.3B (the smallest practical I2V variant) requires ~6-8 GB VRAM at 480p. Even the larger 14B variant fits in 16 GB at 480p with optimizations (FP16, tiling).
3. **Lowest hourly cost** — $0.526/hr is ~48% cheaper than g5.xlarge and ~25% cheaper than g6.xlarge.
4. **Local NVMe storage included** — 125 GB is enough for ComfyUI, Wan model weights (~5-10 GB), and temporary output files.
5. **T4 GPU is well-supported** — ComfyUI and PyTorch have mature T4/CUDA support. Community ComfyUI/Wan workflows are tested on T4.
6. **Proven for ComfyUI** — g4dn.xlarge is the most common "entry-level" GPU instance for ComfyUI in the AWS ecosystem.

**When to consider g5.xlarge instead:**
- If the 14B Wan model is needed and FP16 doesn't fit in 16 GB.
- If generation speed is critical (A10G is ~1.5-2x faster than T4 for inference).
- For the first 3-second 480p smoke test, g4dn.xlarge is sufficient.

## Quota Validation

- Quota name: `Running On-Demand G and VT instances`
- Quota code: `L-DB2E81BA`
- Applied limit: **4 vCPU**
- g4dn.xlarge uses: **4 vCPU**
- Utilization after launch: **4 / 4 (100%)**
- Result: **Fits exactly.** No other G-family instances can run simultaneously.

## Pricing Breakdown (g4dn.xlarge, us-east-2, Linux)

| Component | Price |
|---|---|
| Compute (On-Demand) | $0.526/hr |
| EBS root volume (30 GB gp3) | ~$2.40/month ($0.0033/hr) |
| Public IPv4 | $0.005/hr |
| **Total hourly (running)** | **~$0.534/hr** |
| **Estimated 1-hour test** | **~$0.53** |
| **Estimated 2-hour test** | **~$1.07** |
| **Estimated 3-hour test** | **~$1.60** |

## Charges After Stop/Terminate

| Resource | After Stop | After Terminate |
|---|---|---|
| Compute | Stopped (no charge) | Removed |
| EBS root volume | Charged (~$2.40/month) | Removed (if DeleteOnTermination=true) |
| Public IPv4 | Released (no charge) | Released |
| Local NVMe storage | Data persists (charged via instance) | Lost |

## Direct Links

- EC2 Launch: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- g4dn.xlarge pricing: https://aws.amazon.com/ec2/pricing/on-demand/
- ComfyUI on AWS: https://github.com/comfyanonymous/ComfyUI
- Wan GitHub: https://github.com/Wan-Video/Wan2.1
