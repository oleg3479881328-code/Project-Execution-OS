---
project_name: Project Execution OS
project_mode: compact
status: transfer_ready
updated_at: 2026-06-24
source_of_truth: repository
active_branch: main
---

# PROJECT_STATE.md

## Current State

`Project Execution OS` is an active central project and is prepared for transfer to another executor.

The repository uses the minimum active continuity set required by `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`:

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

## Latest Confirmed Milestone

- Added candidate central skill `gemini-tts-speech-generation`.
- Skill path: `skills/audio/gemini-tts-speech-generation/SKILL.md`.
- References path: `skills/audio/gemini-tts-speech-generation/references.md`.
- Registry updated: `skills/registry.md`.
- Source checked: Gemini API speech generation / TTS documentation, 2026-06-24.
- Observed official source last-updated marker: 2026-06-22 UTC.
- Lifecycle state: `candidate`.
- Review state: `not_reviewed`.
- The skill is not active until Project Execution OS review promotes it.
- Creation commits: `c5cf946a37cf21084af3af9703833bd646de67d5`, `b90d66355b287b606b9e12a4a5f03ed9af252a5b`, `f23e90ea38a325dd8bc6ae4f577ece1bd9d510db`.

## Current Focus

Keep the central project internally consistent and transfer-ready after every meaningful change.

## Current Next Safe Action

No implementation task is currently active.

Next safe action for the new skill is a formal review under `docs/SKILL_REVIEW_STANDARD.md`; until then, use it only as a candidate reference.

When a new task arrives:

1. enter through `START_HERE.md`;
2. follow `docs/ROUTER.md`;
3. read `PROJECT.md`, then this file and `logs/latest.md`;
4. perform only the smallest justified change;
5. update `PROJECT_STATE.md` and `logs/latest.md` after the meaningful step.

## Active Files For Re-entry

Read in this order when resuming central-project work:

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT.md`
4. `PROJECT_STATE.md`
5. `logs/latest.md`
6. `PROJECT_INDEX.md` only when broader navigation is needed
7. routed standards only when the active task requires them

## Known Blockers

- `PROJECT_INDEX.md` still needs a curated canonical-documents entry for `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` during the next safe large-index maintenance pass. Generated indexes already detect the new document automatically.
- `gemini-tts-speech-generation` is registered as `candidate` / `not_reviewed`; it must not be treated as active until reviewed.

## Do-Not-Break Rules

- Do not bypass `START_HERE.md` as the stable top-level entrypoint.
- Do not replace `docs/ROUTER.md` with duplicated navigation logic elsewhere.
- Do not treat chat memory as durable project truth.
- Do not add files, folders, or architectural layers ritualistically.
- Do not claim execution without a confirmed repository event.
- Preserve the smallest sufficient context-loading path.
- Update this file and `logs/latest.md` after every meaningful central-project change.
