---
name: 10-vlan-subinterfaces
description: Configurar e diagnosticar subinterfaces 802.1Q, L3, bridge-domain e BDI no Cisco ASR1001-X sem tratá-lo como switch.
---

# VLANs e subinterfaces

## Objetivo

Entregar VLANs de acesso ou uplink na interface lógica correta.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `interface TenGigabitEthernet<PATH>`
- [INFERIDO] `interface TenGigabitEthernet<PATH>.<SUBINTERFACE>`
- [INFERIDO] `encapsulation dot1Q <VLAN_ID>`
- [INFERIDO] `ip address <IP> <MASK>`
- [INFERIDO] `ipv6 address <PREFIX>`
- [INFERIDO] `description <TEXT>`
- [INFERIDO] `show running-config interface <INTERFACE>`
- [INFERIDO] `show vlans`
- [INFERIDO] `show interfaces trunk`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Confirmar nome real com `interface ?`; distinguir L2, L3, subinterface, bridge-domain e BDI; validar tag, parent interface, MTU, IP e sobreposição.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Encapsulation/IP errados derrubam gestão, PPPoE ou upstream.

## Rollback

Capturar interface completa; restaurar encapsulation/endereço/description e estado administrativo.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

