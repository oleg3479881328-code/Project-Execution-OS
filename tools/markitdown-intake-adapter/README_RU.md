# MarkItDown Intake Adapter MVP

Локальный адаптер для конвертации документов в Markdown на базе официального пакета Microsoft `markitdown`.

## Что делает

- принимает только локальные файлы;
- вызывает только `MarkItDown().convert_local(...)`;
- пишет результат в Markdown-файл;
- возвращает машинно-читаемый статус `PASS`, `NEEDS_OCR` или `ERROR`.

`PASS` — successful conversion. Перевод: успешная конвертация.

`NEEDS_OCR` — scanned PDF did not yield meaningful text and should be routed to a later OCR step. Перевод: сканированный PDF не дал осмысленного текста и должен быть отправлен на следующий OCR-этап.

`ERROR` — conversion failed or the input violated local-only safety rules. Перевод: конвертация не удалась или вход нарушил правила локальной безопасности.

## Граница безопасности

MVP намеренно ограничен только локальной конвертацией.

Отключено и не входит в scope:

- OCR;
- Azure Document Intelligence;
- Azure Content Understanding;
- MCP;
- внешние `http:`, `https:`, `data:` и другие URL;
- paid cloud calls.

## Первый запуск

Точная команда первого запуска:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\markitdown-intake-adapter\bootstrap.ps1
```

Скрипт:

- находит Python относительно локального окружения;
- создаёт `.venv` в папке адаптера;
- ставит pinned dependencies;
- сразу прогоняет smoke test.

## Пример конвертации

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\markitdown-intake-adapter\convert-file.ps1 `
  -InputFile .\tools\markitdown-intake-adapter\example.pdf `
  -OutputFile .\tools\markitdown-intake-adapter\out\example.md
```

## Как обрабатывать `NEEDS_OCR`

Если адаптер вернул `NEEDS_OCR`, это означает, что локальная конвертация не извлекла из PDF достаточный текстовый слой. На текущем MVP-этапе такой файл не нужно считать успешно распарсенным. Его нужно передать в будущий отдельный OCR-пайплайн, который будет спроектирован и одобрен отдельно.

## Что валидируется smoke test

Smoke suite генерирует временные sample-файлы и проверяет:

- text PDF;
- scanned-image PDF без текстового слоя;
- DOCX;
- PPTX;
- XLSX;
- HTML;
- CSV;
- ZIP.

Ожидаемое поведение:

- 7 обычных форматов возвращают `PASS`;
- scanned PDF возвращает `NEEDS_OCR`.

## Что было и не было проверено

Нативная валидация выполняется в доступном Windows-окружении через PowerShell.

Пока не проверялись:

- production deployment;
- remote URL paths;
- Azure/OCR/MCP integrations, потому что они намеренно отключены в MVP.
