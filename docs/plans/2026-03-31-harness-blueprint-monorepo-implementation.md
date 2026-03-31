# Harness Blueprint Monorepo Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bootstrap the first public, installable, teaching-quality version of the `harness-engineering` repository with canonical docs, blueprint templates, installable skills, examples, and mechanical repository checks.

**Architecture:** Build the repository in layers. First establish the root scaffold and entry docs, then add canonical docs and blueprint templates, then add umbrella and module skills, then add example tracks, and finally enforce the repository contract with mechanical checks. Keep the implementation lightweight and repository-native by using Markdown assets plus Python standard-library validation tests.

**Tech Stack:** Markdown, Mermaid, Python 3 standard library, `unittest`, Git, Codex `SKILL.md` skills, `skill-installer`-compatible directory layout

---

## File Structure

### Root Entry and Hygiene

- Create: `README.md`
- Create: `AGENTS.md`
- Create: `.gitignore`
- Create: `.editorconfig`

### Canonical Docs

- Create: `docs/concepts/harness-engineering.md`
- Create: `docs/concepts/harness-loop.md`
- Create: `docs/workflows/overview.md`
- Create: `docs/tools/tool-contracts.md`
- Create: `docs/prompts/prompt-assets.md`
- Create: `docs/evals/eval-design.md`
- Create: `docs/policies/repo-policy.md`
- Create: `docs/examples/overview.md`
- Create: `references/openai/README.md`
- Create: `references/anthropic/README.md`

### Blueprint Templates

- Create: `blueprints/workflows/workflow-template.md`
- Create: `blueprints/tools/tool-contract-template.md`
- Create: `blueprints/prompts/prompt-asset-template.md`
- Create: `blueprints/evals/eval-template.md`
- Create: `blueprints/traces/trace-template.md`
- Create: `blueprints/policies/policy-template.md`

### Skills

- Create: `skills/harness-engineering/SKILL.md`
- Create: `skills/workflow-design/SKILL.md`
- Create: `skills/prompt-assets/SKILL.md`
- Create: `skills/tool-contracts/SKILL.md`
- Create: `skills/eval-design/SKILL.md`
- Create: `skills/trace-review/SKILL.md`
- Create: `skills/repo-legibility/SKILL.md`

### Examples

- Create: `examples/minimal/README.md`
- Create: `examples/minimal/workflow.md`
- Create: `examples/minimal/prompt-asset.md`
- Create: `examples/minimal/tool-contract.md`
- Create: `examples/minimal/eval.md`
- Create: `examples/minimal/trace.md`
- Create: `examples/minimal/policy.md`
- Create: `examples/productized/README.md`
- Create: `examples/productized/repository-shape.md`
- Create: `examples/productized/workflow.md`
- Create: `examples/productized/tool-contract.md`
- Create: `examples/productized/eval.md`
- Create: `examples/productized/trace-review.md`
- Create: `examples/productized/policy.md`

### Validation

- Create: `tests/test_root_scaffold.py`
- Create: `tests/test_canonical_docs.py`
- Create: `tests/test_blueprint_templates.py`
- Create: `tests/test_umbrella_skill.py`
- Create: `tests/test_module_skills.py`
- Create: `tests/test_minimal_example.py`
- Create: `tests/test_productized_example.py`
- Create: `tests/test_repository_checks.py`
- Create: `scripts/check_repository.py`

### Existing Inputs

- Read: `docs/specs/2026-03-31-harness-blueprint-monorepo-design.md`
- Read: `docs/architecture/repository-map.md`
- Read: `docs/architecture/object-model.md`

## Task 1: Bootstrap the Repository Root

**Files:**
- Create: `.gitignore`
- Create: `.editorconfig`
- Create: `README.md`
- Create: `AGENTS.md`
- Create: `tests/test_root_scaffold.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RootScaffoldTests(unittest.TestCase):
    def test_root_files_exist(self):
        expected_files = [
            ".gitignore",
            ".editorconfig",
            "README.md",
            "AGENTS.md",
            "docs/specs/2026-03-31-harness-blueprint-monorepo-design.md",
            "docs/architecture/repository-map.md",
            "docs/architecture/object-model.md",
        ]
        for relative_path in expected_files:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((ROOT / relative_path).exists(), relative_path)

    def test_root_directories_exist(self):
        expected_directories = [
            "docs/concepts",
            "docs/workflows",
            "docs/tools",
            "docs/evals",
            "docs/prompts",
            "docs/policies",
            "docs/examples",
            "skills",
            "blueprints/workflows",
            "blueprints/tools",
            "blueprints/prompts",
            "blueprints/evals",
            "blueprints/traces",
            "blueprints/policies",
            "examples/minimal",
            "examples/productized",
            "references/openai",
            "references/anthropic",
            "scripts",
            "tests",
        ]
        for relative_path in expected_directories:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((ROOT / relative_path).is_dir(), relative_path)

    def test_entry_docs_explain_the_repository(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("# Harness Engineering", readme)
        self.assertIn("skill-installer", readme)
        self.assertIn("docs/architecture/repository-map.md", agents)
        self.assertIn("docs/architecture/object-model.md", agents)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_root_scaffold.py" -v`
