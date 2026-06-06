# Music Utility Validation Backlog

Status: candidate
Updated: 2026-06-06

## Stem Separation

Validate:

- ACE-Step native separation;
- Demucs v4 fallback;
- UVR5 desktop path;
- output quality for vocals, drums, bass, and other stems;
- bleeding and artifact rate;
- Windows usability;
- batch-processing path.

## Audio To MIDI

Validate Spotify Basic Pitch on isolated stems:

- melody transcription;
- polyphonic instrument transcription;
- pitch bends;
- MIDI export;
- Windows installation;
- accuracy boundary for mixed audio versus isolated instruments.

## MIDI Manipulation

Validate `pretty_midi` for:

- tempo inspection;
- chroma analysis;
- transposition;
- note editing;
- MIDI generation;
- export;
- DAW handoff.

## Audio Analysis

Validate Essentia for:

- BPM;
- key and scale;
- tonal descriptors;
- spectral descriptors;
- temporal descriptors;
- large-batch extraction;
- AGPLv3 boundary for proprietary applications.

## Loudness And Export

Validate:

- FFmpeg conversion, fades, mixing, resampling, and `loudnorm`;
- pyloudnorm measurement and normalization;
- one-pass versus two-pass normalization;
- WAV and MP3 export presets;
- batch automation.

## Mastering Prototype

Validate Matchering for:

- reference-based processing;
- Docker path;
- Python-library path;
- UVR5 desktop integration;
- ComfyUI node;
- quality compared with simple loudness normalization;
- boundary where a human audio engineer remains necessary.

## Evidence Package

Preserve version, installation steps, test files, outputs, runtime notes, quality notes, license evidence, and the final decision: promote, keep experimental, or reject.
