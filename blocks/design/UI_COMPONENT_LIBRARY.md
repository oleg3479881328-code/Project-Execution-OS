# UI Component Library

## Purpose

Provide reusable UI component categories for website and SaaS design handoff.

## Core Rule

Components must support the user path. Do not add UI complexity to make the page look busy.

## Navigation Components

### Top Navigation

Use for most marketing sites and SaaS websites.

Must clarify:

- product identity;
- main destinations;
- login path;
- primary CTA.

### Side Navigation

Use for dashboards, admin panels, and complex apps.

Must clarify:

- current location;
- main object types;
- settings/account access.

### Breadcrumbs

Use for deep content, docs, directories, and marketplaces.

## Action Components

### Button

Define:

- primary;
- secondary;
- tertiary/text;
- destructive;
- disabled;
- loading.

### CTA Group

Use when primary and secondary actions both matter.

Example:

- Start free
- Watch demo

### Form Submit Area

Must show:

- primary action;
- cancel/back when needed;
- validation;
- loading;
- success/failure state.

## Content Components

### Card

Use for grouped information.

Types:

- feature card;
- pricing card;
- testimonial card;
- article card;
- listing card;
- dashboard metric card.

### Table

Use for dense structured comparison or admin data.

Must define:

- sorting;
- filtering;
- empty state;
- pagination;
- row actions.

### Accordion

Use for FAQ or expandable details.

Avoid hiding primary information inside accordions.

### Tabs

Use when related views share the same context.

Do not use tabs when separate pages would be clearer.

## Input Components

### Text Input

Must define:

- label;
- placeholder;
- helper text;
- validation;
- error;
- disabled state.

### Select / Combobox

Use select for small known lists. Use combobox for searchable lists.

### File Upload

Must define:

- supported file types;
- size limits;
- upload progress;
- failure handling.

### Search

Must define:

- placeholder;
- result state;
- empty state;
- filter relationship.

## Feedback Components

### Toast

Use for short transient feedback.

### Alert

Use for important persistent messages.

### Modal

Use only when interruption is necessary.

### Empty State

Must include:

- what happened;
- why it matters;
- next action.

### Loading State

Use skeletons for content-loading areas and spinners for short actions.

## SaaS Components

### Pricing Card

Must include:

- plan name;
- best-fit user;
- price;
- included value;
- limits;
- CTA.

### Usage Meter

Use when subscription limits matter.

### Upgrade Prompt

Must explain why upgrade is needed and what unlocks.

### Settings Page

Must group account, billing, integrations, notifications, and security logically.

## Final Rule

Every handoff should identify component types and states. A design without states is incomplete.