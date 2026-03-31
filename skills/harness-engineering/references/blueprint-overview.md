# Harness Blueprint Overview

This packaged copy keeps the installed `harness-engineering` skill usable after
`skill-installer` copies only this directory.

In the source repository, the canonical overview lives at
docs/specs/2026-03-31-harness-blueprint-monorepo-design.md.

## Purpose

`harness-engineering` is a public blueprint for teaching how to design
agent-friendly repositories around workflows, prompt assets, tool contracts,
evals, traces, policies, and review loops.

## Install Model

This repository supports both:

- one umbrella install at `skills/harness-engineering`
- focused installs for workflow-design, prompt-assets, tool-contracts,
  eval-design, trace-review, and repo-legibility

## Standard Loop

`Design -> Execute -> Trace -> Evaluate -> Review -> Iterate -> Design`

## Operating Rule

Skills are entry surfaces. Canonical meaning belongs to docs and blueprints in
the source repository.
