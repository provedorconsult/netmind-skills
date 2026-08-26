"""Contract checks for G18 PPPoE credential operational knowledge."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PPPoECredentialOperationalKnowledgeTests(unittest.TestCase):
    def test_multi_vendor_guardrail_requires_authorized_source_and_sanitization(self):
        guardrails = (ROOT / "ACCESS-GUARDRAILS.md").read_text(encoding="utf-8")
        for phrase in (
            "A senha PPPoE é uma **credencial operacional**",
            "Source of Truth autorizado do\nprojeto consumidor",
            "não deduzi-la",
            "gerar uma nova",
            "não concede `WRITE`, `PERSIST` ou\n`HIGH-IMPACT`",
            "PPPoE password: PRESENT / AVAILABLE_FROM_SOT",
            "senha real nunca entra em evidência",
        ):
            self.assertIn(phrase, guardrails)

    def test_pppoe_procedures_handle_missing_and_available_credential(self):
        procedures = (
            ROOT / "skills/13-ma5800-pppoe-access/SKILL.md",
            ROOT / "skills/cisco-asr1001x/24-pppoe-troubleshooting/SKILL.md",
        )
        for procedure in procedures:
            content = procedure.read_text(encoding="utf-8")
            self.assertIn("## Credencial PPPoE no diagnóstico", content)
            self.assertIn("`UNKNOWN`", content)
            self.assertIn("`CONFIRMADO`", content)
            self.assertIn("armazena", content)


if __name__ == "__main__":
    unittest.main()
