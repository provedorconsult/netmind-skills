"""Isolation checks for the G05 Cisco sample and unchanged Huawei tree."""

import hashlib
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HUAWEI_HASHES = {
    "INDEX.md": "322f9e5f05a48e6c6f13f8c5aa490b2b1e02a2ee76532789112eaf93422486ae",
    "cli/ont-and-profile-discovery.md": "038fd6e70fc5745a870518d2e10096cd9e22ea3d4a0f53301b97ad25f062cd78",
    "config/dba-and-uplink-vlan.md": "0102601f516aeff142e8a7dbdd5ca6bebf37f84c0adbffb386c639e5a469fcf3",
    "diag/gem-mapping-service-failure.md": "2dcd23bb346467a0330a9077a8114c09a62a51ea4d12c3c50ba7fd8f67b15bcd",
    "mon/service-port-counters.md": "5e4d036904ba3b69f2770fed498a9a1f4b796077980a612221a7cb15d81d49e0",
    "update/rollback-prechecks.md": "33e37e630eab22d98bef36d69271eeace331d627a1d019ea83ffa577cf9b46a2",
    "cli/.gitkeep": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
    "config/.gitkeep": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
    "diag/.gitkeep": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
    "mon/.gitkeep": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
    "update/.gitkeep": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
}


class MikroTikCiscoMigrationTests(unittest.TestCase):
    def test_cisco_sample_and_huawei_isolation(self):
        cisco = ROOT / "docs" / "cisco" / "asr1001-x"
        for category in ("cli", "config", "diag", "mon", "update"):
            self.assertEqual(len(list((cisco / category).glob("*.md"))), 1)
        huawei = ROOT / "docs" / "huawei" / "ma5800-x7"
        actual_hashes = {
            path.relative_to(huawei).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in huawei.rglob("*") if path.is_file()
        }
        self.assertEqual(actual_hashes, HUAWEI_HASHES)
        result = subprocess.run(
            [sys.executable, "scripts/build_indexes.py", "--check"],
            cwd=ROOT, check=False, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
