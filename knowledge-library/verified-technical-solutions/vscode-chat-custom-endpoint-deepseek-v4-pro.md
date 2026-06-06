# VS Code Chat: подключение DeepSeek V4 Pro через Custom Endpoint

- **Type:** verified-technical-solution
- **Lifecycle status:** active
- **Captured:** 2026-06-06
- **Reviewed:** 2026-06-06
- **Scope:** встроенный Chat / Agent в VS Code с поддержкой пользовательских language models

## Problem

Кредиты GitHub Copilot закончились, но нужно было сохранить возможность использовать встроенный чат VS Code и агентное редактирование интерфейса через собственный API-ключ DeepSeek.

## Investigation

В интерфейсе VS Code был открыт список `Language Models`. В меню `Add Models...` присутствовал вариант `Custom Endpoint`. После создания группы VS Code сформировал пользовательский файл:

```text
%APPDATA%\Code\User\chatLanguageModels.json
```

Проверка проводилась непосредственно в рабочем VS Code: модель появилась в меню выбора моделей, была выбрана в нижней панели встроенного Chat / Agent и успешно ответила на тестовый запрос. Затем пользователь подтвердил, что всё заработало.

## Solution

### 1. Добавить пользовательскую группу моделей

В VS Code:

```text
Language Models -> Add Models... -> Custom Endpoint
```

Задать название группы:

```text
DeepSeek
```

Ввести API-ключ DeepSeek в защищённое поле VS Code. Не вставлять ключ напрямую в JSON и не сохранять его в GitHub.

Для типа API выбрать:

```text
Chat Completions
```

### 2. Заполнить созданный файл модели

Рабочая конфигурация:

```json
[
    {
        "name": "DeepSeek",
        "vendor": "customendpoint",
        "apiKey": "${input:chat.lm.secret.<generated-secret-id>}",
        "apiType": "chat-completions",
        "models": [
            {
                "id": "deepseek-v4-pro",
                "name": "DeepSeek V4 Pro",
                "url": "https://api.deepseek.com/chat/completions",
                "toolCalling": true,
                "vision": false,
                "maxInputTokens": 1000000,
                "maxOutputTokens": 384000
            }
        ]
    }
]
```

Строка `apiKey` должна оставаться ссылкой VS Code на сохранённый секрет. Значение `<generated-secret-id>` генерируется автоматически на конкретном компьютере.

### 3. Выбрать модель во встроенном Chat / Agent

В нижней строке встроенного чата VS Code:

```text
Auto -> Other Models -> DeepSeek -> DeepSeek V4 Pro
```

После выбора вместо `Auto` отображается:

```text
DeepSeek V4 Pro
```

## Verification

Проверено на рабочем компьютере пользователя:

1. группа `DeepSeek` появилась в списке `Language Models`;
2. модель `DeepSeek V4 Pro` отображалась с возможностью `Tools`;
3. модель была выбрана в нижней строке встроенного чата;
4. чат вернул ответ: `Я использую модель DeepSeek V4 Pro.`;
5. пользователь подтвердил: `Отлично, всё заработало.`

## Important Distinction

Эта настройка относится к **встроенному Chat / Agent VS Code**. Она не переключает автоматически отдельное расширение `Cline`, если оно установлено: у Cline есть собственные настройки провайдера и API-ключа.

Старое сообщение `Credit Limit Reached` может оставаться в истории чата после переключения. Оно относится к предыдущим запросам Copilot и само по себе не означает ошибку DeepSeek.

## Applies To

Использовать, когда:

- в VS Code закончились кредиты Copilot;
- нужно подключить собственный OpenAI-compatible API endpoint;
- требуется встроенный Chat / Agent с агентным редактированием файлов;
- в меню VS Code доступен `Language Models -> Add Models... -> Custom Endpoint`.

## Do Not Load When

Не загружать эту инструкцию автоматически, когда:

- настраивается отдельное расширение `Cline`, а не встроенный чат VS Code;
- нужен только автокомплит во время набора кода;
- используется другой редактор;
- DeepSeek изменил идентификатор модели или требования API, и нужна повторная проверка актуальности.

## Risks And Reuse Limits

- Никогда не сохранять реальный API-ключ в репозитории, issue, чате или скриншоте.
- Перед повторным применением проверить, что идентификатор `deepseek-v4-pro` всё ещё доступен в аккаунте DeepSeek.
- Параметры `maxInputTokens` и `maxOutputTokens` отражают рабочую конфигурацию на дату проверки; при изменении API их нужно актуализировать.
- Наличие встроенного чата не гарантирует замену всех функций Copilot, включая отдельные механизмы автодополнения.

## Related Standards

- `docs/AUTOMATIC_CAPTURE_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
