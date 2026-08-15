"""Repository-level checks for the controlled G04 Huawei migration sample."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIGRATED = {
    "cli": "ont-and-profile-discovery.md",
    "config": "dba-and-uplink-vlan.md",
    "diag": "gem-mapping-service-failure.md",
    "mon": "service-port-counters.md",
    "update": "rollback-prechecks.md",
}


class HuaweiMa5800MigrationTests(unittest.TestCase):
    def test_controlled_sample_and_indexes_are_current(self):
        root = ROOT / "docs" / "huawei" / "ma5800-x7"
        for category, filename in MIGRATED.items():
            self.assertTrue((root / category / filename).is_file())
        self.assertTrue((ROOT / "MA5800-CLI-COMMANDS.md").is_file())
        self.assertTrue((ROOT / "TROUBLESHOOTING-CHECKLIST.md").is_file())
        self.assertTrue((ROOT / "ROLLBACK-CHECKLIST.md").is_file())

        with tempfile.TemporaryDirectory() as temporary:
            isolated_root = Path(temporary)
            shutil.copytree(ROOT / "docs" / "huawei", isolated_root / "docs" / "huawei")
            shutil.copy2(ROOT / "scripts" / "build_indexes.py", isolated_root / "build_indexes.py")

            build = subprocess.run(
                [sys.executable, "build_indexes.py", "--build", "--root", "."],
                cwd=isolated_root,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(build.returncode, 0, build.stderr + build.stdout)

            check = subprocess.run(
                [sys.executable, "build_indexes.py", "--check", "--root", "."],
                cwd=isolated_root,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(check.returncode, 0, check.stderr + check.stdout)
            self.assertEqual(
                (isolated_root / "docs" / "huawei" / "ma5800-x7" / "INDEX.md").read_text(),
                (root / "INDEX.md").read_text(),
            )

        repository_check = subprocess.run(
            [sys.executable, "scripts/build_indexes.py", "--check"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            repository_check.returncode,
            0,
            repository_check.stderr + repository_check.stdout,
        )


if __name__ == "__main__":
    unittest.main()
