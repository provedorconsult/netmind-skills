---
name: 30-safe-change
description: Planejar e controlar mudanças no Cisco ASR1001-X com baseline, autorização, validação e rollback.
---

# Mudança segura

## Objetivo

Impedir alterações improvisadas em produção.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show version`
- [INFERIDO] `show processes cpu`
- [INFERIDO] `show processes memory`
- [INFERIDO] `show running-config`
- [INFERIDO] `show interfaces`
- [INFERIDO] `show ip route`
- [INFERIDO] `show bgp summary`
- [INFERIDO] `show pppoe session`
- [INFERIDO] `configure terminal`
- [INFERIDO] `end`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Identificar equipamento/release/uptime/CPU/memória; salvar estado sanitizado; apresentar comando, objetivo, impacto, dependências, resultado, validação e rollback; confirmar; alterar uma camada; validar e documentar.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

`copy running-config startup-config` muda estado persistente e exige autorização; snapshot pode conter segredos.

## Rollback

Escrever antes da mudança e usar comandos específicos; nunca usar reload como rollback normal.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

