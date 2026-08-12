---
name: 17-policy-map
description: Interpretar policies, classes, police, shape, bandwidth, priority e aplicação em interfaces ou PPPoE no ASR1001-X.
---

# Policy-map e service-policy

## Objetivo

Detectar policy ausente, errada ou na direção incorreta.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show policy-map`
- [INFERIDO] `show policy-map interface`
- [INFERIDO] `policy-map <NAME>`
- [INFERIDO] `class <NAME>`
- [INFERIDO] `police ?`
- [INFERIDO] `shape ?`
- [INFERIDO] `bandwidth ?`
- [INFERIDO] `priority ?`
- [INFERIDO] `service-policy input <NAME>`
- [INFERIDO] `service-policy output <NAME>`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Localizar policy e parent/child; confirmar direção; comparar offered/drop rate e matches; em PPPoE verificar herança em Virtual-Access/Template.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Editar policy compartilhada afeta todos os attachments.

## Rollback

Preferir nova policy; registrar attachments; restaurar versão e direção anteriores.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

