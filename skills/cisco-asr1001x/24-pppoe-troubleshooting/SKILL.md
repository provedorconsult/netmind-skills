---
name: 24-pppoe-troubleshooting
description: Isolar a primeira fase de falha PPPoE desde a ONT até Internet no ASR1001-X BNG, inclusive quando a sessão está UP e já recebeu IP.
---

# Troubleshooting PPPoE

## Objetivo

Localizar exatamente onde uma sessão PPPoE falha, sem tratar `UP` como sinônimo de navegação funcional.

## Pré-requisitos

Usar primeiro `network-device-access`. Identificar ASR1001-X, release IOS XE, privilégio, escopo e Source of Truth. Iniciar em READ-ONLY.

## Comandos candidatos

- [CONFIRMADO em IOS XE 17.09.03a] `show pppoe session all`
- [INFERIDO] `show pppoe session summary`
- [INFERIDO] `show users`
- [INFERIDO] `show aaa sessions`
- [INFERIDO] `show interfaces <VIRTUAL_ACCESS>`
- [INFERIDO] `show policy-map interface <VIRTUAL_ACCESS>`
- [CONFIRMADO em IOS XE 17.09.03a] `show ip route <SUBSCRIBER_IP>`
- [CONFIRMADO em IOS XE 17.09.03a] `show ip nat statistics`
- [CONFIRMADO em IOS XE 17.09.03a] `show ip nat translations`

## Procedimento

Seguir:

`ONT → VLAN/uplink → PADI → PADO → PADR → PADS → LCP → Authentication → AAA/RADIUS → IPCP/IP assignment → Virtual-Access → rota/FIB → service-policy/ACL → NAT/CGNAT → upstream → retorno → DNS/HTTP/HTTPS`.

Parar na primeira falha objetiva.

## Regra para PPPoE UP

Se sessão estiver UP e houver IP:

1. confirmar rota `/32` ou equivalente para o assinante;
2. observar counters RX/TX do Virtual-Access durante tráfego real;
3. se IP for RFC6598/RFC1918, provar tradução NAT/CGNAT dinâmica;
4. diferenciar NAT dinâmico de PATs estáticos de gerenciamento;
5. confirmar upstream e retorno;
6. quando houver terminal do cliente, validar DNS, HTTP/HTTPS e MTU/MSS.

RX crescendo sem tradução dinâmica é evidência para investigar classificação/binding/pool NAT, não motivo para alterar PPPoE.

## Correlação temporal

Capturar counters antes/depois de uma janela curta de teste. Relatar deltas e horário. Configuração estática, isoladamente, não comprova encaminhamento.

## Resultado esperado

Evidência suficiente para classificar cada camada como `CONFIRMADA`, `FALHA` ou `NÃO CONFIRMADA`, com causa raiz apenas quando suportada por sessão, rota e counters.

## Riscos

`clear pppoe`, reset de sessão ou mudança de Virtual-Template afetam clientes e não fazem parte do diagnóstico padrão.

## Rollback

Diagnóstico não altera. Correções seguem skill específica e `30-safe-change`.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Sanitizar usernames PPPoE, credenciais e dados pessoais. Dados reais de rede pertencem ao Source of Truth.

## O que NÃO fazer

Não derrubar sessão para “testar”, não assumir problema na OLT se os counters chegam ao BNG, não culpar DNS antes de testar IP e não persistir configuração antes da homologação.

## Dependências

Usar `14-nat-cgnat`, `26-nat-troubleshooting`, `29-isp-troubleshooting` e `32-pppoe-up-no-navigation` quando a sessão estiver UP sem navegação.

## Fonte

- Cisco ASR1001-X / IOS XE; a CLI real prevalece.
- Evidência operacional validada em IOS XE 17.09.03a sem dados específicos de cliente.
