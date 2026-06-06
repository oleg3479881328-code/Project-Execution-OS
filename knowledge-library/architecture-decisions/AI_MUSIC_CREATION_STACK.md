# AI Music Creation Stack

Type: `architecture-decision`
Lifecycle status: `candidate`
Captured: 2026-06-06
Review status: researched and preserved; not yet active system guidance

## Problem

Music-generation work should not depend on one fashionable model or one prompt-to-track workflow.

A reusable cross-project music capability needs separate paths for:

- local generation;
- managed cloud generation;
- real-time interactive music;
- editing and stems;
- MIDI extraction and manipulation;
- audio analysis;
- loudness normalization and export;
- mastering prototypes;
- rights and provenance review.

## Reusable Architecture Pattern

Use a multi-lane music stack:

```text
brief
  -> select static, adaptive, or real-time mode
  -> select local or managed-cloud generation path
  -> generate or edit
  -> optional stems
  -> optional MIDI extraction and manipulation
  -> optional audio analysis
  -> normalization and export
  -> optional mastering prototype
  -> quality review
  -> rights and provenance review
  -> project handoff
```

Do not force every task through the full pipeline. Load and use only the smallest relevant lane.

## Current Candidate Stack

### Local full-song baseline

- ACE-Step 1.5

Why it is promising:

- local full-song generation;
- UI, CLI, Python API, REST API, and VST3 paths;
- reference audio;
- cover generation;
- repaint workflows;
- track separation;
- multitrack generation;
- Vocal2BGM;
- metadata control;
- multilingual lyrics;
- LoRA workflow;
- Windows portable package.

### Cloud song baseline

- Google Lyria 3
- Eleven Music

Use when managed infrastructure, API integration, or provider-backed product terms matter more than local control.

### Real-time experiment lane

- Magenta RealTime 2 for local Apple-Silicon-oriented experiments and offline NVIDIA inference
- Google Lyria RealTime for experimental cloud WebSocket workflows

Keep real-time work in the experimental lane until a product genuinely requires continuous interactive generation.

### Commercial embedded API candidates

- SOUNDRAW API
- Loudly Music API
- Beatoven API
- AIVA

Use only after checking the exact plan, contract, output rights, and product-fit boundary.

### Utility chain

- Demucs or UVR5 for fallback stem separation
- Spotify Basic Pitch for audio-to-MIDI transcription
- pretty_midi for MIDI manipulation
- Essentia for audio descriptors, subject to AGPLv3 review
- FFmpeg `loudnorm` and pyloudnorm for loudness normalization
- Matchering as an optional reference-mastering prototype

### Research donors

- AudioCraft for MusicGen, AudioGen, MAGNeT, MusicGen Style, JASCO, and AudioSeal patterns
- stable-audio-tools for training, fine-tuning, inpainting, and Gradio experiments

Do not treat research donors as default commercial runtimes without checkpoint-specific license review.

## Applies To

Load this entry when work involves:

- AI-generated music;
- soundtracks for video, games, applications, ads, or creator workflows;
- full-song generation;
- adaptive soundtracks;
- real-time music;
- stems, remixing, MIDI, audio analysis, loudness normalization, or mastering;
- music-generation SaaS or API integration;
- music rights and provenance review.

## Triggers

Relevant triggers include:

- create music;
- generate a soundtrack;
- add music to a video pipeline;
- compare music-generation tools;
- build a music agent;
- integrate a music API;
- create adaptive music;
- create real-time music;
- split stems;
- convert audio to MIDI;
- normalize or master generated music;
- check rights for AI-generated music.

## Do Not Load When

Do not load this entry for:

- ordinary video editing with no music decision;
- voice-over-only tasks;
- sound-effect-only tasks unless they are part of a broader audio package;
- unrelated media production work;
- legal conclusions without checking current provider terms.

## Rights Boundary

Preserve with every generated asset:

- provider or local model;
- model version;
- generation date;
- plan or contract evidence;
- prompt and structured controls;
- uploaded reference assets;
- edits;
- output file;
- normalization and mastering steps;
- review result;
- unresolved risks.

Important limits:

- code license and model-weight license may differ;
- marketing language is not a substitute for the active contract;
- royalty-free does not automatically mean unrestricted redistribution;
- commercial-use permission does not automatically answer every ownership question;
- uploaded references require separate clearance.

## Adaptation Notes

Use the smallest proven stack that solves the active task.

For a local MVP, test ACE-Step 1.5 first.

For a cloud comparison, test Google Lyria 3 and Eleven Music on the same benchmark prompts.

For interactive work, validate whether static or adaptive music solves the problem before introducing a real-time runtime.

## Validation Still Required

This entry remains `candidate` until task-specific tests confirm:

- ACE-Step installation and quality on the available Windows hardware;
- cloud API access, pricing, and terms for the selected providers;
- real-time latency and production-readiness boundaries;
- utility-chain quality and licensing boundaries;
- project-specific rights and platform requirements.

## Evidence And Related Artifacts

Primary music-block files:

- `blocks/music/BLOCK.md`
- `blocks/music/TOOL_SELECTION_MATRIX.md`
- `blocks/music/STACK_ARCHITECTURES.md`
- `blocks/music/VALIDATION_GENERATION.md`
- `blocks/music/VALIDATION_REALTIME.md`
- `blocks/music/VALIDATION_UTILITIES.md`
- `blocks/music/RIGHTS_CHECKLIST.md`
- `blocks/music/REFERENCES_EXTENDED.md`
- `blocks/music/RESEARCH_REPORT_2026-06-06.md`

Selected external sources:

- https://github.com/ace-step/ACE-Step-1.5
- https://github.com/magenta/magenta-realtime
- https://ai.google.dev/gemini-api/docs/music-generation
- https://ai.google.dev/gemini-api/docs/realtime-music-generation
- https://elevenlabs.io/docs/overview/capabilities/music
- https://soundraw.io/api
- https://www.loudly.com/music-api
- https://www.beatoven.ai/api
- https://www.aiva.ai/technology
- https://github.com/facebookresearch/demucs
- https://github.com/spotify/basic-pitch
- https://github.com/craffel/pretty-midi
- https://github.com/MTG/essentia
- https://github.com/csteinmetz1/pyloudnorm
- https://ffmpeg.org/ffmpeg-filters.html
- https://github.com/sergree/matchering
- https://github.com/facebookresearch/audiocraft
- https://github.com/Stability-AI/stable-audio-tools

## Related Standards

- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/AUTOMATIC_CAPTURE_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `blocks/music/BLOCK.md`

## Final Rule

Use a modular music-production stack, not a single-generator dependency.

Promote individual tools to production defaults only after a documented task-specific validation passes.