Expected: FAIL with missing `README.md`, `AGENTS.md`, and root directories.

- [ ] **Step 3: Write minimal implementation**

Create the root directories:

```powershell
git init
git branch -M main
New-Item -ItemType Directory -Force -Path `
  "docs/concepts", `
  "docs/workflows", `
  "docs/tools", `
  "docs/evals", `
  "docs/prompts", `
  "docs/policies", `
  "docs/examples", `
  "skills", `
  "blueprints/workflows", `
  "blueprints/tools", `
  "blueprints/prompts", `
  "blueprints/evals", `
  "blueprints/traces", `
  "blueprints/policies", `
  "examples/minimal", `
  "examples/productized", `
  "references/openai", `
  "references/anthropic", `
  "scripts", `
  "tests" | Out-Null
```

Create `.gitignore`:

```gitignore
__pycache__/
*.pyc
.pytest_cache/
.venv/
venv/
dist/
build/
.DS_Store
Thumbs.db
```

Create `.editorconfig`:

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 2
trim_trailing_whitespace = true

[*.py]
indent_size = 4
```

Create `README.md`:

```markdown
# Harness Engineering

`harness-engineering` is a public blueprint repository for teaching how to design agent-friendly repositories around workflows, prompt assets, tool contracts, evals, traces, policies, and review loops.

## What This Repository Contains

- canonical docs that define the repository's object model and design rules
- blueprint templates for reusable harness objects
- installable skills that route users into the blueprint
- minimal and productized examples that demonstrate the harness loop
- lightweight validation checks for repository legibility

## Installation Model

This repository is designed to be installed through `skill-installer` using either the umbrella skill at `skills/harness-engineering` or focused module skills under `skills/`.

## Start Here

1. Read `docs/specs/2026-03-31-harness-blueprint-monorepo-design.md`
2. Read `docs/architecture/repository-map.md`
3. Read `docs/architecture/object-model.md`
```

Create `AGENTS.md`:

```markdown
# AGENTS.md

Use this file as a routing map, not as the full system definition.

## Read First

- `docs/specs/2026-03-31-harness-blueprint-monorepo-design.md`
- `docs/architecture/repository-map.md`
- `docs/architecture/object-model.md`

## Canonical Sources

- Concepts live under `docs/concepts/`
- Workflow guidance lives under `docs/workflows/`
- Tool contract guidance lives under `docs/tools/`
- Prompt asset guidance lives under `docs/prompts/`
- Eval guidance lives under `docs/evals/`
- Policy guidance lives under `docs/policies/`
- Templates live under `blueprints/`
- Demonstrations live under `examples/`

## Skill Entry Points

