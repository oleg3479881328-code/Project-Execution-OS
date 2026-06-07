# Design Systems

## Purpose

Provide reusable rules for website UI systems that are consistent, buildable, and maintainable.

## Core Rule

A design system is a set of repeatable product decisions, not a moodboard.

## Minimum Design System

Every website design package should define:

- typography scale;
- color roles;
- spacing scale;
- radius rules;
- surface and border rules;
- button styles;
- form styles;
- card styles;
- layout grid;
- responsive breakpoints;
- common component states.

## Typography

Define:

- heading levels;
- body text;
- small text;
- labels;
- line height;
- readable content width.

Rules:

- hierarchy must be obvious;
- body text must be easy to read;
- do not use too many fonts;
- decorative type must not reduce clarity.

## Color

Define color by role.

Required roles:

- background;
- surface;
- primary text;
- secondary text;
- border;
- primary action;
- secondary action;
- success;
- warning;
- error;
- focus.

Rules:

- CTA color must stand out;
- text must remain readable;
- decorative gradients must not compete with content.

## Spacing

Use a consistent spacing scale.

Good defaults:

- small: 4 / 8 / 12;
- medium: 16 / 24 / 32;
- large: 48 / 64 / 96.

Avoid random one-off spacing unless there is a clear design reason.

## Layout

Define:

- max content width;
- section padding;
- grid columns;
- card grid behavior;
- mobile stacking behavior.

## Component States

Required states:

- hover;
- focus;
- active;
- disabled;
- loading;
- error;
- success;
- empty.

## Component Consistency

A button should not change shape, size, or emphasis randomly across sections.

A card should not use unrelated spacing rules from page to page.

A form should not invent new validation behavior per field.

## Accessibility Baseline

Design must consider:

- readable color contrast;
- keyboard focus;
- readable text size;
- clear labels;
- clear error messages;
- mobile readability;
- reduced-motion alternatives when needed.

## Final Rule

If a design cannot describe its system, it is not ready for implementation.