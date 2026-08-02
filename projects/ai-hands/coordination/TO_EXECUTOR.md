# TO_EXECUTOR

## Active Assignment

- Project: `AI Hands`
- Work package: `WP-001 — Local Environment Inventory`
- Status: `READY_FOR_ACK`
- Active channel: pending GitHub issue creation
- Sender: `ChatGPT — Reviewer`
- Recipient: `Execution Agent`

## Objective

Inspect the owner's actual local computer environment and record only directly verified facts needed to choose the MVP local-model executor path.

## Required Inventory

- Operating system and version.
- CPU model and architecture.
- Installed RAM and available RAM.
- GPU model, driver, VRAM or shared-memory details.
- Disk space relevant to local models.
- Ollama installation, version, service status, endpoint, and installed models.
- Any other local model servers already installed.
- Git, Docker, WSL, Python, Node.js, npm, and PowerShell versions and availability.
- Installed or available executor candidates: Goose, OpenHands, Cline CLI/SDK, OpenCode, Aider, or equivalents.

## Boundaries

- Read-only discovery only.
- Do not install, update, remove, download, configure, restart, or modify anything.
- Do not expose secrets, tokens, private keys, passwords, or unrelated personal files.
- Do not infer hardware or models from chat history.
- Stop and report a blocker before requesting elevated privileges.

## Deliverables

1. Immediate signed `ACK` in the active GitHub issue.
2. Verified inventory table with command evidence.
3. Candidate executor compatibility assessment.
4. Recommended smallest next experiment for MVP 1.
5. Signed `COMPLETE` or `BLOCKER` response in the same issue.
6. Update `projects/ai-hands/logs/latest.md` with the latest durable status.

## Reply Contract

Use the signed polite message format required by `docs/AI_COORDINATION_MESSAGE_STANDARD.md`.
