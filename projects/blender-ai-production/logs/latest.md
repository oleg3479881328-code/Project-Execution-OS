# Blender AI Production — latest log

## 2026-09-12 — Deep GitHub donor sweep + architecture refinement

### Owner intent

Preserve every useful finding from the deeper Blender GitHub search so future chats can continue from verified evidence rather than repeat research or inherit casual/hallucinated donor names.

### Research completed

The donor search was expanded by layer instead of looking for a single “best Blender agent.” Verified candidates now cover:

- live MCP/control;
- safe/headless/async execution;
- typed macro/assertion surfaces;
- Codex-native production skill suites;
- deterministic worker runtimes and production gates;
- model/executor benchmarking;
- Blender ↔ ComfyUI integration.

Detailed evidence and source links were appended to the canonical Drive donor audit:
https://docs.google.com/document/d/1_Ftr5qRFPhbPcjS1baNQ1kEZaYxVuohnmDQZFmklL3I/edit

### Newly elevated donors

**`ahujasid/blender-mcp`**
- very large community baseline; MIT; ~28.3k stars / 2.6k forks at the 2026-09-12 snapshot;
- use as the maturity/community comparator against official Blender Lab MCP.

**`djeada/blender-mcp-server`**
- important for our exact workflow because it combines async jobs, reusable Blender scripts, headless execution, Safe Mode, undo and explicit physics stability guidance;
- strongest current donor for safe heavy/batch/simulation execution patterns.

**`PatrykIti/blender-ai-mcp`**
- goal-first routing, compact/search-first tool surface, task-sized macros and deterministic assertions;
- strongest current donor for making a cheap executor behave as bounded “hands” rather than an autonomous architect.

**`dcc-mcp/dcc-mcp-blender`**
- 200+ typed tools, progressive skill loading, CLI/Codex path, validation/publish pipeline, headless + GUI execution and E2E/CI;
- strong full-production/escalation donor, but deliberately not selected as MVP dependency because it is broader than the first acceptance case requires.

**`ifBars/blender-agent-studio`**
- Codex plugin for reproducible Blender work;
- discovered specialist skills for MCP, modeling, animation, rendering, characters, procedural, simulation, art-direction intake, iterative refinement, asset validation and benchmarking;
- valuable idea: preserve the `.blend` and the Python that built it.

**`XliuXjianX/blender-production-skills`**
- production router + specialist skills for native modeling, GN, simulation, materials and validation;
- strong state/routing/simulation donor;
- current GitHub metadata exposes no license, so architecture can be studied but implementation must not be copied until licensing is resolved.

**`jangtrinh/design-os-3d-blender`**
- closest donor to our controller → hands runtime;
- structured `AGENT_OK` / `AGENT_FAIL`, headless passes, production gates, exact-revision evidence and explicit separation between green validator output and visual fidelity;
- establishes that many worker jobs can be deterministic headless scripts instead of long live MCP conversations.

**3DCodeBench — `gaoypeng/3dcodebench`**
- serious benchmark methodology: 212 categories, single/multi-turn/coding-agent modes, executability/image/3D scoring and token/cost logs;
- selected as methodology donor for measuring whether Luna/cheap hands actually save money while maintaining quality.

**`AIGODLIKE/ComfyUI-BlenderAI-node`**
- mature GPL Blender↔ComfyUI integration with render/viewport inputs, masks, depth, texture/material and interpolation workflows;
- useful optional integration, but deliberately not selected as an MVP requirement while simple render-pass/API handoff remains adequate.

**`Lectrov/BlenderComfyLink`**
- useful lightweight protocol idea: base render + ID/segmentation + depth + object JSON → ComfyUI;
- use primarily as data-contract inspiration, not as a preferred dependency.

### Data-hygiene correction

The prior casual conversation mentioned `RFingAdam`, `newo-ether`, and `comfyui-blender-temporal` as if they were donors. Targeted GitHub searches did not verify those exact sources.

They are now explicitly marked:

`UNVERIFIED / DO NOT USE UNTIL A REAL SOURCE IS FOUND`

This was recorded in both the detailed donor audit and current project state to stop future chats from compounding the error.

### Architecture refined

The project no longer treats “MCP” as the only executor path.

Preferred execution model is now:

```text
strong coordinator
  ↓
bounded job packet
  ↓
cheap/appropriate hands model
  ├─ LIVE PATH: MCP for inspection, screenshot, small targeted edits
  └─ HEAVY PATH: saved bpy script → separate Blender headless process
  ↓
deterministic assertions + render evidence
  ↓
beauty/depth/normal/mask/ID passes
  ↓
ComfyUI via explicit API/file contract
  ↓
FFmpeg assembly
  ↓
visual + temporal QA
```

This is a material architectural improvement: expensive simulation/bake/batch work does not need to stay inside a long conversational agent loop.

### Economics decision

Do not claim that Luna is cheaper/better merely because it receives smaller tasks.

A benchmark is now required. Measure:

- pass rate;
- retries;
- coordinator interventions;
- wall time;
- model/API cost;
- Blender simulation/render time separately;
- deterministic assertion pass rate;
- visual acceptance rate;
- replay/resume success from scripts/checkpoints.

