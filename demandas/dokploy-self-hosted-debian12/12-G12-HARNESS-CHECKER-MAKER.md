# G12 — Harness / Checker / Maker

## Goal
Integrar os procedimentos Dokploy ao fluxo Git-native do NetMind Skills.

## Fluxo
`Goal → Maker/Codex → PR → CI → Checker → approve → merge`.

## Classes
`READ_ONLY`, `LOW_RISK`, `MEDIUM_RISK`, `HIGH_RISK`, `DESTRUCTIVE`.

## Acceptance Contract
- Maker executa somente o Goal ativo.
- PR é isolada.
- CI verde não autoriza merge.
- Somente comentário social literal `approve` do Checker autoriza integração.
- Ações destrutivas possuem gate explícito.

## Test Matrix
| ID | Teste | Esperado |
|---|---|---|
| T01 | Goal isolado | escopo preservado |
| T02 | CI | verde |
| T03 | Checker | veredito rastreável |
| T04 | ação destrutiva | bloqueada sem autorização |

## Promotion Criteria
Governança compatível com o Harness atual.
