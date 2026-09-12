# Blender AI Production — PROJECT.md

## Project

- Name: `Blender AI Production`
- Type: AI-assisted 3D / VFX production pipeline project under SOFT
- Status: active — deep donor research consolidated, practical pipeline testing in progress
- Parent umbrella: `SOFT`

## Purpose

Build a reliable, economical, reusable production system in which a strong coordinator plans and reviews work while bounded executors operate Blender and adjacent media tools.

The pipeline is intended to combine deterministic 3D/VFX control with AI-assisted image/video processing rather than asking one expensive autonomous model to own a long Blender session end-to-end.

The first concrete acceptance case is the frozen-champagne shot: a foreground subject may move while the background and the champagne splash/droplets remain frozen at stable coordinates.

## Source Of Truth

Canonical project entrypoint:
- `projects/blender-ai-production/PROJECT.md`

Local agent / execution contract:
- `projects/blender-ai-production/AGENTS.md`

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
- PEOS Frame-Addressable Video Production:
  `../../blocks/video-production/FRAME_ADDRESSABLE_PRODUCTION.md`
- PEOS Generative Frame Production:
  `../../blocks/video-production/GENERATIVE_FRAME_PRODUCTION.md`
- AI Hands bounded-executor architecture:
  `../ai-hands/PROJECT.md`
- SOFT project entrypoint:
  `../soft/PROJECT.md`
- Existing Solution First:
  `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`

Key external primary / donor sources:

- User-supplied Pat Simmons video: https://youtu.be/-545TXdfrTQ
- Pat Simmons case-study article: https://www.aiformortals.co/blog/gpt-6-astra-blender-fallingwater
- Blender Lab official MCP Server: https://www.blender.org/lab/mcp-server/
- `ahujasid/blender-mcp`: https://github.com/ahujasid/blender-mcp
- `djeada/blender-mcp-server`: https://github.com/djeada/blender-mcp-server
- `PatrykIti/blender-ai-mcp`: https://github.com/PatrykIti/blender-ai-mcp
- `dcc-mcp/dcc-mcp-blender`: https://github.com/dcc-mcp/dcc-mcp-blender
- `jangtrinh/design-os-3d-blender`: https://github.com/jangtrinh/design-os-3d-blender
- `gaoypeng/3dcodebench`: https://github.com/gaoypeng/3dcodebench
- `ifBars/blender-agent-studio`: https://github.com/ifBars/blender-agent-studio
- `XliuXjianX/blender-production-skills`: https://github.com/XliuXjianX/blender-production-skills
- `RobLe3/cc-blender-skill`: https://github.com/RobLe3/cc-blender-skill
- `arjun988/blender-skills`: https://github.com/arjun988/blender-skills
- `AIGODLIKE/ComfyUI-BlenderAI-node`: https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node
- Pat Simmons `blender-production` package source: https://fallingwater-astra.vercel.app/blender-production.zip

Detailed strengths, risks, licenses, snapshot maturity signals and adoption decisions live in the Drive donor audit. Do not duplicate that full research in this entrypoint.

## Current Status

- Research from the source video, prior SOFT work, existing Blender/ComfyUI material and a deep GitHub donor sweep has been consolidated.
- The project is registered as a dedicated workstream instead of remaining a loose SOFT discussion.
- A practical zero-touch chain is already being tested in a neighboring work chat around Codex/local execution → Blender → render passes → ComfyUI → FFmpeg.
- That practical work must be reconciled into durable state; it must not be restarted merely because this project exists.
- No end-to-end production-quality frozen-champagne result is yet recorded here as verified.
- No live MCP implementation has yet been selected as final.
- Luna remains a candidate hands model, not a verified default executor.

## Done So Far

- Reused existing SOFT Blender, ComfyUI, frame-generation and subject-isolation research.
- Reused PEOS AI Hands controller/executor role split rather than inventing another generic agent runtime.
- Reused PEOS frame-addressable and generative-frame patterns for exact timing, local repair and incremental rerender.
- Completed a deeper GitHub donor sweep across MCP/control, production skills, deterministic/headless execution, validation/benchmarking and Blender↔ComfyUI integration.
- Identified official Blender Lab MCP as the official live-control baseline and `ahujasid/blender-mcp` as the maturity/community comparator.
- Identified `djeada/blender-mcp-server` as a strong donor for safe async/headless/physics execution and `PatrykIti/blender-ai-mcp` as a strong donor for typed macro/assertion control.
- Identified `jangtrinh/design-os-3d-blender` as the closest donor for structured deterministic hands execution and `gaoypeng/3dcodebench` as the benchmark-methodology donor for model/economics testing.
- Identified optional Blender↔ComfyUI donors without making embedded integration an MVP dependency.
- Corrected unverified donor names from prior chat so they cannot silently become project facts.
- Established a durable Drive folder, detailed donor audit, current state, log and project-local execution contract.

