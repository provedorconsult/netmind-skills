---
name: 08-ospf
description: Diagnosticar e planejar OSPFv2 e OSPFv3 no Cisco ASR1001-X sem misturar sintaxe de releases.
---

# OSPF e OSPFv3

## Objetivo

Validar adjacência, LSDB, áreas, custos e instalação de rotas.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show ip ospf`
- [INFERIDO] `show ip ospf neighbor`
- [INFERIDO] `show ip ospf interface`
- [INFERIDO] `show ip ospf database`
- [INFERIDO] `show ipv6 ospf`
- [INFERIDO] `show ipv6 ospf neighbor`
- [INFERIDO] `router ospf <PROCESS_ID>`
- [INFERIDO] `router ospfv3 <PROCESS_ID>`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Descobrir a sintaxe suportada; validar router-id, área, rede/tipo, timers, MTU e autenticação; comparar LSDB, RIB e CEF.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Mudança de área/timer/autenticação derruba adjacências.

## Rollback

Salvar configuração do processo e interfaces; reverter parâmetro exato.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

