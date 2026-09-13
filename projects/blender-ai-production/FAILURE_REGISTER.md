# Blender AI Production — FAILURE_REGISTER.md

Status: active project runbook / do-not-repeat register
Updated: 2026-09-13
Applies to: Blender scripting, scene generation, render automation, animation and video output in this project

## Purpose

Preserve concrete failures from the 2026-09-13 Blender practical test so future executors do not repeat the same mistakes.

This file is not a general chat summary. It is the project-local failure/prevention register. Before generating or changing Blender Python, animation, render or video-output scripts, read this file together with `AGENTS.md`.

Test environment that exposed these failures:

- Blender: 5.2.1 LTS
- OS: Windows
- owner-approved output root: `C:/Users/oleg3/OneDrive/Desktop/BLEND`

## Governing Rule

`Existing Solution First` is mandatory.

For Blender version-sensitive behavior, do not invent or patch from memory first. Check, in this order:

1. current project knowledge / this register;
2. official Blender release notes and Python API for the installed Blender version;
3. existing proven project donor/pattern;
4. only then write the smallest necessary custom code.

Syntax success is not runtime success. Runtime success is not visual success. Visual success is not temporal/video success.

## Failure Register

### F-01 — Wrong deliverable class: generated image instead of Blender result

**What happened**

The request was for the result to happen inside Blender, but an illustrative generated image was produced instead.

**Why it was wrong**

A lookalike image is not evidence that Blender built or rendered the scene.

**Prevention**

When the owner says the result must be in Blender, do not substitute image generation. Deliver a Blender scene/script/render produced by Blender, or state clearly that Blender runtime verification is unavailable.

**Status**

Process rule accepted.

---

### F-02 — Script incorrectly depended on a sidecar GLB being beside the Python file

**Observed error**

`FileNotFoundError: house_floorplan_to_blender.glb`

**What happened**

The helper script assumed `house_floorplan_to_blender.glb` lived in the same directory as the script. The script was opened from Downloads while the working Blender file/assets were elsewhere.

**Prevention**

For the owner's preferred workflow, standalone build scripts must not require hidden/co-located sidecar assets unless the dependency is explicit and preflight-validated.

If working from an already-open scene, operate on that scene instead of re-importing an unnecessary GLB.

If an external asset is required, use an explicit configured path and fail before mutating the scene if the asset is missing.

**Status**

Verified failure; prevention adopted.

---

### F-03 — Unsafe output-path inference from `__file__`

**Observed error**

Blender attempted to save to `C:/house_from_scratch.blend` and Windows returned `Permission denied`.

**What happened**

The script tried to infer a writable output directory from Blender's script context / `__file__`. In Blender Text Editor execution this did not reliably represent the intended user folder.

**Prevention**

Do not infer the production output root from `__file__` in Blender Text Editor jobs.

For this owner/project, use the explicit approved root:

`C:/Users/oleg3/OneDrive/Desktop/BLEND`

Before any expensive build/render, preflight with `os.makedirs(..., exist_ok=True)` and a tiny write/delete test.

**Status**

Verified failure; fixed by explicit output root.

---

### F-04 — Windows backslash path caused Python `unicodeescape` syntax failure

**Observed error**

`SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes ... truncated \\UXXXXXXXX escape`

**What happened**

A Windows path such as `C:\Users\...` appeared inside Python string content. `\U` was parsed as the beginning of a Unicode escape.

**Prevention**

Inside generated Python use forward-slash Windows paths:

`C:/Users/oleg3/OneDrive/Desktop/BLEND`

Alternative acceptable forms are a correctly escaped string (`C:\\Users\\...`) or a valid raw string, but forward slashes are the project default because they are simplest and work on Windows in Blender/Python.

Do not place an unescaped `C:\Users\...` path inside docstrings either; docstrings are strings and are parsed.

**Status**

Verified failure; fixed and syntax-guarded.

---

### F-05 — Render was visually washed out / nearly white

**Observed result**

The Blender viewport showed colored materials, but the rendered PNG was almost monochrome white and low-contrast.

**What happened**

World strength, Sun/Area-light energy and exposure were too aggressive for the scene/material scale. Structural success was incorrectly treated as visual success before reviewing the final PNG.

**Prevention**

For a new scene/render configuration:

1. render one low-cost still first;
2. inspect the actual PNG, not only viewport material colors;
3. tune world strength, key/fill energy and exposure conservatively;
4. only after the still passes, render animation.

Current successful direction from the test used substantially lower light energy and lower exposure than the washed-out version.

**Status**

Verified visual failure; corrected direction established. Final artistic lighting still requires normal visual QA.

