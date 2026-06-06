# Music Stack Architectures

Status: candidate
Updated: 2026-06-06

## Purpose

Define reusable production patterns for common music-generation tasks.

## A. Local Controlled Generation

Use when repeatability, privacy, local control, or low marginal generation cost matters.

```text
music brief
  -> structured specification
  -> ACE-Step 1.5 local generation or edit
  -> optional native stem separation
  -> optional Basic Pitch transcription on isolated stems
  -> optional pretty_midi editing
  -> optional Essentia descriptors
  -> FFmpeg or pyloudnorm normalization
  -> optional Matchering prototype
  -> quality and rights gate
  -> export package
```

## B. Cloud Commercial Generation

Use when managed infrastructure and provider-backed terms matter more than local control.

```text
music brief
  -> select provider by use case
  -> generate through Eleven Music, Lyria 3, SOUNDRAW, Loudly, Beatoven, or AIVA
  -> preserve provider, model, plan, prompt, output, and license evidence
  -> optional edit or stems path
  -> normalize and package
  -> quality and rights gate
```

## C. Video Soundtrack Automation

Use for short-form video, ads, explainers, and creator workflows.

```text
video analysis
  -> scene map
  -> mood and intensity curve
  -> soundtrack brief
  -> generate static track or scene-aware layers
  -> align cuts, fades, and transitions
  -> normalize loudness
  -> export audio plus metadata
```

## D. Adaptive Runtime Music

Use for games, applications, installations, and dynamic media.

```text
runtime state model
  -> state-to-music map
  -> loops and layer rules
  -> transition rules
  -> fallback behavior
  -> generation or licensed catalog source
  -> latency and continuity tests
```

## E. Real-Time Interactive Music

Use only when continuous control is truly required.

```text
input signals
  -> latency budget
  -> Google Lyria RealTime cloud experiment
     or Magenta RealTime 2 local experiment
  -> streaming buffer
  -> transition smoothing
  -> degradation strategy
  -> optional recording path
```

## Required Metadata

For every generated asset preserve:

- provider or model;
- model version;
- prompt and structured controls;
- source audio or MIDI references;
- generation date;
- plan or license evidence;
- editing steps;
- normalization settings;
- output format;
- quality-review result;
- rights-review result.

## Final Rule

Select an architecture by product need, not by model popularity.