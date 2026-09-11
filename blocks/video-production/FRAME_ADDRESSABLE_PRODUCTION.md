# Frame-Addressable Video Production

## Purpose

Define the reusable Project Execution OS pattern for video systems where every visual state is reproducible from an exact frame/time coordinate, individual shots can be reviewed and re-rendered independently, and quality control can inspect anchor frames and temporal transitions without rebuilding the whole film.

This is the preferred architecture for programmatic explainers, motion-graphics explainers, narrated educational video, data visualization video, and other repeatable video-factory work where deterministic editing and revision speed matter.

## Core Decision

Use **frame-addressable production**, not literal hand-drawn frame-by-frame production, as the default.

Frame-addressable means:

- one canonical timeline;
- exact shot ranges;
- exact semantic beat anchors;
- each visual component derives its state from the current frame or absolute time;
- keyframes/interpolation define motion between anchors;
- any frame can be rendered as a still;
- one changed shot can be re-rendered without rebuilding the entire video;
- the final movie is assembled from deterministic shot outputs plus the master audio track.

Literal image-per-frame generation is a separate technique and should be used only when the visual style truly requires unique painted/generated frames. It is normally slower, harder to revise, more storage-heavy, and less temporally stable.

## Three Different Meanings Of “Frame By Frame”

### 1. Frame-addressable rendering — DEFAULT

Each frame is a deterministic function of:

`project state + shot state + current frame/time`

Examples:

- x/y position at frame 463;
- camera scale at frame 588;
- text opacity at frame 721;
- current subtitle token at frame 1040;
- exact frame on which a callout changes state.

The system renders frames on demand. It does not store thousands of independent source images.

### 2. Keyframe-driven animation — NORMAL AUTHORING LAYER

The editor or agent specifies important states:

`frame 120: x=300, scale=1.0`
`frame 138: x=640, scale=1.08`
`frame 180: x=640, scale=1.03`

Interpolation generates the frames between them.

This is how most motion should be authored.

### 3. Literal image-per-frame production — SPECIAL CASE

Every frame or every small frame group is a unique raster/generated image.

Use only for:

- hand-drawn animation aesthetics;
- stop-motion-like effects;
- generative image/video experiments where per-frame synthesis is intentional;
- special transition sequences where deterministic vector/code animation is insufficient.

Do not use this as the default production model for explainers.

## Canonical Time Model

The system should maintain one source of truth for timing.

Preferred representation:

```text
fps
absolute frame number
absolute seconds
shot-local frame
shot-local seconds
semantic beat / narration token anchor
```

Rules:

1. Never allow several competing time bases without explicit conversion helpers.
2. Audio/narration alignment is the master narrative timing source for voiceover-driven work.
3. Shot boundaries must round to the same frame convention used by the renderer.
4. Final assembly must assert expected frame counts rather than accepting “looks close enough.”

## Production Data Model

### Project

- fps
- width / height
- aspect ratio
- total duration / total frames
- master audio
- theme/style tokens
- global overlays

### Shot

- stable shot id
- start frame / end frame
- narration segment / semantic purpose
- assets
- visual recipe
- camera behavior
- transition behavior
- editable parameters

### Beat

- absolute frame/time anchor
- semantic event
- visual state change
- optional subtitle/token anchor
- optional sound effect cue

### Keyframe

- parameter
- frame
- value
- easing/interpolation mode

Example parameters:

- x / y
- scale
- rotation
- opacity
- blur
- camera position
- crop / focal position
- color or highlight state
- text reveal progress
- mask/path progress

## Rendering Architecture

Preferred stack:

```text
script / narration
-> alignment
-> timeline
-> shot plan
-> beat/keyframe model
-> Remotion frame-addressable renderer
-> shot-segment render cache
-> FFmpeg assembly / audio mux / normalization / export
-> frame and motion QC
```

### Remotion role

Use Remotion for:

- React/component composition;
- exact frame access;
- deterministic interpolation;
- subtitles and overlays;
- camera/motion systems;
- programmable diagrams/data visualizations;
- still rendering of arbitrary frames;
- shot-level rendering.

### FFmpeg / ffmpeg-skill role

Use FFmpeg or a structured wrapper such as `ffmpeg-skill` for:

- probe and media inspection;
- lossless cuts when possible;
- segment concat;
- final audio mux;
- loudness normalization;
- aspect/delivery transforms;
- captions/burn-in when appropriate;
- output verification and contact sheets.

Do not force FFmpeg filter graphs to become the primary authoring system for complex explainer motion when Remotion gives clearer frame-level composition and revision control.

