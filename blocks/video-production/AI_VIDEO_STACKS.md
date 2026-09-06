# AI Video Stacks

## Purpose

Provide reusable AI-enhanced video-production stacks.

## Stack 1 — AI Script + TTS + Manual Edit

Use when validating a content format quickly.

Flow:

`topic -> verified script -> TTS -> CapCut -> captions -> export`

Good for:

- facts channels;
- gadget voiceovers;
- educational shorts.

## Stack 2 — Transcript + AI Clip Suggestions

Use when long-form video needs candidate short clips.

Flow:

`video -> transcript -> timestamp segments -> AI ranking -> human review -> ffmpeg cuts -> captions -> export`

Good for:

- podcasts;
- interviews;
- lectures;
- product reviews.

## Stack 3 — AI Visuals + TTS + Template Render

Use when the video should be original and anonymous.

Flow:

`script -> scene plan -> image/video generation -> TTS -> Remotion/ffmpeg render -> captions -> review`

Good for:

- documentary micro-content;
- science facts;
- explainers;
- original shorts.

## Stack 4 — Multilingual AI Localization

Use when one master becomes many language variants.

Flow:

`master script -> translation -> local QA -> TTS voices -> captions -> localized metadata -> batch render`

Good for:

- 10-language page networks;
- affiliate channels;
- educational products.

## Stack 5 — AI Avatar Video

Use when a presenter layer adds value.

Flow:

`script -> avatar generation -> voice -> edit -> captions -> review`

Good for:

- explainers;
- product demos;
- multilingual presenters.

Risks:

- uncanny output;
- disclosure expectations;
- brand mismatch;
- impersonation concerns.

## Stack 6 — QuizLight Card Generator

Use for language learning by video.

Flow:

`video -> transcript -> phrase selection -> translation -> context extraction -> clip bounds -> card image/context -> save`

## Stack 7 — Codex + Blender Programmable 3D/VFX

Status: candidate — local validation required.

Use when generative video alone does not provide enough deterministic control over cameras, 3D objects, lighting, particles, depth, repeatable animation, or compositing layers.

Default flow:

`Codex local -> Python / bpy -> Blender CLI/background -> .blend + preview/control frames -> rendered frames -> ffmpeg -> final video`

Recommended hybrid flow:

`AI generation / ComfyUI -> Blender -> ffmpeg`

Responsibilities:

- AI / ComfyUI: generation, cleanup, segmentation, enhancement and stylistic layers;
- Blender: camera, geometry, animation, 3D assets, lighting, particles, depth and deterministic VFX;
- ffmpeg: frame/video assembly, transcode and delivery.

Existing-solution-first rule:

- start with Blender's official Python API and CLI/background execution;
- do not build a custom Blender bridge first;
- evaluate existing Blender/Codex MCP projects only when live scene inspection, viewport screenshots, iterative scene mutation, or in-process execution is needed;
- promote this stack to a validated capability only after a reproducible local test produces a valid `.blend` and preview render.

Validation gates:

1. one static preview frame;
2. several control frames;
3. full animation only after visual correctness is established.

Canonical research note:

`knowledge-library/patterns/blender-codex-programmable-3d-vfx-backend-2026-09.md`

## AI Review Rules

Before publishing:

- verify facts;
- verify translation;
- verify pronunciation;
- verify captions;
- verify visual appropriateness;
- disclose synthetic media when required;
- do not imitate a real person without permission.

## Final Rule

AI should increase speed and variation, but human review must remain where facts, rights, identity, or brand trust matter.
