# News Digest Subblock — Personal Secretary OS

## Purpose

Create and improve a practical news-digest workflow inside `personal-secretary-os`.

The subblock exists so Oleg can request a news digest as part of secretary mode, have each digest saved to Notion, and improve the format through real use rather than designing an abstract media product first.

## Status

- Status: `active — v1 created after first digest`
- First real digest created: `2026-06-17`
- Storage layer: Notion database `Утренние дайджесты новостей`
- Notion database URL: `https://app.notion.com/p/13c73590abed4da88c9bb5a98f225a50`
- Notion data source: `collection://1ce0c476-f620-4ed1-bd79-54c46d50ba29`

## Scope

This subblock covers news intake, selection, briefing, saving, and format improvement.

It does not replace the general secretary workflow. It is a focused operating subblock for recurring news work.

## Default Topics

Start with Oleg's stated interests:

- AI and AI tools;
- AI agents, APIs, automation, video generation, content-production tools;
- United States immigration policy;
- USCIS, ICE, I-485, marriage-based adjustment, discretion, background checks, detention, enforcement;
- United States politics;
- Donald Trump and Trump administration policy;
- CDL, trucking, truck drivers, FMCSA, ELD, compliance, safety, freight and driver-workforce issues.

Add topics only when repeated use proves they belong in the recurring digest.

## Source Rules

Use current sources for every digest.

Prefer primary or high-quality sources:

- official government sources for USCIS, ICE, FMCSA, DOT, White House, courts, regulations and agency notices;
- Reuters, AP and other reputable newsrooms for fast political and business coverage;
- official company blogs, status pages, product docs and API docs for AI tools;
- industry-specific sources only when primary or wire sources are insufficient.

When a claim is legally, financially, medically, immigration-related, or otherwise high-impact, mark uncertainty clearly and avoid treating news as personal instruction.

For immigration news, distinguish public reporting from legal advice. Recommend attorney verification when action may affect a case.

## AI Product Coverage Rule

For important AI tools that Oleg may actually use, do not rely only on broad AI news. Check the product's own release surface.

For OpenAI Codex specifically, every serious digest or follow-up about Codex should check:

- official Codex changelog on `developers.openai.com/codex/changelog`;
- official Codex docs for app, CLI, IDE, Chrome extension, Computer Use, Memories, Chronicle, Sites, plugins, Skills, Subagents, GitHub integration, pricing and feature availability when relevant;
- official OpenAI status page for outages, elevated errors, capacity problems and recovery;
- official GitHub release or PR links when the changelog points to them.

Classify Codex news into practical buckets:

- availability and geography;
- new user-facing capabilities;
- CLI/IDE/app releases;
- limits, pricing and rate-limit changes;
- outages and reliability;
- integrations and deployment;
- privacy, security and permissions;
- workflow impact for Oleg and his projects.

Do not treat rumors, Reddit summaries, YouTube summaries, unsourced user claims or other AI summaries as confirmed. Use them as leads only, then verify with official sources or mark as unconfirmed.

## Digest Style

Default style is voice-friendly because Oleg is often driving and listening through voice playback.

Use short natural paragraphs. Do not use dense visual cards, tables, copyable blocks, long bullet stacks, or field-heavy formats such as `Почему важно`, `Тебе что с этого`, `Статус`, `Источники` for every item.

Each item should read like a concise spoken briefing:

`[Topic] — [what happened] — [why it matters in one natural sentence if needed].`

Use citations in ChatGPT responses when sources were browsed. Do not over-format source lists in the spoken part.

## Default Output Shape

A normal digest should include:

1. one short opening paragraph with the main signal of the day;
2. AI and AI tools;
3. immigration and USCIS/ICE;
4. US politics and Trump;
5. CDL/trucking;
6. a short `For Oleg` paragraph with practical follow-up signals;
7. a short `Watch next` paragraph.

The section headings are allowed, but the body must remain voice-friendly prose rather than visual blocks.

## Notion Saving Rule

Each completed digest must be saved as one page in the Notion database `Утренние дайджесты новостей`.

Use these properties when available:

- `Дайджест`: title, usually `Утренний дайджест — YYYY-MM-DD — short topic list`;
- `Дата`: digest date;
- `Тип`: `Утренний`, `Вечерний`, or `Спецвыпуск`;
- `Статус`: `Готово`, `Черновик`, or `Нужно проверить`;
- `Темы`: matching topic tags;
- `Главный фокус`: one short focus sentence;
- `Короткий вывод`: one short conclusion;
- `Есть действия для Олега`: yes/no;
- `Можно использовать для контента`: yes/no;
- `Источники / примечания`: compact source or reliability notes.

Store the full digest text inside the Notion page body.

After every successful Notion save or update, always give Oleg the direct Notion page URL at the end of the response. This is mandatory because the owner needs to inspect the saved result quickly.

If Notion saving fails, still provide the digest and say explicitly that saving failed.

## Improvement Loop

This subblock should improve through operation.

After each real digest, watch for friction:

- too long;
- too short;
- too many irrelevant stories;
- missing recurring topic;
- weak sources;
- not voice-friendly;
- too much political noise;
- not enough practical output;
- sources not suitable for NotebookLM or later research;
- Notion schema missing a useful property;
- missing Notion page link after save or update.

When Oleg corrects the format, treat the correction as a candidate rule. If it affects every future digest, update this file or the relevant project state rather than relying only on chat memory.

## Current Known Preferences

- Do not use per-item field cards with `Почему важно`, `Тебе что с этого`, `Статус`, `Источники`.
- Keep ordinary conversation and digest explanations voice-friendly, not block-heavy.
- The digest should be useful for Oleg personally, not a generic newspaper summary.
- Practical signals matter: AI tools to test, immigration risks to verify, Trump/policy changes to watch, and CDL/FMCSA items that affect drivers or carriers.
- When covering a named AI tool like Codex, include product-release details if they materially affect Oleg's workflow.
- After saving or updating a digest in Notion, always include the direct Notion page link in the final response.

## Boundary

Do not create automation, scraping systems, Telegram delivery, email delivery or scheduled monitoring until repeated manual use proves the need and Oleg explicitly approves the next layer.

Do not store private raw intake or sensitive personal legal/immigration details in this GitHub file.

## Next Practical Step

Use this subblock for the next requested news digest. After delivery, note any format corrections and update this file only when the correction should become a durable rule.