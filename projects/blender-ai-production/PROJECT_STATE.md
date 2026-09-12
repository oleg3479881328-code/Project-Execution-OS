# Blender AI Production — PROJECT_STATE.md

## Status

- Project: `Blender AI Production`
- State: active
- Phase: deep donor consolidation + practical pipeline validation
- Updated: 2026-09-12

## Current Objective

Converge the already-started Blender/ComfyUI experiment and the verified donor landscape into one repeatable, economical, verifiable AI-assisted 3D/VFX production pipeline.

First acceptance case: frozen champagne — foreground subject moves while the background and champagne splash/droplets remain temporally frozen at stable coordinates.

## Current Architecture

The current preferred architecture is layered rather than one giant autonomous agent:

```text
Strong coordinator / planner / reviewer
        ↓
Bounded executor jobs
        ↓
Typed/macros when possible + saved bpy/Python when deterministic work is better
        ↓
LIVE PATH: Blender MCP for inspect / screenshot / targeted edits
HEAVY PATH: Blender headless process for simulation / bake / batch / long render
        ↓
Geometry / camera / physics / frozen FX / beauty-depth-normal-mask-ID passes
        ↓
ComfyUI for AI isolation/look processing where useful
        ↓
FFmpeg deterministic assembly
        ↓
Deterministic + visual + temporal QA
```

Current practical executor evidence: Codex/local agent in the neighboring test.

Candidate future cost optimization: evaluate a cheaper executor model such as Luna for narrow hands-only jobs after the control/verification contract is stable. This is a candidate, not a verified production fact. Acceptance criteria must remain unchanged regardless of executor price.

## Major Architecture Decision — Deep GitHub Sweep 2026-09-12

Do **not** select one repository as “the Blender agent.” The strongest existing solutions specialize by layer. Our best path is to reuse a small set of complementary donor contracts and build only thin project-specific glue.

### Layer A — Live Blender control / MCP

**Official baseline**
- Blender Lab MCP Server — official reference path; benchmark first.
- https://www.blender.org/lab/mcp-server/

**Maturity/community comparator**
- `ahujasid/blender-mcp` — MIT; approximately 28.3k GitHub stars / 2.6k forks at the 2026-09-12 snapshot.
- https://github.com/ahujasid/blender-mcp
- Treat popularity as maturity evidence, not proof that it best fits our safety/physics requirements.

**Safety/headless/async donor**
- `djeada/blender-mcp-server` — MIT.
- https://github.com/djeada/blender-mcp-server
- Important patterns: async jobs, polling/cancel, saved script library, headless transport for heavy Blender jobs, Safe Mode, approved roots, inline-code toggle, module blocklist, undo push, explicit fluid/physics stability guidance.

**Typed truth-first donor**
- `PatrykIti/blender-ai-mcp` — Apache-2.0.
- https://github.com/PatrykIti/blender-ai-mcp
- Important patterns: goal-first routing, compact tool surface, task-sized macros/workflows, deterministic measurements/assertions, scene snapshots/compare, relation/view diagnostics; vision is advisory rather than the final truth source.

**Full production ecosystem / escalation donor**
- `dcc-mcp/dcc-mcp-blender` — MIT; active 2026-09.
- https://github.com/dcc-mcp/dcc-mcp-blender
- 200+ typed tools, progressive skill loading, validation/publish pipeline, CLI/Codex integration, GUI main-thread + headless execution and E2E/CI infrastructure.
- Strong future candidate, but too broad to make the first MVP depend on it without evidence.

**Secondary Codex donor**
- `webita/blender-codex-mcp` — Codex-focused live workflow reference; useful inspect → one change → screenshot → refine discipline, but currently secondary to stronger/general control layers.

**Commercial/lazy-loading donor**
- `youichi-uda/blender-mcp-pro` — public addon/docs, proprietary MCP server.
- Main reusable idea for now: lazy/progressive tool loading to avoid flooding the executor with a giant surface.

### Layer B — Blender production skills / orchestration

