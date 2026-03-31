from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_BLUEPRINTS = {
    "blueprints/workflows/workflow-template.md": [
        "# Workflow Template",
        "Entry Conditions",
        "Exit Conditions",
    ],
    "blueprints/tools/tool-contract-template.md": [
        "# Tool Contract Template",
        "Inputs",
        "Outputs",
        "Approval",
    ],
    "blueprints/prompts/prompt-asset-template.md": [
        "# Prompt Asset Template",
        "Variables",
        "Constraints",
    ],
    "blueprints/evals/eval-template.md": [
        "# Eval Template",
        "Success Criteria",
        "Test Cases",
        "Rubric",
    ],
    "blueprints/traces/trace-template.md": [
        "# Trace Template",
        "Execution Summary",
        "Tool Calls",
        "Findings",
    ],
    "blueprints/policies/policy-template.md": [
        "# Policy Template",
        "Intent",
        "Rules",
        "Enforcement",
    ],
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
