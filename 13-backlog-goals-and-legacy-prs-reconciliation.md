# G13 — Reconciliação de Backlog, Goals e PRs Legadas

## Predecessor

`G12`

## Objetivo

Reconciliar o estado histórico do projeto com a arquitetura aprovada em G11 e
G12.

## Escopo

Auditar Goals G01–G10, G11, G12, PRs #2, #7 e #18, arquivos de backlog,
`.harness/sprints/current.json`, `.harness/state/current.json`,
`.harness/state/working-memory.md` e documentação que ainda trate G08/G09/G10
como fluxo vigente.

Classificar formalmente cada item como `DONE`, `MERGED`, `SUPERSEDED`,
`REPLACED`, `DEFERRED`, `BLOCKED` ou `ACTIVE`.

- PR #7: confirmar que o conteúdo arquitetural relevante já está em
  `ARCHITECTURE.md`; se estiver, registrar `SUPERSEDED BY G11` e fechar a PR.
- PR #18 / G08: não fazer merge; decidir o que pode ser reaproveitado em G14,
  registrar a decisão e só então fechar a PR como superseded.
- PR #2: comparar arquivo a arquivo contra `main` antes de classificar ou
  fechar; identificar conteúdo incorporado, perdido, necessário ou obsoleto.

## Fora de escopo

- Implementar G14 ou qualquer Goal posterior.
- Alterar Skills, registries ou documentação funcional.
- Fazer merge de PR legada sem a auditoria prevista.

## Critérios de aceite

- Há uma única sequência de Goals vigente e nenhuma referência declara G01
  como Goal ativo ou planejado.
- O histórico e o estado de Goals/PRs são auditáveis a partir do repositório.
- A classificação de cada item auditado tem evidência rastreável.

## Condição de conclusão

O Maker abre uma PR exclusiva de G13, solicita o Checker e não faz merge. A
integração depende exclusivamente de um comentário social literal `approve`.
