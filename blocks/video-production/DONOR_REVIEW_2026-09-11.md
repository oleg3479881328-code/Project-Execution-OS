# Video Production Donor Review — 2026-09-11

## Scope

Compare four relevant pieces of the current PEOS/SOFT video stack:

1. `Vincentwei1021/anything2explainer`
2. `Vincentwei1021/video-talkcraft`
3. `kajisho5/ffmpeg-skill`
4. Project Execution OS `blocks/video-production`

The goal is not to choose one product. The goal is to identify the smallest proven pieces that should shape our own Video Factory.

## Executive Decision

Use a layered composition rather than adopting any donor wholesale.

Recommended direction:

```text
PEOS Video Production Block = orchestration / decisions / policy
Remotion = frame-addressable visual renderer
our own shot + beat + keyframe data model = source of truth
video-talkcraft patterns = incremental rendering + QA + workbench donor
anything2explainer patterns = explainer workflow + frame/beat storyboard donor
ffmpeg-skill = media execution / finishing / verification donor
```

Do not make `anything2explainer` or `video-talkcraft` runtime dependencies for commercial use without license authorization.

## Comparison Matrix

| Dimension | anything2explainer | video-talkcraft | ffmpeg-skill | PEOS Video Production |
|---|---|---|---|---|
| Primary role | topic/article -> complete explainer | narration+voice -> motion-designed explainer | deterministic media operations | orchestration/domain decisions |
| Rendering core | Remotion | Remotion | FFmpeg | tool-neutral |
| Exact frame control | strong | strong | strong for media operations, weaker as complex motion authoring layer | not yet formalized before this review |
| Timeline source | narration sentence/frame ranges | word/sentence alignment + shot timing | measured media timeline | project-dependent |
| Motion authoring | custom code + shared primitives | reusable motion-card library + camera systems | filters/overlays/transforms | documented patterns only |
| Incremental shot rendering | limited/basic compared with talkcraft | strong cached per-shot rendering | operations can be incremental but not a shot-authoring system | not yet standardized |
| Review/QC | stills + motion density + build/QC rules | machine gates + anchor/burst/contact-sheet review | probe/check/look/contact sheet | validation principles |
| Owner editing UI | no general workbench | workbench exists | CLI/MCP/tool surface | none canonical |
| Commercial license | noncommercial toolkit | noncommercial toolkit | MIT | internal |
| Best donor value | explainer production choreography | reusable frame-production engine ideas | media hands + verification | overall control plane |

## anything2explainer — What To Reuse Conceptually

### Strong donor patterns

- User confirmation before expensive stages.
- Narration becomes an exact frame timeline before scene coding.
- Storyboard rows include frame ranges and semantic beat anchors.
- Content shots are isolated `Sequence` ranges.
- Visual state is computed from current frame.
- Motion helpers use explicit keyframes and interpolation.
- Each sentence/beat has a visual action rather than static slide replacement.
- Preview is rendered before parallel full build.
- Motion-density checks detect long static sections.

### What Not To Adopt As Core

- fixed black/purple design language;
- a single 1280×720 explainer format;
- assumptions tied to Chinese TTS;
- donor-specific folder/group naming;
- noncommercial toolkit code as commercial dependency.

### Main lesson

The storyboard is not descriptive prose. It is an executable timing contract.

A row such as:

`shot SC04 -> frames 446–612 -> beat 463 -> beat 499 -> beat 534 -> beat 588`

is enough to drive deterministic visual states and validation.

## video-talkcraft — What To Reuse Conceptually

### Strongest donor patterns

- word-level audio alignment;
- separation of absolute time, shot-local narrative time, and Sequence-local time;
- explicit conversion helpers so timing systems do not drift;
- semantic-beat storyboarding instead of one-new-element-per-sentence;
- motion-card taxonomy;
- camera/motion systems separated from card visuals;
- shot-segment master rendering;
- change one shot -> re-render shot ± neighbours;
- final frame-count assertions;
- master audio rendered/muxed once rather than encoded into every segment;
- still batches, burst checks, and contact sheets;
- editable workbench over structured project data.

### Why It Is The Stronger Engine Donor

`anything2explainer` is a stronger end-to-end explainer recipe.

`video-talkcraft` is a stronger reusable production-engine donor because it makes iteration speed, exact timing, reusable motion vocabulary, segment caching, and owner editing first-class concerns.

### Main lesson

The renderer and the editor should share one structured project model.

Do not let the workbench become a second timeline format.

## ffmpeg-skill — What To Reuse / Adopt

### Strong donor patterns

