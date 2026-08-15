# NetMind Skills — Codex Maker Tasks

Estas tarefas foram derivadas do `PRD-NetMind-Skills.md` fornecido para análise.

## Ordem recomendada

1. `01-foundation-audit-and-structure.md`
2. `02-frontmatter-schema-and-validator.md`
3. `03-build-indexes.md`
4. `04-content-migration-huawei.md`
5. `05-content-migration-mikrotik-cisco.md`
6. `06-deprecation-policy.md`
7. `07-ci-markdown-links.md`
8. `08-readme-contributing-and-templates.md`
9. `09-end-to-end-ai-validation.md`
10. `10-final-release-gate.md`

## Protocolo

Cada arquivo é um Goal independente para o Codex atuar como Maker. Antes de
iniciar a implementação de qualquer arquivo, o Maker deve criar o Goal
correspondente usando a ferramenta **Goal**; um Goal não substitui o fluxo de
Pull Request e não autoriza merge.

O Maker:
- implementa;
- testa;
- abre/atualiza PR;
- solicita Checker;
- aguarda.

O Checker:
- revisa a PR;
- publica o veredito por comentário social;
- `approve` = autorização para merge;
- qualquer outro veredito = sem merge.

Nenhuma tarefa pode ser integrada sem o comentário social literal `approve`
publicado pelo Checker na Pull Request daquela tarefa.

O Maker nunca deve interpretar CI verde como autorização de merge.

## Observação

As tarefas foram separadas para reduzir risco, facilitar revisão e permitir que cada PR seja auditada isoladamente. A migração de conteúdo foi deliberadamente dividida em amostras antes da expansão geral.
