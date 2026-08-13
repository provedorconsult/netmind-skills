---
name: 28-ma5800-access
description: Orientar acesso SSH à Huawei MA5800-X7 privada através do Cisco ASR1001-X sem expor credenciais ou tentar acesso direto pela Internet.
---

# Acesso downstream à MA5800

## Objetivo

Usar o ASR como salto autorizado até `${DOWNSTREAM_HOST}`.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [CONFIRMADO] na sessão de origem: `ssh -l ${DOWNSTREAM_USERNAME} ${DOWNSTREAM_HOST}`. Validar no alvo.

## Discovery e classificação

O comando acima foi informado pelo operador como utilizado. Para variações, toda nova linha é `[INFERIDO]` até ser aceita na CLI. Executar ajuda contextual no modo correto, registrar a saída como `[DISCOVERY]` e preservar rejeições como `[ERRO]`.

## Procedimento

[CONFIRMADO] O comando foi informado como utilizado. Acessar primeiro o ASR pelo método autorizado; a partir dele, executar SSH para a OLT privada; carregar as Skills Huawei; manter prompts e sintaxes separados.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Usuário é dado operacional; senha/chave nunca deve ser registrada. Saltos podem confundir equipamento/prompt.

## Rollback

Somente acesso. Não alterar rota/ACL de gestão para contornar falha.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.
