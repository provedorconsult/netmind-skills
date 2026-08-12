---
name: 18-route-map-prefix-list
description: Planejar e auditar ip/ipv6 prefix-list e route-map para BGP, redistribuição, PBR ou NAT no ASR1001-X.
---

# Route-map e prefix-list

## Objetivo

Controlar prefixos e atributos sem substituir policies existentes.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show route-map`
- [INFERIDO] `show ip prefix-list`
- [INFERIDO] `show ipv6 prefix-list`
- [INFERIDO] `ip prefix-list <NAME> ?`
- [INFERIDO] `ipv6 prefix-list <NAME> ?`
- [INFERIDO] `route-map <NAME> permit <SEQUENCE>`
- [INFERIDO] `match ?`
- [INFERIDO] `set ?`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Inventariar sequência, match, set, callers, neighbor/direção e prefixos afetados; observar implicit deny; salvar configuração antes da proposta.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Uma sequência pode retirar rotas ou redirecionar tráfego em massa.

## Rollback

Restaurar sequências e bindings exatos; não sobrescrever a policy inteira.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

