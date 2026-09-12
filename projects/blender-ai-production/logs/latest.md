# Blender AI Production — latest log

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
