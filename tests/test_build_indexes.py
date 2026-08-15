import sys
import tempfile
import unittest
from pathlib import Path
import subprocess
import time

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
            check_before = {path: path.read_bytes() for path in root.rglob("INDEX.md")} | {root / "llms.txt": (root / "llms.txt").read_bytes()}
            self.assertEqual(self.command(root, "--check").returncode, 0)
            check_after = {path: path.read_bytes() for path in root.rglob("INDEX.md")} | {root / "llms.txt": (root / "llms.txt").read_bytes()}
            self.assertEqual(check_after, check_before)
            before = {path: path.read_bytes() for path in root.rglob("INDEX.md")} | {root / "llms.txt": (root / "llms.txt").read_bytes()}
            self.assertEqual(self.command(root, "--build").returncode, 0)
            after = {path: path.read_bytes() for path in root.rglob("INDEX.md")} | {root / "llms.txt": (root / "llms.txt").read_bytes()}
            self.assertEqual(after, before)
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
            (root / "docs/huawei/INDEX.md").unlink()
            self.assertNotEqual(self.command(root, "--check").returncode, 0)
            self.assertEqual(self.command(root, "--build").returncode, 0)
            self.assertEqual(self.command(root, "--check").returncode, 0)

    def test_builds_one_thousand_documents_within_ten_seconds(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = root / "docs/huawei/ma5800-x7/diag"
            directory.mkdir(parents=True)
            for number in range(1000):
                (directory / f"documento-{number:04d}.md").write_text(
                    DOCUMENT.replace("# ONT", f"# ONT {number}"), encoding="utf-8"
                )
            start = time.perf_counter()
            result = self.command(root, "--build")
            elapsed = time.perf_counter() - start
            self.assertEqual(result.returncode, 0, result.stderr)
            print(f"INDEX_BUILD_1000_ELAPSED_SECONDS={elapsed:.3f}")
            self.assertLess(elapsed, 10, f"build took {elapsed:.3f}s")
