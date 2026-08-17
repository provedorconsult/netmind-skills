# Demanda — Capability Registry v1

**Prioridade sugerida:** P1

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de auditoria/evolução. Não executar diretamente pelo Maker.

## Objetivo

Criar registry estruturado de capabilities observadas ou comprovadas.

## Exemplos de capabilities

- GPON
- EPON
- VLAN
- QinQ
- PPPoE
- IPoE
- RADIUS
- NAT
- CGNAT
- BGP
- OSPF
- IPv6
- QoS
- Multicast
- SNMP
- SSH
- Telnet
- OMCI
- ONT provisioning

## O Checker deve definir

- schema;
- namespaces/IDs;
- evidência;
- escopo por equipamento/versão;
- pré-condições;
- limitações;
- relação com Compatibility Registry;
- relação com Skill Router.

## Regra

Capability não significa autorização de execução.

## Saída esperada do Checker

O Checker deve devolver uma destas decisões:

- `ACCEPT` — transformar em Goal;
- `REWORK` — ajustar escopo antes de virar Goal;
- `MERGE_WITH` — combinar com outra demanda;
- `DEFER` — adiar;
- `REJECT` — não executar.

Se `ACCEPT`, o Checker deve criar o Goal formal e o prompt específico para o Maker.