- umbrella entry: `skills/harness-engineering/SKILL.md`
- focused entries: `skills/*/SKILL.md`
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest discover -s tests -p "test_root_scaffold.py" -v`
Expected: PASS with `OK`.

- [ ] **Step 5: Commit**

```bash
git add .gitignore .editorconfig README.md AGENTS.md tests/test_root_scaffold.py
git commit -m "chore: bootstrap repository root"
```

### Task 2: Add Canonical Docs and Reference Indexes

**Files:**
- Create: `docs/concepts/harness-engineering.md`
- Create: `docs/concepts/harness-loop.md`
- Create: `docs/workflows/overview.md`
- Create: `docs/tools/tool-contracts.md`
- Create: `docs/prompts/prompt-assets.md`
- Create: `docs/evals/eval-design.md`
- Create: `docs/policies/repo-policy.md`
- Create: `docs/examples/overview.md`
- Create: `references/openai/README.md`
- Create: `references/anthropic/README.md`
- Create: `tests/test_canonical_docs.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_DOCS = {
    "docs/concepts/harness-engineering.md": ["# Harness Engineering", "Repository as system of record", "workflow", "trace"],
    "docs/concepts/harness-loop.md": ["# Harness Loop", "Design -> Execute -> Trace -> Evaluate -> Review -> Iterate -> Design"],
    "docs/workflows/overview.md": ["# Workflow Design", "Workflow", "exit conditions"],
    "docs/tools/tool-contracts.md": ["# Tool Contracts", "inputs", "outputs", "approval"],
    "docs/prompts/prompt-assets.md": ["# Prompt Assets", "versioned", "variables"],
    "docs/evals/eval-design.md": ["# Eval Design", "success criteria", "trace-aware"],
    "docs/policies/repo-policy.md": ["# Repository Policy", "No duplicate definitions", "quality checks"],
    "docs/examples/overview.md": ["# Example Tracks", "minimal", "productized"],
    "references/openai/README.md": ["# OpenAI References", "https://openai.com/index/harness-engineering/"],
    "references/anthropic/README.md": ["# Anthropic References", "https://code.claude.com/docs/en/sub-agents"],
}


class CanonicalDocsTests(unittest.TestCase):
    def test_expected_docs_exist_with_required_markers(self):
        for relative_path, markers in EXPECTED_DOCS.items():
            file_path = ROOT / relative_path
            with self.subTest(relative_path=relative_path):
                self.assertTrue(file_path.exists(), relative_path)
                text = file_path.read_text(encoding="utf-8")
                for marker in markers:
                    self.assertIn(marker, text, f"{relative_path} missing marker: {marker}")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_canonical_docs.py" -v`
Expected: FAIL with missing canonical doc files.

- [ ] **Step 3: Write minimal implementation**

Create `docs/concepts/harness-engineering.md`:

```markdown
# Harness Engineering

Harness engineering is the practice of designing repositories, workflows, prompts, tools, evals, traces, and review loops so agents can work reliably inside a system of record.

## Core Ideas

- Repository as system of record
- Workflow-first design
- Installable entry points
- Trace-aware improvement
- Mechanical guardrails
```

Create `docs/concepts/harness-loop.md`:

```markdown
# Harness Loop

The repository standardizes the following loop:

`Design -> Execute -> Trace -> Evaluate -> Review -> Iterate -> Design`

## Why This Loop Exists

- Design defines the objects.
- Execution produces outcomes and traces.
- Review and eval feed object-level iteration.
```

Create `docs/workflows/overview.md`:

```markdown
# Workflow Design

A workflow defines task phases, checkpoints, tool calls, eval handoff, and exit conditions.

## What To Specify

- entry conditions
- task phases
- decision points
- tool use
- exit conditions
```

Create `docs/tools/tool-contracts.md`:

```markdown
# Tool Contracts

Tool contracts describe the agent-facing surface of a tool.

## Required Fields

- inputs
- outputs
- error shape
- approval boundary
- safety expectations
```

Create `docs/prompts/prompt-assets.md`:

```markdown
# Prompt Assets

Prompt assets are versioned prompt units that should be reviewed and referenced explicitly.

## Required Traits

- versioned
- named
- tied to a task
- explicit about variables
```

Create `docs/evals/eval-design.md`:

```markdown
# Eval Design

Eval design starts with explicit success criteria and should be trace-aware when output-only judgment is insufficient.

## Eval Questions

- what counts as success criteria
- what cases must be covered
- what failures traces should expose
```

Create `docs/policies/repo-policy.md`:

```markdown
# Repository Policy

The repository policy keeps canonical meaning stable and reviewable.

## Core Rules

- No duplicate definitions across docs, skills, and examples.
- Examples may simplify but may not redefine canonical meaning.
- Quality checks should enforce important repository rules mechanically.
```

Create `docs/examples/overview.md`:

```markdown
# Example Tracks

The repository ships two example tracks:

- minimal: the smallest legible harness loop
- productized: a more realistic repository organization
```

Create `references/openai/README.md`:

```markdown
# OpenAI References

- https://openai.com/index/harness-engineering/
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://developers.openai.com/api/docs/guides/agent-builder
- https://developers.openai.com/api/docs/guides/agent-evals
```

Create `references/anthropic/README.md`:

```markdown
# Anthropic References

- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/memory
- https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest discover -s tests -p "test_canonical_docs.py" -v`
Expected: PASS with `OK`.

