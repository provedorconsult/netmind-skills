# G13 — Reconciliação de backlog, Goals e PRs legadas

## Escopo e evidência

Esta auditoria usa `main` após G11 (PR #19) e G12 (PR #20), os metadados e
diffs das PRs #2, #7 e #18 no GitHub e os arquivos versionados nesta revisão.
Ela não implementa trabalho institucional futuro, registries adicionais, Skill
Router ou alterações de Skills.

## Sequência vigente

G13 é o único Goal ativo. G01–G10 são preservados como backlog histórico e não
podem ser promovidos automaticamente pela ordem antiga. A classificação abaixo
descreve seu resultado histórico ou a decisão de não execução; `BLOCKED` no
catálogo continua a impedir execução incidental de item legado.

| Goal | Classificação | Evidência / decisão |
|---|---|---|
| G01 | DONE / MERGED | PR #11, merge `5ef86c2`. |
| G02 | DONE / MERGED | PR #12, merge `d18512c`. |
| G03 | DONE / MERGED | PR #13, merge `44ba455`. |
| G04 | DONE / MERGED | PR #14, merge `e493128`. |
| G05 | DONE / MERGED | PR #15, merge `0108cda`. |
| G06 | DONE / MERGED | PR #16, merge `550ffed`. |
| G07 | DONE / MERGED | PR #17, merge `3a70f87`. |
| G08 | SUPERSEDED | PR #18 não é mesclável contra G11/G12; o material permanece como fonte histórica de futura revisão institucional. |
| G09 | SUPERSEDED | A navegação documental legada não valida o fluxo de registries aprovado em G11. |
| G10 | BLOCKED | Release gate legado depende da arquitetura pós-registry, registries necessários e revisão institucional. |
| G11 | DONE / MERGED | PR #19, merge `5ba9d39`; fixa a arquitetura canônica. |
| G12 | DONE / MERGED | PR #20, head aprovado `20634b6`, merge `ed3b157`; entrega Equipment Registry v1. |
| G13 | ACTIVE | Fonte canônica: `13-backlog-goals-and-legacy-prs-reconciliation.md`. |

## PRs legadas

### PR #2 — SUPERSEDED

PR #2, head `9447724`, foi comparada arquivo a arquivo com `main`.

| Resultado | Arquivos |
|---|---|
| Incorporados sem divergência | `AUDIT-SPECIFIC-DATA.md`, `MA5800-CLI-COMMANDS.md`, Skills MA5800 06/07/08/12, Skill Cisco 28 e manifesto da skill de backup. |
| Incorporados e evoluídos posteriormente | `README.md`, Skills MA5800 01/02, catálogo e README Cisco, `network-config-backup/SKILL.md` e `references/vendor-commands.md`. |

Não há arquivo exclusivo necessário apenas na PR. A parametrização, a auditoria
de dados e a skill de backup já estão em `main`; as divergências posteriores
endurecem acesso, evidência, discovery e coleta de backup. A PR é encerrada sem
merge como superseded por conteúdo já integrado/evoluído.

### PR #7 — SUPERSEDED BY G11

PR #7, head `493cd53`, propõe Device Fingerprint, registries, compatibilidade,
capabilities, discovery e roteamento. Essas decisões relevantes estão em
`ARCHITECTURE.md` e `architecture-reconciliation-audit.md` por G11. A árvore
física universal proposta não é adotada: G11 preserva `docs/` como projeção
navegável e usa registries explícitos. A PR é referência histórica, não fonte
canônica, e é encerrada como `SUPERSEDED BY G11`.

### PR #18 / G08 — SUPERSEDED, NÃO MESCLAR

PR #18, head `8f35e02`, foi auditada contra `main`. Seu README, template de
índice e teste de entrada divergem; `CONTRIBUTING.md` e o teste ainda não estão
em `main`. O conteúdo útil fica preservado no commit e na PR como material de
consulta para futura revisão institucional, com estes limites:

- a introdução AI-Native, comandos de validação e orientação de contribuição
  são candidatos a reaproveitamento;
- o título ainda define o projeto pelos equipamentos Huawei/Cisco e não atende
  a arquitetura G11/G12;
- o template de índice usa metadados/categorias incompatíveis com o builder;
- o teste codifica essa documentação anterior.

Não copiar nem mesclar esta PR. Ela é encerrada como superseded; qualquer
reaproveitamento deverá ser reavaliado contra a arquitetura canônica e ter Goal
próprio.

## Integridade do estado

As decisões acima são espelhadas no catálogo e no log do Harness. O GitHub é a
autoridade para PRs e merges; este relatório preserva as referências para que a
sequência histórica seja auditável no repositório.
