---
name: 20-ma5800-ont-wan-pppoe
description: Planejar, descobrir e validar uma WAN roteada PPPoE na ONT Huawei EG8145X6-10 de bancada, provisionada por profile/OMCI na MA5800-X7 R018 sem inventar sintaxe nem persistir credenciais.
---

# WAN roteada PPPoE na ONT

## Objetivo

Migrar a ONT de bancada do baseline bridge para o objetivo de roteamento: a EG8145X6-10 atua como cliente PPPoE, recebe endereço do BNG e entrega LAN por NAT/DHCP/Wi-Fi conforme o plano.

## Quando usar

Usar ao planejar ou diagnosticar WAN Internet roteada na ONT, profiles de WAN, entrega OMCI, PPPoE, NAT, DHCP ou bindings LAN/Wi-Fi.

## Pré-requisitos

Confirmar MA5800V100R018/SPH507, firmware exato da EG8145X6-10, ONT de bancada, VLAN 100 até o ASR1001-X, credencial de teste temporária, autorização e rollback para bridge.

## Comandos confirmados

- [CONFIRMADO] Os displays de ONT, profiles, service-port e VLAN existentes neste pacote.
- Não há comando confirmado para criar WAN profile, WAN roteada, PPPoE, NAT ou DHCP na ONT.

## Comandos de descoberta

- [INFERIDO] Iniciar por `?` nos contextos CONFIG, GPON INTERFACE e profile relevantes; após execução, registrar literalmente cada consulta como [DISCOVERY].
- [INFERIDO] Descobrir primeiro comandos de consulta de WAN/profile e somente depois a sintaxe de criação.
- Não sugerir nomes como `ont wan-*`, `wan-profile` ou equivalentes até a própria CLI R018 apresentá-los.

## Sintaxe

Nenhuma sintaxe de WAN PPPoE foi confirmada. Descobrir: mecanismo de profile reutilizável, modo route, VLAN 100, PPPoE, autenticação suportada, NAT, DHCP LAN, bindings ETH/Wi-Fi, DNS/MTU e forma segura de informar segredo.

## Exemplos

Estado informado pelo operador: ONT de bancada autorizada em bridge. Objetivo ainda não confirmado na CLI: ONT roteada, WAN PPPoE na VLAN 100, ASR1001-X como servidor/BNG e AAA/RADIUS como autenticador.

## Resultado esperado

ONT inicia a sessão PPPoE, recebe IP no BNG, instala conectividade WAN e entrega endereçamento/conectividade aos clientes LAN/Wi-Fi, sem expor a credencial.

## Erros conhecidos

Nenhum erro literal de WAN PPPoE na ONT foi fornecido. Registrar PADI/PADO/PADR/PADS, LCP, autenticação e IPCP como fases distintas.

## Diagnóstico

Validar na ordem: WAN/profile aplicado → VLAN/GEM/service-port → PADI no BNG → PADO → PADR/PADS → LCP → PAP/CHAP → IPCP/IP → rota/DNS → NAT/DHCP/LAN/Wi-Fi. Parar na primeira falha.

## Dependências

Firmware da ONT, suporte OMCI/vendor-specific, profile compatível, VLAN 100, GEM 1, service-port 1000, uplink, BNG e AAA.

## Riscos

Trocar bridge por route pode interromper a bancada, duplicar NAT/DHCP, alterar bindings LAN/Wi-Fi e persistir segredo na configuração operacional da OLT/ONT.

## Rollback

Capturar o baseline bridge completo, profiles e bindings. Validar previamente a sintaxe de remoção da WAN roteada e restauração do bridge; não depender de reset de fábrica.

## Regras de segurança

Usar somente credencial de teste; receber segredo por canal seguro no momento da execução; mascarar saídas; não colocar valor real em comando de exemplo, Skill, Git, PR, comentário ou log; preferir referência/secret injection se a plataforma suportar.

## O que NÃO fazer

Não usar credencial de assinante real na descoberta; não assumir que service profile Ethernet configura WAN; não executar sintaxe de outra release; não alterar a ONT online fora da bancada.

## Fonte

- Estado e objetivo informados pelo operador para a ONT de bancada.
- Evidência CLI primária: MA5800V100R018, patch SPH507.
- Huawei ONT Web Page Reference e documentação EG8145X6 disponíveis no portal oficial.
- Huawei PPPoE documentation: cliente/servidor, discovery, sessão e autenticação.
- A CLI R018 e o firmware da ONT prevalecem; outra versão deve ser marcada [VERSÃO DIFERENTE].
