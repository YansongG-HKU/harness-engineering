from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAMES = [
    "harness-engineering",
    "workflow-design",
    "prompt-assets",
    "tool-contracts",
    "eval-design",
    "trace-review",
    "repo-legibility",
]


def extract_markdown_paths(skill_text: str) -> list[str]:
    return re.findall(r"`([^`\n]+\.md)`", skill_text)


class SkillInstallerPackagingTests(unittest.TestCase):
    def install_skill_directory(self, skill_name: str) -> Path:
        temp_root = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(temp_root, ignore_errors=True))
        installed_dir = temp_root / skill_name
        shutil.copytree(ROOT / "skills" / skill_name, installed_dir)
        return installed_dir

    def test_installed_skills_only_reference_packaged_markdown_assets(self):
        for skill_name in SKILL_NAMES:
            with self.subTest(skill_name=skill_name):
                installed_dir = self.install_skill_directory(skill_name)
                skill_text = (installed_dir / "SKILL.md").read_text(encoding="utf-8")
                referenced_paths = extract_markdown_paths(skill_text)

                self.assertGreater(
                    len(referenced_paths),
                    0,
                    f"{skill_name} should reference packaged markdown assets",
                )

                for relative_path in referenced_paths:
                    self.assertFalse(
                        Path(relative_path).is_absolute(),
                        f"{skill_name} should use relative packaged paths: {relative_path}",
                    )
                    self.assertTrue(
                        (installed_dir / relative_path).exists(),
                        f"{skill_name} missing packaged asset after install: {relative_path}",
                    )


if __name__ == "__main__":
    unittest.main()
