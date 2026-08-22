# Туся Reddit Telegram Bot

Version: 0.1.0-alpha
Status: Architecture approved for implementation
Execution channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/79

## Product goal

Telegram-бот круглосуточно мониторит выбранные Reddit-ресурсы, фильтрует новые публикации по управляемой базе слов и фраз, присылает подходящие посты владельцу в Telegram и по запросу создает черновик ответа через GPT API.

Бот не публикует ответы в Reddit автоматически.

## MVP scope

- Один владелец и один разрешенный Telegram chat ID.
- Управление Reddit-ресурсами внутри Telegram.
- Управление словами и фразами внутри Telegram.
- Фоновый мониторинг активных ресурсов.
- Первый опрос формирует baseline без старого спама.
- Дедупликация по Reddit post ID.
- Лента новых совпадений в Telegram.
- Просмотр полного поста внутри Telegram.
- Прямая ссылка на Reddit.
- Генерация и сохранение GPT-черновика.
- Настройки мониторинга и черновиков.
- SQLite с миграциями.
- Логи ошибок и решений в корне проекта.

## Explicitly out of scope

- Автоматическая публикация в Reddit.
- Reddit OAuth владельца.
- Многопользовательский SaaS.
- Платежи.
- Мониторинг других платформ.
- Веб-панель администратора.
- Семантическая AI-классификация до завершения keyword MVP.

## Main menu

- 📡 Лента
- ➕ Добавить ресурс
- 🔤 Добавить слово
- 🗂 Ресурсы
- 🧾 Слова
- ⚙️ Настройки

## Security invariants

- `TELEGRAM_BOT_TOKEN`, `OPENAI_API_KEY` и другие секреты существуют только в server-side environment/secrets.
- Секреты не попадают в GitHub, Telegram, SQLite и логи.
- Бот отвечает только разрешенному owner chat ID.
- Никакого автоматического Reddit publishing.
- AI-ответ всегда считается черновиком и требует ручного решения владельца.
