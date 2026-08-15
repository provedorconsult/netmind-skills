import sys
import tempfile
import unittest
from pathlib import Path
import subprocess

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
DOCUMENT = """---
fabricante: huawei
modelo: [ma5800-x7]
categoria: diag
topicos: [ont]
descricao: Diagnóstico de ONT.
versao_firmware_testada: V100R018
ultima_atualizacao: "2026-08-15"
---
# ONT
"""


class BuildIndexesTests(unittest.TestCase):
    def command(self, root, mode):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / "build_indexes.py"), mode, "--root", str(root)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_build_check_and_navigation_chain(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            doc = root / "docs/huawei/ma5800-x7/diag/ont.md"
            doc.parent.mkdir(parents=True)
            doc.write_text(DOCUMENT, encoding="utf-8")
            self.assertEqual(self.command(root, "--build").returncode, 0)
            self.assertEqual(self.command(root, "--check").returncode, 0)
            self.assertIn("[huawei](docs/huawei/INDEX.md)", (root / "INDEX.md").read_text(encoding="utf-8"))
            self.assertIn("[ma5800-x7](ma5800-x7/INDEX.md)", (root / "docs/huawei/INDEX.md").read_text(encoding="utf-8"))
            self.assertIn("[ont](diag/ont.md)", (root / "docs/huawei/ma5800-x7/INDEX.md").read_text(encoding="utf-8"))
            for source, target in ((root / "INDEX.md", "docs/huawei/INDEX.md"), (root / "docs/huawei/INDEX.md", "ma5800-x7/INDEX.md"), (root / "docs/huawei/ma5800-x7/INDEX.md", "diag/ont.md")):
                self.assertIn(target, source.read_text(encoding="utf-8"))
                self.assertTrue((source.parent / target).is_file())
            (root / "INDEX.md").write_text("stale\n", encoding="utf-8")
            self.assertNotEqual(self.command(root, "--check").returncode, 0)
            self.assertEqual(self.command(root, "--build").returncode, 0)
            self.assertEqual(self.command(root, "--check").returncode, 0)
