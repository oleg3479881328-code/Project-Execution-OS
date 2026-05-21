# ChatGPT Codex GitHub Integration

## Purpose

This is the ChatGPT-facing integration entrypoint for the GitHub-based `ChatGPT <-> Codex` collaboration loop.

Use it when:

- reasoning work is ready for Codex execution;
- GitHub issue, PR, or review thread will carry the task;
- durable multi-agent coordination is needed.

## Canonical Protocol

The canonical full protocol currently lives here:

`docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`

Use that document for:

- the complete role model;
- message header rules;
- handoff packet expectations;
- execution report expectations;
- fallback and default-decision behavior;
- review and validation separation.

## Related Artifacts

- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`
- `docs/AI_COORDINATION_HUB_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`

## Design Rule

Keep ChatGPT-specific routing here.

Keep the deeper reusable protocol stable and reviewable in the canonical protocol artifact.
