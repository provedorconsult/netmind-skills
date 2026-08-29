"""Independent mutation checks for G18 PPPoE credential operational knowledge."""

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_operational_safety import (  # noqa: E402
    PPPOE_CREDENTIAL_CONTRACT,
    validate_pppoe_credential_contract,
)


EXPECTED_RULES = {
    "ACCESS-GUARDRAILS.md": {
        "authorized-source": "Source of Truth autorizado",
        "no-unauthorized-source": "fontes não autorizadas",
        "no-historical-credential": "conhecimento histórico como credencial atual",
        "no-inference": "não deduzi-la",
        "no-generation": "gerar uma nova",
        "no-repository-storage": "repositório não armazena senhas PPPoE",
        "no-secret-in-evidence": "senha real nunca entra em evidência",
        "no-secret-in-fixtures": "fixtures",
        "no-secret-in-examples": "exemplos",
        "no-secret-in-skills": "Skills",
        "no-secret-in-git": "Git",
        "no-secret-in-prs": "PRs",
        "no-secret-in-comments": "comentários",
        "no-secret-in-logs": "logs",
        "sanitized-marker": "PPPoE password: PRESENT / AVAILABLE_FROM_SOT",
        "availability-does-not-reveal-value": "O valor da senha não é evidência sanitizada",
        "no-authority-write": "`WRITE`",
        "no-authority-persist": "`PERSIST`",
        "no-authority-high-impact": "`HIGH-IMPACT`",
    },
    "skills/13-ma5800-pppoe-access/SKILL.md": {
        "authorized-source": "exclusivamente do Source of Truth autorizado",
        "no-alternative-retrieval": "consultar somente a fonte autorizada",
        "no-storage": "não armazena",
        "no-inference": "inferir a senha",
        "no-generation": "nem gerar uma\nnova",
        "no-alternative-recovery": "ou recupera a senha",
        "unknown-for-missing-source": "registrar `UNKNOWN`",
        "unknown-means-not-supplied": "não foi fornecida pelo Source of Truth",
        "confirmed-is-availability-only": "`CONFIRMADO` apenas para a disponibilidade",
        "confirmed-does-not-reveal-value": "sem incluí-la na evidência sanitizada",
        "no-authority-olt": "alteração na OLT",
        "no-authority-aaa": "OLT, AAA",
        "no-authority-bng": "AAA, BNG",
        "no-authority-bras": "BNG ou BRAS",
    },
    "skills/cisco-asr1001x/24-pppoe-troubleshooting/SKILL.md": {
        "authorized-source": "exclusivamente pelo Source of Truth autorizado",
        "no-storage": "não a armazena",
        "no-inference": "não inferir",
        "no-generation": "nem gerar credencial",
        "no-alternative-recovery": "nem recupera",
        "unknown-for-missing-source": "limitação como `UNKNOWN`",
        "confirmed-is-availability-only": "apenas a disponibilidade como `CONFIRMADO`",
        "confirmed-does-not-reveal-value": "nunca registrá-la em\nevidência sanitizada",
        "no-authority-write": "`WRITE`",
        "no-authority-persist": "`PERSIST`",
        "no-authority-high-impact": "`HIGH-IMPACT`",
        "no-authority-aaa": "em AAA",
        "no-authority-bng": "AAA, BNG",
        "no-authority-bras": "BNG, BRAS",
    },
}


class PPPoECredentialOperationalKnowledgeTests(unittest.TestCase):
    @staticmethod
    def documents():
        return {
            relative: (ROOT / relative).read_text(encoding="utf-8")
            for relative in EXPECTED_RULES
        }

    def test_validator_declares_each_independent_rule(self):
        for relative, expected_rules in EXPECTED_RULES.items():
            with self.subTest(document=relative):
                self.assertEqual(
                    PPPOE_CREDENTIAL_CONTRACT[relative]["rules"],
                    expected_rules,
                )

    def test_declared_documents_satisfy_every_atomic_contract_rule(self):
        self.assertEqual(validate_pppoe_credential_contract(self.documents()), [])

    def test_removing_each_atomic_rule_is_detected_independently(self):
        documents = self.documents()
        for relative, expected_rules in EXPECTED_RULES.items():
            for rule, required_fragment in expected_rules.items():
                with self.subTest(document=relative, rule=rule):
                    mutated = dict(documents)
                    mutated[relative] = documents[relative].replace(required_fragment, "", 1)
                    failures = validate_pppoe_credential_contract(mutated)
                    self.assertIn(
                        f"{relative}: missing PPPoE credential rule [{rule}]",
                        failures,
                    )

    def test_sanitized_marker_never_contains_a_synthetic_secret(self):
        synthetic_secret = "SYNTHETIC_PPPoE_SECRET_NOT_FOR_USE"
        marker = "PPPoE password: PRESENT / AVAILABLE_FROM_SOT"
        self.assertEqual(
            marker,
            EXPECTED_RULES["ACCESS-GUARDRAILS.md"]["sanitized-marker"],
        )
        self.assertNotIn(synthetic_secret, marker)


if __name__ == "__main__":
    unittest.main()
