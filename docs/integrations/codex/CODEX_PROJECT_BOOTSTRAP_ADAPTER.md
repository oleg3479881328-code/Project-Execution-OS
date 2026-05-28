# Codex Project Bootstrap Adapter

## Canonical Contract

The project-level requirement is defined in `docs/PROJECT_BOOTSTRAP_STANDARD.md`.

## Codex Discovery Facts

Current Codex documentation identifies `AGENTS.md` as its instruction-discovery file. Codex reads global guidance from the Codex home directory and project guidance from the project root hierarchy when a run starts.

Current Codex app documentation describes the user selecting a project folder for Codex to work in.

Current Codex hooks documentation exposes a `SessionStart` lifecycle event and identifies the working directory in its input.

## Implementation Boundary

These capabilities support checking and initializing a selected project folder at session start.

They do not, by themselves, prove that pressing a create-project control in the desktop interface creates bootstrap files before a Codex session starts.

Accordingly, the Project Execution OS guarantee for Codex environments is:

- creation-time bootstrap when a confirmed creation-template mechanism is available;
- otherwise bootstrap before substantive work in the first Codex session opened in the selected project folder.

## Confirmed Supported Mechanism

The confirmed supported mechanism is a Codex `SessionStart` hook.

On systems where a shared user-level bootstrap is desired, install:

- `~/.codex/hooks.json`
- a hook script referenced from that file, for example under `~/.codex/hooks/`

That hook may create missing `AGENTS.md` and `PROJECT_ENTRYPOINT.md` at session start when the selected folder is clearly a new project folder and still in safe zero state.

This is a session-start guarantee, not a click-time create-project guarantee.

## Required Root Artifacts

A Codex-facing folder that has completed bootstrap contains:

```text
AGENTS.md
PROJECT_ENTRYPOINT.md
```

`AGENTS.md` serves Codex instruction discovery. `PROJECT_ENTRYPOINT.md` remains the project entrypoint artifact for humans and AI participants.

## External References

- OpenAI Codex documentation: `Custom instructions with AGENTS.md`
- OpenAI Codex documentation: `Hooks`
- OpenAI Codex documentation: `Codex app`
