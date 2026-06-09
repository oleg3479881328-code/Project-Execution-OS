# Research Standard v2

## Purpose

This standard defines how Project Execution OS performs research before planning, implementation, or recommendation.

## Default Rule

Research must prefer verified existing solutions before new design or implementation when external or internal evidence is relevant.

Examples:
- existing project artifacts;
- Project Execution OS or CKL reusable artifacts;
- official documentation;
- GitHub repositories;
- open-source examples;
- RFCs or standards;
- YouTube demonstrations, tutorials, walkthroughs, reviews, and product/interface videos;
- other public evidence sources appropriate to the domain.

## Research Order

1. Existing repository artifacts
2. Existing project memory
3. Central reusable knowledge
4. Publicly verifiable external sources
5. Only then new synthesis or recommendation

For design, architecture, implementation, debugging, integration, tool setup, or workflow creation, expand step 4 in this preferred order:

1. official documentation;
2. official examples or reference implementations;
3. relevant GitHub repositories or open-source projects;
4. GitHub Issues or Discussions with real fixes;
5. manuals or technical guides;
6. YouTube demonstrations, tutorials, walkthroughs, reviews, and interface videos when practical usage, UX, workflows, or closed-source competitor behavior matters;
7. community discussions such as Reddit only as supporting practical evidence.

For UX/UI, product-discovery, workflow-discovery, competitor review, no-code tools, creator tools, video tools, design tools, AI product tools, browser extensions, Telegram apps, YouTube systems, and user-facing SaaS ideas, YouTube is a first-class research source.

YouTube evidence does not replace official documentation or source code when implementation correctness, API behavior, licensing, or security is being decided. It is strongest for product behavior, UX, market examples, practical workflows, and discovery of closed-source solutions.

## Output Requirements

Research artifacts should separate:
- confirmed facts;
- existing solutions checked;
- YouTube videos or channels checked when YouTube research was relevant;
- observed UX/workflow patterns;
- donor patterns selected if any;
- assumptions;
- recommendations;
- new custom work still required;
- open questions;
- risks.

## Smallest Useful Research

Do not over-research small tasks.

Use the smallest useful research effort that can support a safe next action.

## Reuse-First Rule

Follow `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`.

For technical and project-system tasks, it is mandatory to:

- search before invention;
- adapt before rebuilding;
- stop searching once a sufficiently adequate proven solution exists for the current task or MVP.

If no verified solution exists and the task depends on one, stop rather than inventing behavior.
