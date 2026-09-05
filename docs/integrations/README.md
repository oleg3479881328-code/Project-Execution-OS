# Integrations

This folder stores AI-specific or tool-specific integration layers that should not dominate the root operating-system documents.

Use this layer when the core repository workflow needs a concrete adapter for:

- ChatGPT;
- Codex through GitHub;
- model/provider-specific execution candidates;
- transcription/media connectors;
- runtime-specific transport layers.

## Current integrations

- `chatgpt/CORE_SYSTEM_PROMPT.md`
- `chatgpt/CODEX_GITHUB_PROTOCOL.md`
- `codex/`
- `notion/README.md`
- `scrapegraphai/`
- `archify/`
- `whisper-transcribe-ai/README.md` — active connected transcription integration; verify transcript coverage before whole-source analysis.
- `cline-glm-5-3-flash/README.md` — candidate low-cost secondary coding-agent route for VS Code; not yet promoted above candidate.

## Operational rule

If a canonical integration document URL is already known and accessible, the model should fetch and read it directly instead of asking the user to paste it again.

## Design rule

The operating system stays tool-neutral at the core.

Model-specific or connector-specific guidance should live here unless it is truly universal.

Candidate integrations must not be presented as production defaults until their stated validation gate is satisfied.