Use a small 3DCodeBench-inspired harness plus the project’s own physics/frozen-champagne microtasks.

### Updated donor strategy

Do not install one monolithic Blender-agent solution.

Use complementary donor patterns:

- **live transport benchmark:** official Blender Lab MCP + ahujasid + one production-oriented candidate;
- **hands runtime:** design-os headless contract + djeada safety/async/headless patterns;
- **truth layer:** Patryk typed macros/assertions;
- **production skill synthesis:** RobLe3 + Xliu + Blender Agent Studio + selective arjun988 + Pat Simmons after package audit;
- **Comfy boundary:** explicit render passes/metadata first; embedded ComfyUI only if benchmarked value is clear;
- **economics benchmark:** 3DCodeBench methodology.

### Verification boundary remains

Still not verified:

- completed production-quality frozen-champagne artifact;
- final live MCP winner on the owner’s Windows/Blender environment;
- Luna as hands executor;
- measured cheap-hands economics;
- Pat Simmons skill ZIP contents;
- Windows adaptation of selected headless scripts;
- objective benefit of embedded Blender↔ComfyUI integration.

### Next action

1. Reconcile output/evidence from the neighboring practical test — do not restart it.
2. Inspect Pat Simmons `blender-production.zip` directly.
3. Define one tiny deterministic benchmark job packet.
4. Benchmark live transport and headless execution paths.
5. Run a 3DCodeBench-inspired hands-model comparison.
6. Promote only proven patterns into the compact project Blender Production Skill.
7. Continue into the frozen-champagne acceptance shot.

---

## 2026-09-12 — Project bootstrap + donor consolidation

### Owner intent

Stop treating Blender/ComfyUI work as scattered chat experiments. Make it a durable project so another chat/executor can recover the state, reuse prior research and continue without reconstructing context from memory.

### Project created

- Canonical PEOS project path: `projects/blender-ai-production/`
- Drive project folder: https://drive.google.com/drive/folders/1tynpKSjLZHbEpU1jetSiwzI9vTzDBZtZ
- Durable donor/research audit: https://docs.google.com/document/d/1_Ftr5qRFPhbPcjS1baNQ1kEZaYxVuohnmDQZFmklL3I/edit

### Existing Solution First work completed

Reused existing internal research rather than starting from scratch:

- `MCP-серверы для видеоредакторов`
- `AI Frame-by-Frame Video Generation`
- `Cinematic Subject Isolation Workflows`
- current SOFT Blender / ComfyUI inventory knowledge
- neighboring practical zero-touch Blender/ComfyUI test context

External donors reviewed or identified:

- official Blender Lab MCP Server — official baseline
- Pat Simmons / GPT-6 Astra Blender production case study
- `arjun988/blender-skills`
- `RobLe3/cc-blender-skill`
- `PatrykIti/blender-ai-mcp`
- `djeada/blender-mcp-server`
- Pat Simmons `blender-production.zip` — located but package audit still pending

### Main architecture decision

Do not copy the source video's one-large-autonomous-agent pattern as the default operating model.

Use:

```text
strong coordinator / reviewer
→ bounded executor
→ Blender MCP for live inspection/action
→ bpy/saved Python for deterministic work
→ render passes
→ ComfyUI only where AI processing adds value
→ FFmpeg deterministic assembly
→ visual/temporal QA
```

Current practical executor evidence is Codex/local agent. Luna is a candidate future low-cost hands layer, not yet a verified current executor.

### Donor patterns selected

From `arjun988/blender-skills`:

- low-res/proxy FX before expensive simulation;
- explicit timing brief;
- art-direct motion before final cache;
- cache before final render;
- controlled simulation domains / particle counts.

From `RobLe3/cc-blender-skill`:

- plan/blockout/camera/light/refine/render/composite/export order;
- stable naming and chunked bpy operations;
- numerical checks + visual screenshot/render validation;
- preserve accepted baseline and failed evidence;
- failure-classification / refinement loop instead of blind retry.

From Pat Simmons case study:

- research → PRD → fresh build context → execute → QA → correction → milestone files;
- MCP + bpy hybrid;
- single-writer discipline and checkpoints are important;
- large autonomous sessions can be very expensive and still leave substantial defects.

### First acceptance case

Frozen champagne.

A passing proof must show that, after the freeze point:

- the background is stable;
- champagne splash/droplets stay at stable coordinates and shape;
- approved foreground subject/action may continue moving;
- occlusion and temporal continuity are acceptable;
- failed frame ranges can be regenerated without rebuilding accepted ranges.

### Verification boundary

Do not yet claim:

- production-ready Blender ↔ ComfyUI ↔ FFmpeg pipeline;
- finished frozen-champagne output;
- Luna validated as hands executor;
- Pat Simmons skill package audited;
- final choice of Blender MCP server.

### Next action

Reconcile durable evidence from the already-running neighboring practical test, then inspect the Pat Simmons package and benchmark the official Blender MCP against the strongest community alternative on a tiny deterministic scene. Do not restart the current test.
