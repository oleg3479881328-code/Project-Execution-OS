# Design Picker MVP

## Purpose

`Design Picker` is a local internal website for collecting design donors, browsing them as visual cards, marking what should be reused, and exporting a clean selection record.

## Windows Launch

### Fastest path

Double-click:

`Launch-Design-Picker.bat`

This opens:

`index.html`

in your default browser.

### One copy-ready command

From PowerShell inside `projects/design-picker/`:

```powershell
.\Launch-Design-Picker.bat
```

No install step is required for the MVP.

## Owner Workflow

1. Launch the site.
2. Click `Add donor`.
3. Paste a public website URL.
4. Leave `Manual preview override` empty to use the automatic preview adapter.
5. Add tags, notes, and pattern selections.
6. Mark the donor as `Primary`, `Partial`, `Rejected`, or `Undecided`.
7. Use search and filters to shape the shortlist.
8. Export Markdown or JSON when the board is ready.

## Current MVP Capabilities

- clean local website with visual donor cards;
- add donor flow with one required field: source URL;
- automatic title fallback from the donor domain;
- automatic preview generation through a preview-provider adapter;
- manual preview override;
- edit, delete, and refresh donor actions;
- search by title, URL, notes, tags, and patterns;
- filter by decision status and by pattern;
- design statuses: `primary`, `partial`, `rejected`, `undecided`;
- reusable pattern selection:
  - `hero`
  - `cards`
  - `pricing`
  - `navigation`
  - `motion`
  - `dashboard`
  - `onboarding`
  - `checkout`
  - `custom`
- owner notes and strong-points field;
- Markdown export;
- JSON export;
- local persistence through browser `localStorage`.

## Files

- `index.html` — app shell
- `styles.css` — visual system and responsive layout
- `app.js` — state, preview adapter, filters, editor, export logic
- `Launch-Design-Picker.bat` — Windows double-click launcher

## Preview Provider Adapter

The MVP keeps preview generation behind a small adapter seam inside `app.js`.

Current runtime order:

1. manual preview override;
2. hosted screenshot endpoint;
3. built-in visual fallback card.

Current hosted screenshot endpoint:

```text
https://image.thum.io/get/width/1440/crop/900/noanimate/{url}
```

This is a local-validation adapter, not a final locked dependency.

## Existing Solutions Reused Conceptually

- Linkwarden:
  - screenshot-preservation direction;
  - future backend preview path;
  - donor preservation mindset.
- Karakeep:
  - visual browsing feel;
  - lightweight bookmark-card UX inspiration;
  - modern collection-oriented browsing patterns.

## What Is Still Deferred

- server-side metadata extraction;
- Linkwarden API integration;
- screenshot caching;
- private-network URL blocking on a backend;
- authentication;
- multi-user access;
- deployment;
- AI tagging or automatic design analysis.

## Security Note

This MVP stores data only in the current browser profile and uses an external screenshot endpoint for public URLs.

Use public donor URLs only during this MVP phase.