## Incremental Rendering Rule

A production-grade system should not require a full-film re-render for a one-shot correction.

Target workflow:

```text
change shot S14
-> invalidate S14 and transition neighbours only
-> render those segments
-> assert segment frame counts
-> concatenate cached + new segments
-> mux unchanged master audio
-> produce new preview
```

This is one of the highest-value donor patterns from `video-talkcraft`.

## Frame Review Model

Do not inspect every frame manually.

Use a hierarchy:

### Anchor stills

Render stills at:

- shot opening;
- major semantic beat;
- peak state;
- pre-exit;
- transition boundary.

### Burst review

For state switches and fast transitions, inspect short bursts such as:

`N-2, N, N+2`

or a small sequence around the transition.

Single stills cannot reveal temporal popping, accidental one-frame flashes, or bad easing.

### Motion-density check

Compare sampled neighbouring frames to detect shots that have become unintentionally static.

This is a QC signal, not a creativity metric. Small purposeful movement may need a different threshold than large camera motion.

### Contact sheets

Tile multiple anchor frames into sheets so a reviewer/vision model can judge:

- consistency;
- composition;
- subtitle collisions;
- visual hierarchy;
- repeated layouts;
- chapter pacing.

## Editing UX Target

For an owner-friendly system, build a visual workbench on top of the frame-addressable model.

The user should be able to:

1. scrub the timeline to an exact frame;
2. select a shot or visual element;
3. move/scale/rotate/crop with the mouse;
4. press “set keyframe” or let the editor auto-create a keyframe;
5. change easing or duration;
6. preview only the current shot;
7. render an exact still;
8. compare before/after;
9. re-render only the affected shot;
10. export the assembled film.

The UI should edit structured project data. It should not become a second independent timeline format disconnected from the renderer.

## Donor Findings — 2026-09-11

### anything2explainer

Strong patterns:

- explicit global frame ranges per narration sentence and shot;
- semantic beat anchors inside each shot;
- Remotion `Sequence` segmentation;
- frame-driven motion helpers and keyframes;
- pre-rendered still/preview checks;
- motion-density QC;
- fixed review points before full production.

Treat as architecture donor only unless commercial authorization is obtained. Toolkit license is PolyForm Noncommercial.

### video-talkcraft

Stronger donor for a reusable production engine because it adds:

- word-level narration alignment;
- reusable motion-card library;
- explicit multiple time-base conversion helpers;
- shot-segment rendering cache;
- changed-shot + neighbour re-render;
- frame-count assertions;
- anchor/burst/contact-sheet review;
- editable post-production workbench.

Treat as architecture/methodology donor under current noncommercial license unless commercial authorization is obtained.

### ffmpeg-skill

Strong complementary execution layer:

- structured FFmpeg operations;
- probe-first workflow;
- lossless-first operations;
- dry-run and machine-readable results;
- output verification;
- contact-sheet inspection support;
- local/offline operation;
- MIT license.

It is not the primary motion-design/frame-authoring engine. It is the finishing, transformation, validation, and assembly layer.

## Recommended PEOS Architecture

```text
VIDEO PRODUCTION BRAIN
  research / script / narration / shot decisions

FRAME PRODUCTION LAYER
  timeline
  shot graph
  semantic beats
  keyframes
  motion recipes
  Remotion renderer

INCREMENTAL RENDER LAYER
  per-shot cache
  dependency invalidation
  still/burst rendering

MEDIA EXECUTION LAYER
  ffmpeg-skill / FFmpeg
  probe / concat / mux / normalize / export

QC LAYER
  frame anchors
  burst checks
  contact sheets
  stillness/motion checks
  final technical validation

OWNER WORKBENCH
  timeline scrub
  mouse transform
  keyframe editing
  shot-only preview
  before/after
```

## Adoption Decision

Adopt the architecture pattern now.

Do not clone the donor implementations into a commercial product without license clearance.

For our own implementation, build original code around the general concepts and rely on permissively licensed dependencies/tools where possible.

The first validation should be a short internal explainer in which:

- narration is aligned to exact frames;
- 5–10 shots are defined;
- at least one shot has multiple semantic beat anchors;
- every shot can render as isolated stills/video;
- one shot can be changed and re-rendered without a full rebuild;
- final assembly is verified by frame count and media probe.

## Final Rule

The source of truth is not “a rendered MP4.”

The source of truth is a deterministic timeline + shot/beat/keyframe model from which any required frame and the final film can be reproduced.