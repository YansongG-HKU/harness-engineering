# Findings & Decisions

## Requirements
- The user wants to work inside `E:\projects\harness-engineering`.
- The user asked to use `using-superpowers` and move forward step by step according to their needs.
- Prior local Codex history suggests the broader topic is building a `harness-engineering` repository informed by `obra/superpowers`.
- The user chose option `A`: write a complete design/spec first before deciding implementation.
- The user chose option `A` again for scope: the first spec should cover the whole repository architecture and design principles.
- The user chose option `A` for positioning: use an OpenAI-style platformized workflow/eval/trace repository as the main baseline.
- The user chose option `B` for audience: make the repository a public blueprint others can fork, study, and extend.
- The user chose option `B` for derivative strategy: borrow useful ideas from `obra/superpowers`, but make the architecture, naming, and system identity its own.
- The user explicitly stressed that the repository is about `harness-engineering`, using OpenAI and Anthropic as primary references.
- The user wants the repository to support installation through `skill-installer`.
- The user chose option `C` for installation shape: support both a top-level umbrella skill and individually installable module skills from the same repo.
- The user chose option `A` for v1 priority: teaching and conceptual clarity should come before immediate production acceleration.
- The user approved the recommended top-level approach: a `Harness Blueprint Monorepo`.

## Research Findings
- The current project directory is empty.
- The current project directory is not yet a Git repository.
- The brainstorming skill requires design approval before any implementation or scaffolding.
- As of 2026-03-31, both OpenAI and Anthropic publicly recommend starting with a single agent plus tools, and only moving to multi-agent orchestration when complexity clearly requires it.
- OpenAI frames agent systems around three core parts: model, tools, and instructions; it also emphasizes standardized reusable tools, guardrails, human intervention, and eval-driven iteration.
- OpenAI's current platform direction includes versioned prompts, workflow/version objects in Agent Builder, trace graders, asynchronous eval runs, and explicit safety controls such as structured outputs, user-message isolation for untrusted input, and tool approvals.
- Anthropic's public guidance emphasizes defining measurable success criteria first, using multidimensional evals, prompt templates with variables, test-case generation, subagents with isolated context windows, hooks, CLAUDE.md memory, and MCP as the main extension surface.
- Anthropic's public engineering guidance on multi-agent systems emphasizes teaching the orchestrator how to delegate, giving subagents clear boundaries and output formats, and evaluating with transcript/trace-aware methods instead of only final-answer checks.
- Across both vendors, the mature pattern is not "just prompts"; it is a repository/system that combines prompt assets, workflow definitions, tool contracts, memory/instruction layers, eval datasets, trace logging, and safety controls.
- OpenAI now explicitly uses the term `harness engineering` in a February 11, 2026 engineering post about Codex. In that framing, engineers increasingly design environments, scaffolding, feedback loops, and repository structure so agents can do reliable work, rather than writing code by hand.
- In OpenAI's `harness engineering` write-up, the repository itself becomes the system of record: a short `AGENTS.md` acts as a map, while structured docs, plans, specs, quality grades, and reference material live in a versioned knowledge tree inside the repo.
- OpenAI's `harness engineering` pattern also emphasizes making the application legible to agents via direct access to UI state, logs, metrics, traces, and mechanical architectural enforcement through linters and structural tests.
- Anthropic's strongest complementary contribution is `context engineering`: file/folder structure as searchable context, subagents for isolated task windows, hooks for automated checks, CLAUDE.md plus auto memory for persistent instructions/learnings, and MCP for standardized tool/data connectivity.
- OpenAI's public eval stack is more platformized around Agent Builder, trace grading, datasets, and asynchronous eval runs. Anthropic's public eval guidance is more rubric-driven and repository-operational, stressing success criteria, multidimensional grading, pass@k vs pass^k, and eval-driven development.
- The best synthesis for this repo is not “a prompt collection” and not “a clone of superpowers.” It is a public blueprint for agent harness design: how to structure repo knowledge, workflows, prompts, tools, evals, traces, policies, and review loops so agents can build and maintain software reliably.
- The `skill-installer` skill installs from a GitHub repo/path into `$CODEX_HOME/skills/<skill-name>`, so this repo must expose stable installable skill paths, clean per-skill directories, and docs that make repo-path installation obvious.
- Because `skill-installer` installs path basenames as skill names by default and aborts if the destination already exists, naming and package granularity are first-class architecture decisions for this repo.
- OpenAI's current Codex docs state that `skills` are the authoring format for reusable workflows, while `plugins` are the installable distribution unit for reusable skills and apps in Codex. That means a modern public repo should at least be plugin-aware even if v1 distribution relies on `skill-installer`.
- OpenAI's Codex skills docs also make the expected on-disk structure explicit: each skill is a directory containing `SKILL.md` plus optional `scripts/`, `references/`, `assets/`, and `agents/openai.yaml`.
- The openai/skills repository exposes many installable skills as sibling directories under `skills/.curated/<skill-name>`, which is a strong precedent for this repo's module-level install paths.
- The approved design has now been written into canonical docs under `docs/specs/` and `docs/architecture/`, which are the initial source-of-truth files for the repository.
- The implementation plan has been written to `docs/plans/2026-03-31-harness-blueprint-monorepo-implementation.md`.
- A design consistency fix was applied during planning: `docs/tools/` and `blueprints/tools/` are explicit parts of the canonical layout so the repository structure matches the `Tool Contract` object model.
- The repository has now been initialized as Git and development is proceeding on branch `codex/bootstrap-root`.
- Task 1 verified that the root bootstrap can be driven cleanly with Python `unittest` checks before any production scaffold files are added.
- Because the approved spec and architecture docs were created before `git init`, immediate migration into a separate git worktree is deferred until those source-of-truth files are committed.
- Empty scaffold directories need placeholder files such as `.gitkeep`; otherwise a clean Git checkout would drop them and invalidate repository-shape tests.
- The first canonical documentation layer is now implemented and anchored by explicit marker tests for concepts, workflows, tool contracts, prompt assets, evals, policy, examples, and vendor reference indexes.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Use brainstorming before writing code or scaffolding | Required by skill and appropriate for an empty greenfield repository |
| Use planning files in the repo root | Preserves context across sessions and fits the user's request for step-by-step progress |
| Treat this turn as a spec-definition phase | The user selected a design-first approach |
| Frame the first design at the repository level, not subsystem level | The user wants the top-level architecture and principles first |
| Ground the top-level spec in vendor-public patterns from OpenAI and Anthropic | The user explicitly asked what mature mainstream approaches look like |
| Bias the architecture toward workflow objects, evals, traces, and versioned prompt assets | This is the strongest overlap with the OpenAI-style public pattern the user selected |
| Optimize the design for public readability and reuse, not just personal convenience | The user wants a reusable blueprint that other people can adopt |
| Use `superpowers` as inspiration, not as the reference architecture | The chosen strategy is moderate borrowing rather than close imitation |
| Center the repo around harness engineering as a discipline | This is the clearest project identity emerging from current OpenAI and Anthropic material |
| Treat installability as part of the public architecture, not a post-hoc addon | `skill-installer` compatibility affects repo layout, naming, and onboarding |
| Model the repo as a multi-skill source tree rather than a single monolith | This fits the chosen umbrella-plus-modules installation pattern and aligns with OpenAI's curated skills repo layout |
| Favor conceptual clarity in the first public release | The repository is intended to teach harness engineering, not just ship utilities quickly |
| Organize the project as a blueprint monorepo, not a docs-only atlas or runtime-first starter kit | This is the best balance between concept teaching and installable reusable structure |
| Write the canonical design first into `docs/specs/` and focused architecture docs | This creates a stable source of truth before any implementation or scaffolding begins |
| Write the implementation plan under `docs/plans/` and keep it within the repository's own naming system | This keeps plans aligned with the public blueprint identity |
| Start implementation on a feature branch immediately after `git init` | Avoids doing feature work directly on `main` while the repository is still being bootstrapped |
| Defer git worktree creation until committed source-of-truth files exist | A fresh worktree can only check out committed files, and the approved design docs still need to enter repository history |
| Preserve intentionally empty scaffold directories with `.gitkeep` files | Git does not track empty directories, but the repository contract and tests require them to exist |
| Keep canonical docs intentionally concise in v1 | The repository is teaching-first, so each document should establish stable concepts without overloading the initial layer |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| `rg.exe` could not run due to access denied | Used PowerShell `Get-ChildItem` and `Select-String` instead |
| The folder is not yet a Git repository, so the spec cannot be committed yet | Keep the written spec on disk and defer commit until repository initialization |

