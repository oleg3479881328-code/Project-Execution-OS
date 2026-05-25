# External Pattern Research Module

## Status

`candidate`

## Purpose

Evaluate an outside repository, product, workflow, public tool, or architecture pattern and determine whether selected ideas deserve adaptation into an existing Oleg system or project.

## When To Use

Use for an external repository, public product pattern, open-source workflow, plugin/skill collection, architecture pattern, automation approach, template system, or donor solution being evaluated for reuse in Project Execution OS, CKL, Agent Network OS, Website Design System, Chrome extension work, or another named existing project.

## When Not To Use

Do not use for a simple factual explanation with no reuse decision, a new-project startup route, already-approved implementation work, or a link that only needs lightweight preservation without evaluation.

Stop researching when an adequate donor already covers the practical MVP need and more comparison would only delay execution.

## Available Skills

- `external-pattern-evaluation` — evaluates one donor source, identifies reusable patterns, separates evidence from recommendations, and gives a promotion decision.

## Available Commands

- `/research-external-pattern` — evaluates one external source for possible adaptation into a named existing system or project.

## Connector Requirements

No connector is assumed. Read or write access must be checked at the moment a real action needs it. Without write access, this module may still produce an analysis in chat but cannot claim durable recording occurred.

## Output Boundary

Allowed outputs:

- analysis and recommendation;
- reference capture after explicit preservation direction;
- candidate standard or candidate reusable pattern after explicit promotion direction;
- bounded execution handoff after implementation is already decided.

Forbidden behavior:

- silently promoting an external reference into a binding standard;
- claiming a save, update, or implementation without confirmed execution;
- expanding platform architecture before a real repeated need proves it.

## Evidence / Source Pattern

Structural inspiration: `https://github.com/anthropics/knowledge-work-plugins`, especially its separation of manifest files, connector declarations, reusable skills, and explicit commands.

Related internal records:

- `Reference-Idea-Library/references/anthropic-knowledge-work-plugins.md`
- `docs/AGENT_MODULE_FORMAT_STANDARD.md`

## Validation Record

No completed validation case yet. This module remains `candidate` until it is used on a new real external-pattern evaluation and the outcome is recorded.