---

### F-06 — Blender 5.0+ removed legacy `Action.fcurves`

**Observed error**

`AttributeError: 'Action' object has no attribute 'fcurves'`

**Root cause**

The script used pre-5.0 animation API assumptions. Blender 4.4 introduced slotted/layered Actions; Blender 5.0 removed the legacy `action.fcurves`, `action.groups` and `action.id_root` API.

Official sources:

- Blender 5.0 Python API release notes: https://developer.blender.org/docs/release_notes/5.0/python_api/
- Blender 4.4 Python API / Slotted Actions: https://developer.blender.org/docs/release_notes/4.4/python_api/
- Upgrade guide: https://developer.blender.org/docs/release_notes/4.4/upgrading/slotted_actions/

**Prevention**

Do not directly access `action.fcurves` in Blender 5.x.

If F-Curve access is actually required, use the current slot/channelbag APIs or Blender convenience functions from `bpy_extras.anim_utils` / `action.fcurve_ensure_for_datablock()` as documented for the current version.

If direct F-Curve editing is not required, prefer ordinary `keyframe_insert()` and avoid touching Action internals at all.

**Status**

Verified failure; root cause confirmed by official Blender documentation.

---

### F-07 — Blender 5.x video output requires `media_type='VIDEO'` before `file_format='FFMPEG'`

**Observed error**

Setting `scene.render.image_settings.file_format = 'FFMPEG'` failed because `FFMPEG` was not present in the active image-format enum.

**Root cause**

Blender 5.0 changed the Image & Movies Python API. `ImageFormatSettings.media_type` must be set to the appropriate media type before setting `file_format`.

Official sources:

- Blender 5.0 Python API release notes, Image & Movies: https://developer.blender.org/docs/release_notes/5.0/python_api/
- `ImageFormatSettings.media_type`: https://docs.blender.org/api/main/bpy.types.ImageFormatSettings.html
- Blender video formats / FFmpeg containers/codecs: https://docs.blender.org/manual/en/5.0/files/media/video_formats.html

**Correct order for Blender 5.x**

```python
fmt = scene.render.image_settings
fmt.media_type = 'VIDEO'
fmt.file_format = 'FFMPEG'
scene.render.ffmpeg.format = 'MPEG4'
scene.render.ffmpeg.codec = 'H264'
```

For still PNG, explicitly switch back first:

```python
fmt.media_type = 'IMAGE'
fmt.file_format = 'PNG'
```

**Verification**

After applying the documented order, Blender 5.2.1 successfully produced the uploaded MP4 from the 120-frame orbit test.

**Status**

Verified failure + verified fix in the owner's Blender environment.

---

### F-08 — Orbit camera parenting/transform order was unsafe

**What happened**

An early orbit script positioned the camera in world space and only then parented it to the pivot. Parenting can change/effect the resulting transform and makes the intended radius/orbit less deterministic.

**Prevention**

For a pivot-orbit rig:

1. create pivot at scene center;
2. parent camera to pivot;
3. set camera **local** offset from pivot;
4. track camera toward a stable target;
5. animate pivot rotation.

For Blender 5.x, do not manipulate removed Action internals just to force interpolation. Use keyframes with a simple supported animation setup, and visually/temporally validate the resulting orbit.

**Status**

Preventive correction adopted.

---

### F-09 — Exact MP4 filename assumption was wrong

**Observed output**

The produced movie was named with a frame-range suffix, e.g. `house_complete_v7_orbit_360_5s0001-0120.mp4`, rather than the exact requested base filename.

**Why this matters**

`scene.render.filepath` for animation/video should be treated as an output base/prefix unless exact naming behavior has been verified for the active Blender version/settings.

**Prevention / preferred production path**

For production-quality deterministic delivery, prefer:

`Blender numbered image sequence -> FFmpeg assembly -> exact final MP4 name`

Direct Blender FFmpeg output is acceptable for quick preview videos, but do not assume the exact final filename. If direct movie output is used, discover/verify the actual produced file before reporting the path.

**Status**

Observed open normalization issue. Do not claim exact video filename until verified.

---

### F-10 — Fragmented patch delivery created avoidable confusion

**What happened**

Several iterations were delivered as separate fixes (`finish...`, revised builder, another package) before the owner explicitly required one complete bundle.

**Prevention**

For this project, when a Blender pipeline revision is requested after a failure, deliver a **complete self-contained bundle** by default:

- from-scratch script;
- current-scene/repair script when useful;
- README;
- verification report;
- stable filenames/version;
- one declared output root;
- prior stable fallback only when it has clear value.

