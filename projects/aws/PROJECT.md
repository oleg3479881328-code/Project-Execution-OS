# AWS Project

## Status

Active infrastructure / remote-workstation project.

## Purpose

Maintain the user's AWS account, cost controls, credits, and the Olga Polo remote Windows workstation used to move large files between services such as PassGallery, Wix, and Google Drive without routing bulk transfers through the user's local internet connection.

## Canonical Current State

Open: `CURRENT_STATE.md`

## Key Operational Links

- AWS Console: https://console.aws.amazon.com/
- AWS Billing and Cost Management: https://console.aws.amazon.com/costmanagement/home
- Tailscale Machines console: https://console.tailscale.com/admin/machines
- Active implementation task / execution log: https://github.com/oleg3479881328-code/AI-Coordination-Hub/issues/3

## Project Rules

- Prefer a persistent-but-normally-stopped Windows EC2 workstation.
- Owner-facing workflow must converge on one launcher/button.
- Do not expose RDP publicly.
- Remote access is through Tailscale/private networking.
- Cost control is mandatory; avoid always-on compute and unnecessary persistent resources.
- Preserve exact resource identifiers and current state in `CURRENT_STATE.md`.