## Resources
- `C:/Users/guoya/.codex/superpowers/skills/using-superpowers/SKILL.md`
- `C:/Users/guoya/.codex/superpowers/skills/brainstorming/SKILL.md`
- `C:/Users/guoya/.codex/superpowers/skills/writing-plans/SKILL.md`
- `C:/Users/guoya/.codex/skills/planning-with-files/SKILL.md`
- OpenAI harness engineering post: https://openai.com/index/harness-engineering/
- OpenAI practical guide to building agents: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- OpenAI Agent Builder guide: https://developers.openai.com/api/docs/guides/agent-builder
- OpenAI agent evals guide: https://developers.openai.com/api/docs/guides/agent-evals
- OpenAI trace grading guide: https://developers.openai.com/api/docs/guides/trace-grading
- OpenAI evals guide: https://developers.openai.com/api/docs/guides/evals
- OpenAI evaluation best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- OpenAI agent safety guide: https://developers.openai.com/api/docs/guides/agent-builder-safety
- OpenAI prompting guide: https://developers.openai.com/api/docs/guides/prompting
- Anthropic tool use overview: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- Anthropic define success + eval design guide: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- Anthropic evaluation tool guide: https://platform.claude.com/docs/en/test-and-evaluate/eval-tool
- Anthropic prompt tools guide: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools
- Anthropic subagents docs: https://code.claude.com/docs/en/sub-agents
- Anthropic hooks docs: https://code.claude.com/docs/en/hooks
- Anthropic memory docs: https://code.claude.com/docs/en/memory
- Anthropic MCP docs: https://code.claude.com/docs/en/mcp
- Anthropic engineering on multi-agent research: https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic engineering on agent evals: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `skill-installer` skill docs: `C:/Users/guoya/.codex/skills/.system/skill-installer/SKILL.md`
- OpenAI Codex skills docs: https://developers.openai.com/codex/skills
- OpenAI API skills guide: https://developers.openai.com/api/docs/guides/tools-skills
- OpenAI skills repository README: https://github.com/openai/skills/blob/main/README.md
- OpenAI curated skills directory: https://github.com/openai/skills/tree/main/skills/.curated

## Visual/Browser Findings
- No browser or image findings yet.
