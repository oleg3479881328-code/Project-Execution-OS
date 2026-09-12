# Blender AI Production — Agent Instructions

## Required Entry Order

Before project work:

1. Read the global Project Execution OS `START_HERE.md`.
2. Follow `docs/ROUTER.md` to this project.
3. Read `projects/blender-ai-production/PROJECT.md`.
4. Read `PROJECT_STATE.md` when current execution state, continuation, prior tests or handoff context matter.
5. Read `logs/latest.md` when the latest result/blocker matters.
6. Load only the task-relevant deeper sources.

Do not reconstruct the project from chat memory when durable state exists.

## Authority And Roles

- The owner defines intent, desired visual outcome, constraints and priorities.
- The coordinator/controller owns architecture, task decomposition, acceptance criteria, escalation and final review.
- The executor is a bounded mechanical worker: it performs specified Blender/ComfyUI/FFmpeg actions, gathers evidence and reports results.
- The executor must not silently change project architecture, choose a new model/tool stack, relax acceptance criteria, or reinterpret the visual target.
- When a material decision is missing, stop at the decision boundary and report verified facts/options rather than inventing a new direction.

Reuse the AI Hands role contract rather than creating a second generic agent framework:
- `../ai-hands/PROJECT.md`
- `../ai-hands/AGENTS.md`

## Existing Solution First

Before creating an adapter, MCP bridge, Blender skill, simulation helper, QA loop or media execution utility:

1. check this project's donor audit;
2. check SOFT Master Software Inventory;
3. check the Video Production Block / capability registry when media execution is involved;
4. prefer official Blender APIs/MCP where they fit;
5. reuse/configure/integrate/adapt a proven donor before building custom code.

Do not bulk-install donor skill collections. Select only what solves a demonstrated gap.

## Blender Scene Mutation Contract

- Exactly one writer mutates a given live `.blend` at a time.
- Verify the active Blender file before mutation.
- Save a checkpoint before risky or broad changes.
- Use stable names for objects, materials, cameras, collections and render outputs.
- Prefer `bpy` / Blender data APIs and saved scripts for deterministic repeatable operations.
- Use MCP for live scene inspection, bounded actions, screenshots/renders and targeted corrections.
- Treat context-sensitive Blender operators carefully; do not assume UI context.
- Do not overwrite an accepted baseline with an experimental repair.

## Simulation / FX Contract

- Start with low-resolution or proxy simulation.
- Lock timing/composition before expensive bake/cache/render.
- Keep simulation domains and particle counts bounded.
- Bake/cache accepted simulation state before final rendering.
- For the frozen-champagne target, once the accepted splash state is chosen, the post-freeze liquid state must become deterministic/fixed rather than continuing fluid evolution.

## Frame / Video Production Contract

Reuse:

- `../../blocks/video-production/FRAME_ADDRESSABLE_PRODUCTION.md`
- `../../blocks/video-production/GENERATIVE_FRAME_PRODUCTION.md`

Key rules:

- use one canonical timeline/frame convention;
- keep shot/range boundaries explicit;
- approved state must be reproducible from durable project data;
- repair/rerender bounded frame windows or shot segments when possible;
- do not regenerate the whole film because one interval failed;
- final MP4 is a delivery artifact, not the editable source of truth.

## Validation Ladder

A step is not complete because code executed without error.

After meaningful mutations, validate in this order as applicable:

1. structural/data validation — expected objects, names, transforms, frame ranges, caches and output paths exist;
2. deterministic checks — frame counts, fixed coordinates, masks/passes, file existence, media probe;
3. visual checks — viewport screenshot, render still, contact sheet or sampled frames;
4. temporal checks — burst review around freeze/transition frames and neighbouring-frame comparison;
5. acceptance criteria — compare against the actual requested shot behavior.

If a visual/temporal defect remains, report failure honestly and preserve evidence.

## Failure / Refinement Loop

Adapt the reusable pattern from `RobLe3/cc-blender-skill` rather than blindly retrying:

1. freeze the last accepted baseline;
2. preserve the failed artifact;
3. capture the smallest evidence set that proves the failure;
4. classify the failure dimension;
5. check whether an existing skill/method already solves it;
6. improve/reuse the method before another broad rebuild when the same failure repeats;
7. repair only the affected artifact/range;
8. revalidate neighbours and downstream outputs.

## Executor Job Packet

Every bounded executor job should specify:

- job id / shot id / frame range;
- current accepted baseline/checkpoint;
- exact goal;
- allowed tools/actions;
- forbidden/destructive actions;
- input/reference paths;
- expected outputs;
- acceptance checks;
- maximum retry or escalation boundary;
- evidence to return.

Every executor response should return:

- what changed;
- commands/scripts/actions run;
- exact files/objects/ranges affected;
- renders/screenshots/reports produced;
- validation results;
- errors/warnings;
- whether acceptance passed;
- next recommended action or escalation.

## Cost And Efficiency Rule

The project intentionally separates expensive reasoning from mechanical execution.

- Keep coordinator reasoning focused on decisions, decomposition and review.
- Keep executor context narrow and task-specific.
- Persist state in project files/checkpoints instead of making long-running agents repeatedly reread huge chat histories.
- Measure actual wall time, retries, render time and model/API cost before claiming an architecture is cheaper.
- Luna or another lower-cost model may occupy the executor slot only after it passes the same execution/QA contract. Do not lower acceptance criteria to make a cheaper executor appear successful.

## Security

- Blender MCP / generated Python may execute arbitrary local code.
- Use isolated/test environments where practical.
- Limit filesystem/network access to what the task requires.
- Never expose credentials/secrets to executor prompts, logs or donor code.
- Require owner approval for destructive, privileged, credential-related, externally publishing or purchasing actions.

## Current First Acceptance Case

Frozen champagne.

After the freeze point:

- background does not move;
- accepted champagne splash/droplets preserve stable position and shape;
- approved foreground subject/action can continue moving;
- occlusion is plausible;
- no temporal pop/flicker at the freeze boundary;
- failed intervals can be replaced without rebuilding accepted intervals.

## Required Deeper References When Relevant

- Drive donor audit: https://docs.google.com/document/d/1_Ftr5qRFPhbPcjS1baNQ1kEZaYxVuohnmDQZFmklL3I/edit
- Video Production Block: `../../blocks/video-production/BLOCK.md`
- Frame-addressable production: `../../blocks/video-production/FRAME_ADDRESSABLE_PRODUCTION.md`
- Generative frame production: `../../blocks/video-production/GENERATIVE_FRAME_PRODUCTION.md`
- AI Hands: `../ai-hands/PROJECT.md`
- Existing Solution First: `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
