---
name: 31-production-checklist
description: Validar o Cisco ASR1001-X após mudança e antes do aceite de produção em ambiente ISP.
---

# Checklist de produção

## Objetivo

Emitir aceite baseado em evidências e manter acesso.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show version`
- [INFERIDO] `show interfaces`
- [INFERIDO] `show ip route`
- [INFERIDO] `show bgp summary`
- [INFERIDO] `show pppoe session`
- [INFERIDO] `show aaa sessions`
- [INFERIDO] `show ip nat statistics`
- [INFERIDO] `show policy-map interface`
- [INFERIDO] `show processes cpu`
- [INFERIDO] `show processes memory`
- [INFERIDO] `show ip ssh`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Marcar IOS XE, configuração, interfaces/uplinks, rotas, BGP, PPPoE, AAA, NAT, QoS, CPU, memória, SSH e persistência autorizada; falha em item impede aceite.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Salvar configuração defeituosa dificulta rollback; não persistir antes da validação.

## Rollback

Acionar plano específico da mudança e repetir checklist.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

