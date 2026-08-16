"""Regression checks for the G11 canonical architecture contract."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CanonicalArchitectureTests(unittest.TestCase):
    def test_contract_covers_components_and_navigation(self):
        document = (ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
        for name in ("Device Fingerprint", "Equipment Registry", "Compatibility Registry", "Capability Registry", "Command Registry", "Error Registry", "Skill Router", "Evidence Registry"):
            self.assertIn(name, document)
        self.assertIn("docs/<fabricante>/<modelo>/<categoria>/", document)
        self.assertTrue((ROOT / "llms.txt").is_file())
        self.assertTrue((ROOT / "INDEX.md").is_file())

    def test_audit_records_no_integral_migration(self):
        audit = (ROOT / "architecture-reconciliation-audit.md").read_text(encoding="utf-8")
        self.assertIn("Nenhum arquivo técnico foi movido ou apagado", audit)
        self.assertIn("não migrados em massa", audit)


if __name__ == "__main__":
    unittest.main()