Do not make the owner manually assemble a working version from patches unless the owner asks for a patch.

**Status**

Owner requirement; mandatory for future bundle revisions.

---

### F-11 — Syntax verification was presented too close to runtime verification

**What happened**

Python source was compiled successfully outside Blender, but later Blender-runtime failures still occurred (`Action.fcurves`, `FFMPEG` media type). A syntax `PASS` did not prove Blender 5.2 compatibility.

**Prevention**

Always label verification levels separately:

1. `SYNTAX PASS` — Python parses;
2. `API PREFLIGHT PASS` — required properties/enums exist in the target Blender;
3. `BLENDER RUNTIME PASS` — script executed inside the target Blender;
4. `ARTIFACT PASS` — expected files exist and can be probed;
5. `VISUAL PASS` — rendered still is readable/correct;
6. `TEMPORAL PASS` — sampled animation/video behaves correctly.

Never use `checked`, `verified`, `works`, or `ready` without saying which level actually passed.

**Status**

Mandatory validation language rule.

---

### F-12 — We coded first and consulted official Blender docs too late

**What happened**

After multiple Blender 5.2 failures, the owner explicitly stopped the patch cycle and required existing-solution/documentation research. Only then were the version-specific API changes identified from official Blender documentation.

**Prevention**

For every version-sensitive Blender API task, especially animation, output formats, rendering, operators and data model changes:

1. identify exact Blender version;
2. search project prior solutions;
3. inspect official release notes/API for that version;
4. inspect an existing proven donor if relevant;
5. then write code.

This is not optional. It is a concrete application of `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`.

**Status**

Highest-priority process correction from this test.

## Mandatory Preflight For Future Blender Scripts

Before generating a substantial script or a full bundle:

1. **Version** — record `bpy.app.version_string` / target Blender version.
2. **Output root** — use `C:/Users/oleg3/OneDrive/Desktop/BLEND` unless the owner changes it.
3. **Writable path** — create and delete a tiny test file before expensive work.
4. **Dependencies** — verify every external `.blend`, `.glb`, texture, rig or animation path before scene mutation.
5. **Official API check** — consult current Blender release notes/API for every version-sensitive API surface being used.
6. **Tiny probe first** — test one object / one keyframe / one still / a very short animation before the full job.
7. **Still before animation** — approve or at least inspect a low-cost still before 120+ frame rendering.
8. **Video path** — for Blender 5.x set `media_type='VIDEO'` before `file_format='FFMPEG'`.
9. **Animation API** — do not use removed `action.fcurves` in Blender 5.x.
10. **Visual QA** — inspect the actual render file, not only viewport state.
11. **Temporal QA** — sample beginning/middle/end and neighbouring frames of animation.
12. **Package whole revision** — deliver one complete bundle, not a chain of patches.
13. **Verification labels** — distinguish syntax/API/runtime/artifact/visual/temporal verification.
14. **Preserve evidence** — keep the failed screenshot/error/output and the last accepted `.blend` checkpoint.

## Preferred Video Production Rule

For quick previews:

`Blender direct FFmpeg movie output` is acceptable after API preflight.

For repeatable production delivery:

```text
Blender renders numbered frames
-> deterministic frame-count/file checks
-> FFmpeg assembles exact final MP4
-> ffprobe verifies duration/fps/codec
-> sampled-frame/contact-sheet temporal QA
```

This better matches the existing project architecture and avoids coupling final delivery naming/encoding to Blender UI/API quirks.

## Known Good / Known Verified From This Test

- Explicit Windows output root with forward slashes avoids the observed path and Unicode issues.
- Blender 5.2.1 can build the procedural house scene from generated `bpy` code.
- Blender 5.x requires the current layered/slotted Action model; legacy `Action.fcurves` is removed in 5.0.
- Blender 5.x requires setting `ImageFormatSettings.media_type` before `file_format`.
- Direct Blender MPEG-4/H.264 output succeeded after using the documented media-type order.
- The direct animation output filename may include a frame-range suffix; exact naming remains a separate normalization concern.

## Related Project Rules

- `AGENTS.md`
- `PROJECT_STATE.md`
- `logs/latest.md`
- `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `../../blocks/video-production/FRAME_ADDRESSABLE_PRODUCTION.md`
- `../../blocks/video-production/GENERATIVE_FRAME_PRODUCTION.md`

## Final Do-Not-Repeat Rule

Do not respond to the next Blender scripting failure by immediately inventing another patch.

First classify the failure, search this register, check the exact Blender-version documentation, preserve the last accepted scene, run the smallest possible probe, and only then produce one complete corrected bundle.