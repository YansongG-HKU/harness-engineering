# Repository Map Reference

This packaged copy keeps the installed `repo-legibility` skill usable after
`skill-installer` copies only this directory.

In the source repository, the canonical source lives at
docs/architecture/repository-map.md.

## Repository Map

Definitions live in docs, templates live in blueprints, entry flows live in
skills, demonstrations live in examples.

## Top-Level Areas

- `docs/` holds canonical definitions and architecture rules
- `skills/` holds installable entry points
- `blueprints/` holds canonical templates
- `examples/` holds teaching examples
- `scripts/` and `tests/` enforce repository legibility

## Drift Prevention Rules

- Skills may guide users, but may not redefine canonical concepts.
- Examples may simplify patterns, but may not contradict docs or blueprints.
- References may explain inspiration, but may not become the design contract.
