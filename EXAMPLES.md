# Exemplos de uso pelo Codex

## Descobrir sintaxe

> Use $02-ma5800-cli-discovery para descobrir como continuar `ont add` nesta R018 sem alterar a OLT.

Resposta esperada: começar por `ont add ?`, avançar um token por vez, preservar retornos e não apresentar a sequência como confirmada até uma execução bem-sucedida.

## Diagnosticar ONT add

> Use $07-ma5800-ont-provisioning e $15-ma5800-error-database para analisar `Failure: The maximum bandwidth of the referenced DBA profile exceeds the limitation`.

Resposta esperada: consultar DBA, line profile, T-CONT, GEM e capacidade/ont-type; não reduzir Max automaticamente.

## Validar serviço

> Use $ma5800-decision-tree para uma ONT online cujo PPPoE não autentica.

Resposta esperada: confirmar profiles, GEM, service-port up, VLAN na PON/uplink, chegada ao BNG e só então AAA.

## Preparar cleanup

> Use $18-ma5800-cleanup para avaliar a exclusão do DBA 200.

Resposta esperada: exibir profile e bind-times, localizar T-CONT/line profile, mostrar impacto e rollback e solicitar confirmação explícita; nunca executar por conta própria.

## Planejar nova OLT

> Use $01-ma5800-baseline para comparar outra MA5800-X7.

Resposta esperada: validar release/patch/hardware; tratar todos os comandos não confirmados naquela unidade por discovery com `?`.

## Migrar a ONT de bancada de bridge para route

> Use $20-ma5800-ont-wan-pppoe para preparar uma WAN PPPoE roteada na EG8145X6-10.

Resposta esperada: reconhecer bridge como baseline, descobrir a sintaxe R018 sem inventar comandos, planejar profile/OMCI, VLAN 100, PPPoE, NAT/DHCP e bindings LAN/Wi-Fi, solicitar a credencial de teste somente no momento seguro da execução e preparar rollback para bridge.
