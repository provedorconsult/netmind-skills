---
name: 03-interface-diagnostics
description: Diagnosticar estado, erros, drops, flaps, MTU, velocidade, duplex e transceiver das interfaces do Cisco ASR1001-X.
---

# Diagnóstico de interfaces

## Objetivo

Isolar falha física ou lógica sem presumir comandos de switch.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show interfaces`
- [INFERIDO] `show interfaces status`
- [INFERIDO] `show interfaces description`
- [INFERIDO] `show interfaces counters errors`
- [INFERIDO] `show interfaces counters`
- [INFERIDO] `show interfaces transceiver`
- [INFERIDO] `show interfaces transceiver detail`
- [INFERIDO] `show interfaces <INTERFACE>`
- [INFERIDO] `show interfaces status err-disabled`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Confirmar interface e tipo; comparar admin/line protocol; correlacionar CRC, input/output errors, drops, resets e flaps; verificar MTU/speed/duplex/SFP. Se uma forma for rejeitada, usar `show interfaces ?`.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Contadores cumulativos sem janela temporal causam falso diagnóstico.

## Rollback

Não aplicável. Não executar clear counters sem autorização.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