**`ifBars/blender-agent-studio`**
- MIT; new project, active 2026-09.
- https://github.com/ifBars/blender-agent-studio
- Codex plugin with reproducible Blender workflows and specialist skills for MCP, modeling, animation, rendering, character, procedural, simulation, art direction, iterative refinement, validation and agent benchmarking.
- Strong idea: preserve both `.blend` and the Python that built it.
- Use as a skill/router/benchmark donor, not yet as proven infrastructure by popularity.

**`XliuXjianX/blender-production-skills`**
- https://github.com/XliuXjianX/blender-production-skills
- Production router + skills for native modeling, Geometry Nodes, simulation, material surfacing and geometry validation.
- Strong patterns: one router/state entrypoint, native Blender systems before unnecessary GN complexity, explicit phase/state/scoring artifacts, read-only third-party asset handling.
- GitHub metadata currently shows no license: study architecture, but do not copy implementation until licensing is resolved.

**`RobLe3/cc-blender-skill`**
- Keep as a core donor for professional assembly order, stable naming, chunked bpy execution, visual QA and `quality-refinement-autoloop`.

**`arjun988/blender-skills`**
- Keep as a selective donor for FX timing brief, proxy/low-resolution simulation, art-directed motion, bounded domains/particle counts and cache-before-final discipline.

**Pat Simmons `blender-production.zip`**
- Source verified: https://fallingwater-astra.vercel.app/blender-production.zip
- Package contents remain unaudited. Do not describe internals as confirmed until directly inspected.

### Layer C — Deterministic hands runtime / validation / benchmarking

**`jangtrinh/design-os-3d-blender`**
- MIT; created 2026-09-06; ~68 stars / 17 forks at current snapshot.
- https://github.com/jangtrinh/design-os-3d-blender
- Closest donor to our controller → hands architecture.
- Important patterns: verified bpy knowledge, structured `AGENT_OK` / `AGENT_FAIL`, deterministic headless passes, production gates, exact-revision evidence, explicit warning that a green validator does not equal visual fidelity.
- Important implication: the executor does not need a long live MCP conversation for every task. Many jobs can be written as bounded scripts, run headless, and return structured evidence.
- Documented shell path is macOS/Linux oriented; Windows adaptation must be tested.

**3DCodeBench — `gaoypeng/3dcodebench`**
- Apache-2.0; ~96 stars; paper released 2026-06.
- https://github.com/gaoypeng/3dcodebench
- 212 procedural Blender categories; single-shot, multi-turn and coding-agent settings; scoring includes executability, image similarity, 3D-shape distance and LLM judge; released raw logs include token/cost/status data and agent transcripts.
- This is now the preferred methodology donor for testing the economics hypothesis. Instead of assuming Luna is sufficient, adapt a tiny benchmark and measure executor pass rate, retries, wall time and cost.

**Agentic Blender Donut Benchmark — `erkantaylan/agentic-blender-donut-benchmark`**
- https://github.com/erkantaylan/agentic-blender-donut-benchmark
- Supporting qualitative evidence: self-reports can be wrong; visual checks are mandatory; long agents lose work without per-phase save discipline; durable journals/renders transfer knowledge between fresh agents; deterministic geometry can sometimes beat heavier physics.
- Use the failure lessons, not the literal ten-agent workflow.

### Layer D — Blender ↔ ComfyUI

**`AIGODLIKE/ComfyUI-BlenderAI-node`**
- GPL-3.0; ~1.5k stars / 104 forks at current snapshot.
- https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node
- Deep Blender/ComfyUI integration: ComfyUI nodes inside Blender, local/remote ComfyUI, render/viewport input, projected masks, depth, texture/material workflows, image exchange, AI mesh import/replace, interpolation/style-transfer examples.
- Strong optional integration donor, but large/complex. Do not make MVP depend on it while the explicit render-pass/API/file handoff remains adequate.
- GPL boundary matters if code is incorporated rather than simply used as an external tool.

**`Lectrov/BlenderComfyLink`**
- https://github.com/Lectrov/BlenderComfyLink
- Simple donor for beauty + ID/segmentation + depth + JSON metadata → ComfyUI.
- README says MIT but repository metadata did not surface a license; verify before code reuse.
- Old/small project; use as protocol/data-shape inspiration, not a preferred dependency.

