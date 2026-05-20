# Agent Library Standard

## Purpose

This standard defines a central reusable agent library for `Project Execution OS`.

The goal is to stop recreating the same agent roles from scratch while avoiding an uncontrolled pile of one-off agents.

## What The Library Stores

The library stores reusable agent role templates, not live runtime sessions.

It should preserve:

- reusable agent roles;
- stable agent contracts;
- orchestration patterns;
- review and evidence expectations;
- when-to-use and when-not-to-use rules.

It should not preserve:

- temporary chat participants;
- project-specific state;
- one-off experiments with no reuse value;
- implicit runtime memory.

## Three Layers

### 1. Library Agent

A reusable central template for a role such as:

- `Reviewer`
- `Research-Agent`
- `Documentation-Agent`
- `Orchestrator-Agent`

### 2. Project Agent

A project-local instance derived from a library role and adapted to a specific repository or workflow run.

### 3. Runtime Participant

A currently active named participant in a GitHub thread, chat, or execution loop.

## Best Patterns Adopted From Open Sources

The following patterns are explicitly adopted from well-known public multi-agent frameworks:

### Specialist-first roles

Use specialized agents that are strong at one task instead of overloading one general-purpose agent with every responsibility.

This matches OpenAI Agents SDK guidance to prefer specialized agents and focused prompts.

### Manager / Supervisor pattern

Use a central manager or supervisor when one role should keep overall control and call specialists for bounded subtasks.

This matches:

- OpenAI `agents as tools`
- LangGraph supervisor architecture

### Handoff pattern

Use handoff when routing itself is part of the workflow and the chosen specialist should temporarily own the next part of the interaction.

This matches:

- OpenAI handoffs
- AutoGen handoff design pattern

### Reviewer / Evaluator loop

Use a separate reviewer or evaluator role when correctness must be checked before acceptance.

This matches common iterative evaluation patterns described in OpenAI orchestration guidance and AutoGen reflection-style patterns.

### Minimal history rule

Do not pass every agent the full raw history by default.

Each agent should receive only the context it actually needs.

This is aligned with:

- OpenAI handoff input filtering
- LangGraph message-history control

## Default Architecture Rule

Default to the smallest useful multi-agent shape:

1. single agent if one role is enough
2. manager plus specialists if one role must keep control
3. handoff if ownership should move
4. reviewer added only when acceptance quality requires it

Do not start with complex agent swarms by default.

## Library Location

Central agent library:

`agent-library/`

Suggested structure:

```text
agent-library/
  README.md
  PROJECT_INDEX.md
  templates/
    _TEMPLATE/
      AGENT.md
    reviewer/
      AGENT.md
    research-agent/
      AGENT.md
    documentation-agent/
      AGENT.md
    orchestrator-agent/
      AGENT.md
```

## Required Agent Template Contract

Each reusable agent template should define:

```text
name:
role_type:
purpose:
when_to_use:
when_not_to_use:
default_orchestration_mode:
inputs:
outputs:
context_needed:
context_not_needed:
constraints:
handoff_rules:
review_rules:
evidence_rules:
failure_modes:
lifecycle_state:
version:
```

## Allowed Orchestration Modes

- `single_agent`
- `manager_calls_specialists`
- `handoff_to_specialist`
- `reviewer_loop`

More advanced patterns may exist later, but these are the standard starting set.

## Lifecycle

Allowed lifecycle states:

- `draft`
- `candidate`
- `reviewed`
- `active`
- `deprecated`
- `rejected`

No reusable agent template starts as `active`.

## Activation Rule

A central library agent becomes `active` only when:

1. the template exists in the library;
2. it has a clear reusable contract;
3. it has been used or reviewed in real workflow practice;
4. its risks and boundaries are documented;
5. its status is explicitly promoted.

## Memory And Context Rule

Library agents must declare the minimum context they need.

Do not assume:

- full repository read access by default;
- full conversation history by default;
- global project memory by default.

Pass only the smallest useful context slice.

## Project Instantiation Rule

When a project uses a library agent:

- copy or adapt the template into the project;
- bind it to the project scope;
- record project-specific constraints;
- keep the project instance separate from the central template.

## Sources

Primary public patterns used here:

- OpenAI Agents SDK:
  - `Agents`
  - `Agent orchestration`
  - `Handoffs`
- Microsoft AutoGen:
  - `AutoGen`
  - `Handoffs`
  - `Mixture of Agents`
- LangGraph:
  - `langgraph`
  - `langgraph-supervisor`
  - `prebuilt` and message-history control patterns
