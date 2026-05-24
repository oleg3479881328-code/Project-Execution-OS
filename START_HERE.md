# START HERE — Project Execution OS

## Purpose

This is the single top-level entrypoint into `Project Execution OS`.

Its job is navigation only: identify why a human or AI entered the system and route to the smallest relevant internal node.

Do not store operating rules, project-storage decisions, workflow details, tool procedures, architecture, agent logic, or execution instructions in this file.

## Route

- possible new project or new initiative -> `Start New Project.md`
- operating-mode uncertainty -> `docs/MODE_CLASSIFIER.md`
- idea or reference that should be preserved but is not yet a project -> `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- lifecycle or storage-layer decision -> `docs/PROJECT_LIFECYCLE_MODEL.md`
- entry into a specific existing project -> that project's current entrypoint; if it is missing, use `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- small bounded existing-project action -> `docs/MICRO_TASK_MODE.md`
- research task -> `docs/RESEARCH_STANDARD.md`
- review task -> `docs/REVIEW_STANDARD.md`
- already-decided Codex execution handoff -> `docs/CODEX_HANDOFF_STANDARD.md`
- GitHub-based ChatGPT / Codex coordination -> `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`
- stable ChatGPT system-layer configuration -> `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`

## Final Rule

This file is the front door, not the building.

Choose the path and continue inside the relevant node.