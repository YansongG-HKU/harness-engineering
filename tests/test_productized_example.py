from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = {
    "examples/productized/README.md": [
        "# Productized Example",
        "repository-shape.md",
        "trace-review.md",
    ],
    "examples/productized/repository-shape.md": [
        "# Repository Shape",
        "docs/",
        "skills/",
        "blueprints/",
    ],
    "examples/productized/workflow.md": [
        "# Workflow",
        "review checkpoints",
        "blueprints/workflows/workflow-template.md",
    ],
    "examples/productized/tool-contract.md": [
        "# Tool Contract",
        "approval",
        "blueprints/tools/tool-contract-template.md",
    ],
    "examples/productized/eval.md": [
        "# Eval",
        "success criteria",
        "blueprints/evals/eval-template.md",
    ],
    "examples/productized/trace-review.md": [
        "# Trace Review",
        "Trace",
        "review loop",
        "blueprints/traces/trace-template.md",
    ],
    "examples/productized/policy.md": [
        "# Policy",
        "quality checks",
        "blueprints/policies/policy-template.md",
    ],
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
