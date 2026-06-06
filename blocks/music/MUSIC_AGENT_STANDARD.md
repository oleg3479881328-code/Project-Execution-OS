# Music Agent Standard

## Purpose

This standard defines how an agent should reason and communicate during music-related work.

## Agent Behavior

The agent must:

- ask what role the music plays before recommending tools;
- distinguish static, adaptive, and real-time music needs;
- separate creative decisions from implementation decisions;
- identify missing constraints that materially affect the result;
- avoid claiming legal safety without checking current license and platform terms;
- avoid treating a model demo as proof of production readiness;
- produce outputs that another executor can implement or validate.

## Minimum Input Set

Capture only what is needed for the active task:

- target product or content format;
- musical role;
- duration or runtime behavior;
- mood and genre direction;
- instrumental or vocal requirement;
- scene, state, or transition requirements;
- platform or runtime constraints;
- export format;
- commercial-use context;
- budget or local-compute constraints when relevant.

## Default Output Structure

Use the smallest relevant structure:

1. goal;
2. music role;
3. constraints;
4. recommended path;
5. tool or model choice with rationale;
6. output specification;
7. validation checklist;
8. rights and platform caveats;
9. project handoff notes.

## Tool Evaluation Rule

When evaluating a music model or service, check:

- static vs adaptive vs real-time capability;
- input controls: text, audio, MIDI, API, application state;
- latency;
- local or cloud execution;
- hardware support;
- export options;
- integration path;
- license and commercial-use terms;
- reproducibility;
- implementation maturity;
- known limitations.

## Handoff Rule

A handoff is incomplete unless it identifies:

- what must be built or generated;
- what inputs are required;
- what assets and settings are preserved;
- what quality checks must pass;
- what legal or platform questions remain open;
- where project-specific state should be stored.

## Boundary

This standard does not replace a composer, audio engineer, legal review, or project-specific technical specification.

## Final Rule

Recommend a music workflow, not merely a fashionable model.