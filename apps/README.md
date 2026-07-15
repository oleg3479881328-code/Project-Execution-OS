# Applications

This folder contains application adapters and user interfaces that compose reusable capability blocks.

Rules:

- applications may orchestrate capabilities and present UI;
- reusable technical operations remain inside `capabilities/`;
- application code must not duplicate a capability provider implementation;
- applications depend on versioned capability contracts;
- local validation tools remain separate from product-specific applications.

## Current applications

- `block-studio/` — local visual laboratory for opening, running, and inspecting capability blocks.
