# Auditoria da migração G05 — MikroTik e Cisco

## Resultado do inventário MikroTik

Não há conteúdo técnico MikroTik/RouterOS no repositório no início de G05:
somente referências de planejamento em `05-content-migration-mikrotik-cisco.md`,
`README-TASKS.md` e `foundation-audit.md`. Portanto não foram criados diretório,
modelo, versão, comando ou módulo MikroTik. A ausência é intencional para não
inventar evidência; uma migração MikroTik futura requer fonte técnica primária.

## Mapa de origem → destino — Cisco

| Origem | Destino | Tipo | Observação |
|---|---|---|---|
| `skills/cisco-asr1001x/02-cli-discovery/SKILL.md` | `docs/cisco/asr1001-x/cli/contextual-cli-discovery.md` | cli | Preserva descoberta, `[INFERIDO]`, `[DISCOVERY]`, `[ERRO]` e guardrails. |
| `skills/cisco-asr1001x/10-vlan-subinterfaces/SKILL.md` | `docs/cisco/asr1001-x/config/vlan-subinterface-prechecks.md` | config | Preserva prechecks e comandos sem versão inventada. |
| `skills/cisco-asr1001x/24-pppoe-troubleshooting/SKILL.md` | `docs/cisco/asr1001-x/diag/pppoe-session-up-no-navigation.md` | diag | Preserva evidência IOS XE 17.09.03a e limites destrutivos. |
| `skills/cisco-asr1001x/23-cpu-memory/SKILL.md` | `docs/cisco/asr1001-x/mon/cpu-memory-observation.md` | mon | Preserva consultas inferidas e ausência de versão real. |
| `skills/cisco-asr1001x/30-safe-change/SKILL.md` | `docs/cisco/asr1001-x/update/change-persistence-gates.md` | update | Preserva gates, persistência e rollback. |

## Conteúdo preservado no legado

Todas as Skills Cisco e os catálogos `CISCO-ASR1001X-COMMANDS.md`,
`CISCO-ASR1001X-DECISION-TREE.md`, `CISCO-ASR1001X-ERROR-DATABASE.md` e
`CISCO-ASR1001X-ROLLBACK.md` permanecem intactos. A amostra não é migração
integral e não altera Huawei, harness ou G06.
