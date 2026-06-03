# References

## Provenance

- Created inside `Project-Execution-OS` as the central reusable skill for durable reasoning-model <-> executor-agent collaboration through GitHub.
- Based on the canonical protocol entrypoint in `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`.
- Aligned with `Start New Project.md` sections `ChatGPT To Codex Interaction Model` and `Codex Handoff Contract`.
- Expanded to include sync discipline learned from live coordination on `last30days-telegram-bot`: `GitHub main` as source of truth, mandatory `git status` preflight, minimal commits only, and post-fix SHA reporting.
- Expanded on 2026-06-03 from live QuizLight coordination: when an issue thread becomes too long for reliable connector reading, keep the active GitHub issue / PR / review thread as transport and add root-level `AI_COORDINATION_STATE.md` as the compact operational snapshot.
- The canonical snapshot rules live in `docs/AI_COORDINATION_STATE_STANDARD.md`.
- The reusable starter file lives in `templates/AI_COORDINATION_STATE.md`.
