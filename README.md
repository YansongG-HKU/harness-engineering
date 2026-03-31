# Harness Engineering

`harness-engineering` is a public blueprint repository for teaching how to design
agent-friendly repositories around workflows, prompt assets, tool contracts,
evals, traces, policies, and review loops.

## What This Repository Contains

- canonical docs that define the repository's object model and design rules
- blueprint templates for reusable harness objects
- installable skills that route users into the blueprint
- minimal and productized examples that demonstrate the harness loop
- lightweight validation checks for repository legibility

## Installation Model

This repository is designed to be installed through `skill-installer` using
either the umbrella skill at `skills/harness-engineering` or focused module
skills under `skills/`.

## Start Here

1. Read `docs/specs/2026-03-31-harness-blueprint-monorepo-design.md`
2. Read `docs/architecture/repository-map.md`
3. Read `docs/architecture/object-model.md`
