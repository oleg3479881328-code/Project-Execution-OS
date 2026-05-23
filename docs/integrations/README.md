# Integrations

This folder stores AI-specific or tool-specific integration layers that should not dominate the root operating-system documents.

Use this layer when the core repository workflow needs a concrete adapter for:

- ChatGPT
- Codex through GitHub
- future model-specific system prompts
- future runtime-specific transport layers

Current integrations:

- `chatgpt/CORE_SYSTEM_PROMPT.md`
- `chatgpt/CODEX_GITHUB_PROTOCOL.md`
- `notion/README.md`

Operational rule:

If a canonical integration document URL is already known and accessible, the model should fetch and read it directly instead of asking the user to paste it again.

Design rule:

The operating system stays tool-neutral at the core.

Model-specific or connector-specific guidance should live here unless it is truly universal.
