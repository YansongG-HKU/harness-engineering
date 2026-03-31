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
    "skills/harness-engineering/references/blueprint-overview.md",
    "skills/harness-engineering/references/repository-map.md",
    "skills/harness-engineering/references/object-model.md",
    "skills/harness-engineering/references/workflow-design.md",
    "skills/harness-engineering/references/prompt-assets.md",
    "skills/harness-engineering/references/tool-contracts.md",
    "skills/harness-engineering/references/eval-design.md",
    "skills/harness-engineering/references/harness-loop.md",
    "skills/harness-engineering/references/repo-policy.md",
    "skills/harness-engineering/templates/workflow-template.md",
    "skills/harness-engineering/templates/prompt-asset-template.md",
    "skills/harness-engineering/templates/tool-contract-template.md",
    "skills/harness-engineering/templates/eval-template.md",
    "skills/harness-engineering/templates/trace-template.md",
    "skills/workflow-design/references/workflow-overview.md",
    "skills/workflow-design/templates/workflow-template.md",
    "skills/prompt-assets/references/prompt-assets.md",
    "skills/prompt-assets/templates/prompt-asset-template.md",
    "skills/tool-contracts/references/tool-contracts.md",
    "skills/tool-contracts/templates/tool-contract-template.md",
    "skills/eval-design/references/eval-design.md",
    "skills/eval-design/templates/eval-template.md",
    "skills/trace-review/references/harness-loop.md",
    "skills/trace-review/templates/trace-template.md",
    "skills/repo-legibility/references/repository-map.md",
    "skills/repo-legibility/references/repo-policy.md",
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
