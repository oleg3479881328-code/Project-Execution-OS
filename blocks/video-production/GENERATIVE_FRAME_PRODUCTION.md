# Generative Frame Production

## Purpose

Define the reusable Project Execution OS pattern for AI-assisted frame production where visual content itself is generated or re-rendered across time, rather than only composed deterministically from code, graphics, text, and existing media.

This layer complements `FRAME_ADDRESSABLE_PRODUCTION.md`.

`FRAME_ADDRESSABLE_PRODUCTION.md` governs exact timing, shot boundaries, keyframes, deterministic composition, incremental rendering, and QC.

This document governs the generative visual layer: keyframe synthesis, first/last-frame interpolation, video-to-video stylization, geometry-conditioned generation, selective frame repair, and temporal consistency.

## Core Decision

Do not treat generative frame production as thousands of unrelated image generations.

Preferred production model:

```text
shot brief
-> spatial/identity constraints
-> key visual states
-> generative interpolation or guided video synthesis
-> defect-frame inspection
-> local repair/inpainting
-> temporal stabilization / retiming
-> deterministic composition + audio + overlays
-> final QC
```

The creative source of truth is therefore split:

1. deterministic timing and shot graph;
2. generative recipe and conditioning state;
3. approved keyframes / reference frames;
4. resulting generated shot segments.

The final MP4 remains a delivery artifact, not the editable master.

## Four Production Modes

### 1. Deterministic frame-addressable composition

Use Remotion/code/keyframes when:

- text, diagrams, UI, charts, HUDs, subtitles, motion graphics, or exact branded layouts dominate;
- frame-perfect revision speed matters;
- the scene can be described with deterministic geometry and media layers.

This is the default for explainers and structured information video.

### 2. Keyframe-to-video generative interpolation

Use first/last or sparse-keyframe conditioned generation when:

- the scene requires organic movement or photorealistic/illustrative synthesis;
- important visual states can be approved at discrete anchor frames;
- the motion between those anchors can be generated rather than hand-authored.

Typical pattern:

```text
approved keyframe A
+ approved keyframe B
+ text / motion condition
+ optional depth / pose / line / mask controls
-> generated intermediate motion
```

This is the preferred generative interpretation of “frame-by-frame” for many AI-video shots.

### 3. Video-to-video temporal stylization

Use when a real or rendered guidance video already defines:

- camera motion;
- body motion;
- choreography;
- object trajectories;
- timing.

The generative system then changes style, materials, texture, lighting, or appearance while attempting to preserve the source motion.

Avoid independent per-frame diffusion without temporal constraints because it tends to produce flicker, identity drift, and texture instability.

### 4. Literal frame repair / image-per-frame intervention

Use local frame editing for exceptions:

- bad anatomy on one or a few frames;
- incorrect logo/text/detail;
- local occlusion defect;
- transition artifact;
- continuity break.

Repair should normally be followed by a short temporal rebake / interpolation / propagation window around the corrected frame rather than replacing one isolated frame and leaving adjacent frames untouched.

## Keyframe Architecture

A generative keyframe is more than an image file.

Store with it:

- shot id;
- absolute frame/time;
- image hash/path;
- prompt / negative prompt when applicable;
- model/checkpoint/version;
- seed;
- sampler/scheduler and step settings when applicable;
- LoRA/adapters and weights;
- identity references;
- ControlNet/pose/depth/lineart/mask inputs;
- camera intent;
- approved/rejected state;
- provenance/licensing metadata.

This makes a shot reproducible enough for revision and audit even when the underlying generative model is stochastic.

## Conditioning Hierarchy

Prefer stronger constraints as the production need becomes more exact.

Approximate control ladder:

```text
text only
-> text + image reference
-> identity adapter / LoRA
-> first/last frame
-> pose / depth / line / mask control
-> 3D blockout + render passes
-> manual frame correction / paintover
```

For high-value shots, do not ask the model to infer geometry that can be explicitly supplied.

## Blender / DCC Hybrid Pattern

For exact camera motion, architecture, choreography, or object interaction:

```text
Blender blockout
-> camera + rough character/object animation
-> depth / normal / pose / silhouette passes
-> generative renderer / ComfyUI graph
-> approved keyframes / generated shot
-> repair / temporal stabilization
```

The 3D layer provides geometry and motion truth; the generative layer provides appearance.

This is preferable to trying to force a text-to-video model to rediscover the same spatial plan on every iteration.

## 2D / Krita Hybrid Pattern

For drawn/anime/illustrative work:

```text
rough key poses / genga
-> line / sketch guidance
-> generative inbetweening
-> color / style propagation
-> frame inspection
-> local paint/inpaint corrections
-> temporal recheck
```

The artist remains responsible for the important poses and corrections; the model handles computational inbetweening and repetitive rendering.

## Temporal Consistency Rule

Independent image generation for adjacent frames is not an acceptable default.

Use one or more of:

- first/last-frame conditioning;
- sparse-keyframe conditioning;
- cross-frame/temporal attention;
- optical-flow propagation;
- recurrent/reference feature propagation;
- fixed identity adapters / LoRA;
- depth / pose / line controls;
- deterministic source video guidance;
- post-generation deflicker and retiming.

