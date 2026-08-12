---
name: 01-baseline
description: Coletar e sanitizar o baseline de hardware, IOS XE, configuração, rotas, interfaces, recursos, licenças, boot e redundância do Cisco ASR1001-X.
---

# Baseline do ASR1001-X

## Objetivo

Produzir fotografia somente leitura antes de diagnóstico ou mudança.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show version`
- [INFERIDO] `show running-config`
- [INFERIDO] `show startup-config`
- [INFERIDO] `show interfaces`
- [INFERIDO] `show ip interface brief`
- [INFERIDO] `show ipv6 interface brief`
- [INFERIDO] `show ip route`
- [INFERIDO] `show ipv6 route`
- [INFERIDO] `show arp`
- [INFERIDO] `show cdp neighbors`
- [INFERIDO] `show lldp neighbors`
- [INFERIDO] `show platform`
- [INFERIDO] `show processes cpu`
- [INFERIDO] `show processes memory`
- [INFERIDO] `show memory statistics`
- [INFERIDO] `show inventory`
- [INFERIDO] `show license summary`
- [INFERIDO] `show license`
- [INFERIDO] `show bootvar`
- [INFERIDO] `show rom-monitor`
- [INFERIDO] `show redundancy`
- [INFERIDO] `show redundancy states`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Executar `show version` primeiro; selecionar documentação da release; coletar demais leituras; sanitizar password, secret, key, community, RADIUS, BGP e PPP; registrar uptime e timestamp.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

`show running-config` e `show startup-config` podem expor segredos mesmo quando cifrados.

## Rollback

Não aplicável a leituras. Excluir imediatamente qualquer artefato não sanitizado.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

