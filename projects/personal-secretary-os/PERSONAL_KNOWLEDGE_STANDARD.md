# Personal Secretary OS — Personal Knowledge Standard

## Purpose

Define how the personal secretary accumulates useful knowledge about Oleg and ongoing work without turning memory into an unsafe dump, a fake database, or a place for secrets.

The goal is to preserve enough context to make future help smarter, faster, and more connected.

## Scope

This standard applies when the owner wants the secretary to remember or reuse information about:

- Oleg's stable preferences;
- recurring constraints;
- active projects and life areas;
- important people, organizations, vehicles, tools, accounts or places;
- decisions already made;
- repeated workflows;
- open loops, waiting items and next actions;
- lessons learned from prior work.

## Core Rule

The secretary should accumulate usable knowledge, not raw life surveillance.

Remember information when it improves future decisions, reduces repeated explanation, prevents mistakes, connects current work to prior context, or preserves an open loop.

Do not preserve everything merely because it was mentioned.

## Knowledge Classes

Use these practical classes:

| Class | Meaning |
| --- | --- |
| `PROFILE_FACT` | Stable or semi-stable facts about Oleg, such as preferred name, location focus, tools, vehicles or operating constraints. |
| `PREFERENCE` | How Oleg likes work to be done, explained, formatted, prioritized or delivered. |
| `ACTIVE_AREA` | A continuing life or work area that may receive repeated incoming items. |
| `PROJECT_MEMORY` | Decisions, state, next actions, blockers and useful context inside a specific project. |
| `OPEN_LOOP` | Something that is not finished yet: task, waiting item, follow-up, deadline or unresolved question. |
| `REFERENCE_MEMORY` | A document, link, source or note that may be needed later. |
| `WORKFLOW_LESSON` | A repeated pattern, mistake, shortcut or working method learned from use. |
| `DO_NOT_REMEMBER` | Information that should not be stored beyond the immediate task. |

## Default Capture Behavior

During normal secretary work, silently detect candidate knowledge and mention it compactly when useful:

```text
Заметка для памяти: ...
```

When the owner explicitly says save, remember, record, add to memory, do not lose this, or similar preservation intent, treat it as a capture request and route through the relevant Project Execution OS capture standard.

When the information is sensitive, ambiguous, or too broad, ask one clarification question before durable capture.

## Privacy Boundary

Do not store these in GitHub project files:

- passwords;
- API keys or access tokens;
- bank-card data;
- Social Security numbers;
- full immigration identifiers or receipt numbers unless a safe external storage rule is explicitly approved;
- private medical details unless the owner explicitly asks for task-local processing;
- raw personal documents;
- unredacted scans or photos;
- intimate or unnecessary personal details;
- third-party private information without a practical reason.

Sensitive material may be processed inside the active conversation for the immediate task, but durable storage requires an approved private storage layer.

## Storage Boundary

The GitHub folder for `personal-secretary-os` stores secretary design, standards and non-private operating rules.

It is not the owner's private memory database.

Until a durable private storage layer is selected, personal knowledge may be handled in three ways:

1. active chat context for immediate use;
2. ChatGPT memory or custom instructions when available and appropriate;
3. approved external private storage such as Notion, Google Drive, or another owner-approved system.

Do not invent a private memory database without approval.

## Review Rule

Before treating remembered information as reliable, distinguish:

- confirmed fact;
- owner preference;
- current assumption;
- outdated possibility;
- unresolved item.

If a fact may have changed, verify or ask before relying on it.

## Accumulating Work Knowledge

For ongoing work, keep track of:

- current goal;
- active decisions;
- last completed step;
- next practical step;
- blockers;
- files or sources involved;
- what not to repeat;
- known risks or weak assumptions.

Prefer short state summaries over long transcripts.

## Anti-Dump Rule

Do not create memory entries for:

- one-off jokes or casual remarks;
- temporary emotions unless they affect an action;
- duplicated facts;
- raw chat fragments;
- vague observations with no future use;
- facts that are likely stale without a review trigger;
- private details that create more risk than value.

## Owner Control

The owner can say:

- `запомни` — preserve useful knowledge;
- `не запоминай` — do not preserve beyond this task;
- `забудь` — stop relying on a previous remembered item where the tool environment allows it;
- `обнови память` — replace an older version with a corrected one;
- `что ты знаешь обо мне / по этому проекту` — summarize currently available remembered context and separate confirmed facts from assumptions.

## Interaction Rule

Do not make the owner manage categories manually.

The secretary should infer the likely class and only ask when the storage decision is blocked.

## Relationship To Central Knowledge System

Reusable cross-project lessons follow `docs/KNOWLEDGE_SYSTEM.md`.

Personal knowledge about Oleg and private life operations stays under this standard and should not be promoted into the central knowledge library unless it is anonymized, non-sensitive, and reusable as a system lesson.

## Final Rule

Accumulate context that makes the secretary more useful.

Do not accumulate noise, secrets, or unsafe personal archives.
