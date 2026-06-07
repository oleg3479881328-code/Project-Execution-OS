# Automation Patterns

## Purpose

Define reusable automation architectures for video-production workflows.

## Core Rule

Automate repeatable steps, preserve human review where quality, rights, facts, or brand risk matter.

## Pattern 1 — Local Script Pipeline

Use for first automation MVP.

Typical flow:

`input folder -> script -> yt-dlp/local import -> ffmpeg -> subtitle/voice step -> export folder -> review`

Good for:

- owner-controlled testing;
- batch clipping;
- preset exports;
- early desktop tooling.

## Pattern 2 — Queue-Based Worker Pipeline

Use when processing volume grows.

Typical parts:

- upload/import queue;
- job table;
- workers;
- ffmpeg processing;
- retry logic;
- output storage;
- notification;
- review queue.

## Pattern 3 — AI-Assisted Clip Selection

Use when long videos need automatic candidate moments.

Typical parts:

- transcript;
- timestamp segmentation;
- scoring/ranking;
- clip boundary proposal;
- human review;
- export.

Rule:

AI should propose clips, not silently publish them.

## Pattern 4 — Multilingual Render Matrix

Use when one master asset becomes many localized exports.

Typical parts:

- language list;
- translated script;
- TTS voice;
- localized captions;
- per-language metadata;
- export preset;
- QA status.

## Pattern 5 — Publish Package Builder

Use when direct autopublishing is not yet justified.

Package should include:

- final video;
- title;
- description;
- hashtags/tags when relevant;
- thumbnail or first-frame note;
- source note;
- rights note;
- affiliate link or CTA;
- platform target;
- language;
- publish status.

## Pattern 6 — Analytics Feedback Loop

Use after publication.

Store:

- video id;
- platform;
- account/page;
- publish date;
- source;
- template;
- hook type;
- length;
- language;
- views;
- watch time;
- completion rate;
- clicks;
- revenue;
- notes.

## Final Rule

The first automation target is repeatability, not full autonomy. Full autopublishing should come only after quality gates and failure handling are proven.