## Current Focus

Prove the smallest reliable execution architecture before synthesizing a custom production skill.

Target architecture:

```text
strong coordinator / reviewer
        ↓
bounded executor job
        ↓
appropriate hands model
        ├── LIVE: MCP for inspect / screenshot / targeted edit
        └── HEAVY: saved bpy script → isolated Blender headless process
        ↓
deterministic assertions + render evidence
        ↓
geometry / camera / physics / frozen FX / beauty-depth-normal-mask-ID passes
        ↓
ComfyUI via explicit API/file contract where AI processing adds value
        ↓
FFmpeg deterministic assembly
        ↓
visual + temporal QA
```

A cheaper executor model such as Luna may be evaluated in the hands slot, but only through the same acceptance contract and measured benchmark used for stronger executors.

## Next Practical Step

Do not restart the neighboring experiment.

1. Reconcile its current outputs/status into `PROJECT_STATE.md` and `logs/latest.md`.
2. Directly inspect Pat Simmons `blender-production.zip` before adopting anything from it.
3. Define one tiny deterministic benchmark job packet with scene truth + proof render.
4. Benchmark live control: official Blender Lab MCP vs `ahujasid/blender-mcp` and one production-oriented candidate.
5. Benchmark deterministic/headless execution using saved scripts + structured success/failure/evidence.
6. Adapt a small 3DCodeBench-style comparison for the hands model; test Luna only if it is technically available in the chosen execution surface.
7. Promote only proven donor patterns into a compact project Blender Production Skill.
8. Continue to the frozen-champagne acceptance shot.

## Key Decisions And Constraints

- `Existing Solution First` is mandatory: reuse/configure/integrate/adapt before building new Blender-agent infrastructure.
- Strong reasoning stays at the coordination/review layer; executor work should be bounded and testable whenever possible.
- Reuse `AI Hands` for the generic controller/executor contract rather than maintaining a competing agent framework.
- Reuse PEOS frame-addressable/generative-frame patterns for exact timing, local repair and incremental rerender.
- Do not infer that GPT-6 Astra is required merely because the source video used it.
- Do not treat MCP as the only execution path; use headless deterministic Blender jobs when that is safer or cheaper.
- Do not bulk-install donor skill libraries. Inspect and selectively reuse only relevant pieces.
- Do not copy donor code when licensing is missing/unclear; architecture patterns may be studied separately.
- One writer may mutate a given `.blend` scene at a time. Parallel agents may research/review but must not race scene writes.
- Preserve accepted `.blend` checkpoints before risky changes and save per phase for long jobs.
- Verify the active `.blend` file before mutation.
- Prototype simulations / FX at low resolution before expensive bake/render.
- Deterministic checks and visual evidence are both required. API success, validator success, object counts or agent self-report alone do not prove a correct shot.
- Prefer selective rerender of failed frame ranges over rebuilding an accepted sequence.
- Keep known defects/limitations explicit; do not hide physics/geometry defects with AI stylization.
- Blender MCP / generated Python can execute arbitrary local code. Use isolation, limited permissions, approved roots, backups and safe checkpoints.
- Keep Blender→ComfyUI boundary explicit (beauty/depth/normal/mask/ID + metadata) until embedded integration proves objectively useful.
- Do not claim the Pat Simmons `blender-production.zip` has been audited until its actual contents are inspected.
- Do not claim Luna economics or production readiness until task-specific benchmark evidence exists.
- Unverified names `RFingAdam`, `newo-ether`, and `comfyui-blender-temporal` are not project donors unless a real source is later established.

## Read Next

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `logs/latest.md`
4. Drive donor audit: https://docs.google.com/document/d/1_Ftr5qRFPhbPcjS1baNQ1kEZaYxVuohnmDQZFmklL3I/edit
5. `../../blocks/video-production/FRAME_ADDRESSABLE_PRODUCTION.md`
6. `../../blocks/video-production/GENERATIVE_FRAME_PRODUCTION.md`
7. Existing MCP research: https://docs.google.com/document/d/1NDScqwJL9V5j2Pyh_WijYh-aDay3aSMaWUfj-qyeEj8/edit
8. Frame-by-frame research: https://docs.google.com/document/d/1ws9EXpciQxrF1_A-p8UVB6BchxKgs8cli-qBtId41Us/edit
9. Subject-isolation research: https://docs.google.com/document/d/1Slck3DEFjxywm7iZ0vmSz9V0JoPcwOhopduC0wT-2s4/edit
10. `../ai-hands/PROJECT.md`
11. `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
