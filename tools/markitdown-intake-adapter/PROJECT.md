# MarkItDown Intake Adapter

## Purpose

Local-only Windows-first MVP adapter for converting approved local documents into Markdown with Microsoft's official `markitdown` package.

## Scope

- wrapper scripts and validation for `MarkItDown().convert_local(...)`;
- local PowerShell bootstrap and conversion entrypoints;
- disposable smoke samples for bounded validation;
- transfer-ready status files for executor continuity.

## Out Of Scope

- remote URL fetching;
- MCP exposure;
- Azure Document Intelligence;
- Azure Content Understanding;
- LLM OCR;
- paid services and secrets.

## First Run

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\markitdown-intake-adapter\bootstrap.ps1
```

## Main Conversion Command

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\markitdown-intake-adapter\convert-file.ps1 -InputFile .\path\to\file.pdf -OutputFile .\path\to\file.md
```
