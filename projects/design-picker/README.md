# Design Picker MVP

## Назначение

`Design Picker` — это локальный внутренний сайт для сбора дизайн-доноров, просмотра их как визуальных карточек, фиксации того, что стоит переиспользовать, и экспорта понятной selection record.

## Запуск на Windows

### Самый быстрый путь

Двойной клик по:

`Launch-Design-Picker.bat`

Откроется:

`index.html`

в браузере по умолчанию.

### Одна готовая команда

Из PowerShell внутри `projects/design-picker/`:

```powershell
.\Launch-Design-Picker.bat
```

Для MVP ничего устанавливать не нужно.

## Как пользоваться

1. Запусти сайт.
2. Нажми `Добавить донора`.
3. Вставь публичный URL сайта.
4. Оставь поле `Ручная замена превью` пустым, чтобы использовать автоматический preview adapter.
5. Добавь теги, заметки и выбранные паттерны.
6. Поставь статус: `Основной`, `Частичный`, `Отклонён` или `Не решено`.
7. Используй поиск и фильтры, чтобы собрать shortlist.
8. Экспортируй Markdown или JSON, когда отбор готов.

## Что уже умеет MVP

- аккуратный локальный сайт с визуальными карточками доноров;
- добавление донора с одним обязательным полем: source URL;
- автоматическое название по домену, если вручную не заполнено;
- автоматическая генерация превью через preview-provider adapter;
- ручная замена превью;
- действия: редактировать, удалить, обновить превью;
- поиск по названию, URL, заметкам, тегам и паттернам;
- фильтрация по статусу решения и по паттерну;
- внутренние статусы: `primary`, `partial`, `rejected`, `undecided`;
- выбор переиспользуемых паттернов:
  - `hero`
  - `cards`
  - `pricing`
  - `navigation`
  - `motion`
  - `dashboard`
  - `onboarding`
  - `checkout`
  - `custom`
- заметки владельца и поле сильных сторон;
- экспорт в Markdown;
- экспорт в JSON;
- локальное сохранение через browser `localStorage`.

## Файлы

- `index.html` — оболочка приложения
- `styles.css` — визуальная система и responsive layout
- `app.js` — состояние, preview adapter, фильтры, редактор и экспорт
- `Launch-Design-Picker.bat` — Windows launcher для двойного клика

## Preview Provider Adapter

MVP держит генерацию превью за небольшим adapter seam внутри `app.js`.

Текущий порядок работы:

1. manual preview override;
2. hosted screenshot endpoint;
3. встроенная fallback-карточка.

Текущий hosted screenshot endpoint:

```text
https://image.thum.io/get/width/1440/crop/900/noanimate/{url}
```

Это локальный validation adapter, а не финальная жёстко зафиксированная зависимость.

## Что заимствовано концептуально

- Linkwarden:
  - направление на screenshot-preservation;
  - будущий backend path для превью;
  - модель сохранения доноров.
- Karakeep:
  - ощущение визуального browse-режима;
  - лёгкий bookmark-card UX;
  - современные паттерны коллекционного просмотра.

## Что пока отложено

- server-side metadata extraction;
- Linkwarden API integration;
- screenshot caching;
- private-network URL blocking on a backend;
- authentication;
- multi-user access;
- deployment;
- AI tagging or automatic design analysis.

## Замечание по безопасности

Этот MVP хранит данные только в текущем профиле браузера и использует внешний screenshot endpoint для публичных URL.

На этой стадии используй только публичные donor URL.
