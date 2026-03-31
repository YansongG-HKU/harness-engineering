from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = {
    "examples/minimal/README.md": ["# Minimal Example", "workflow.md", "trace.md"],
    "examples/minimal/workflow.md": [
        "# Workflow",
        "blueprints/workflows/workflow-template.md",
    ],
    "examples/minimal/prompt-asset.md": [
        "# Prompt Asset",
        "blueprints/prompts/prompt-asset-template.md",
    ],
    "examples/minimal/tool-contract.md": [
        "# Tool Contract",
        "blueprints/tools/tool-contract-template.md",
    ],
    "examples/minimal/eval.md": [
        "# Eval",
        "blueprints/evals/eval-template.md",
    ],
    "examples/minimal/trace.md": [
        "# Trace",
        "blueprints/traces/trace-template.md",
    ],
    "examples/minimal/policy.md": [
        "# Policy",
        "blueprints/policies/policy-template.md",
    ],
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
