# AWS Instance Selection — Reels Factory MVP Smoke Test

Date: 2026-06-10 (final)
Region: us-east-2 (Ohio)

## Canonical First-Run Route

| Decision | Value | Justification |
|---|---|---|
| **Instance** | **g5.xlarge** | 24 GB VRAM (A10G) — sufficient for I2V-14B-480P FP16 |
| **Model** | Wan2.1-I2V-14B-480P | Only I2V variant available (no I2V-1.3B exists) |
| **Model format** | Diffusers (FP16) | Official Wan-AI format, 7 sharded safetensors |
| **Workflow** | `wanvideo_2_1_14B_I2V_example_03.json` | From ComfyUI-WanVideoWrapper |
| **Root volume** | 100 GB gp3 | DLAMI + deps + model (~30 GB) + cache + output |
| **Hourly cost** | $1.014/hr ($1.006 compute + $0.0033 EBS + $0.005 IPv4) |
| **Estimated test cost** | ~$3-6 (2-3 hours) |

## Why Not g4dn.xlarge?

g4dn.xlarge has 16 GB VRAM. I2V-14B-480P at FP16 requires ~18-22 GB. g4dn.xlarge is insufficient for the primary FP16 route.

**g4dn.xlarge is only viable as a fallback** with FP8 quantized models (`Wan2_1-I2V-14B-480P_fp8_e4m3fn.safetensors` from Kijai/WanVideo_comfy) and block swapping enabled.

## Candidates Compared

| Instance | vCPU | GPU VRAM | Price/hr | I2V-14B FP16 | I2V-14B FP8 |
|---|---|---|---|---|---|
| g4dn.xlarge | 4 | 16 GB (T4) | $0.526 | ❌ Insufficient | ⚠️ Possible with swapping |
| **g5.xlarge** | **4** | **24 GB (A10G)** | **$1.006** | **✅ Sufficient** | ✅ |
| g6.xlarge | 4 | 24 GB (L4) | ~$0.70 | ✅ Sufficient | ✅ |

## Quota

- Quota: `Running On-Demand G and VT instances` — 4 vCPU
- g5.xlarge uses 4 vCPU — fits exactly (100% utilization)

## Storage Breakdown (100 GB gp3)

| Component | Estimated Size |
|---|---|
| Deep Learning AMI GPU PyTorch | ~15 GB |
| ComfyUI + dependencies + pip cache | ~5 GB |
| I2V-14B-480P model (Diffusers) | ~30 GB |
| Text encoder (T5) | ~10 GB |
| CLIP vision + VAE | ~5 GB |
| HuggingFace cache | ~10 GB |
| Temporary output + swap | ~5 GB |
| **Total** | **~80 GB** |
| **Recommended** | **100 GB** (safety margin) |

## Direct Links

- g5.xlarge pricing: https://aws.amazon.com/ec2/pricing/on-demand/
- Wan2.1-I2V-14B-480P: https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P
- I2V workflow: https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_2_1_14B_I2V_example_03.json
