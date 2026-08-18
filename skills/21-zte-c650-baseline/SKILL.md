---
name: 21-zte-c650-baseline
description: Confirmar, em modo somente leitura, o fingerprint e o baseline GPON sanitizável da ZTE ZXA10 C650 observada na release V1.1.2.
---

# Baseline ZTE ZXA10 C650

## Objetivo

Confirmar modelo, software, hardware, GPON e transporte sem modificar a OLT.
Esta Skill cobre somente a CLI e release observadas; a equivalência C610/ZTE650
não prova compatibilidade para outro equipamento.

## Pré-requisitos

- Alvo, protocolo e credenciais confirmados pelo Source of Truth.
- Escopo vigente `READ` ou `DISCOVERY`.
- Host key e identidade da sessão validados antes das consultas.

## Comandos confirmados

- [CONFIRMADO] `show software` para `ZXA10 C650`, software `V1.1.2`.
- [CONFIRMADO] `show hostname`, `show card` e `show equipment` para baseline.
- [CONFIRMADO] `show interface brief` e `show vlan summary` para transporte.
- [CONFIRMADO] `show gpon profile tcont` e `show gpon onu profile vlan`.
- [CONFIRMADO] `show gpon onu state` para estado, com sanitização obrigatória.

## Descoberta segura

Use `show ?` e ajuda contextual antes de consultas parametrizadas. As referências
`gpon_olt-`, `gpon_onu-`, `vport-` e `xgei-` devem vir da CLI ou do Source of
Truth, nunca de suposição ou varredura.

## Regras de segurança

- Preserve respostas brutas fora do repositório e remova serial de ONU, LOID,
  dados de assinante, IP, segredo e descrição de circuito antes de publicar.
- `show version` foi rejeitado no contexto observado; use `show software`.
- Não executar `configure`, criação/remoção, `commit`, `write`, `save`, reload
  ou reset. A disponibilidade de uma credencial não autoriza escrita.

## Fonte

- Evidência primária sanitizada: [fingerprint de CLI](../../docs/zte/zxa10-c650/cli/fingerprint-and-cli-discovery.md).
- Evidência de monitoramento: [GPON e transporte](../../docs/zte/zxa10-c650/mon/gpon-transport-observation.md).
