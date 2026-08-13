---
name: 29-isp-troubleshooting
description: Diagnosticar serviços ISP desde cliente e GPON até BNG, CGNAT, BGP e Internet, integrando ASR1001-X e MA5800-X7.
---

# Troubleshooting ISP ponta a ponta

## Objetivo

Encontrar a primeira camada falha antes de alterar configuração.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show interfaces`
- [INFERIDO] `show ip route`
- [INFERIDO] `show bgp summary`
- [INFERIDO] `show pppoe session`
- [INFERIDO] `show aaa sessions`
- [INFERIDO] `show ip nat statistics`
- [INFERIDO] `show policy-map interface`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Seguir Cliente → ONT → GPON → GEM → Service-Port → VLAN → Uplink → ASR → PPPoE → AAA → IP → NAT/CGNAT → BGP/Upstream → Internet; parar e trocar para a Skill do equipamento correto.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Mudança em camada posterior pode mascarar a causa e ampliar incidente.

## Rollback

Diagnóstico não altera; correções isoladas com rollback.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