## Data Hygiene Correction

Do not carry forward unverified donor names from chat as if they were sources.

Targeted GitHub searches did **not** verify the previously mentioned names:

- `RFingAdam`
- `newo-ether`
- `comfyui-blender-temporal`

Until an actual source is found, these are **UNVERIFIED / DO NOT USE**. Real verified alternatives are documented above.

## Current Donor Priority By Job

### Live connection benchmark

1. Official Blender Lab MCP — official baseline.
2. `ahujasid/blender-mcp` — ecosystem/maturity baseline.
3. `djeada/blender-mcp-server` — production safety/headless/async candidate.
4. `PatrykIti/blender-ai-mcp` — typed/macros/truth-first candidate.
5. `dcc-mcp/dcc-mcp-blender` — full-feature escalation option.

This is a benchmark queue, not a declared winner order.

### Hands runtime contract

Primary donor patterns:

1. `design-os-3d-blender` — headless + structured outcomes + evidence gates.
2. `djeada/blender-mcp-server` — async/headless scripts + safety controls.
3. `PatrykIti/blender-ai-mcp` — typed macros/assertions to reduce executor improvisation.

### Production skill synthesis

Build a **small internal production skill only after benchmark evidence**, selectively using:

- RobLe3 quality/refinement/orchestration;
- Xliu routing/state/simulation/validation patterns;
- Blender Agent Studio reproducibility + specialist routing + benchmark patterns;
- arjun988 FX/simulation discipline;
- Pat Simmons package after direct audit.

Do not copy whole libraries into the project.

### Blender → ComfyUI contract

MVP baseline remains explicit deterministic passes:

```text
beauty
+ depth
+ normal
+ mask / ID
+ structured object/shot metadata
→ ComfyUI API/file workflow
```

Only benchmark embedded integration after the current simple contract works reliably.

## Existing Work Reused

### Internal research

- Blender MCP and editor-control research:
  https://docs.google.com/document/d/1NDScqwJL9V5j2Pyh_WijYh-aDay3aSMaWUfj-qyeEj8/edit
- Frame-by-frame / Blender → ComfyUI research:
  https://docs.google.com/document/d/1ws9EXpciQxrF1_A-p8UVB6BchxKgs8cli-qBtId41Us/edit
- Subject-isolation / compositing research:
  https://docs.google.com/document/d/1Slck3DEFjxywm7iZ0vmSz9V0JoPcwOhopduC0wT-2s4/edit
- Detailed donor audit:
  https://docs.google.com/document/d/1_Ftr5qRFPhbPcjS1baNQ1kEZaYxVuohnmDQZFmklL3I/edit

### Practical test already underway

Known neighboring-chat test shape:

```text
Codex dispatcher
→ Blender scene build/render
→ Depth / Normal / Mask passes
→ ComfyUI via API
→ FFmpeg final MP4
```

This is active practical evidence, but the project has not yet received enough durable output evidence to mark the full chain verified. Reconcile results rather than restart.

## Frozen Champagne MVP — Acceptance Contract

A passing proof must demonstrate control, not merely aesthetics.

Required behavior:

1. foreground subject/action may move;
2. background must remain still after the freeze point;
3. champagne splash/droplets must retain stable coordinates and shape after the freeze point;
4. foreground/background/liquid occlusion must be plausible;
5. frame-to-frame continuity must be acceptable;
6. final sequence must be assembled reproducibly;
7. failed ranges should be replaceable without rebuilding accepted ranges.

Likely production path:

```text
source / subject isolation if needed
→ camera match / scene blockout
→ champagne FX low-res prototype
→ approve desired splash state
→ bake/freeze/convert accepted state to deterministic geometry or fixed particles
→ foreground action through frozen scene
→ beauty/depth/normal/mask/ID passes
→ optional ComfyUI processing
→ FFmpeg assembly
→ deterministic + visual + temporal QA
```

## Model / Economics Benchmark Requirement

The central hypothesis is now explicit:

> strong coordinator + cheaper bounded hands may outperform one expensive autonomous model economically without lowering output quality.

This is **not yet proven**.

