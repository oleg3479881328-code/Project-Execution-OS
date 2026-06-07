# Design Donor Catalog Template

## Purpose

Provide a ready-to-use repository-backed catalog format for visual donor selection.

Use this as the initial implementation before building a dedicated UI.

## Catalog Maintenance Rules

- Keep the catalog curated, not exhaustive.
- Prefer clear screenshots and stable source links.
- Tag each donor by project type and reusable section patterns.
- Record why a donor matters.
- Record what should not be copied.
- Review stale links periodically.
- Store project-specific shortlists inside the target project, not in this reusable template.

## Recommended Folder Shape

```text
blocks/design/library/
  README.md
  catalog.md
  screenshots/
    donor-001.png
    donor-002.png
  boards/
    example-project-board.md
```

## Catalog Index

| ID | Title | Preview | Source | Project Type | Style Tags | Section Tags | Complexity | Strong Points | Reuse Notes | Avoid Notes | Copy / Asset Risk | Added |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `donor-001` | Example donor | `screenshots/donor-001.png` | `https://example.com` | SaaS landing page | minimal, light, technical | hero, pricing, FAQ | medium | Clear hierarchy | Adapt section order and CTA placement | Do not reuse copy or proprietary illustrations | Check asset licenses | YYYY-MM-DD |

## Donor Detail Card

```md
# donor-XXX — Title

## Source
- URL:
- Preview:
- Source type: live site / gallery / template / component library / screenshot / internal project
- Added date:

## Fit
- Project type:
- Audience:
- Conversion goal:
- Complexity: low / medium / high

## Tags
- Style:
- Sections:
- Components:

## Strong Points
- ...

## Reuse Notes
- ...

## Avoid Notes
- ...

## Implementation Notes
- Responsive implications:
- Motion implications:
- Libraries or stack implications:

## Copy / Asset Risk
- ...
```

## Project-Specific Design Board

```md
# Design Board — Project Name

## Project Goal
- ...

## Shortlist
| Donor ID | Preview | Role In Proposed Design | Owner Decision | Notes |
| --- | --- | --- | --- | --- |
| `donor-001` | `path/to/preview.png` | primary direction / hero / cards / pricing / navigation / motion | selected / partial / rejected / undecided | ... |

## Owner Selection Record

### Primary Direction
- donor id:
- why selected:

### Borrow These Patterns
- donor id + section/component:

### Avoid
- rejected direction or pattern:

### Style Notes In Owner's Words
- ...

### Open Design Decisions
- ...
```

## Future UI Mapping

A future visual Design Picker UI should map directly to this schema:

- thumbnail grid;
- filters by project type, style, section, and complexity;
- donor detail drawer;
- select as primary;
- select partial pattern;
- reject;
- add owner note;
- export project design board;
- export design-selection record for the agent.

## Final Rule

Start simple, preserve the data structure, and leave a clean upgrade path to a visual application.