# Chrome Extension Publishing

## Purpose

Prepare extension projects for Chrome Web Store submission and review.

## Publishing Path

1. Confirm Manifest V3 support.
2. Confirm the extension works from local unpacked install.
3. Confirm production build output.
4. Confirm required permissions are minimal and explained.
5. Confirm privacy policy is ready when required.
6. Confirm screenshots, description, and feature claims match actual behavior.
7. Confirm payment, login, and license flows if monetized.
8. Confirm support/contact path.
9. Submit to Chrome Web Store.
10. Record review result and required fixes in the project, not in the reusable block.

## Store Listing Checklist

Prepare:

- extension name;
- short description;
- detailed description;
- category;
- screenshots;
- icon set;
- privacy policy URL when required;
- support URL or email;
- permission justifications;
- test credentials if review needs account access;
- pricing explanation if paid features exist.

## Technical Checklist

Before submission:

- production build succeeds;
- unpacked extension loads cleanly;
- popup/options/content UI work;
- background service worker behavior is tested;
- storage works after browser restart;
- permissions are no broader than required;
- no private keys are bundled;
- no development endpoints remain;
- version number is updated.

## Review Risk Checklist

High-risk areas:

- broad host permissions;
- unclear privacy policy;
- misleading screenshots or claims;
- hidden data flow;
- payment UX that does not explain access clearly;
- features that depend on unstable webpage structure;
- unsupported claims around AI accuracy, finance, law, health, or immigration.

## Post-Submission

Record:

- submission date;
- version submitted;
- approval/rejection result;
- reviewer notes;
- fixes required;
- final approved version;
- source commit/tag.

Keep project-specific review history in the project repository or project docs, not in this central reusable block.

## Final Rule

Do not publish until permissions, privacy, production build, and listing claims are aligned.