- probe before action;
- structured operations instead of raw shell/filter strings from the agent;
- stream-copy/lossless operations when possible;
- dry-run before destructive/expensive execution;
- machine-readable contracts/results;
- no input overwrite;
- technical verification after render;
- contact-sheet review when visual output changed;
- local-first operation;
- MIT license.

### Correct Role

`ffmpeg-skill` should be treated as media execution infrastructure, not as the primary motion-design engine.

Best placement:

```text
Remotion shot renderer
-> shot mp4 segments
-> ffmpeg-skill / FFmpeg
   concat
   mux master audio
   normalize
   adapt aspect/delivery
   verify
```

## PEOS Gap Found

Before this review, the Video Production Block had the correct domain principle — repeatable pipeline + composable capability blocks — but did not explicitly define a reusable frame-addressable authoring model.

That gap is now captured in:

`blocks/video-production/FRAME_ADDRESSABLE_PRODUCTION.md`

## Recommended Modules For Our Video Factory

### Module A — Narrative Alignment

Input:

- script
- audio

Output:

- sentences/tokens with exact time/frame anchors

### Module B — Shot Graph

Input:

- aligned narrative
- design plan

Output:

- stable shot IDs
- frame ranges
- asset dependencies
- semantic purpose

### Module C — Beat Timeline

Within every shot:

- frame/time anchor
- visual event
- optional SFX event
- optional subtitle/token anchor

### Module D — Keyframe/Motion Layer

Stores editable animation parameters independently from renderer components.

### Module E — Motion Recipes

Reusable recipes such as:

- slide/pop/fade;
- draw-on line/arrow;
- counter;
- callout/highlight;
- camera push/pull;
- browser/document tour;
- comparison split;
- diagram flow;
- image pan/zoom;
- chart reveal;
- transition families.

Do not copy donor code under incompatible licensing. Implement our own recipes or use permissively licensed components.

### Module F — Frame Renderer

Remotion-based deterministic renderer.

Requirements:

- render full shot;
- render exact frame;
- render list of frames;
- render low-res preview;
- accept structured project/shot data.

### Module G — Incremental Render Cache

Cache per-shot outputs and invalidate only changed shots and transition neighbours.

### Module H — Media Finishing

Use FFmpeg/ffmpeg-skill-style operations for concat/mux/export/verification.

### Module I — Frame QC

- anchor stills;
- transition bursts;
- motion/stillness sampling;
- contact sheets;
- subtitle safe-zone checks;
- technical media probe.

### Module J — Owner Workbench

Minimum future UI:

- timeline scrubber;
- exact frame number;
- shot list;
- canvas preview;
- mouse move/scale/rotate/crop;
- set/remove keyframe;
- easing selector;
- shot-only preview;
- before/after;
- render current frame;
- render current shot;
- export assembled video.

## Recommended Validation Project

Do not start with a 3–5 minute film.

Build an internal 30–45 second test:

- 5–8 shots;
- 30 fps;
- one narration/audio track;
- one diagram shot;
- one image/B-roll shot;
- one typography/data shot;
- one multi-beat shot with at least 3 exact beat anchors;
- one transition that overlaps neighbouring shots;
- one deliberately changed shot to prove incremental re-render;
- final FFmpeg concat/mux/verification.

Acceptance criteria:

1. any named frame can be rendered to a still;
2. frame N is deterministic across renders;
3. shot boundaries are frame-exact;
4. changing one shot does not require a full visual rebuild;
5. master audio remains sample/frame aligned after reassembly;
6. final frame count matches the project duration contract;
7. contact-sheet review finds no layout/safe-zone failure;
8. source project remains editable without touching raw rendered frames.

## License Boundary

- `anything2explainer`: PolyForm Noncommercial; commercial toolkit use requires authorization.
- `video-talkcraft`: PolyForm Noncommercial; commercial toolkit use requires authorization.
- `ffmpeg-skill`: MIT according to its repository.
- Remotion has its own current licensing/terms and must be checked at adoption/deployment time.

General ideas, workflows, and architectural patterns may inform our own original implementation; donor code should not be copied where its license does not permit the intended use.

## Final Decision

Adopt now:

- frame-addressable timeline;
- shot/beat/keyframe source model;
- Remotion as preferred programmable visual renderer;
- shot-segment incremental rendering;
- master-audio-separate assembly;
- frame-count assertions;
- still/burst/contact-sheet QC;
- FFmpeg/ffmpeg-skill-style finishing and verification.

Defer:

- literal image-per-frame generation as a default;
- copying donor code;
- large motion-card library before the first internal validation;
- complex workbench UI before the data model and incremental renderer are proven.