# Archify Pilot Validation

## Date

2026-08-30 (America/New_York)

## Environment

- OS: Windows NT 10.0.26200.0
- Repository: `C:\Users\oleg3\OneDrive\Documents\Project-Execution-OS__archify-132`
- Branch: `codex/issue-132-archify-pilot`
- Repository HEAD at input snapshot: `b4119aea4fc0cf7c602943cc8071ed3db549dfeb`
- Node: `v24.13.0`
- npm: `11.6.2`
- npx: `11.6.2`
- Codex: `codex-cli 0.151.0-alpha.7.1`
- Archify: `v2.16.0` (upstream `tt-a1i/archify`, source HEAD `5de7275fe87a66a19d52a4d9b0b3a4f2a5a90115`)
- Archify installation/invocation path: cloned upstream skill package at `C:\Users\oleg3\AppData\Local\Temp\archify-upstream-132-v2\repo\archify`, invoked directly with `node bin/archify.mjs`; this uses the working Codex environment and does not install `tt-a1i/codex`.

## Installation / invocation method

Official upstream documentation identifies `npx skills use tt-a1i/archify@archify --agent codex` as the try-without-install path and documents the bundled zero-dependency CLI. For this pilot, the verified upstream package was invoked directly so the real renderer and validators could be exercised deterministically in the current Codex environment.

## Exact commands

```powershell
[System.Environment]::OSVersion.VersionString
node --version
npm --version
npx --version
codex --version
git ls-remote https://github.com/tt-a1i/archify.git HEAD
node C:\Users\oleg3\AppData\Local\Temp\archify-upstream-132-v2\repo\archify\bin\archify.mjs doctor
node C:\Users\oleg3\AppData\Local\Temp\archify-upstream-132-v2\repo\archify\bin\archify.mjs validate architecture docs/architecture/archify/project-execution-os.architecture.json --repo-root . --quality showcase --json
node C:\Users\oleg3\AppData\Local\Temp\archify-upstream-132-v2\repo\archify\bin\archify.mjs deliver architecture docs/architecture/archify/project-execution-os.architecture.json docs/architecture/archify/project-execution-os.architecture.html --repo-root . --quality showcase --json
node C:\Users\oleg3\AppData\Local\Temp\archify-upstream-132-v2\repo\archify\bin\archify.mjs visual-check docs/architecture/archify/project-execution-os.architecture.html --json
node C:\Users\oleg3\AppData\Local\Temp\archify-upstream-132-v2\repo\archify\scripts\check-update.mjs
```

## Input scope

High-level architecture map of Project Execution OS only. Relationships are authored from `START_HERE.md`, `docs/ROUTER.md`, `PROJECT.md`, current state/log files, repository structure, and execution standards. The map does not claim runtime reachability, impact, risk, ownership, merge safety, or network topology.

## Generated artifacts

- `docs/architecture/archify/project-execution-os.architecture.json`
- `docs/architecture/archify/project-execution-os.architecture.html`
- `docs/architecture/archify/VALIDATION.md`

Final delivery receipts:

- JSON SHA-256: `31afeaaa27ff6861c2427a8e50354cee17326a3043a7e2dc382a535ec5d631c0` (5996 bytes)
- HTML SHA-256: `eea6888458e82fd7f2c3f8f5043e33baecbc983dbc13196b0cf0e9df8abcb701` (738008 bytes)

## Validation results

| Criterion | Result | Evidence |
|---|---|---|
| Upstream Archify launches | PASS | `doctor` reported Archify ready; all runtime checks OK |
| Working Codex runtime | PASS | `codex --version` returned `codex-cli 0.151.0-alpha.7.1` |
| Custom renderer absent | PASS | only upstream `bin/archify.mjs` used |
| JSON is real Archify IR | PASS | `schema_version: 1`, `diagram_type: architecture`; Archify validate accepted it |
| JSON validation | PASS | showcase validation: 9/9 checks, 0 errors, 0 warnings |
| HTML created by Archify | PASS | `deliver` returned `ok: true` and artifact receipt |
| HTML validation | PASS | delivery receipt: 9/9 checks, showcase composition pass |
| HTML opens locally | PASS | Chrome available; `visual-check` loaded the local file |
| HTML self-contained | PASS | delivered single HTML artifact; no separate runtime asset was required |
| START_HERE → docs/ROUTER route | PASS | both nodes and authored connection are present; source evidence verified at pinned revision |
| Four PEOS layers distinguishable | PASS | explicit `L1`–`L4` labels and tags on the four layer nodes |
| Authored route traceable | PASS | guided views `system-entry` and `execution-review`; Archify delivery verified 20 source references |
| Speculation excluded | PASS | cards/metadata state documented-authored boundary; no runtime/topology claims |
| Secrets absent | PASS | no credentials or tokens in generated artifacts or validation receipt |
| Human visual comprehension | UNKNOWN | automated visual evidence passes; owner visual review remains pending |
| Desktop visual containment | PASS | `visual-check`: 1440×900, 1600×1000, 1920×1080, 2048×1320; light and dark captures passed |

## Raw result summary

- `doctor`: all checks `[ok]`, Archify ready.
- Final `validate`: `ok: true`, composition `pass`, 9/9 checks, 0 errors, 0 warnings.
- Final `deliver`: `ok: true`, verified repository revision and 20 source references.
- Final `visual-check`: `ok: true`, containment/readability/viewer chrome/captures all passed; `visualReview: pending` is the upstream human-review boundary.
- Update checker: `{"status":"silent","reason":"current"}`.

## Problems encountered

- Initial validation required the documented `--repo-root` because source evidence was declared.
- Archify reported layout micro-segments, label collisions, and desktop readability diagnostics. These were fixed only by adjusting authored positions/labels within the JSON; no renderer or PEOS architecture was changed.
- Initial visual-check found 4px vertical overflow at 1440×900. Removing redundant explanatory cards and compacting the authored execution row resolved it; the final visual-check passed.

## Fixes / fallbacks used

- Used the official upstream Archify package and its bundled CLI.
- Used the supported `--repo-root` evidence verification option.
- No Mermaid, D2, Graphviz, draw.io, custom renderer, `tt-a1i/codex` installation, production deployment, or system architecture change.

## Remaining limitations

- Automated visual evidence is not owner visual approval. The technical result is `TECHNICAL PASS — OWNER REVIEW PENDING` until the owner inspects the HTML.
- The map is an authored high-level architecture view, not proof of live runtime reachability or operational topology.

## Final technical verdict

`TECHNICAL PASS — OWNER REVIEW PENDING`
