from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_DOCS = {
    "docs/concepts/harness-engineering.md": [
        "# Harness Engineering",
        "Repository as system of record",
        "workflow",
        "trace",
    ],
    "docs/concepts/harness-loop.md": [
        "# Harness Loop",
        "Design -> Execute -> Trace -> Evaluate -> Review -> Iterate -> Design",
    ],
    "docs/workflows/overview.md": [
        "# Workflow Design",
        "Workflow",
        "exit conditions",
    ],
    "docs/tools/tool-contracts.md": [
        "# Tool Contracts",
        "inputs",
        "outputs",
        "approval",
    ],
    "docs/prompts/prompt-assets.md": [
        "# Prompt Assets",
        "versioned",
        "variables",
    ],
    "docs/evals/eval-design.md": [
        "# Eval Design",
        "success criteria",
        "trace-aware",
    ],
    "docs/policies/repo-policy.md": [
        "# Repository Policy",
        "No duplicate definitions",
        "quality checks",
    ],
    "docs/examples/overview.md": [
        "# Example Tracks",
        "minimal",
        "productized",
    ],
    "references/openai/README.md": [
        "# OpenAI References",
        "https://openai.com/index/harness-engineering/",
    ],
    "references/anthropic/README.md": [
        "# Anthropic References",
        "https://code.claude.com/docs/en/sub-agents",
    ],
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
