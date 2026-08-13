---
name: 02-cli-discovery
description: Descobrir sintaxe e modos no Cisco ASR1001-X com ajuda contextual antes de usar qualquer comando não confirmado.
---

# Discovery da CLI IOS XE

## Objetivo

Transformar hipóteses documentais em sintaxe específica do equipamento.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `?`
- [INFERIDO] `show ?`
- [INFERIDO] `show interfaces ?`
- [INFERIDO] `show ip ?`
- [INFERIDO] `show ipv6 ?`
- [INFERIDO] `show bgp ?`
- [INFERIDO] `show pppoe ?`
- [INFERIDO] `show aaa ?`
- [INFERIDO] `show policy-map ?`
- [INFERIDO] `show service-policy ?`
- [INFERIDO] `show platform ?`
- [INFERIDO] `show controllers ?`
- [INFERIDO] `show license ?`
- [INFERIDO] `show bootvar ?`
- [INFERIDO] `configure terminal`
- [INFERIDO] `interface ?`
- [INFERIDO] `router ?`
- [INFERIDO] `ip ?`
- [INFERIDO] `ipv6 ?`
- [INFERIDO] `aaa ?`
- [INFERIDO] `policy-map ?`
- [INFERIDO] `class-map ?`
- [INFERIDO] `route-map ?`
- [INFERIDO] `ip access-list ?`
- [INFERIDO] `username ?`
- [INFERIDO] `line ?`
- [INFERIDO] `snmp-server ?`
- [INFERIDO] `logging ?`
- [INFERIDO] `service ?`
- [INFERIDO] `boot ?`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Identificar prompt/mode; inserir um token por vez; conservar a saída literal; classificar consulta executada como `[DISCOVERY]`; só classificar ação bem-sucedida como `[CONFIRMADO]`.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Ajuda contextual em modo de configuração pode revelar opções perigosas; não concluir linha mutável sem autorização.

## Rollback

Sair do modo sem alterar. Se um prefixo executar, parar e auditar o running-config.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

