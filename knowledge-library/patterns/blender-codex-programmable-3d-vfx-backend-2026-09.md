# Blender + Codex as Programmable 3D/VFX Backend

Status: candidate reusable pattern — validation required
Date captured: 2026-09-06

## Core Finding

Blender should be treated in our stack primarily as a programmable 3D/VFX execution backend for AI agents, not only as a manual 3D editor.

The key operating pattern is:

`Codex local -> Python / bpy -> Blender CLI or background mode -> .blend / preview frames / rendered frames -> FFmpeg -> final video`

This is supported by Blender's official Python API and background execution model. A 2026-09-06 practical walkthrough from Pimenov demonstrated the same pattern end to end with Codex controlling Blender through Python scripts rather than by manually operating the UI.

## Existing-Solution-First Decision

Do not build a custom Blender integration first.

Phase 1 should use the smallest proven path:

1. local Codex;
2. Blender installed locally;
3. Python scripts using `bpy`;
4. Blender CLI/background execution;
5. preview render and saved `.blend` file;
6. FFmpeg only when frame/video assembly is needed.

A Blender MCP layer is optional and should be introduced only if interactive inspection, viewport screenshots, live scene mutation, or iterative agent vision materially improves the workflow.

Existing Blender/Codex MCP projects should be evaluated before any custom bridge is written.

## Why This Matters

This pattern gives us deterministic control over parts of media production that are difficult to control with generative video alone:

- cameras and camera motion;
- 3D objects;
- lights and shadows;
- physically repeatable animation;
- particles, splashes, smoke, debris and similar effects;
- foreground/background layering;
- depth and compositing support;
- scene reuse across multiple renders;
- deterministic re-rendering after small changes.

## Recommended Hybrid Stack

Use each tool where it is strongest:

`AI generation / ComfyUI -> Blender -> FFmpeg`

Typical responsibility split:

- ComfyUI / AI: image generation, cleanup, segmentation, enhancement, generative elements and stylization;
- Blender: camera, geometry, animation, 3D assets, lighting, particles, deterministic VFX, scene depth and repeatable rendering;
- FFmpeg: transcode, assembly, batch encoding and final delivery operations.

Do not treat Blender as a replacement for ComfyUI. Treat it as a complementary deterministic layer.

## Example Relevance — Champagne Video

For the Olga champagne video concept, Blender could own the controllable physical/VFX layer:

- bottle;
- cork;
- champagne stream;
- droplets/particles;
- camera motion;
- lights;
- depth;
- foreground/background effect layers.

AI can remain responsible for segmentation, cleanup, generative enhancement and stylistic transformation.

## Validation Gates

The preferred validation pattern is incremental:

1. one static preview frame;
2. several control frames at selected timestamps;
3. only then a full animation render.

This prevents expensive full renders before scene correctness is established.

## First Local Validation

The first experiment should be intentionally small:

1. install current Blender LTS on the Windows workstation;
2. let Codex discover the Blender executable;
3. run a background health check;
4. have Codex generate one `bpy` script;
5. create a simple scene with object, material, light and camera;
6. save `scene-v01.blend`;
7. render `preview.png`;
8. verify both artifacts manually.

Success means the pattern can be promoted toward a reusable capability. Failure should be diagnosed against official Blender documentation and existing integrations before custom code is designed.

## Hardware Note

The owner's HP Victus with NVIDIA RTX laptop GPU is suitable for the first validation and simple/medium scenes. Heavy Cycles scenes, large textures, and complex simulations may be constrained by available VRAM and should not be assumed viable until measured locally.

## MCP Boundary

Do not start with MCP by default.

Consider MCP only when we need capabilities such as:

- inspect the live scene;
- inspect objects and properties;
- receive viewport screenshots;
- execute Python inside a running Blender session;
- iteratively modify and inspect a scene;
- export assets such as GLB;
- connect asset libraries.

Before implementing such a layer, review existing projects such as Blender/Codex MCP integrations and adapt one if adequate.

## Promotion Rule

This note is research-backed system knowledge, not yet a validated executable capability.

Do not register `Blender + Codex` as a ready capability until the local end-to-end test produces at minimum:

- a generated Python script;
- a valid `.blend` file;
- a successful preview render;
- reproducible rerun instructions;
- known Blender executable path and version;
- basic GPU/render compatibility results.

## Sources

- https://www.blender.org/
- https://docs.blender.org/api/current/
- https://pimenov.ai/knowledge/blender-codex-pervaya-3d-scena/
- https://github.com/webita/blender-codex-mcp
- https://github.com/bestmaa/codex-blender

## Final Decision

Blender + Codex should be kept in the Project Execution OS reusable capability stack as a candidate pattern for AI-controlled 3D/VFX production.

Default path: `Codex -> bpy -> Blender CLI`.

MCP is a second-stage enhancement, not a prerequisite.
