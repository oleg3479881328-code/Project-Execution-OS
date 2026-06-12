# Project State

Status: in_progress
Task: Implement local-only MarkItDown intake adapter MVP for Issue #51.
Current Phase: initial implementation created; validation pending
Active Branch: codex/issue-51-markitdown-adapter
Active Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51
Next Action: run bootstrap, execute smoke tests, validate URL rejection, update durable coordination files
Known Constraints:
- use `MarkItDown().convert_local(...)` only
- keep changes isolated under `tools/markitdown-intake-adapter/` plus allowed coordination files
- no remote fetch, MCP, Azure, OCR plugin, or paid-service paths
