# EXECUTE NEWS LAYER MVP

## Цель

Построить первый рабочий MVP News Layer для Project Execution OS.

Цель MVP — не создать новостную платформу.

Цель MVP — доказать работоспособность цикла:

Miniflux
→ получение новостей через API
→ подготовка AI bundle
→ генерация дайджеста
→ экспорт источников для NotebookLM

Если этот цикл работает, MVP считается успешным.

---

## Главный принцип

MVP FIRST.

Не улучшать.
Не расширять.
Не полировать.

Плохой рабочий результат лучше идеальной незавершённой системы.

---

## Архитектурное решение

Не создавать собственный сборщик новостей.

Использовать готовые open-source решения:

* Miniflux — основной intake layer
* RSSHub — только если источник не имеет RSS

Архитектура:

Sources
↓
RSS / RSSHub
↓
Miniflux
↓
AI Processing
↓
Digest / Timeline / Watchlist / Source Pack
↓
Storage Decision

---

## Что НЕ делать

Запрещено:

* создавать собственный RSS reader
* создавать собственный feed parser
* создавать собственный news database engine
* создавать UI
* создавать dashboard
* создавать Telegram-бота
* создавать email-рассылку
* создавать vector database
* создавать semantic search
* создавать multi-agent architecture
* подключать платные API
* добавлять функциональность вне MVP

---

## Что нужно создать

Создать отдельный модуль:

news-layer-mvp/

Структура:

news-layer-mvp/
├── README.md
├── env.example
├── docker-compose.yml
├── sources/
│   ├── starter_sources.md
│   └── starter_sources.opml
├── scripts/
│   ├── pull_miniflux_articles.py
│   ├── build_ai_bundle.py
│   ├── export_source_pack.py
│   └── generate_digest_prompt.py
├── outputs/
│   ├── .gitkeep
│   └── README.md
└── logs/
└── NEWS_LAYER_MVP_LOG.md

Если структура репозитория требует адаптации — адаптировать минимально и объяснить причину в логе.

---

## Конфигурация

Создать env.example.

Без реальных секретов.

Пример:

MINIFLUX_BASE_URL=http://localhost:8080
MINIFLUX_AUTH_VALUE=replace_with_local_value
NEWS_OUTPUT_DIR=outputs
NEWS_MAX_ARTICLES=50
NEWS_DEFAULT_CATEGORY=all

Опционально:

RSSHUB_BASE_URL=http://localhost:1200
NEWS_INCLUDE_READ=false
NEWS_LOOKBACK_HOURS=48

---

## Docker

Создать docker-compose.yml.

Минимум:

* Miniflux
* PostgreSQL

RSSHub можно добавить как optional.

После запуска должно быть возможно открыть локальный Miniflux.

README должен объяснять:

* запуск
* создание API доступа
* импорт OPML

---

## Источники

Создать стартовые категории:

* politics
* economy
* law
* immigration
* AI
* technology
* markets
* local

Не пытаться собрать весь интернет.

Сделать небольшой качественный набор.

Если источник не проверен:

НЕ выдумывать URL.

Писать:

TODO_VERIFY

---

## Скрипт 1

pull_miniflux_articles.py

Функции:

* подключение к Miniflux API
* получение свежих или непрочитанных статей
* нормализация данных
* экспорт в JSONL

Поля:

* title
* url
* author
* published_at
* feed
* category
* status
* content snippet

Результат:

outputs/articles_TIMESTAMP.jsonl

---

## Скрипт 2

build_ai_bundle.py

Функции:

* чтение JSONL
* дедупликация
* группировка
* создание Markdown bundle

Формат:

# AI News Bundle

## Instructions For Analysis

1. What happened
2. What is confirmed
3. What is uncertain
4. Why it matters
5. Practical meaning
6. Confidence
7. What to watch next
8. Source pack

## Articles

...

Результат:

outputs/ai_bundle_TIMESTAMP.md

---

## Скрипт 3

export_source_pack.py

Функции:

* чтение JSONL
* дедупликация ссылок
* экспорт чистого списка URL

Результат:

outputs/source_pack_TIMESTAMP.txt

Только ссылки.

Без описаний.

Без комментариев.

Формат должен подходить для NotebookLM.

---

## Скрипт 4

generate_digest_prompt.py

Функции:

* создание готового промпта для LLM
* промпт должен требовать:

  * digest
  * confidence labels
  * source grouping
  * separation of facts and uncertainty

Результат:

outputs/digest_prompt_TIMESTAMP.md

---

## Логирование

Создать:

logs/NEWS_LAYER_MVP_LOG.md

Обязательно логировать:

* созданные файлы
* решения
* предположения
* ошибки
* исправления
* ограничения
* следующий шаг

Запрещено утверждать, что что-либо протестировано, если оно не запускалось.

Использовать статус:

generated_not_executed

если код только создан.

---

## Критерии приёмки

MVP считается готовым если:

1. Есть docker-compose для Miniflux.
2. Есть env.example.
3. Есть starter_sources.md.
4. Есть starter_sources.opml.
5. Есть pull_miniflux_articles.py.
6. Есть build_ai_bundle.py.
7. Есть export_source_pack.py.
8. Есть generate_digest_prompt.py.
9. Есть README.
10. Есть лог.
11. Нет кастомного UI.
12. Нет scope creep.

---

## Формат финального отчёта

После завершения вернуть:

### CREATED FILES

список созданных файлов

### MODIFIED FILES

список изменённых файлов

### DIRECTORY TREE

дерево директорий

### IMPLEMENTED

что реализовано

### NOT IMPLEMENTED

что не реализовано

### RISKS

риски

### EXECUTION STATUS

Для каждого пункта:

* implemented_and_tested
  или
* implemented_not_tested
  или
* generated_not_executed

### NEXT RECOMMENDED STEP

ровно один следующий шаг

---

## Финальная инструкция

Сделай минимальную рабочую реализацию.

Не улучшай архитектуру.

Не расширяй scope.

Не строй инфраструктуру, которую уже решают Miniflux и RSSHub.

Главная цель — получить рабочий цикл:

Miniflux
→ articles.jsonl
→ AI bundle
→ digest
→ source pack
