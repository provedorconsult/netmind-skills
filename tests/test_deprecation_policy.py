"""Checks for the deprecated-document policy."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCUMENT = "---\nfabricante: cisco\nmodelo: [asr1001-x]\ncategoria: cli\ntopicos: [historico]\ndescricao: \"Documento histórico.\"\nversao_firmware_testada: \"N/A\"\nultima_atualizacao: \"2026-08-16\"\nstatus: deprecated\n---\n\n# Histórico\n"


class DeprecationPolicyTests(unittest.TestCase):
    def test_deprecated_documents_are_excluded_from_active_indexes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = root / "docs" / "_deprecated" / "cisco" / "asr1001-x" / "cli" / "historical.md"
            document.parent.mkdir(parents=True)
            document.write_text(DOCUMENT, encoding="utf-8")
            shutil.copy2(ROOT / "scripts" / "build_indexes.py", root / "build_indexes.py")
            build = [sys.executable, "build_indexes.py", "--build", "--root", "."]
            first = subprocess.run(build, cwd=root, check=False, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr + first.stdout)
            snapshot = (root / "INDEX.md").read_bytes()
            second = subprocess.run(build, cwd=root, check=False, capture_output=True, text=True)
            self.assertEqual(second.returncode, 0, second.stderr + second.stdout)
            self.assertEqual((root / "INDEX.md").read_bytes(), snapshot)
            check = subprocess.run([sys.executable, "build_indexes.py", "--check", "--root", "."], cwd=root, check=False, capture_output=True, text=True)
            self.assertEqual(check.returncode, 0, check.stderr + check.stdout)
            self.assertFalse((root / "docs" / "_deprecated" / "cisco" / "INDEX.md").exists())

    def test_without_evidence_no_active_model_is_deprecated(self):
        self.assertFalse((ROOT / "docs" / "_deprecated").exists())
        self.assertIn("not-deprecated", (ROOT / "deprecation-audit.md").read_text())


if __name__ == "__main__":
    unittest.main()
