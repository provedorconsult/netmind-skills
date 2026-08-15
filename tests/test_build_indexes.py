import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import build_indexes


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
    def test_build_is_deterministic_and_check_detects_drift(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            doc = root / "docs/huawei/ma5800-x7/diag/ont.md"
            doc.parent.mkdir(parents=True)
            doc.write_text(DOCUMENT, encoding="utf-8")
            generated = build_indexes.artifacts(root)
            for path, content in generated.items():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            self.assertEqual(build_indexes.artifacts(root), generated)
            self.assertIn(root / "INDEX.md", generated)
            self.assertIn(root / "llms.txt", generated)
            self.assertIn("[ont](diag/ont.md)", generated[root / "docs/huawei/ma5800-x7/INDEX.md"])
            (root / "INDEX.md").write_text("stale\n", encoding="utf-8")
            self.assertNotEqual((root / "INDEX.md").read_text(encoding="utf-8"), build_indexes.artifacts(root)[root / "INDEX.md"])
