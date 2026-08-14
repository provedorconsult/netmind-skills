---
name: 26-nat-troubleshooting
description: Rastrear falhas de NAT/PAT/CGNAT no ASR1001-X com correlação temporal de sessão, tradução, counters e retorno.
---

# Troubleshooting NAT e CGNAT

## Objetivo

Determinar por que um assinante não traduz, não sai ao upstream ou não recebe retorno.

## Pré-requisitos

Usar primeiro `network-device-access`. Confirmar ASR1001-X, release IOS XE, privilégio, Source of Truth e escopo READ-ONLY inicial.

## Comandos candidatos

- [CONFIRMADO em IOS XE 17.09.03a] `show ip nat translations`
- [CONFIRMADO em IOS XE 17.09.03a] `show ip nat statistics`
- [INFERIDO] `show ip nat pool`
- [INFERIDO] `show access-lists <ACL>`
- [CONFIRMADO em IOS XE 17.09.03a] `show ip route <SUBSCRIBER_IP>`
- [INFERIDO] `show ip cef <SUBSCRIBER_IP>`

## Procedimento

Seguir:

`cliente → PPPoE/IPoE → rota/FIB → classificação ACL → binding NAT → pool → tradução → outside/upstream → retorno`.

Para cada camada registrar evidência e parar na primeira falha objetiva.

## Correlação temporal obrigatória

Durante tráfego controlado do assinante:

1. coletar NAT statistics/translations e counters da sessão;
2. gerar tráfego por intervalo curto conhecido;
3. coletar novamente;
4. comparar deltas.

Interpretação:

- tráfego chega ao BNG, mas traduções permanecem zero → classificação/binding/pool ausente ou incorreto;
- traduções crescem, mas há `in-to-out` drops ou falha de pool/porta → capacidade/pool/classificação;
- traduções crescem e counters downstream aumentam → NAT/retorno até BNG está funcional; validar cliente/DNS/HTTP;
- apenas PATs estáticos existentes não comprovam NAT dinâmico de assinantes.

## Checklist de pool público

Antes de qualquer correção, provar:

- IPv4/bloco autorizado;
- rota de retorno;
- IP candidato sem consumidor prévio em config, NAT, ARP, rota específica ou protocolo de roteamento relevante;
- inside/outside corretos;
- ACL limitada ao prefixo pretendido;
- NAT/PAT existentes a preservar.

Não inferir disponibilidade de endereço em loopback ou PAT de gerenciamento.

## Resultado esperado

Responder objetivamente:

`pacote chega ao BNG? cria tradução? sai para upstream? há retorno?` — cada resposta deve ser `SIM`, `NÃO` ou `NÃO CONFIRMADO`, acompanhada da evidência.

## Riscos

Dados de tradução podem identificar assinantes; sanitizar antes de versionar. `clear`, mudança de modo CGN ou alteração ampla de ACL/pool são HIGH-IMPACT.

## Rollback

Nenhum clear automático. Correção deve remover somente binding/pool/ACL criados, em ordem inversa, após checar dependências.

## Persistência

Não executar `write memory`/save como parte implícita da correção. Persistência exige gate separado depois da validação do running-config.

## Regras de segurança

Seguir SHOW → ANALISAR → VALIDAR → PROPOR → CONFIRMAR → ALTERAR → VALIDAR → DOCUMENTAR. Dados reais de rede ficam no Source of Truth.

## O que NÃO fazer

Não limpar traduções globalmente, não reutilizar ACL ampla sem analisar outros prefixos, não reutilizar IPv4 público de gerenciamento por conveniência e não salvar antes da homologação.

## Dependências

Usar com `14-nat-cgnat`, `24-pppoe-troubleshooting`, `30-safe-change`, `31-production-checklist` e `32-pppoe-up-no-navigation`.

## Fonte

- Cisco ASR1001-X / IOS XE; CLI real prevalece.
- Evidência operacional validada em IOS XE 17.09.03a sem incorporar dados específicos de cliente.
