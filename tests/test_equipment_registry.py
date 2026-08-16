import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import validate_equipment_registry as validator


VALID = """format: netmind-equipment-registry
format_version: \"1.0\"
records:
  - id: equipment:vendor:family:model
    manufacturer: {id: manufacturer:vendor, value: Vendor}
    family: {id: family:vendor:family, value: Family}
    model: {id: model:vendor:family:model, value: Model}
    software_cli: {id: null, value: null}
    version: {id: null, value: null}
    firmware_patch: {id: null, value: null}
    evidence:
      - classification: CONFIRMADO
        reference: README.md#title
        statement: Evidence.
"""


class EquipmentRegistryTests(unittest.TestCase):
    def validate(self, content):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "registry.yaml"
            path.write_text(content, encoding="utf-8")
            original_root = validator.ROOT
            validator.ROOT = Path(temporary)
            (validator.ROOT / "README.md").write_text("# title\n", encoding="utf-8")
            try:
                return validator.validate(path)
            finally:
                validator.ROOT = original_root

    def test_valid_registry_passes(self):
        self.assertEqual(self.validate(VALID), [])

    def test_unknown_identity_must_use_null_pair(self):
        errors = self.validate(VALID.replace("software_cli: {id: null, value: null}", "software_cli: {id: software:vendor:os, value: null}"))
        self.assertTrue(any("both be known or both be null" in error for error in errors))

    def test_unknown_family_requires_unknown_derived_id_segment(self):
        unknown_family = VALID.replace(
            "family: {id: family:vendor:family, value: Family}",
            "family: {id: null, value: null}",
        ).replace("model:vendor:family:model", "model:vendor:unknown:model").replace(
            "equipment:vendor:family:model", "equipment:vendor:unknown:model"
        )
        self.assertEqual(self.validate(unknown_family), [])
        invalid = unknown_family.replace("model:vendor:unknown:model", "model:vendor:family:model")
        self.assertTrue(any("unknown family" in error for error in self.validate(invalid)))

    def test_evidence_reference_must_be_local_and_anchored(self):
        errors = self.validate(VALID.replace("README.md#title", "missing.md"))
        self.assertTrue(any("Markdown anchor" in error for error in errors))
