# Demanda — Harden Harness Merge Gate

**Prioridade sugerida:** P0

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Problema identificado

O merge gate atual autoriza merge quando encontra qualquer comentário social literal `approve` do Checker e CI verde, mas não vincula explicitamente a aprovação ao HEAD atual da PR.

Isso pode permitir aprovação obsoleta após novo commit.

Também deve ser analisado o comportamento para:

- PR Draft;
- `approve` seguido de `request-changes`;
- `approve` seguido de `blocked`;
- mudança de HEAD;
- CI nova após HEAD novo;
- comentário de Checker incorreto;
- PR fechada;
- merge conflict;
- múltiplos vereditos.

## Impacto

Falha de governança. Pode permitir merge de código diferente do que foi revisado.

## O Checker deve analisar

- `scripts/harness-merge-gate.py`
- `scripts/test-harness-gates.sh`
- fixtures em `tests/harness/`
- política em `.harness/policies/`
- documentação em `HARNESS.md`
- semântica do comentário social `approve`

## Resultado esperado da análise

Definir um Goal que faça o gate exigir:

- PR aberta;
- PR não Draft;
- HEAD atual conhecido;
- CI verde para o HEAD atual;
- `approve` do Checker válido para o HEAD atual;
- ausência de veredito posterior que invalide a aprovação;
- re-review obrigatória após novo SHA.

## Critérios que o futuro Goal deve testar

- approve válido no mesmo SHA;
- approve obsoleto após novo SHA;
- request-changes posterior;
- blocked posterior;
- PR Draft;
- CI falha;
- CI ausente;
- Checker incorreto;
- comentário `LGTM`;
- comentário `approved`;
- comentário `approve` com texto adicional;
- PR fechada.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
