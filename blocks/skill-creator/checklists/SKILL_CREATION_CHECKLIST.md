# Skill Creation Checklist

Use this checklist before a new central skill is registered or activated.

## Need

- [ ] The task is recurring, not one-off.
- [ ] The task is narrow enough to be one skill.
- [ ] The need is not already covered by an existing skill, block, standard, or project artifact.
- [ ] Relevant external donor solutions were checked when appropriate.

## Classification

- [ ] `skill` is the correct artifact type.
- [ ] A broader `block` is not required instead.
- [ ] A mandatory `standard` is not required instead.
- [ ] A project-specific artifact is not sufficient.
- [ ] A raw reference should not remain only a reference.

## Structure

- [ ] Folder path follows `skills/<category>/<skill-name>/`.
- [ ] `SKILL.md` exists.
- [ ] YAML frontmatter is present.
- [ ] Name is lowercase and hyphen-separated.
- [ ] Inputs are defined.
- [ ] Outputs are defined.
- [ ] Workflow is reproducible.
- [ ] Constraints are explicit.
- [ ] Failure modes are explicit.
- [ ] Validation checklist exists.
- [ ] References exist or absence is explained.

## Review And Lifecycle

- [ ] Initial lifecycle state is explicit.
- [ ] Review status is explicit.
- [ ] Duplicate scope check passed.
- [ ] Compatibility notes are present.
- [ ] Fake execution claims are absent.
- [ ] The skill is not treated as `active` before review passes.

## Registration

- [ ] The artifact exists before registry update.
- [ ] `skills/registry.md` is updated only after creation.
- [ ] Any related block or standard link is recorded.
- [ ] Activation is recorded separately from creation.

## Final Rule

A generated or committed skill is not automatically reviewed or active.