- [ ] **Step 5: Commit**

```bash
git add docs/concepts/harness-engineering.md docs/concepts/harness-loop.md docs/workflows/overview.md docs/tools/tool-contracts.md docs/prompts/prompt-assets.md docs/evals/eval-design.md docs/policies/repo-policy.md docs/examples/overview.md references/openai/README.md references/anthropic/README.md tests/test_canonical_docs.py
git commit -m "docs: add canonical concepts and reference indexes"
```

### Task 3: Create Blueprint Templates

**Files:**
- Create: `blueprints/workflows/workflow-template.md`
- Create: `blueprints/tools/tool-contract-template.md`
- Create: `blueprints/prompts/prompt-asset-template.md`
- Create: `blueprints/evals/eval-template.md`
- Create: `blueprints/traces/trace-template.md`
- Create: `blueprints/policies/policy-template.md`
- Create: `tests/test_blueprint_templates.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_BLUEPRINTS = {
    "blueprints/workflows/workflow-template.md": ["# Workflow Template", "Entry Conditions", "Exit Conditions"],
    "blueprints/tools/tool-contract-template.md": ["# Tool Contract Template", "Inputs", "Outputs", "Approval"],
    "blueprints/prompts/prompt-asset-template.md": ["# Prompt Asset Template", "Variables", "Constraints"],
    "blueprints/evals/eval-template.md": ["# Eval Template", "Success Criteria", "Test Cases", "Rubric"],
    "blueprints/traces/trace-template.md": ["# Trace Template", "Execution Summary", "Tool Calls", "Findings"],
    "blueprints/policies/policy-template.md": ["# Policy Template", "Intent", "Rules", "Enforcement"],
}


class BlueprintTemplateTests(unittest.TestCase):
    def test_blueprints_exist_with_required_sections(self):
        for relative_path, markers in EXPECTED_BLUEPRINTS.items():
            file_path = ROOT / relative_path
            with self.subTest(relative_path=relative_path):
                self.assertTrue(file_path.exists(), relative_path)
                text = file_path.read_text(encoding="utf-8")
                for marker in markers:
                    self.assertIn(marker, text, f"{relative_path} missing marker: {marker}")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_blueprint_templates.py" -v`
Expected: FAIL with missing blueprint template files.

- [ ] **Step 3: Write minimal implementation**

Create `blueprints/workflows/workflow-template.md`:

```markdown
# Workflow Template

## Purpose

Describe the class of task this workflow handles.

## Entry Conditions

- What must be true before execution begins

## Stages

1. design
2. execute
3. trace
4. evaluate
5. review
6. iterate

## Exit Conditions

- What successful completion looks like
- What should halt execution
```

Create `blueprints/tools/tool-contract-template.md`:

```markdown
# Tool Contract Template

## Purpose

What the tool exists to do for the workflow.

## Inputs

- parameter names and meaning

## Outputs

- expected response shape

## Approval

- whether approval is required
- what operations are risky
```

Create `blueprints/prompts/prompt-asset-template.md`:

```markdown
# Prompt Asset Template

## Purpose

What task the prompt asset supports.

## Variables

- variable name
- expected type
- intended use

## Constraints

- what the prompt should avoid
- what success looks like
```

Create `blueprints/evals/eval-template.md`:

```markdown
# Eval Template

## Purpose

What the eval is meant to validate.

## Success Criteria

- explicit goals

## Test Cases

- representative inputs

## Rubric

- pass conditions
- fail conditions
```

Create `blueprints/traces/trace-template.md`:

```markdown
# Trace Template

## Execution Summary

- input
- output
- outcome

## Tool Calls

- tool used
- reason
- result

## Findings

- what the trace reveals about the harness
```

Create `blueprints/policies/policy-template.md`:

```markdown
# Policy Template

## Intent

What this policy protects or standardizes.

## Rules

- explicit repository rules

## Enforcement

- what checks or review gates should enforce the rules
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest discover -s tests -p "test_blueprint_templates.py" -v`
Expected: PASS with `OK`.

- [ ] **Step 5: Commit**

```bash
git add blueprints/workflows/workflow-template.md blueprints/tools/tool-contract-template.md blueprints/prompts/prompt-asset-template.md blueprints/evals/eval-template.md blueprints/traces/trace-template.md blueprints/policies/policy-template.md tests/test_blueprint_templates.py
git commit -m "docs: add blueprint templates"
```

