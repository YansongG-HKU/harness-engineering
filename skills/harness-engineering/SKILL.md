---
name: harness-engineering
description: Route users through a self-contained harness-engineering blueprint package that mirrors the repository's canonical docs and templates.
---

# Harness Engineering

Use this skill when the user wants to understand or design repository-level
harness engineering.

## Read First

- `references/blueprint-overview.md`
- `references/repository-map.md`
- `references/object-model.md`

## Route by Task

- For workflow structure questions, open `references/workflow-design.md` and `templates/workflow-template.md`
- For prompt asset design, open `references/prompt-assets.md` and `templates/prompt-asset-template.md`
- For tool-facing interface design, open `references/tool-contracts.md` and `templates/tool-contract-template.md`
- For eval strategy, open `references/eval-design.md` and `templates/eval-template.md`
- For trace interpretation, open `references/harness-loop.md` and `templates/trace-template.md`
- For repository readability and guardrails, open `references/repository-map.md` and `references/repo-policy.md`

## Focused Skill Names

If you want narrower installs from the same repo, the focused skill names are
workflow-design, prompt-assets, tool-contracts, eval-design, trace-review, and
repo-legibility.

## Operating Rule

These packaged references exist so the skill remains usable after
`skill-installer` copies only this directory. In the source repository,
canonical meaning still lives under docs/ and blueprints/, especially
docs/specs/2026-03-31-harness-blueprint-monorepo-design.md,
docs/architecture/repository-map.md, and docs/architecture/object-model.md.
