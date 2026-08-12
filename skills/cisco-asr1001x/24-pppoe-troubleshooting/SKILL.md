---
name: 24-pppoe-troubleshooting
description: Isolar a primeira fase de falha PPPoE desde a ONT até Internet no ASR1001-X BNG.
---

# Troubleshooting PPPoE

## Objetivo

Localizar exatamente onde uma sessão para.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show pppoe session`
- [INFERIDO] `show pppoe session summary`
- [INFERIDO] `show users`
- [INFERIDO] `show aaa sessions`
- [INFERIDO] `show interfaces virtual-access`
- [INFERIDO] `show policy-map interface`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Seguir ONT → VLAN → uplink → ASR interface → PADI → PADO → PADR → PADS → LCP → Authentication → AAA/RADIUS → IP assignment → service-policy → Internet; parar na primeira falha.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Clear de sessão ou mudança de template afeta cliente(s); não executar automaticamente.

## Rollback

Diagnóstico não altera. Correção deve ter rollback por camada.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