### Task 4: Implement the Umbrella Skill

**Files:**
- Create: `skills/harness-engineering/SKILL.md`
- Create: `tests/test_umbrella_skill.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = ROOT / "skills/harness-engineering/SKILL.md"


class UmbrellaSkillTests(unittest.TestCase):
    def test_umbrella_skill_exists(self):
        self.assertTrue(SKILL_PATH.exists(), str(SKILL_PATH))

    def test_umbrella_skill_routes_to_canonical_docs(self):
        text = SKILL_PATH.read_text(encoding="utf-8")
        self.assertIn("name: harness-engineering", text)
        self.assertIn("docs/architecture/repository-map.md", text)
        self.assertIn("docs/architecture/object-model.md", text)
        self.assertIn("workflow-design", text)
        self.assertIn("trace-review", text)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_umbrella_skill.py" -v`
Expected: FAIL with missing `skills/harness-engineering/SKILL.md`.

- [ ] **Step 3: Write minimal implementation**

Create `skills/harness-engineering/SKILL.md`:

```markdown
---
name: harness-engineering
description: Route users into the harness-engineering blueprint, canonical docs, examples, and module skills.
---

# Harness Engineering

Use this skill when the user wants to understand or design repository-level harness engineering.

## Read First

- `docs/specs/2026-03-31-harness-blueprint-monorepo-design.md`
- `docs/architecture/repository-map.md`
- `docs/architecture/object-model.md`

## Route by Task

- For workflow structure questions, use `skills/workflow-design/SKILL.md`
- For prompt asset design, use `skills/prompt-assets/SKILL.md`
- For tool-facing interface design, use `skills/tool-contracts/SKILL.md`
- For eval strategy, use `skills/eval-design/SKILL.md`
- For trace interpretation, use `skills/trace-review/SKILL.md`
- For repository readability and guardrails, use `skills/repo-legibility/SKILL.md`

## Operating Rule

This repository treats skills as entry points into canonical docs and blueprint assets, not as the primary source of truth.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest discover -s tests -p "test_umbrella_skill.py" -v`
Expected: PASS with `OK`.

- [ ] **Step 5: Commit**

```bash
git add skills/harness-engineering/SKILL.md tests/test_umbrella_skill.py
git commit -m "feat: add umbrella harness skill"
```

### Task 5: Implement the Focused Module Skills

**Files:**
- Create: `skills/workflow-design/SKILL.md`
- Create: `skills/prompt-assets/SKILL.md`
- Create: `skills/tool-contracts/SKILL.md`
- Create: `skills/eval-design/SKILL.md`
- Create: `skills/trace-review/SKILL.md`
- Create: `skills/repo-legibility/SKILL.md`
- Create: `tests/test_module_skills.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

SKILLS = {
    "skills/workflow-design/SKILL.md": ["name: workflow-design", "docs/workflows/overview.md", "blueprints/workflows/workflow-template.md"],
    "skills/prompt-assets/SKILL.md": ["name: prompt-assets", "docs/prompts/prompt-assets.md", "blueprints/prompts/prompt-asset-template.md"],
    "skills/tool-contracts/SKILL.md": ["name: tool-contracts", "docs/tools/tool-contracts.md", "blueprints/tools/tool-contract-template.md"],
    "skills/eval-design/SKILL.md": ["name: eval-design", "docs/evals/eval-design.md", "blueprints/evals/eval-template.md"],
    "skills/trace-review/SKILL.md": ["name: trace-review", "blueprints/traces/trace-template.md", "Trace"],
    "skills/repo-legibility/SKILL.md": ["name: repo-legibility", "docs/policies/repo-policy.md", "repository legibility"],
}


class ModuleSkillTests(unittest.TestCase):
    def test_module_skills_exist_and_link_to_canonical_assets(self):
        for relative_path, markers in SKILLS.items():
            file_path = ROOT / relative_path
            with self.subTest(relative_path=relative_path):
                self.assertTrue(file_path.exists(), relative_path)
                text = file_path.read_text(encoding="utf-8")
                for marker in markers:
                    self.assertIn(marker, text, f"{relative_path} missing marker: {marker}")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_module_skills.py" -v`
Expected: FAIL with missing module skill files.

- [ ] **Step 3: Write minimal implementation**

Create `skills/workflow-design/SKILL.md`:

