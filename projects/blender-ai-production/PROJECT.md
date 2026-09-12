# Blender AI Production — PROJECT.md

## Project

- Name: `Blender AI Production`
- Type: AI-assisted 3D / VFX production pipeline project under SOFT
- Status: active — research consolidated, practical pipeline testing in progress
- Parent umbrella: `SOFT`

## Purpose

Build a reliable, economical, reusable production system in which a strong coordinator plans and reviews work while bounded executors operate Blender and adjacent media tools.

The pipeline is intended to combine deterministic 3D/VFX control with AI-assisted image/video processing rather than asking one expensive autonomous model to own a long Blender session end-to-end.

The first concrete acceptance case is the frozen-champagne shot: a foreground subject may move while the background and the champagne splash/droplets remain frozen at stable coordinates.

## Source Of Truth

Canonical project entrypoint:
- `projects/blender-ai-production/PROJECT.md`

Current operational state:
- `projects/blender-ai-production/PROJECT_STATE.md`

Current work log:
- `projects/blender-ai-production/logs/latest.md`

Durable research / donor audit:
- https://docs.google.com/document/d/1_Ftr5qRFPhbPcjS1baNQ1kEZaYxVuohnmDQZFmklL3I/edit

Durable Drive project folder:
- https://drive.google.com/drive/folders/1tynpKSjLZHbEpU1jetSiwzI9vTzDBZtZ

## Source Trail

Existing internal research to reuse rather than repeat:

- MCP servers for video editors / Blender MCP comparison:
  https://docs.google.com/document/d/1NDScqwJL9V5j2Pyh_WijYh-aDay3aSMaWUfj-qyeEj8/edit
- AI Frame-by-Frame Video Generation:
  https://docs.google.com/document/d/1ws9EXpciQxrF1_A-p8UVB6BchxKgs8cli-qBtId41Us/edit
- Cinematic Subject Isolation Workflows:
  https://docs.google.com/document/d/1Slck3DEFjxywm7iZ0vmSz9V0JoPcwOhopduC0wT-2s4/edit
- SOFT project entrypoint:
  `../soft/PROJECT.md`
- Existing Solution First:
  `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`

External primary / donor sources:

- User-supplied Pat Simmons video: https://youtu.be/-545TXdfrTQ
- Pat Simmons case-study article: https://www.aiformortals.co/blog/gpt-6-astra-blender-fallingwater
- Blender Lab official MCP Server: https://www.blender.org/lab/mcp-server/
- `arjun988/blender-skills`: https://github.com/arjun988/blender-skills
- `RobLe3/cc-blender-skill`: https://github.com/RobLe3/cc-blender-skill
- `PatrykIti/blender-ai-mcp`: https://github.com/PatrykIti/blender-ai-mcp
- `djeada/blender-mcp-server`: https://github.com/djeada/blender-mcp-server
- Pat Simmons `blender-production` package source: https://fallingwater-astra.vercel.app/blender-production.zip

## Current Status

- Research from the video, prior SOFT work and existing Blender/ComfyUI material has been consolidated.
- The project is now registered as a dedicated workstream instead of remaining a loose SOFT discussion.
- A practical zero-touch chain is already being tested in a neighboring work chat around Codex/local execution → Blender → render passes → ComfyUI → FFmpeg.
- That practical work must be reconciled into this durable project state; it must not be restarted merely because this project was created.
- No end-to-end production-quality frozen-champagne result is yet recorded here as verified.

## Done So Far

- Reused the existing SOFT Blender, ComfyUI, frame-generation and subject-isolation research.
- Audited selected donor patterns from `arjun988/blender-skills` and `RobLe3/cc-blender-skill`.
- Identified the official Blender Lab MCP server as the first official baseline to benchmark.
- Captured the Pat Simmons/Astra workflow as a donor pattern rather than a model requirement.
- Recorded the preferred hybrid control pattern: MCP for live inspection/correction; `bpy`/saved Python for deterministic repeatable scene construction.
- Established a durable Drive folder and research/donor audit.

## Current Focus

Turn the current research and neighboring practical test into one repeatable production architecture with measurable acceptance gates.

Target architecture:

```text
strong coordinator / reviewer
        ↓
bounded executor jobs (current practical executor: Codex/local agent)
        ↓
Blender MCP + bpy/Python
        ↓
geometry / camera / physics / frozen FX / render passes
        ↓
ComfyUI where AI isolation/look processing is useful
        ↓
FFmpeg deterministic assembly
        ↓
visual + temporal QA
```

A cheaper executor model such as Luna may be evaluated as the hands layer, but it is not yet recorded as the verified executor of the current practical pipeline.

## Next Practical Step

Do not restart the experiment.

1. Reconcile the outputs/status of the already-running neighboring Blender/ComfyUI test into `PROJECT_STATE.md` and `logs/latest.md`.
2. Directly inspect the Pat Simmons `blender-production.zip` package before adopting anything from it.
3. Benchmark the official Blender Lab MCP server against the strongest community candidate on a tiny deterministic scene.
4. Extract only the donor skills/patterns that solve demonstrated gaps.
5. Use the frozen-champagne shot as the first real acceptance test.

## Key Decisions And Constraints

- `Existing Solution First` is mandatory: reuse/configure/integrate/adapt before building new Blender-agent infrastructure.
- Strong reasoning stays at the coordination/review layer; executor work should be bounded and testable whenever possible.
- Do not infer that GPT-6 Astra is required merely because the source video used it.
- Do not bulk-install donor skill libraries. Inspect and selectively reuse only the relevant pieces.
- One writer may mutate a given `.blend` scene at a time. Parallel agents may research/review but must not race scene writes.
- Preserve accepted `.blend` checkpoints before risky changes.
- Verify the active `.blend` file before mutation.
- Prototype simulations / FX at low resolution before expensive bake/render.
- Visual evidence is required. API success, object counts or script completion alone do not prove a correct shot.
- Prefer selective re-render of failed frame ranges over rebuilding an accepted sequence.
- Keep known defects/limitations explicit; do not hide failure behind materials, lighting or AI stylization.
- Blender MCP / generated Python can execute arbitrary local code. Use isolation, limited permissions, backups and safe checkpoints.
- Do not claim the Pat Simmons `blender-production.zip` has been audited until its actual contents are inspected.
- Do not claim Blender ↔ ComfyUI ↔ FFmpeg is production-ready until an end-to-end artifact and QA evidence are recorded.

## Read Next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. Drive donor audit: https://docs.google.com/document/d/1_Ftr5qRFPhbPcjS1baNQ1kEZaYxVuohnmDQZFmklL3I/edit
4. Existing MCP research: https://docs.google.com/document/d/1NDScqwJL9V5j2Pyh_WijYh-aDay3aSMaWUfj-qyeEj8/edit
5. Frame-by-frame research: https://docs.google.com/document/d/1ws9EXpciQxrF1_A-p8UVB6BchxKgs8cli-qBtId41Us/edit
6. Subject-isolation research: https://docs.google.com/document/d/1Slck3DEFjxywm7iZ0vmSz9V0JoPcwOhopduC0wT-2s4/edit
7. `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
