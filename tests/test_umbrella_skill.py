from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = ROOT / "skills/harness-engineering/SKILL.md"


class UmbrellaSkillTests(unittest.TestCase):
    def test_umbrella_skill_exists(self):
        self.assertTrue(SKILL_PATH.exists(), str(SKILL_PATH))

    def test_umbrella_skill_routes_to_canonical_docs(self):
        self.assertTrue(SKILL_PATH.exists(), str(SKILL_PATH))
        text = SKILL_PATH.read_text(encoding="utf-8")
        self.assertIn("name: harness-engineering", text)
        self.assertIn("docs/architecture/repository-map.md", text)
        self.assertIn("docs/architecture/object-model.md", text)
        self.assertIn("workflow-design", text)
        self.assertIn("trace-review", text)


if __name__ == "__main__":
    unittest.main()