```markdown
---
name: workflow-design
description: Guide users through workflow design using the repository's canonical workflow docs and template.
---

# Workflow Design

Use this skill when the task is about workflow shape, checkpoints, handoffs, or exit conditions.

## Canonical References

- `docs/workflows/overview.md`
- `blueprints/workflows/workflow-template.md`
```

Create `skills/prompt-assets/SKILL.md`:

```markdown
---
name: prompt-assets
description: Guide users through prompt asset design using the repository's canonical prompt docs and template.
---

# Prompt Assets

Use this skill when the task is about reusable prompt assets, prompt variables, or prompt constraints.

## Canonical References

- `docs/prompts/prompt-assets.md`
- `blueprints/prompts/prompt-asset-template.md`
```

Create `skills/tool-contracts/SKILL.md`:

```markdown
---
name: tool-contracts
description: Guide users through tool contract design using the repository's canonical tool docs and template.
---

# Tool Contracts

Use this skill when the task is about agent-facing tool interfaces, approvals, or safety boundaries.

## Canonical References

- `docs/tools/tool-contracts.md`
- `blueprints/tools/tool-contract-template.md`
```

Create `skills/eval-design/SKILL.md`:

```markdown
---
name: eval-design
description: Guide users through eval design using the repository's canonical eval docs and template.
---

# Eval Design

Use this skill when the task is about success criteria, test cases, graders, or regression design.

## Canonical References

- `docs/evals/eval-design.md`
- `blueprints/evals/eval-template.md`
```

Create `skills/trace-review/SKILL.md`:

```markdown
---
name: trace-review
description: Guide users through trace reading and review loops using the repository's canonical trace template.
---

# Trace Review

Use this skill when the task is about understanding how a run happened, what a Trace reveals, or what object should change next.

## Canonical References

- `docs/concepts/harness-loop.md`
- `blueprints/traces/trace-template.md`
```

Create `skills/repo-legibility/SKILL.md`:

```markdown
---
name: repo-legibility
description: Guide users through repository legibility, canonical boundaries, and mechanical guardrails.
---

# Repository Legibility

Use this skill when the task is about repository legibility, source-of-truth boundaries, policy, or quality checks.

## Canonical References

- `docs/architecture/repository-map.md`
- `docs/policies/repo-policy.md`
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest discover -s tests -p "test_module_skills.py" -v`
Expected: PASS with `OK`.

- [ ] **Step 5: Commit**

```bash
git add skills/workflow-design/SKILL.md skills/prompt-assets/SKILL.md skills/tool-contracts/SKILL.md skills/eval-design/SKILL.md skills/trace-review/SKILL.md skills/repo-legibility/SKILL.md tests/test_module_skills.py
git commit -m "feat: add focused harness module skills"
```

### Task 6: Add the Minimal Example Track

**Files:**
- Create: `examples/minimal/README.md`
- Create: `examples/minimal/workflow.md`
- Create: `examples/minimal/prompt-asset.md`
- Create: `examples/minimal/tool-contract.md`
- Create: `examples/minimal/eval.md`
- Create: `examples/minimal/trace.md`
- Create: `examples/minimal/policy.md`
- Create: `tests/test_minimal_example.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = {
    "examples/minimal/README.md": ["# Minimal Example", "workflow.md", "trace.md"],
    "examples/minimal/workflow.md": ["# Workflow", "blueprints/workflows/workflow-template.md"],
    "examples/minimal/prompt-asset.md": ["# Prompt Asset", "blueprints/prompts/prompt-asset-template.md"],
    "examples/minimal/tool-contract.md": ["# Tool Contract", "blueprints/tools/tool-contract-template.md"],
    "examples/minimal/eval.md": ["# Eval", "blueprints/evals/eval-template.md"],
    "examples/minimal/trace.md": ["# Trace", "blueprints/traces/trace-template.md"],
    "examples/minimal/policy.md": ["# Policy", "blueprints/policies/policy-template.md"],
}


class MinimalExampleTests(unittest.TestCase):
    def test_minimal_example_files_exist_and_trace_back_to_blueprints(self):
        for relative_path, markers in EXPECTED_FILES.items():
            file_path = ROOT / relative_path
            with self.subTest(relative_path=relative_path):
                self.assertTrue(file_path.exists(), relative_path)
                text = file_path.read_text(encoding="utf-8")
                for marker in markers:
                    self.assertIn(marker, text, f"{relative_path} missing marker: {marker}")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_minimal_example.py" -v`
Expected: FAIL with missing `examples/minimal/*` files.

