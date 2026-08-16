"""Failure/recovery evidence for the G07 validation commands."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALID = "---\nfabricante: huawei\nmodelo: [ma5800-x7]\ncategoria: cli\ntopicos: [teste]\ndescricao: \"Teste.\"\nversao_firmware_testada: \"N/A\"\nultima_atualizacao: \"2026-08-16\"\n---\n\n# Teste\n"


def command(script, *arguments, cwd):
    return subprocess.run([sys.executable, ROOT / "scripts" / script, *arguments], cwd=cwd, check=False, capture_output=True, text=True)


class CiDocumentValidatorTests(unittest.TestCase):
    def test_frontmatter_markdown_links_and_indexes_fail_then_recover(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            docs = root / "docs" / "huawei" / "ma5800-x7" / "cli"
            docs.mkdir(parents=True)
            document = docs / "test.md"
            document.write_text(VALID, encoding="utf-8")
            self.assertEqual(command("validate_frontmatter.py", "docs", cwd=root).returncode, 0)
            document.write_text("# Sem frontmatter\n", encoding="utf-8")
            self.assertNotEqual(command("validate_frontmatter.py", "docs", cwd=root).returncode, 0)
            document.write_text(VALID, encoding="utf-8")
            self.assertEqual(command("validate_frontmatter.py", "docs", cwd=root).returncode, 0)

            self.assertEqual(command("build_indexes.py", "--build", "--root", ".", cwd=root).returncode, 0)
            self.assertEqual(command("build_indexes.py", "--check", "--root", ".", cwd=root).returncode, 0)
            (root / "INDEX.md").write_text("stale\n", encoding="utf-8")
            self.assertNotEqual(command("build_indexes.py", "--check", "--root", ".", cwd=root).returncode, 0)
            self.assertEqual(command("build_indexes.py", "--build", "--root", ".", cwd=root).returncode, 0)
            self.assertEqual(command("build_indexes.py", "--check", "--root", ".", cwd=root).returncode, 0)

            markdown = root / "note.md"
            markdown.write_text("# Valid\n", encoding="utf-8")
            self.assertEqual(command("lint_markdown.py", ".", cwd=root).returncode, 0)
            markdown.write_text("# Invalid  \n", encoding="utf-8")
            self.assertNotEqual(command("lint_markdown.py", ".", cwd=root).returncode, 0)
            markdown.write_text("# Valid\n", encoding="utf-8")
            self.assertEqual(command("lint_markdown.py", ".", cwd=root).returncode, 0)

            markdown.write_text("[valid](docs/huawei/ma5800-x7/cli/test.md)\n", encoding="utf-8")
            self.assertEqual(command("validate_markdown_links.py", ".", cwd=root).returncode, 0)
            markdown.write_text("[broken](missing.md)\n", encoding="utf-8")
            self.assertNotEqual(command("validate_markdown_links.py", ".", cwd=root).returncode, 0)
            markdown.write_text("[valid](docs/huawei/ma5800-x7/cli/test.md)\n", encoding="utf-8")
            self.assertEqual(command("validate_markdown_links.py", ".", cwd=root).returncode, 0)


if __name__ == "__main__":
    unittest.main()
