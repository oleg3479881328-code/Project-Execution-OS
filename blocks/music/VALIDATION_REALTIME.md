# Real-Time Music Validation Backlog

Status: candidate
Updated: 2026-06-06

## Magenta RealTime 2

Validate:

- small model on Apple Silicon;
- base model hardware threshold;
- offline NVIDIA workflow;
- prompt control;
- note and MIDI control;
- AUv3 example;
- C++ embedding path;
- recording and export strategy;
- latency benchmark;
- production-readiness boundary.

## Google Lyria RealTime

Validate:

- WebSocket session lifecycle;
- latency;
- continuous prompt steering;
- weighted prompt mixing;
- BPM changes;
- scale changes;
- density and brightness controls;
- mute-bass and mute-drums behavior;
- hard-transition behavior after context reset;
- pricing;
- region availability;
- service stability;
- current terms for the intended product.

## Evidence Package

Preserve:

- tested version;
- date;
- machine profile;
- connection mode;
- prompts and controls;
- audio recordings;
- latency measurements;
- failure modes;
- fallback behavior;
- current terms evidence;
- result: promote, keep experimental, or reject.

## Final Rule

Do not choose real-time generation when a static or adaptive soundtrack solves the product need more simply.