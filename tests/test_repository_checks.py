from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RepositoryCheckTests(unittest.TestCase):
    def test_check_repository_script_runs_clean(self):
        script = ROOT / "scripts/check_repository.py"
        self.assertTrue(script.exists(), str(script))
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Repository contract OK", result.stdout)


if __name__ == "__main__":
    unittest.main()