Required measurements before making Luna the default hands model:

- task success/pass rate;
- number of retries;
- coordinator interventions/escalations;
- wall-clock time;
- model/API token cost;
- Blender simulation/render time separated from model time;
- correctness against deterministic assertions;
- visual acceptance rate;
- ability to resume/replay from saved scripts/checkpoints.

Adapt 3DCodeBench methodology plus our own Blender/physics tasks rather than relying on anecdotal impressions.

## Verification Ledger

### Confirmed / sufficiently researched

- Blender has mature Python automation and multiple MCP control options.
- Official Blender Lab MCP exists and should be benchmarked as the official baseline.
- `ahujasid/blender-mcp` is a very large/mature community comparator.
- `djeada/blender-mcp-server` provides directly relevant headless/async/safety patterns.
- `PatrykIti/blender-ai-mcp` provides directly relevant goal-first/macro/assertion patterns.
- DCC-MCP provides a broad typed production ecosystem and validates progressive skill loading / validation / headless ideas.
- `design-os-3d-blender` directly validates structured headless worker + evidence-gate architecture.
- 3DCodeBench provides a serious benchmark methodology for executor/model economics.
- Real Blender↔ComfyUI donors exist; AIGODLIKE is mature but embedded integration is optional for MVP.
- Prior internal research covers Blender/ComfyUI frame workflows and SAM2/BiRefNet-style subject isolation.
- A neighboring practical test is already exercising a Codex → Blender → passes → ComfyUI → FFmpeg architecture.

### Not yet verified in this project

- completed production-quality frozen-champagne video;
- completed end-to-end Blender ↔ ComfyUI ↔ FFmpeg run with preserved evidence;
- Luna as the actual executor in the current test;
- measured Luna vs stronger-executor quality/time/cost on our task contract;
- Pat Simmons package contents / compatibility / safety;
- best live MCP layer for the actual Windows + Blender environment;
- Windows adaptation of selected headless donor patterns;
- whether embedded Blender↔ComfyUI integration provides enough value to justify added complexity.

## Do Not Repeat

- Do not start a new general Blender-agent framework before benchmarking existing solutions.
- Do not bulk-install entire skill collections.
- Do not restart the current neighboring practical experiment from zero.
- Do not let multiple agents mutate the same `.blend` simultaneously.
- Do not spend on high-res FX/cache before low-res motion is accepted.
- Do not treat successful code execution or agent self-report as visual success.
- Do not hide physics/geometry defects with AI stylization.
- Do not expose a cheap executor to a giant unrestricted 100+ tool surface unless progressive discovery proves necessary.
- Do not make ComfyUI embedding a requirement while explicit pass/API handoff works.
- Do not carry unverified donor names from chat into architecture decisions.
- Do not claim production readiness without a concrete final artifact + QA evidence.

## Next Safe Actions

1. Pull durable evidence/results from the already-running neighboring practical test into this project state/log.
2. Inspect the actual Pat Simmons `blender-production.zip` donor package.
3. Define one tiny deterministic benchmark job packet with expected scene truth + proof render.
4. Benchmark the live path: official Blender Lab MCP vs `ahujasid/blender-mcp` and one production-oriented candidate.
5. Benchmark the deterministic/headless path using saved scripts + structured success/failure/evidence.
6. Add a small 3DCodeBench-inspired executor comparison for the hands slot; include Luna only if it is technically available in the chosen execution surface.
7. Promote only the winning/relevant donor patterns into our compact Blender Production Skill.
8. Run/finish the frozen-champagne MVP and record timing, cost, defects and selective-rerender behavior.

## Durable Locations

- Project entrypoint: `projects/blender-ai-production/PROJECT.md`
- Agent/executor contract: `projects/blender-ai-production/AGENTS.md`
- Current log: `projects/blender-ai-production/logs/latest.md`
- Drive folder: https://drive.google.com/drive/folders/1tynpKSjLZHbEpU1jetSiwzI9vTzDBZtZ
- Detailed research / donor audit: https://docs.google.com/document/d/1_Ftr5qRFPhbPcjS1baNQ1kEZaYxVuohnmDQZFmklL3I/edit