The goal is to preserve:

- identity;
- silhouette;
- material/texture continuity;
- color palette;
- camera geometry;
- lighting direction;
- object persistence.

## Local Revision Model

A generative system is production-friendly only if corrections can be localized.

Target workflow:

```text
find defective frame/interval
-> freeze shot timing
-> repair keyframe or local frame
-> regenerate only bounded temporal window
-> compare neighbour frames
-> approve
-> replace only affected shot segment
-> final concat/mux
```

Do not automatically regenerate an entire film because one generated shot contains a defect.

## Relationship To Frame-Addressable Production

The two layers must share one canonical timing system.

Example:

```text
SHOT S14 = frames 4200–4380

Generative layer:
  KF-A frame 4200
  KF-B frame 4290
  KF-C frame 4380
  generated visual segment

Deterministic layer:
  subtitle starts frame 4224
  callout appears frame 4271
  logo overlay frames 4310–4380
  SFX frame 4332
```

The generated visual is therefore just one media layer inside an exact frame-addressable shot.

## Recommended PEOS Stack

```text
VIDEO PRODUCTION BRAIN
  research / script / direction / shot intent

TIMING + SHOT GRAPH
  exact frames / beats / audio alignment

GENERATIVE VISUAL LAYER
  references / keyframes / LoRA / controls
  ComfyUI / Wan FLF2V / ToonCrafter / V2V / inpainting

DETERMINISTIC COMPOSITION LAYER
  Remotion
  typography / overlays / diagrams / subtitles / exact keyframes

MEDIA EXECUTION LAYER
  FFmpeg / ffmpeg-skill
  extraction / sequences / concat / mux / retime / export

QC LAYER
  anchor frames
  burst checks
  temporal consistency
  identity / geometry / text / logo checks
  frame counts / media verification
```

## Current Donor/Tool Roles

### ComfyUI

Treat as the graph/orchestration environment for generative visual shots, conditioning maps, custom model pipelines, and local/cloud inference.

Do not let ComfyUI become the only project-state format for the whole film. Shot timing and cross-shot production state should remain in the higher-level Video Production system.

### Wan FLF2V family

Use as a candidate first/last-frame generative interpolation path when compatible model weights and hardware/runtime are available.

Exact model version, license, resolution, frame count, VRAM need, and commercial-use terms must be revalidated before production use.

### ToonCrafter

Use as a candidate donor/model for cartoon/2D interpolation between key images.

Do not treat reported community wrappers, memory requirements, or licensing summaries as interchangeable with the upstream project; verify the exact code and weights being used.

### Krita AI Diffusion

Strong owner-facing candidate surface for frame/animation inspection, inpainting, and artist correction while using ComfyUI as backend.

Use when manual paintover and local correction are central to the workflow.

### EbSynth

Useful propagation/stylization path where a source video already provides motion and selected keyframes provide appearance.

Current product terms/pricing and whether a specific desktop/web/studio route is suitable for commercial work must be checked at adoption time.

### Remotion

Not a replacement for generative interpolation.

Use it after or around generated media for deterministic composition, exact timing, overlays, subtitles, motion graphics, and revision-safe assembly.

### FFmpeg / ffmpeg-skill

Use for frame extraction, image-sequence assembly, rate conversion, segment work, muxing, technical verification, and delivery transforms.

## Hardware / Infrastructure Rule

Do not choose a generative model from headline capability alone.

Before adoption, record:

- tested GPU / VRAM requirement;
- supported resolution;
- frame/window length;
- generation time;
- quantized/offload variants;
- cloud fallback path;
- model/license restrictions.

Large generative video models may belong on rented/cloud GPU even when deterministic composition and editorial work remain local.

## Validation Plan

Validate with a short shot, not a full film.

Recommended test:

1. 3–5 second scene;
2. two or three approved keyframes;
3. one explicit identity or geometry constraint;
4. generate intermediate motion;
5. intentionally repair one defective frame/region;
6. regenerate/propagate only the bounded neighbourhood;
7. insert result into the frame-addressable Remotion timeline;
8. overlay deterministic text/graphics;
9. verify exact frame count and final mux.

Success means the shot can be changed locally without restarting the whole production.

## Source Review Note — 2026-09-11

A user-supplied research memo on AI frame-by-frame video production highlighted the following useful architecture patterns:

- classical keyframe/inbetween separation maps well to AI-assisted production;
- identity consistency requires references/adapters/geometry controls rather than independent frame prompts;
- first/last-frame and sparse-keyframe generation are preferable to unrelated per-frame synthesis;
- video-to-video workflows need temporal constraints to suppress flicker;
- Blender/ComfyUI and Krita/ComfyUI are important hybrid DCC patterns;
- selective frame repair is a core production capability;
- final retiming/interpolation/deflicker is a separate finishing stage.

The memo also contains time-sensitive claims about model versions, VRAM, licensing, pricing, and performance. Those claims are not promoted to canonical fact without current source verification.

## Final Rule

For AI-assisted frame production, preserve human/agent control at the important visual states and automate the inbetweening, propagation, and repetitive rendering.

Do not confuse generative freedom with production control.
