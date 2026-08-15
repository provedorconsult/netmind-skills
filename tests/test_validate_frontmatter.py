"""Deterministic coverage for the docs frontmatter validator."""

import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import validate_frontmatter as validator


VALID = """---
fabricante: huawei
modelo: [MA5800-X7]
categoria: diag
topicos: [gpon, ont]
descricao: Diagnóstico de ONT.
versao_firmware_testada: V100R018
ultima_atualizacao: "2026-08-15"
---

# Documento
"""


class ValidateFrontmatterTests(unittest.TestCase):
    def validate(self, content):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "docs" / "huawei" / "ma5800-x7"
            path.mkdir(parents=True)
            document = path / "documento.md"
            document.write_text(content, encoding="utf-8")
            return validator.validate_docs(Path(temporary) / "docs")

    def test_valid_frontmatter_passes(self):
        self.assertEqual(self.validate(VALID), [])

    def test_missing_frontmatter_fails(self):
        failures = self.validate("# Sem frontmatter\n")
        self.assertIn("missing YAML frontmatter", failures[0])

    def test_invalid_yaml_fails(self):
        failures = self.validate("---\nfabricante: [\n---\n")
        self.assertIn("invalid YAML frontmatter", failures[0])

    def test_missing_required_field_fails(self):
        failures = self.validate(VALID.replace("categoria: diag\n", ""))
        self.assertIn("missing required field 'categoria'", failures[0])

    def test_incompatible_structural_type_fails(self):
        failures = self.validate(VALID.replace("modelo: [MA5800-X7]", "modelo: MA5800-X7"))
        self.assertIn("field 'modelo' must be list", failures[0])


if __name__ == "__main__":
    unittest.main()
