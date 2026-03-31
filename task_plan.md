# Task Plan: Harness Engineering Repo Kickoff

## Goal
Define the first approved design for a new `harness-engineering` repository so we can implement it step by step in the right direction.

## Current Phase
Phase 5

## Phases
### Phase 1: Requirements & Discovery
- [x] Confirm current project directory state
- [x] Check whether this folder already contains a repository
- [x] Clarify the user's intended first deliverable
- [x] Narrow the first spec to a single manageable slice
- [x] Clarify the target form of the repository itself
- [x] Clarify the primary audience and adoption model
- [x] Clarify how derivative vs original the blueprint should be
- [x] Document findings in `findings.md`
- [x] Capture the requirement that the repo support installation via `skill-installer`
- [x] Clarify the packaging granularity for `skill-installer`
- [x] Clarify whether the blueprint should optimize for teaching or immediate production adoption
- **Status:** complete

### Phase 2: Planning & Structure
- [x] Propose viable repository approaches
- [x] Recommend one approach with trade-offs
- [x] Present a concrete design for approval
- **Status:** complete

### Phase 3: Specification
- [x] Write the approved design to a spec document
- [x] Self-review the spec for ambiguity and scope
- [x] Ask the user to review the written spec
- **Status:** complete

### Phase 4: Implementation Planning
- [x] Create a detailed implementation plan from the approved spec
- [x] Offer execution options for the plan
- **Status:** complete

### Phase 5: Implementation & Verification
- [x] Implement the approved plan
- [x] Verify behavior with tests or other checks
- [ ] Deliver results clearly
- **Status:** in_progress

## Key Questions
1. No open implementation questions remain. The remaining step is final handoff to the user.

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Start with brainstorming instead of scaffolding | The project direction is still open and the brainstorming skill requires design approval before implementation |
| Treat this folder as a new project root | `E:\projects\harness-engineering` is currently empty and not a Git repository |
| Make the first deliverable a design/spec | The user explicitly chose a spec-first kickoff |
| Scope the first spec to the full repository architecture and design principles | The user chose option `A` for the spec focus |
| Use an OpenAI-style platformized architecture as the baseline | The user chose option `A` after reviewing mainstream OpenAI/Anthropic approaches |
| Design the repo as a public reusable blueprint | The user chose option `B` for the audience and adoption model |
| Use a medium-borrowing strategy from `obra/superpowers` | The user chose option `B`: absorb strong ideas but make architecture and naming its own |
| Treat “harness engineering” as the central concept, not as a side note | The user explicitly emphasized that this repo is about harness engineering informed by OpenAI and Anthropic |
| Make the repository installable through `skill-installer` | The user explicitly wants the public blueprint to support skill-installer-based installation |
| Support dual distribution inside the repo: one umbrella skill plus separately installable module skills | The user chose option `C` for packaging granularity |
| Optimize v1 for teaching and conceptual clarity | The user chose option `A` for the public blueprint's first-version priority |
| Use a `Harness Blueprint Monorepo` as the top-level architecture | Best fit for pedagogy, installability, and an OpenAI-style workflow/eval/trace-centered design |
| Keep v1 `skill-installer` first while leaving room for a future plugin layer | This preserves the current distribution goal without locking the repository into one packaging mechanism |
| Store the implementation plan under `docs/plans/` instead of `docs/superpowers/plans/` | The repository's own information architecture should stay centered on harness engineering, not on `superpowers` naming |
| Execute the implementation plan inline in this session | The user repeatedly asked to continue step by step without pausing for a mode switch |
| Start implementation on `codex/bootstrap-root` instead of `main` | This satisfies the safety rule to avoid doing feature work directly on the main branch |
| Continue implementation on the current feature branch after bootstrap | This kept work in the requested folder while preserving branch isolation without a disruptive midstream move |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| `rg.exe` access denied in this environment | 1 | Fell back to native PowerShell search commands |
| Design docs cannot be committed yet | 1 | Deferred commit until the directory is initialized as a Git repository |
| Git worktree setup cannot be used immediately | 1 | Deferred until the repository had committed source-of-truth files; implementation then continued safely on the current feature branch |

## Notes
- Keep implementation blocked until the design is approved.
- Re-read this plan before major decisions.
- All eight implementation tasks are complete.
- Final handoff and verification summary are the only remaining step.
