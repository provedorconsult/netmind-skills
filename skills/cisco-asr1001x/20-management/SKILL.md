---
name: 20-management
description: Planejar hostname, domínio, NTP, logging, SNMP, ACL/VRF de gestão e source-interface no Cisco ASR1001-X.
---

# Gerenciamento

## Objetivo

Manter observabilidade e acesso seguro.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `hostname <NAME>`
- [INFERIDO] `ip domain name <DOMAIN>`
- [INFERIDO] `logging ?`
- [INFERIDO] `ntp ?`
- [INFERIDO] `snmp-server ?`
- [INFERIDO] `show clock`
- [INFERIDO] `show logging`
- [INFERIDO] `show running-config | section snmp`
- [INFERIDO] `show running-config | include source-interface`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Inventariar VRF/rota/ACL e fontes; sanitizar community/key; preservar acesso; testar NTP/syslog/SNMP no destino autorizado.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Alterar VRF, ACL, rota ou source-interface pode isolar o equipamento.

## Rollback

Garantir console/out-of-band; restaurar objeto individual.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

