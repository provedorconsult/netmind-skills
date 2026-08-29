"""Contract checks for G18 PPPoE credential operational knowledge."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PPPoECredentialOperationalKnowledgeTests(unittest.TestCase):
    def test_guardrails_protect_authorized_source_and_all_secret_surfaces(self):
        guardrails = (ROOT / "ACCESS-GUARDRAILS.md").read_text(encoding="utf-8")
        for phrase in (
            "A senha PPPoE é uma **credencial operacional**",
            "Source of Truth autorizado do\nprojeto consumidor",
            "não deduzi-la, procurá-la em fontes não autorizadas,\ngerar uma nova nem tratar conhecimento histórico como credencial atual",
            "O\nrepositório não armazena senhas PPPoE; a senha real nunca entra em evidência,\nfixtures, exemplos, Skills, Git, PRs, comentários ou logs.",
            "não concede `WRITE`, `PERSIST` ou\n`HIGH-IMPACT`",
            "PPPoE password: PRESENT / AVAILABLE_FROM_SOT",
            "O valor da senha não é evidência sanitizada. A presença pode ser reportada sem\nrevelar o segredo",
        ):
            self.assertIn(phrase, guardrails)

    def test_ma5800_procedure_preserves_states_and_authority_boundaries(self):
        content = (ROOT / "skills/13-ma5800-pppoe-access/SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "## Credencial PPPoE no diagnóstico",
            "deve vir exclusivamente do Source of Truth autorizado do sistema consumidor",
            "esta Skill não armazena, deduz, gera ou recupera a senha.",
            "registrar `UNKNOWN`: a senha PPPoE\natual não foi fornecida pelo Source of Truth.",
            "registrar `CONFIRMADO` apenas para a disponibilidade",
            "sem incluí-la na evidência sanitizada.",
            "não autoriza alteração na OLT, AAA, BNG ou BRAS",
        ):
            self.assertIn(phrase, content)

    def test_asr_procedure_preserves_states_and_authority_boundaries(self):
        content = (
            ROOT / "skills/cisco-asr1001x/24-pppoe-troubleshooting/SKILL.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "## Credencial PPPoE no diagnóstico",
            "fornecida exclusivamente pelo Source of Truth autorizado do sistema\nconsumidor",
            "esta Skill não a armazena, deduz, gera nem recupera.",
            "marcar a limitação como `UNKNOWN` e não inferir\nnem gerar credencial.",
            "tratar apenas a disponibilidade como `CONFIRMADO`",
            "nunca registrá-la em\nevidência sanitizada.",
            "não autoriza `WRITE`, `PERSIST` ou\n`HIGH-IMPACT`",
        ):
            self.assertIn(phrase, content)


if __name__ == "__main__":
    unittest.main()
