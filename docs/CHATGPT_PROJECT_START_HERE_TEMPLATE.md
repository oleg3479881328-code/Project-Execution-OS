# ChatGPT Project START_HERE Template

## Purpose

This file defines the canonical format for the small `START_HERE.md` attachment placed inside a ChatGPT Project when the real project lives and evolves in durable external systems such as Notion, GitHub, Google Drive, or other connected workspaces.

The attachment is only a stable entrance into the project. It is not the project description, project memory, project state, roadmap, log, or snapshot.

## Core Rule

The real canonical `START_HERE` lives in the project's durable workspace.

The attached ChatGPT Project `START_HERE.md` should remain short and stable. It must explain in a few sentences what the file is, make clear that the project may evolve independently across multiple systems, and point the AI to the canonical live `START_HERE`.

Ordinary project evolution must not require replacing this attachment.

## Default Russian Template

Use this format by default for Oleg's ChatGPT Projects:

```md
# START_HERE

Этот файл — стабильная входная точка в проект, а не сам проект и не его текущее состояние.
Проект живой и может развиваться одновременно в Notion, GitHub, Google Drive и других связанных системах.
Перед началом работы всегда сначала открой канонический START_HERE по ссылке ниже и уже оттуда следуй по актуальным маршрутам, источникам истины, текущему состоянию и инструкциям проекта.
Не считай этот файл, историю чата или память модели актуальным состоянием проекта.

Канонический START_HERE:
<URL>
```

## Usage Rules

- Keep the explanatory part to roughly 3–4 sentences.
- Write it in Russian by default so both Oleg and the AI can read it directly.
- The only project-specific value normally changed is `<URL>`.
- The URL must point to the canonical live project `START_HERE`, not merely to a generic project home page unless that page itself is the canonical entrypoint.
- The canonical live `START_HERE` may route onward to Notion, GitHub, Google Drive, databases, logs, current state, or other systems as the project evolves.
- Do not duplicate live project state, task lists, architecture, research, decisions, or history inside the attached file.
- Do not regenerate the attachment merely because the project changed behind the canonical entrypoint.

## Final Rule

ChatGPT attachment = stable door.
Canonical live `START_HERE` = living router.
Project systems behind it = evolving project.
