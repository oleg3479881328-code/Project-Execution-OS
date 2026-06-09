# Server Rental Research Intake — Google Doc Partial — 2026-06-09

## Source

Google Doc: `Облачные GPU для AI: Стратегия Аренды`

Document ID: `1M8Ihfg0iFB6H4HvZtxiDJ8uuJzmYYsDBhnbBmpDdUXI`

## Intake Status

`partial`

The Drive connector exposed only the first section of the document. This file stores only the visible portion and must not be treated as a complete research report.

## Strong Strategic Findings Worth Preserving

### 1. Thin-Terminal Strategy

The document strongly supports the architecture already captured in this block:

- laptop as terminal;
- cheap persistent VPS as head node;
- temporary GPU workers;
- pay-as-you-go execution;
- automatic shutdown;
- workload-based GPU selection;
- hybrid use of international providers, marketplaces, and regional nodes.

### 2. Provider Categories

The visible section identifies these provider groups as worth research:

- RunPod;
- Vast.ai;
- Lambda Labs;
- TensorDock;
- Modal;
- Spheron;
- Replicate;
- Baseten;
- Fal;
- Beam;
- Hyperbolic;
- AWS;
- GCP;
- Azure;
- Oracle;
- AutoDL;
- Alibaba Cloud;
- Tencent Cloud;
- Huawei Cloud.

### 3. China As Separate Track

The visible section distinguishes:

- mainland China;
- Hong Kong;
- international accounts;
- domestic accounts;
- passport KYC;
- payment friction;
- ICP Filing for public mainland hosting;
- Hong Kong as a different operational path.

This confirms that China should remain a separate research track rather than being merged into the default US infrastructure path.

### 4. GPU Selection By Workload

The visible section reinforces the principle that H100 is often overkill for ordinary media workloads and that lower-cost cards may produce better economics.

Candidate GPU profiles mentioned:

- RTX 4090;
- RTX 5090;
- RTX A6000;
- A100 80GB;
- H100;
- H20.

## Data Points Seen In The Partial Document

These are `unverified intake values`, not canonical facts:

- RunPod RTX 4090: `$0.54/hour`
- RunPod H100 SXM: `$1.50/hour`
- Vast.ai RTX 4090: `$0.15-$0.44/hour`
- Lambda A100 80GB: `$1.20/hour`
- Lambda H100 SXM: `$2.50/hour`
- TensorDock RTX 4090: `$0.38/hour`
- TensorDock H100 SXM: `$1.99/hour`
- Modal L40S: `$0.000542/second`
- Modal A100 80GB: `$0.000694/second`
- Modal H100: `$0.001097/second`
- Spheron RTX 4090: `$0.67/hour`
- Spheron H100 SXM Spot: `$0.80/hour`
- AutoDL RTX 4090: approximately `$0.15-$0.22/hour`
- AutoDL A100 80GB: approximately `$0.60/hour`
- Mainland China H20: from `$0.80/hour`
- Hong Kong A100 80GB: from `$2.20/hour`

All values require primary-source verification and current-date refresh before recommendation.

## Important Caution Flags

The visible section contains strong claims that must not be accepted without verification:

- `60-85%` OpEx reduction;
- exact provider prices;
- exact payment methods;
- exact region multipliers;
- exact ICP applicability wording;
- exact egress costs for hyperscalers;
- `Hugging Face blocked` wording;
- `ideal for NVLink clusters` claims;
- model-specific GPU fit claims;
- comparative statements such as `L40S instead of overvalued H100`.

## Next Actions

- obtain the remaining document text;
- verify official pricing pages;
- separate marketplace spot values from stable on-demand values;
- verify US registration and payment flows;
- verify mainland China versus Hong Kong rules;
- extract the model tables and architecture sections from the remainder;
- merge only validated findings into the canonical block files.
