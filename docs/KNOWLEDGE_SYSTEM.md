# Knowledge System v1

## 1. Purpose

This document defines how Project Execution OS stores and promotes knowledge.

The goal is to prevent useful lessons from disappearing inside chats or one-off projects.

## 2. Knowledge Layers

Project Execution OS uses two knowledge layers:

```text
Project-local knowledge
→ Central reusable knowledge
```

## 3. Project-Local Knowledge

Every project has its own local library:

`projects/<project-id>/project-library/`

Purpose:

- store lessons from that specific project;
- preserve project-specific decisions;
- capture domain details;
- store reusable snippets that may or may not apply elsewhere.

Project-local knowledge is not automatically central knowledge.

## 4. Central Knowledge Library

Central reusable knowledge lives here:

`knowledge-library/`

Purpose:

- store patterns reusable across projects;
- store anti-patterns;
- store agent templates;
- store workflow lessons;
- store architecture decisions;
- store research methods;
- store reusable execution standards.

## 5. Promotion Rule

A project-local knowledge item can be promoted to central knowledge only if:

1. it is extracted in `08_KNOWLEDGE_EXTRACT.md`;
2. it is useful beyond one project;
3. it does not contain project-only noise;
4. it has clear reuse instructions;
5. it has been reviewed;
6. it is logged after promotion.

## 6. Knowledge Entry Types

Allowed central entry types:

```text
knowledge-library/patterns/
knowledge-library/anti-patterns/
knowledge-library/agent-templates/
knowledge-library/workflow-lessons/
knowledge-library/research-methods/
knowledge-library/architecture-decisions/
knowledge-library/execution-standards/
```

## 7. Required Knowledge Entry Format

Each knowledge entry should include:

```text
# <Title>

## Type

pattern / anti-pattern / agent-template / workflow-lesson / research-method / architecture-decision / execution-standard

## Source

Project:
Workflow run:
Source artifact:

## Problem

What problem this knowledge solves.

## Pattern / Lesson

The reusable idea.

## When To Use

Where this applies.

## When Not To Use

Where this does not apply.

## Adaptation Notes

How to adapt without blind copying.

## Risks

What can go wrong.

## Review Status

not_reviewed / reviewed_with_required_improvements / reviewed_passed / active
```

## 8. Decentralized Project Libraries

Each project keeps its own library even after central promotion.

Reason:

- project context must remain local;
- central library must stay clean;
- project-specific lessons may not generalize;
- future agents need both local and central memory.

## 9. Search Order For New Work

When starting or continuing a project, check knowledge in this order:

1. current project state;
2. current project workflow runs;
3. current project library;
4. central knowledge library;
5. external open-source and documentation research.

## 10. Anti-Dump Rule

The knowledge library is not a dumping ground.

Do not store:

- random chat fragments;
- unreviewed opinions as active rules;
- duplicated entries;
- project-only details in central library;
- giant unreadable prompt blobs without structure.

## 11. Central Library Activation

A central knowledge entry becomes active only after review.

Before review it may be stored as:

- draft;
- candidate;
- reviewed_with_required_improvements.

Active means approved for reuse.
