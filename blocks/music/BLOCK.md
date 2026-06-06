# Music Block

## Purpose

This block gives `Project Execution OS` one reusable domain layer for music-related work across projects.

It helps an agent move from product intent or creative intent to the correct musical workflow, tool choice, output specification, validation path, and implementation handoff.

## Status

`candidate`

## When To Use

Use this block when the task involves:

- AI-generated music;
- adaptive or interactive soundtracks;
- music for video, games, ads, applications, or creator workflows;
- background-score generation;
- music-tool evaluation or integration research;
- prompt design for music-generation systems;
- music-agent behavior;
- DAW-aware or application-aware music handoff;
- legal, licensing, or platform-risk review for generated music.

## When Not To Use

Do not use this block for:

- ordinary video editing with no music decision;
- voice-over generation;
- sound-effect-only tasks unless they are part of a broader music package;
- final legal conclusions without checking current license and platform terms;
- project-specific implementation details that belong in the target project repository.

## Core Rule

Do not treat AI music as a single prompt-to-track task.

A valid music workflow should connect:

`goal -> use case -> musical role -> constraints -> generation or sourcing method -> arrangement behavior -> export requirements -> rights check -> quality review -> project handoff`

## Required Reading Inside This Block

Open only the smallest relevant path:

1. `blocks/music/MUSIC_WORKFLOW_PIPELINE.md`
2. `blocks/music/MUSIC_AGENT_STANDARD.md` when defining agent behavior, prompts, or output structure
3. `blocks/music/REFERENCES.md` when evaluating tools, donor solutions, or research directions

## Typical Modes

This block may route work into:

- static soundtrack generation;
- adaptive soundtrack generation;
- real-time interactive music;
- background music for short-form content;
- music for long-form video;
- game or application music systems;
- music-tool research;
- music licensing and platform-risk review;
- implementation handoff for a specific project.

## Typical Outputs

Typical outputs:

- music use-case definition;
- soundtrack brief;
- scene-to-music map;
- generation prompt package;
- tool comparison;
- export specification;
- legal and platform-risk checklist;
- project handoff packet;
- recommendation to create a narrower skill when a repeatable workflow becomes clear.

## Boundary

This block is the reusable central domain layer.

Keep project-specific tracks, prompts, implementation plans, API keys, final asset files, and production logs in the target project repository or its approved storage layer.

## Final Rule

Choose the smallest music workflow that solves the actual project need.

Do not confuse an interesting model with a validated product capability.