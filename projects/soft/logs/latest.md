# SOFT — latest log

## 2026-09-06 — Drive organization and re-entry bootstrap

### Owner intent

Make the SOFT Google Drive source self-explanatory so a new chat can immediately understand the project, know where material belongs, and recover the correct canonical sources without relying on prior chat context.

### Changes completed

- Created top-level Drive routing folders under SOFT:
  - `00 — PROJECT GUIDE`
  - `01 — OUR SOFTWARE`
  - `02 — THIRD-PARTY SOFTWARE`
  - `90 — INBOX — TO SORT`
- Organized project-control area under `00 — PROJECT GUIDE`.
- Created `SOFT — DRIVE GUIDE — READ FIRST` with:
  - project purpose;
  - new-chat entry sequence;
  - folder meanings;
  - file placement rules;
  - naming guidance;
  - source-of-truth precedence;
  - key project links.
- Created `SOFT — SOURCE MAP` with explicit roles for:
  - Project Execution OS global START_HERE;
  - canonical SOFT `PROJECT.md`;
  - SOFT Drive root;
  - OUR SOFTWARE / THIRD-PARTY SOFTWARE / INBOX sections;
  - official vendor sources;
  - our verified tests;
  - community evidence;
  - chat/model memory.
- Updated `projects/soft/PROJECT.md` to match the actual Drive structure.
- Created `PROJECT_STATE.md` because SOFT now has meaningful execution state.

### Technical note

The Google Drive connector can create folders but its delete action rejected folder URLs. Two initially unnecessary helper folders were therefore repurposed into useful project-control routing nodes instead of being left as garbage:
- `01 — GUIDES & INDEXES`
- `02 — SOURCE MAP`

### Validation

- Main Guide is stored under the SOFT project-control tree.
- Source Map is stored under the source-map tree.
- Canonical project links in Drive and GitHub point to the same SOFT project.
- No product-specific folders were created because no concrete product material has yet been placed into SOFT.

### Next action

Route the next real software item through Existing Solution First, then classify it into OUR SOFTWARE, THIRD-PARTY SOFTWARE, or temporary INBOX only when unresolved.
