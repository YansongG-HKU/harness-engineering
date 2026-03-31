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
        readme_path = ROOT / "README.md"
        agents_path = ROOT / "AGENTS.md"
        self.assertTrue(readme_path.exists(), "README.md")
        self.assertTrue(agents_path.exists(), "AGENTS.md")
        readme = readme_path.read_text(encoding="utf-8")
        agents = agents_path.read_text(encoding="utf-8")
        self.assertIn("# Harness Engineering", readme)
        self.assertIn("skill-installer", readme)
        self.assertIn("docs/architecture/repository-map.md", agents)
        self.assertIn("docs/architecture/object-model.md", agents)


if __name__ == "__main__":
    unittest.main()
