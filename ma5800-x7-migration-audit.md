# Auditoria da migração G04 — Huawei MA5800-X7

## Escopo e decisão de amostra

Esta migração preserva todos os documentos legados na raiz do repositório e
migra uma amostra controlada para `docs/huawei/ma5800-x7/`. A seleção cobre as
cinco categorias canônicas para testar a arquitetura AI-Native sem antecipar
a migração integral de fabricantes ou Goals posteriores.

## Rastreabilidade

| Documento legado | Módulo resultante | Decisão |
|---|---|---|
| `MA5800-CLI-COMMANDS.md`, `COMMAND-MATRIX.md` | `docs/huawei/ma5800-x7/cli/ont-and-profile-discovery.md` | Preservar consultas confirmadas, discovery e forma rejeitada. |
| `MA5800-CLI-COMMANDS.md`, `COMMAND-MATRIX.md`, `ACCESS-GUARDRAILS.md` | `docs/huawei/ma5800-x7/config/dba-and-uplink-vlan.md` | Reorganizar evidência de DBA/VLAN com guardrails. |
| `TROUBLESHOOTING-CHECKLIST.md` | `docs/huawei/ma5800-x7/diag/gem-mapping-service-failure.md` | Isolar a assinatura de GEM mapping ausente. |
| `COMMAND-MATRIX.md`, `MA5800-CLI-COMMANDS.md` | `docs/huawei/ma5800-x7/mon/service-port-counters.md` | Isolar leitura de estado, contadores e VLANs. |
| `ROLLBACK-CHECKLIST.md` | `docs/huawei/ma5800-x7/update/rollback-prechecks.md` | Reorganizar prechecks, abort e pós-validação. |

## Conteúdo preservado e não migrado nesta fatia

Os legados `MA5800-DECISION-TREE.md`, `MA5800-ERROR-DATABASE.md`,
`ONT-PROVISIONING-CHECKLIST.md`, `EXAMPLES.md` e o restante dos catálogos
permanecem intactos para migração posterior. Nenhum conteúdo foi classificado
como descartável, e nenhuma sintaxe, equipamento, versão ou resultado novo foi
inventado.

## Limitações conhecidas

- A amostra não é migração integral do acervo Huawei.
- Valores como IDs, portas, VLANs e o service-port `1000` continuam sendo
  evidência do baseline legado, não parâmetros universais.
- O conteúdo de WAN PPPoE roteada não traz sintaxe confirmada nesta base; ela
  deve ser descoberta com `?` na release e no alvo autorizados.
- `categoria: index` aparece exclusivamente nos índices gerados; não é uma
  categoria operacional de Skill.
