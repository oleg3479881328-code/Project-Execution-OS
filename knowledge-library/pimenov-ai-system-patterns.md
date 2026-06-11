# Pimenov.ai — системные паттерны для Project Execution OS / reusable system patterns for Project Execution OS

Дата фиксации / Date captured: 2026-06-11
Источник / Source: https://pimenov.ai/

---

# Русская версия

## Назначение

Сохранить применимые инженерные паттерны, извлечённые из целевого разбора `pimenov.ai`, для будущего использования в проектах Project Execution OS.

## Основные паттерны, которые стоит применять

### 1. Делать системы agent-ready

Полезная для агентов система должна иметь предсказуемые маршруты, чистые данные, стабильные точки входа, явные связи и машиночитаемые правила. Удобного интерфейса только для человека недостаточно.

Применение к Project Execution OS:

- сохранять `START_HERE.md` минимальным и стабильным;
- маршрутизировать работу через `docs/ROUTER.md`;
- выбирать самый узкий релевантный маршрут под активную задачу;
- иметь явные точки входа для проектов;
- не заставлять агента читать весь репозиторий по умолчанию.

Возможный будущий стандарт:

- создать `AGENT_READY_PROJECT_STANDARD.md` с минимальной структурой проекта: точка входа, текущее состояние, ближайшее действие, ограничения, активные файлы и границы прав доступа.

### 2. Отделять проектирование от исполнения

Агент должен помогать понять задачу, спроектировать рабочий процесс, задокументировать его и улучшить. Когда повторяемый процесс стабилизировался, рутинное исполнение нужно переносить в детерминированный слой: скрипт, skill, pipeline или оркестратор.

Правило:

- первый запуск: проектирование и отладка с агентом;
- после стабилизации: детерминированное исполнение;
- агент остаётся для исключений, ревью и оптимизации.

Релевантные проекты:

- фабрика рилсов;
- обработка контента;
- публикационные процессы;
- серверные операции;
- будущие процессы личного секретаря;
- извлечение видеокарточек для QuizLight;
- массовые операции с файлами.

### 3. Использовать eval-циклы вместо бесконечного расширения промптов

Хороший результат должен пройти явные проверки качества, прежде чем двигаться дальше.

Минимальный цикл:

1. сгенерировать;
2. проверить по заранее заданным критериям;
3. отклонить результат ниже порога;
4. исправить;
5. проверить повторно;
6. утвердить только прошедший вариант.

Реальные ошибки нужно превращать в будущие регрессионные тесты.

Рекомендуемые первые применения:

- чек-лист качества рилсов;
- ревью дизайна сайтов;
- проверка качества исследований;
- важные письма;
- ревью кода;
- проверка юридических и миграционных документов.

### 4. Разделять роли генератора и ревьюера

Для нетривиальной работы нельзя смешивать создание и утверждение результата в один неразделённый проход.

Рекомендуемый паттерн:

1. исполнитель создаёт черновик;
2. независимый ревьюер проверяет его по правилам;
3. исполнитель исправляет проблемы;
4. человек утверждает внешние или рискованные действия.

### 5. Перед изменениями инфраструктуры проводить read-only аудит

До изменения серверов сначала нужно изучить и задокументировать текущее состояние.

Результаты аудита:

- паспорт каждого сервера;
- общее операционное состояние инфраструктуры.

Рекомендуемые поля паспорта сервера:

- провайдер;
- регион;
- стоимость;
- назначение;
- IP-адреса и домены;
- запущенные сервисы;
- контейнеры;
- открытые порты;
- диски;
- резервные копии;
- дата последней проверки;
- разрешённые изменения;
- инструкция отката;
- статус: активный, тестовый, на паузе, можно удалить.

### 6. Сохранять human approval gates для внешних действий

Агенты должны работать с ограничениями прав, сопоставимыми с правами сотрудников.

Для будущего личного секретаря:

- чтение почты: отдельное разрешение;
- создание черновика письма: отдельное разрешение;
- отправка письма: только по явному подтверждению владельца;
- просмотр календаря: отдельное разрешение;
- создание событий: отдельное разрешение;
- удаление: ограничить;
- пароли, токены, банковские данные и похожие секреты: никогда не хранить в проектных файлах.

### 7. База знаний должна быть машиночитаемой и поддерживаться в актуальном состоянии

Конкретный инструмент вторичен. Важны:

- единый источник правды;
- машиночитаемая структура;
- явные связи;
- процесс обновления;
- удаление или архивирование устаревших знаний;
- обнаружение пробелов и осиротевших материалов.

Будущий граф знаний должен быть операционным, а не декоративным. Он должен выявлять:

- часто повторяющуюся тему без оформленного знания;
- изолированный полезный материал;
- устаревшие блоки;
- ссылки-сироты;
- слабые или случайные связи.

## Применение к отдельным проектам

### Блок дизайна сайтов

Использовать итеративный цикл визуального ревью:

1. собрать минимальную версию;
2. запустить локально;
3. сделать скриншоты;
4. проверить через vision;
5. прокликать пользовательские сценарии;
6. исправить проблемы;
7. повторно сделать скриншоты;
8. сравнить варианты;
9. при необходимости сгенерировать ассеты;
10. сохранить извлечённые правила дизайна.

### Фабрика рилсов

До автоматизации использовать ручной чек-лист качества:

