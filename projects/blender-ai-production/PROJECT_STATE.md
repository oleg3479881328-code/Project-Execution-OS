# Blender AI Production — PROJECT_STATE.md

## Status

- Project: `Blender AI Production`
- State: active
- Phase: donor consolidation + practical pipeline validation
- Updated: 2026-09-12

## Current Objective

Converge the already-started Blender/ComfyUI experiment and the newly consolidated donor research into one repeatable, economical, verifiable AI-assisted 3D/VFX production pipeline.

First acceptance case: frozen champagne — foreground subject moves while the background and champagne splash/droplets remain temporally frozen at stable coordinates.

## Current Architecture

```text
Coordinator / planner / reviewer
        ↓
Bounded executor jobs
        ↓
Blender MCP + bpy/Python
        ↓
Geometry / camera / physics / frozen FX / render passes
        ↓
ComfyUI for AI isolation/look work where useful
        ↓
FFmpeg deterministic assembly
        ↓
Visual + temporal QA
```

Current practical executor evidence: Codex/local agent in the neighboring test.

Candidate future cost optimization: evaluate a cheaper executor model such as Luna for narrow hands-only jobs after the control/verification contract is stable. This is a candidate, not a verified current production fact.

## Existing Work Reused

### Internal research

- Blender MCP and editor-control research:
  https://docs.google.com/document/d/1NDScqwJL9V5j2Pyh_WijYh-aDay3aSMaWUfj-qyeEj8/edit
- Frame-by-frame / Blender → ComfyUI research:
  https://docs.google.com/document/d/1ws9EXpciQxrF1_A-p8UVB6BchxKgs8cli-qBtId41Us/edit
- Subject-isolation / compositing research:
  https://docs.google.com/document/d/1Slck3DEFjxywm7iZ0vmSz9V0JoPcwOhopduC0wT-2s4/edit

### Practical test already underway

Known neighboring-chat test shape:

```text
Codex dispatcher
→ Blender scene build/render
→ Depth / Normal / Mask passes
→ ComfyUI via API
→ FFmpeg final MP4
```

This is active practical evidence, but the current project has not yet received enough durable output evidence to mark the full chain verified. Reconcile results rather than restart.

## Donor Findings Captured

### Official Blender Lab MCP

Treat as official baseline to benchmark first. It exposes Blender Python through MCP and carries a serious arbitrary-code security boundary.

Source:
https://www.blender.org/lab/mcp-server/

### Pat Simmons / Astra case study

Reusable pattern:

```text
research
→ PRD
→ fresh build context
→ Blender execution
→ visual/self QA
→ corrections
→ milestone .blend files
```

Most important reusable implementation decision:

- MCP for live inspection and targeted corrections;
- saved Python / `bpy` for precise, repeatable construction.

Do not inherit the one-large-autonomous-agent operating model by default.

### `arjun988/blender-skills`

Selected reusable rules:

- approve motion at low resolution before high-resolution simulation;
- use a timing brief and proxy emitter before expensive FX work;
- cache before final render;
- constrain domains and particle counts;
- treat simulation as an art-directed, baked production step.

### `RobLe3/cc-blender-skill`

Selected reusable rules:

- plan → blockout → camera lock → lighting → geometry/material refinement → render → composite → export;
- stable object naming and chunked `bpy` execution;
- visual validation after numerical/API validation;
- preserve baseline and failure evidence;
- classify failure before retrying;
- improve reusable method/orchestration before repeated blind rebuilds.

### Pat Simmons `blender-production.zip`

Source:
https://fallingwater-astra.vercel.app/blender-production.zip

State: source located, direct package audit pending. Do not adopt or describe its internals as verified until the package is actually inspected.

## Frozen Champagne MVP — Acceptance Contract

A passing proof must demonstrate control, not merely aesthetics.

Required behavior:

1. foreground subject/action may move;
2. background must remain still after the freeze point;
3. champagne splash/droplets must retain stable coordinates and shape after the freeze point;
4. foreground/background/liquid occlusion must be plausible;
5. frame-to-frame continuity must be acceptable;
6. final sequence must be assembled reproducibly;
7. failed ranges should be replaceable without rebuilding accepted ranges.

Likely production path:

```text
source / subject isolation if needed
→ camera match / scene blockout
→ champagne FX prototype
→ approve desired splash state
→ freeze/bake/convert accepted state to deterministic geometry or fixed particles
→ foreground action through frozen scene
→ beauty/depth/normal/mask passes
→ optional ComfyUI processing
→ FFmpeg assembly
→ temporal QA
```

## Verification Ledger

### Confirmed / sufficiently researched

- Blender has mature Python automation and multiple MCP control options.
- Official Blender Lab MCP exists and should be benchmarked as the official baseline.
- `arjun988/blender-skills` contains reusable VFX/physics production patterns.
- `RobLe3/cc-blender-skill` contains useful orchestration and quality-refinement patterns.
- Prior internal research covers Blender/ComfyUI frame workflows and SAM2/BiRefNet-style subject isolation.
- A neighboring practical test is already exercising a Codex → Blender → passes → ComfyUI → FFmpeg architecture.

### Not yet verified in this project

- completed production-quality frozen-champagne video;
- completed end-to-end Blender ↔ ComfyUI ↔ FFmpeg run with preserved evidence;
- Luna as the actual executor in the current test;
- Pat Simmons package contents / compatibility / safety;
- best MCP server for the actual local Windows + Blender environment;
- measured time/cost advantage of coordinator + cheap executor vs one large autonomous model.

## Do Not Repeat

- Do not start a new Blender-agent framework before comparing the official Blender MCP and existing donor solutions.
- Do not bulk-install entire skill collections.
- Do not restart the current neighboring practical experiment from zero.
- Do not let multiple agents mutate the same `.blend` simultaneously.
- Do not spend on high-res FX/cache before low-res motion is accepted.
- Do not treat successful code execution as visual success.
- Do not hide physics/geometry defects with AI stylization.
- Do not claim production readiness without a concrete final artifact + QA evidence.

## Next Safe Actions

1. Pull durable evidence/results from the already-running neighboring practical test into this project state/log.
2. Inspect the actual `blender-production.zip` donor package.
3. Benchmark official Blender Lab MCP vs the strongest community candidate on a tiny deterministic scene.
4. Define the minimum reusable Blender execution contract for the hands layer: input, allowed tools, checkpoints, evidence, acceptance/failure output.
5. Run/finish the frozen-champagne MVP and record timing, cost, defects and rerender behavior.

## Durable Locations

- Project entrypoint: `projects/blender-ai-production/PROJECT.md`
- Current log: `projects/blender-ai-production/logs/latest.md`
- Drive folder: https://drive.google.com/drive/folders/1tynpKSjLZHbEpU1jetSiwzI9vTzDBZtZ
- Research / donor audit: https://docs.google.com/document/d/1_Ftr5qRFPhbPcjS1baNQ1kEZaYxVuohnmDQZFmklL3I/edit
