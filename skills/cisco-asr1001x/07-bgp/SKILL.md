---
name: 07-bgp
description: Interpretar e planejar BGP IPv4 e IPv6, vizinhos, políticas e atributos no Cisco ASR1001-X IOS XE.
---

# BGP para ISP

## Objetivo

Operar BGP com visibilidade prévia de prefixos, direção e impacto.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show bgp ?`
- [INFERIDO] `show ip bgp ?`
- [INFERIDO] `show bgp summary`
- [INFERIDO] `show ip bgp summary`
- [INFERIDO] `show bgp neighbors`
- [INFERIDO] `show ip bgp neighbors`
- [INFERIDO] `show bgp ipv4 unicast`
- [INFERIDO] `show bgp ipv6 unicast`
- [INFERIDO] `router bgp <ASN>`
- [INFERIDO] `address-family ipv4`
- [INFERIDO] `address-family ipv6`
- [INFERIDO] `neighbor <IP> remote-as <ASN>`
- [INFERIDO] `neighbor <IP> description <TEXT>`
- [INFERIDO] `neighbor <IP> update-source <INTERFACE>`
- [INFERIDO] `neighbor <IP> ebgp-multihop <TTL>`
- [INFERIDO] `neighbor <IP> password <BGP_PASSWORD>`
- [INFERIDO] `neighbor <IP> route-map <NAME> in`
- [INFERIDO] `neighbor <IP> prefix-list <NAME> out`
- [INFERIDO] `neighbor <IP> maximum-prefix <COUNT>`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Confirmar release/AFI/SAFI e neighbor; inventariar received/advertised prefixes; modelar community, local-pref, MED, AS-path e weight; mostrar direção IN/OUT e diff de política; validar sem reset destrutivo.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Policy ou maximum-prefix incorreto pode retirar tabela/Internet; password é segredo.

## Rollback

Capturar seção BGP e policies; reverter linhas específicas; nunca reiniciar todo BGP como primeira ação.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.