- первый кадр захватывает внимание;
- тема понятна без звука;
- субтитры читаемые;
- нет визуального мусора;
- длительность подходит платформе;
- нет очевидных проблем с авторскими правами;
- результат соответствует целевой платформе;
- ролик можно публиковать без ручной переделки.

### Личный секретарь

Оставаться в ручном режиме проверки, пока не обработано минимум 10 реальных входящих пакетов. Не добавлять преждевременно Telegram, Notion, n8n, долговременное хранилище или широкую автоматизацию.

## Что пока явно не делать

Не внедрять решения только потому, что идеи выглядят интересными:

- миграцию в Notion;
- граф знаний;
- Telegram-бота;
- слой n8n;
- широкую мультиагентную архитектуру;
- сложную RBAC-систему;
- аудиослой;
- полное копирование чужого технологического стека.

## Ближайшее рекомендуемое действие

Создать простой ручной чек-лист качества рилсов и применить его к реальным результатам до любой автоматизации.

---

# English version

## Purpose

Preserve reusable engineering patterns extracted from a targeted review of `pimenov.ai` for future use across Project Execution OS projects.

## Core patterns worth adopting

### 1. Agent-ready systems

A useful system for agents must provide predictable routes, clean data, stable entrypoints, explicit relationships, and machine-readable rules. Human-friendly presentation alone is insufficient.

Application to Project Execution OS:

- keep `START_HERE.md` minimal and stable;
- route through `docs/ROUTER.md`;
- use the narrowest relevant route for the active request;
- keep project entrypoints explicit;
- avoid forcing an agent to read the whole repository by default.

Potential future standard:

- create `AGENT_READY_PROJECT_STANDARD.md` with the minimum project structure: entrypoint, current state, next action, constraints, active files, and permissions boundary.

### 2. Separate design from execution

Use an agent to understand a problem, design a workflow, document it, and improve it. Once a repeated workflow stabilizes, move routine execution into a deterministic layer such as a script, skill, pipeline, or orchestrator.

Rule:

- first run: agent-led design and debugging;
- after stabilization: deterministic execution;
- agent remains for exceptions, review, and optimization.

Relevant projects:

- reels factory;
- content processing;
- publishing workflows;
- server operations;
- future personal secretary workflows;
- QuizLight video-card extraction;
- bulk file operations.

### 3. Use eval loops instead of endlessly expanding prompts

A good result should pass explicit quality checks before moving forward.

Minimal loop:

1. generate;
2. evaluate against predefined criteria;
3. reject below-threshold output;
4. repair;
5. re-evaluate;
6. approve only passed output.

Use real failures as future regression tests.

Recommended first applications:

- reels quality checklist;
- website design review;
- research quality checks;
- important letters;
- code review;
- legal and immigration document review.

### 4. Separate generator and reviewer roles

For non-trivial work, do not let generation and approval collapse into one undifferentiated pass.

Recommended pattern:

1. executor creates draft;
2. independent reviewer checks against rules;
3. executor fixes issues;
4. human approves external or high-risk actions.

### 5. Read-only infrastructure audit before changes

Before changing servers, first inspect and document the current state.

Audit outputs:

- server passport for each machine;
- overall operating state for the infrastructure.

Suggested server passport fields:

- provider;
- region;
- cost;
- purpose;
- IP addresses and domains;
- running services;
- containers;
- open ports;
- disks;
- backups;
- last checked date;
- allowed changes;
- rollback instructions;
- status: active, test, paused, removable.

### 6. Human approval gates for external actions

Agents should operate with permission boundaries comparable to employees.

For the future personal secretary:

- reading email: separate permission;
- drafting email: separate permission;
- sending email: explicit owner approval;
- viewing calendar: separate permission;
- creating events: separate permission;
- deletion: restricted;
- passwords, tokens, bank-card data, and similar secrets: never store in project files.

### 7. Knowledge systems must be machine-readable and maintained

The tool is secondary. The important properties are:

- one source of truth;
- machine-readable structure;
- explicit links;
- update process;
- retirement of stale knowledge;
- detection of gaps and orphan materials.

A future graph should be operational, not decorative. It should reveal:

- recurring topic without a formal knowledge entry;
- isolated high-value material;
- stale blocks;
- orphan references;
- weak or accidental connections.

## Project-specific applications

### Website design block

Adopt an iterative visual review loop:

1. build minimum version;
2. run locally;
3. capture screenshots;
4. inspect via vision;
5. click through user flows;
6. fix issues;
7. repeat screenshots;
8. compare variants;
9. generate assets where necessary;
10. preserve extracted design rules.

### Reels factory

Use a manual quality checklist before automation:

- first frame captures attention;
- theme is understandable without sound;
- subtitles are readable;
- no visual clutter;
- duration fits the platform;
- no obvious copyright issue;
- output matches the target platform;
- publishable without manual repair.

### Personal secretary

Stay in manual validation mode until at least 10 real intake batches are processed. Do not add Telegram, Notion, n8n, durable storage, or broad automation prematurely.

## Explicit non-actions for now

Do not implement merely because the patterns are interesting:

- Notion migration;
- knowledge graph;
- Telegram bot;
- n8n layer;
- broad multi-agent architecture;
- complex RBAC;
- audio layer;
- full-stack copy of another person's tooling.

## Immediate recommended next step

Create a simple manual reels-quality checklist and use it on real outputs before automating anything.