- [ ] **Step 3: Write minimal implementation**

Create `examples/minimal/README.md`:

```markdown
# Minimal Example

This example shows the smallest legible harness loop for a simple issue triage assistant.

## Files

- `workflow.md`
- `prompt-asset.md`
- `tool-contract.md`
- `eval.md`
- `trace.md`
- `policy.md`
```

Create `examples/minimal/workflow.md`:

```markdown
# Workflow

This workflow classifies one incoming issue as `bug`, `billing`, or `question`.

Derived from: `blueprints/workflows/workflow-template.md`
```

Create `examples/minimal/prompt-asset.md`:

```markdown
# Prompt Asset

The prompt asset asks the model to classify one issue and justify the decision briefly.

Derived from: `blueprints/prompts/prompt-asset-template.md`
```

Create `examples/minimal/tool-contract.md`:

```markdown
# Tool Contract

The tool contract exposes a single lookup for product area metadata.

Derived from: `blueprints/tools/tool-contract-template.md`
```

Create `examples/minimal/eval.md`:

```markdown
# Eval

The eval checks whether the classification is correct and whether the explanation stays within the allowed response shape.

Derived from: `blueprints/evals/eval-template.md`
```

Create `examples/minimal/trace.md`:

```markdown
# Trace

The trace records the prompt asset used, the optional metadata lookup, the final label, and any mismatch discovered during review.

Derived from: `blueprints/traces/trace-template.md`
```

Create `examples/minimal/policy.md`:

```markdown
# Policy

The policy forbids unsafe tool actions and requires the example to stay readable to first-time users.

Derived from: `blueprints/policies/policy-template.md`
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest discover -s tests -p "test_minimal_example.py" -v`
Expected: PASS with `OK`.

- [ ] **Step 5: Commit**

```bash
git add examples/minimal/README.md examples/minimal/workflow.md examples/minimal/prompt-asset.md examples/minimal/tool-contract.md examples/minimal/eval.md examples/minimal/trace.md examples/minimal/policy.md tests/test_minimal_example.py
git commit -m "feat: add minimal teaching example"
```

### Task 7: Add the Productized Example Track

**Files:**
- Create: `examples/productized/README.md`
- Create: `examples/productized/repository-shape.md`
- Create: `examples/productized/workflow.md`
- Create: `examples/productized/tool-contract.md`
- Create: `examples/productized/eval.md`
- Create: `examples/productized/trace-review.md`
- Create: `examples/productized/policy.md`
- Create: `tests/test_productized_example.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = {
    "examples/productized/README.md": ["# Productized Example", "repository-shape.md", "trace-review.md"],
    "examples/productized/repository-shape.md": ["# Repository Shape", "docs/", "skills/", "blueprints/"],
    "examples/productized/workflow.md": ["# Workflow", "review checkpoints", "blueprints/workflows/workflow-template.md"],
    "examples/productized/tool-contract.md": ["# Tool Contract", "approval", "blueprints/tools/tool-contract-template.md"],
    "examples/productized/eval.md": ["# Eval", "success criteria", "blueprints/evals/eval-template.md"],
    "examples/productized/trace-review.md": ["# Trace Review", "Trace", "review loop", "blueprints/traces/trace-template.md"],
    "examples/productized/policy.md": ["# Policy", "quality checks", "blueprints/policies/policy-template.md"],
}


class ProductizedExampleTests(unittest.TestCase):
    def test_productized_example_files_exist_and_link_to_blueprints(self):
        for relative_path, markers in EXPECTED_FILES.items():
            file_path = ROOT / relative_path
            with self.subTest(relative_path=relative_path):
                self.assertTrue(file_path.exists(), relative_path)
                text = file_path.read_text(encoding="utf-8")
                for marker in markers:
                    self.assertIn(marker, text, f"{relative_path} missing marker: {marker}")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_productized_example.py" -v`
Expected: FAIL with missing `examples/productized/*` files.

- [ ] **Step 3: Write minimal implementation**

Create `examples/productized/README.md`:

```markdown
# Productized Example

This example shows how the harness blueprint scales into a repository that supports long-lived review loops and multiple installable entry points.

## Files

- `repository-shape.md`
- `workflow.md`
- `tool-contract.md`
- `eval.md`
- `trace-review.md`
- `policy.md`
```

Create `examples/productized/repository-shape.md`:

