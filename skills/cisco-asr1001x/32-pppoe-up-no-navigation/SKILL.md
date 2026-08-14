---
name: 32-pppoe-up-no-navigation
description: Diagnosticar assinante PPPoE que autentica e recebe IP, mas não navega, isolando a quebra entre BNG, políticas, NAT/CGNAT, upstream e cliente.
---

# PPPoE UP, IP recebido, sem navegação

## Objetivo

Determinar com evidência o primeiro ponto de falha quando a sessão PPPoE está UP e o assinante recebeu IPv4, mas não alcança a Internet.

## Pré-requisitos

Usar primeiro `network-device-access`. Confirmar equipamento, release IOS XE, privilégio, caminho de acesso autorizado e Source of Truth. Começar em READ-ONLY. Não assumir que PPPoE UP implica forwarding completo.

## Fluxo obrigatório

Seguir e marcar cada camada como `CONFIRMADA`, `FALHA` ou `NÃO CONFIRMADA`:

`cliente/ONT → OLT/VLAN → BNG/Virtual-Access → rota/FIB → ACL/policy → NAT/CGNAT → upstream → retorno → DNS/HTTP/HTTPS`.

Parar na primeira falha objetiva.

## Comandos candidatos

- [CONFIRMADO em IOS XE 17.09.03a] `show pppoe session all`
- [CONFIRMADO em IOS XE 17.09.03a] `show ip route <SUBSCRIBER_IP>`
- [CONFIRMADO em IOS XE 17.09.03a] `show ip nat statistics`
- [CONFIRMADO em IOS XE 17.09.03a] `show ip nat translations`
- [INFERIDO] `show interfaces <VIRTUAL_ACCESS>`
- [INFERIDO] `show policy-map interface <VIRTUAL_ACCESS>`
- [INFERIDO] `show access-lists <ACL>`
- [INFERIDO] `show ip cef <SUBSCRIBER_IP>`
- [INFERIDO] `show ip route 0.0.0.0 0.0.0.0`

Comandos marcados `[CONFIRMADO]` continuam dependentes do contexto de modo e release; a CLI real prevalece.

## Correlação temporal obrigatória

Não concluir apenas por configuração estática. Fazer amostragem antes/depois enquanto o assinante gera tráfego:

1. registrar counters PPPoE/Virtual-Access e NAT;
2. gerar ping/HTTPS no cliente, quando houver acesso;
3. aguardar intervalo curto e conhecido;
4. coletar novamente;
5. comparar deltas.

Interpretação mínima:

- RX PPPoE cresce e NAT não cria tradução → investigar classificação/binding/pool CGNAT;
- tradução nasce e TX PPPoE cresce → retorno chegou ao BNG; validar cliente/DNS/HTTP;
- RX PPPoE não cresce → voltar para OLT/VLAN/forwarding;
- NAT mostra drops/falha de pool/porta → tratar capacidade/classificação antes de upstream.

## NAT/CGNAT

Se o assinante usa RFC6598 ou RFC1918, provar explicitamente se existe tradução dinâmica. Não confundir PATs estáticos de gerenciamento com NAT dinâmico de assinantes. Confirmar `inside`, `outside`, ACL exclusiva, pool público autorizado, rota de retorno e ausência de consumidor prévio do IP público.

Nunca inferir que um IP público observado em loopback ou PAT de gerenciamento está disponível para CGNAT.

## Testes do cliente

Quando disponível, validar por ordem:

1. gateway/BNG;
2. IPv4 público conhecido;
3. DNS explícito;
4. HTTP/HTTPS;
5. traceroute;
6. MTU/MSS/PMTUD.

Aprovação de dataplane no ASR não substitui confirmação de navegação do cliente; registrar claramente a limitação quando o terminal não estiver disponível.

## Critério de causa raiz

Só marcar `CONFIRMADA` quando houver correlação entre sessão, rota, counters e camada de falha. Evitar frases como “parece NAT” sem demonstrar que o tráfego chega ao BNG e não gera tradução/retorno.

## Mudança corretiva

Qualquer criação/alteração de ACL, pool, binding NAT, interface, rota ou policy é `[HIGH-IMPACT] [DESTRUTIVO]` e exige gate separado. Gerar Change Plan com:

- baseline sanitizado;
- bloco privado exato;
- bloco público autorizado;
- inside/outside;
- sintaxe validada por CLI;
- impacto e capacidade;
- preservação de NAT/PAT existente;
- validação pós-mudança;
- rollback específico.

## Persistência

`write memory`, `copy running-config startup-config` ou equivalente é uma mudança persistente separada. Só persistir após validar running-config e obter autorização explícita. Depois, comparar startup-config com as linhas aprovadas.

## Rollback

Remover apenas objetos criados pela mudança, na ordem inversa do binding → pool → ACL, depois de confirmar que não possuem outros consumidores. Nunca usar `clear ip nat translation *`, reload ou remoção global como rollback padrão.

## Segurança e documentação

Sanitizar credenciais, communities, chaves, usernames PPPoE e dados pessoais. Endereços, hostnames, topologia e valores reais do cliente pertencem ao Source of Truth, nunca a esta skill.

## Dependências

Usar em conjunto com:

- `11-pppoe-bng`;
- `14-nat-cgnat`;
- `24-pppoe-troubleshooting`;
- `26-nat-troubleshooting`;
- `30-safe-change`;
- `31-production-checklist`.

## Resultado esperado

Relatório capaz de responder: “PPPoE está UP e recebeu IP; em qual camada o pacote para, qual evidência prova isso, qual correção é necessária e qual gate ainda falta?”
