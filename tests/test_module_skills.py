from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

SKILLS = {
    "skills/workflow-design/SKILL.md": [
        "name: workflow-design",
        "docs/workflows/overview.md",
        "blueprints/workflows/workflow-template.md",
    ],
    "skills/prompt-assets/SKILL.md": [
        "name: prompt-assets",
        "docs/prompts/prompt-assets.md",
        "blueprints/prompts/prompt-asset-template.md",
    ],
    "skills/tool-contracts/SKILL.md": [
        "name: tool-contracts",
        "docs/tools/tool-contracts.md",
        "blueprints/tools/tool-contract-template.md",
    ],
    "skills/eval-design/SKILL.md": [
        "name: eval-design",
        "docs/evals/eval-design.md",
        "blueprints/evals/eval-template.md",
    ],
    "skills/trace-review/SKILL.md": [
        "name: trace-review",
        "blueprints/traces/trace-template.md",
        "Trace",
    ],
    "skills/repo-legibility/SKILL.md": [
        "name: repo-legibility",
        "docs/policies/repo-policy.md",
        "repository legibility",
    ],
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
