# Auditoria da migração G05 — MikroTik e Cisco

## Resultado do inventário MikroTik

Não há conteúdo técnico MikroTik/RouterOS no repositório no início de G05:
somente referências de planejamento em `05-content-migration-mikrotik-cisco.md`,
`README-TASKS.md` e `foundation-audit.md`. Portanto não foram criados diretório,
modelo, versão, comando ou módulo MikroTik. A ausência é intencional para não
inventar evidência; uma migração MikroTik futura requer fonte técnica primária.

## Mapa de origem → destino — Cisco

| Origem | Destino | Status | Observação |
|---|---|---|---|
| `02-cli-discovery/SKILL.md` | `cli/contextual-cli-discovery.md` | migrated | Descoberta, `[INFERIDO]`, `[DISCOVERY]` e `[ERRO]`. |
| `10-vlan-subinterfaces/SKILL.md` | `config/vlan-subinterface-prechecks.md` | migrated | Prechecks e comandos sem versão inventada. |
| `24-pppoe-troubleshooting/SKILL.md` | `diag/pppoe-session-up-no-navigation.md` | migrated | Evidência IOS XE 17.09.03a e limites destrutivos. |
| `23-cpu-memory/SKILL.md` | `mon/cpu-memory-observation.md` | migrated | Consultas inferidas e versão N/A. |
| `30-safe-change/SKILL.md` | `update/change-persistence-gates.md` | migrated | Gates, persistência e rollback. |
| `01-baseline`, `03-interface-diagnostics`, `04-optical-diagnostics`, `05-ip-routing`, `06-static-routing`, `07-bgp`, `08-ospf`, `09-ipv6` (`SKILL.md`) | — | preserved-legacy | Inventariados; fora da amostra controlada. |
| `11-pppoe-bng`, `12-aaa-local`, `13-aaa-radius`, `14-nat-cgnat`, `15-acl`, `16-qos`, `17-policy-map`, `18-route-map-prefix-list` (`SKILL.md`) | — | preserved-legacy | Inventariados; fora da amostra controlada. |
| `19-loopback`, `20-management`, `21-ssh`, `22-boot-config-register`, `25-bgp-troubleshooting`, `26-nat-troubleshooting`, `27-service-policy-troubleshooting`, `28-ma5800-access` (`SKILL.md`) | — | preserved-legacy | Inventariados; fora da amostra controlada. |
| `29-isp-troubleshooting`, `31-production-checklist`, `32-pppoe-up-no-navigation` (`SKILL.md`) | — | preserved-legacy | Inventariados; fora da amostra controlada. |
| `CISCO-ASR1001X-COMMANDS.md` | — | preserved-legacy | Catálogo integral preservado para migração posterior. |
| `CISCO-ASR1001X-DECISION-TREE.md` | — | preserved-legacy | Árvore integral preservada para migração posterior. |
| `CISCO-ASR1001X-ERROR-DATABASE.md` | — | preserved-legacy | Banco de erros integral preservado para migração posterior. |
| `CISCO-ASR1001X-ROLLBACK.md` | — | preserved-legacy | Guia de rollback integral preservado para migração posterior. |
| `README.md` | — | preserved-legacy | Índice e contexto do pacote preservados. |

## Conteúdo preservado no legado

Todas as Skills Cisco e os catálogos `CISCO-ASR1001X-COMMANDS.md`,
`CISCO-ASR1001X-DECISION-TREE.md`, `CISCO-ASR1001X-ERROR-DATABASE.md` e
`CISCO-ASR1001X-ROLLBACK.md` permanecem intactos. A amostra não é migração
integral e não altera Huawei, harness ou G06.