```markdown
# Repository Shape

This example demonstrates a layered repository with `docs/`, `skills/`, `blueprints/`, `examples/`, and validation scripts living together.
```

Create `examples/productized/workflow.md`:

```markdown
# Workflow

The workflow coordinates repository review, example updates, and review checkpoints before publication.

Derived from: `blueprints/workflows/workflow-template.md`
```

Create `examples/productized/tool-contract.md`:

```markdown
# Tool Contract

The tool contract models a documentation checker that requires approval before modifying published artifacts.

Derived from: `blueprints/tools/tool-contract-template.md`
```

Create `examples/productized/eval.md`:

```markdown
# Eval

The eval measures documentation completeness, structural consistency, and trace-aware success criteria.

Derived from: `blueprints/evals/eval-template.md`
```

Create `examples/productized/trace-review.md`:

```markdown
# Trace Review

This trace review shows how a Trace exposes a missing repository mapping and how the review loop routes the fix back to the right canonical object.

Derived from: `blueprints/traces/trace-template.md`
```

Create `examples/productized/policy.md`:

```markdown
# Policy

The policy requires quality checks, clear ownership of canonical meaning, and review before changes to public teaching assets.

Derived from: `blueprints/policies/policy-template.md`
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest discover -s tests -p "test_productized_example.py" -v`
Expected: PASS with `OK`.

- [ ] **Step 5: Commit**

```bash
git add examples/productized/README.md examples/productized/repository-shape.md examples/productized/workflow.md examples/productized/tool-contract.md examples/productized/eval.md examples/productized/trace-review.md examples/productized/policy.md tests/test_productized_example.py
git commit -m "feat: add productized teaching example"
```

### Task 8: Add Mechanical Repository Checks

**Files:**
- Create: `scripts/check_repository.py`
- Create: `tests/test_repository_checks.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepositoryCheckTests(unittest.TestCase):
    def test_check_repository_script_runs_clean(self):
        script = ROOT / "scripts/check_repository.py"
        self.assertTrue(script.exists(), str(script))
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Repository contract OK", result.stdout)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_repository_checks.py" -v`
Expected: FAIL with missing `scripts/check_repository.py`.

- [ ] **Step 3: Write minimal implementation**

Create `scripts/check_repository.py`:

```python
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "docs/specs/2026-03-31-harness-blueprint-monorepo-design.md",
    "docs/architecture/repository-map.md",
    "docs/architecture/object-model.md",
    "skills/harness-engineering/SKILL.md",
    "skills/workflow-design/SKILL.md",
    "skills/prompt-assets/SKILL.md",
    "skills/tool-contracts/SKILL.md",
    "skills/eval-design/SKILL.md",
    "skills/trace-review/SKILL.md",
    "skills/repo-legibility/SKILL.md",
    "blueprints/workflows/workflow-template.md",
    "blueprints/tools/tool-contract-template.md",
    "blueprints/prompts/prompt-asset-template.md",
    "blueprints/evals/eval-template.md",
    "blueprints/traces/trace-template.md",
    "blueprints/policies/policy-template.md",
    "examples/minimal/README.md",
    "examples/productized/README.md",
]


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    if missing:
        print("Missing required repository paths:")
        for path in missing:
            print(f"- {path}")
        return 1
    print("Repository contract OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m unittest discover -s tests -v`
Expected: PASS with all repository contract tests green.

- [ ] **Step 5: Commit**

```bash
git add scripts/check_repository.py tests/test_repository_checks.py
git commit -m "test: add repository contract checker"
```

## Self-Review

### Spec Coverage

- Root scaffold, entry docs, and directory shape: covered by Task 1.
- Canonical docs and reference indexes: covered by Task 2.
- Blueprint templates for all core objects, including tool contracts: covered by Task 3.
- Umbrella and module skills with `skill-installer`-friendly paths: covered by Tasks 4 and 5.
- Minimal and productized example tracks: covered by Tasks 6 and 7.
- Mechanical repository checks and legibility enforcement: covered by Task 8.

No spec gaps remain for the approved version 1 bootstrap.

### Placeholder Scan

- No `TBD`, `TODO`, or `implement later` placeholders remain in the task steps.
- No unresolved path placeholders remain.

### Type Consistency

- Skill names are consistent across the spec, repository map, and task steps.
- Blueprint paths are consistent across docs, skills, examples, and the repository checker.
- The object model remains centered on workflows, prompt assets, tool contracts, evals, traces, and policies.
