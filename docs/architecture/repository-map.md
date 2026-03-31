# Repository Map

## Purpose

This document explains the intended top-level structure of `harness-engineering` and the source-of-truth rules for each area.

## Top-Level Map

```text
harness-engineering/
  AGENTS.md
  README.md
  docs/
  skills/
  blueprints/
  examples/
  references/
  scripts/
  tests/
```

## Directory Roles

| Path | Role | Owns Canonical Meaning? | Notes |
|------|------|------|------|
| `README.md` | human entry point | No | explains what the repository is and how to start |
| `AGENTS.md` | agent routing map | No | points agents to the correct docs and assets |
| `docs/specs/` | design contracts | Yes | holds approved design and planning inputs |
| `docs/concepts/` | conceptual definitions | Yes | defines repository vocabulary |
| `docs/architecture/` | structural rules | Yes | defines boundaries, maps, and object relationships |
| `docs/workflows/` | workflow explanation docs | Yes | explains workflow patterns and examples |
| `docs/tools/` | tool contract docs | Yes | explains tool contract design and usage |
| `docs/evals/` | eval explanation docs | Yes | explains eval goals, rubric, and usage patterns |
| `docs/prompts/` | prompt asset docs | Yes | explains prompt asset design and usage |
| `docs/policies/` | system policy docs | Yes | defines constraints and approval rules |
| `docs/examples/` | example explanation docs | No | explains the example set without redefining canonical meaning |
| `skills/` | installable skill entry points | No | exposes repository capabilities via `skill-installer` |
| `blueprints/` | canonical templates | Yes, for structure | standard object patterns and forms |
| `examples/` | instantiated teaching cases | No | concrete demonstrations built from blueprints |
| `references/` | external mappings | No | stores inspirations and external-source notes |
| `scripts/` | support utilities | No | validates, generates, or checks repository assets |
| `tests/` | quality verification | No | tests docs structure, mappings, and repository checks |

## Source-of-Truth Rule

Definitions live in docs, templates live in blueprints, entry flows live in skills, demonstrations live in examples.

## Entry Surfaces

### README.md

Should answer:

- what harness engineering is in the context of this repository
- who the repository is for
- how to install the umbrella skill
- where to start reading

### AGENTS.md

Should answer:

- where an agent should look first for architecture
- how to locate blueprint assets
- which skill or doc to use for workflow, eval, trace, and legibility work

It should remain short and route-oriented.

## Skill Layout

Version 1 skill layout:

```text
skills/
  harness-engineering/
  workflow-design/
  prompt-assets/
  tool-contracts/
  eval-design/
  trace-review/
  repo-legibility/
```

Each skill directory basename is a public install name when distributed through `skill-installer`.

## Blueprint Layout

Version 1 blueprint layout:

```text
blueprints/
  workflows/
  tools/
  prompts/
  evals/
  traces/
  policies/
```

These directories should contain canonical object templates, not long narrative explanations.

## Example Layout

Version 1 example layout:

```text
examples/
  minimal/
  productized/
```

- `minimal/` is the shortest understandable end-to-end teaching case.
- `productized/` shows a more realistic long-lived repository organization.

## Drift Prevention Rules

- Skills may guide users, but may not redefine canonical concepts.
- Examples may simplify patterns, but may not contradict docs or blueprints.
- References may explain inspiration, but may not become the repository's design contract.
