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
