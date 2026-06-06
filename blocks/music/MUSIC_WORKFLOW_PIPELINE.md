# Music Workflow Pipeline

## Purpose

Use this pipeline to structure music-related work before implementation or asset generation.

## Workflow

```text
1. Define the product or creative goal.
2. Identify the musical role: background, foreground, transition, loop, adaptive layer, interactive response, or full composition.
3. Define the target medium: short video, long-form video, game, application, live interaction, ad, podcast, or other format.
4. Capture constraints: duration, tempo, mood, genre, intensity curve, loop behavior, scene transitions, vocals or instrumental-only, platform, export format, latency, local-vs-cloud execution, and budget.
5. Decide whether the need is static, adaptive, or real-time.
6. Choose the smallest suitable generation, sourcing, or composition method.
7. Build a scene-to-music or state-to-music map when timing matters.
8. Generate or prototype.
9. Validate quality: fit, continuity, repetition, transition quality, loudness, artifacts, and export usability.
10. Check license, commercial-use terms, attribution requirements, training-data claims when relevant, and target-platform risk.
11. Prepare the project handoff: assets, prompts, settings, decisions, open questions, and implementation notes.
```

## Static Soundtrack Path

Use when one finished audio file is enough.

Typical output:

- soundtrack brief;
- prompt or sourcing plan;
- target duration;
- edit points;
- export format;
- usage-rights notes.

## Adaptive Soundtrack Path

Use when music changes according to scenes, states, or product events.

Typical output:

- state list or scene map;
- transition rules;
- layer structure;
- loop rules;
- intensity curve;
- fallback behavior;
- runtime constraints.

## Real-Time Interactive Path

Use when the system must react continuously to user input, MIDI, audio, gameplay, or live application state.

Typical output:

- input signals;
- latency target;
- hardware assumptions;
- runtime model choice;
- degradation strategy;
- recording or export path;
- validation test plan.

## Review Questions

Before calling the result ready, check:

- Does the music serve the product goal rather than merely sound impressive?
- Is the selected workflow simpler than the alternatives?
- Are transition and looping requirements explicit?
- Are export and runtime requirements buildable?
- Are legal and platform-risk claims supported by current terms?
- Is the handoff clear enough that another executor can continue without guessing?

## Final Rule

Prototype the musical behavior first. Scale generation volume only after the workflow is validated.