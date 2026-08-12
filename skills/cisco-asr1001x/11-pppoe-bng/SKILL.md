---
name: 11-pppoe-bng
description: Planejar e interpretar PPPoE BNG e IPoE quando suportado, com Virtual-Access, AAA, RADIUS, pools, QoS, IPv4 e IPv6 no ASR1001-X.
---

# PPPoE e BNG

## Objetivo

Terminar sessões PPPoE da ONT/CPE no BNG e avaliar IPoE/ISG somente quando aplicável à release e ao desenho.

## Pré-requisitos

Identificar o ASR1001-X e executar `show version` de forma sanitizada. Confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes de qualquer mudança.

## Comandos candidatos

- [INFERIDO] `show pppoe session`
- [INFERIDO] `show pppoe session summary`
- [INFERIDO] `show users`
- [INFERIDO] `show aaa sessions`
- [INFERIDO] `show users all`
- [INFERIDO] `show interfaces virtual-access`
- [INFERIDO] `show interfaces virtual-template`
- [INFERIDO] `show running-config interface Virtual-Template<NUMBER>`

## Discovery e classificação

Toda linha acima é `[INFERIDO]` até ser aceita na CLI, exceto quando explicitamente marcada `[CONFIRMADO]`. Antes de usar, executar ajuda contextual (`?`, `show ?`, `show <TOKEN> ?`) no modo correto e registrar a saída como `[DISCOVERY]`. Uma rejeição literal vira `[ERRO]`.

## Procedimento

Descobrir sintaxe na release; mapear VLAN/interface de acesso, bba-group/VPDN se presentes, Virtual-Template, autenticação, pool, RADIUS, accounting, NAT inside e service-policy; validar primeiro na ONT de bancada. Para IPoE, identificar mecanismo real de subscriber/ISG, DHCP e accounting por `show ?`; não adaptar comandos PPPoE.

## Resultado esperado

Evidência suficiente para concluir o estado ou apresentar uma mudança conservadora sem inventar sintaxe.

## Diagnóstico

Correlacionar configuração, estado operacional e contadores. Parar na primeira camada falha e registrar comando, modo, horário e retorno literal sanitizado.

## Dependências

Consultar a matriz global, a decision tree, o banco de erros e as Skills relacionadas antes de propor alteração.

## Riscos

Alterar template/AAA afeta sessões clonadas em massa.

## Rollback

Preservar template, grupos, AAA e pools; desfazer novo binding e encerrar apenas sessão de teste se autorizado.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Mascarar `password`, `secret`, `key`, `community`, RADIUS, BGP, PPP e chaves SSH. Todo comando mutável também recebe `[DESTRUTIVO]`.

## O que NÃO fazer

Não executar alteração sem confirmação explícita; não usar sintaxe de memória; não expor segredos; não usar reload/clear/reset como primeira ação; não salvar configuração antes da validação.

## Fonte

- Equipamento-alvo: Cisco ASR1001-X; versão real ainda não fornecida.
- Documentação oficial Cisco ASR1000/IOS XE listada no README do pacote.
- A CLI real prevalece. Marcar exemplos de outra release como `[VERSÃO DIFERENTE]`; nunca misturar IOS, IOS XE e IOS XR.
