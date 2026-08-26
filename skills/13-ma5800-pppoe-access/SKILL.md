---
name: 13-ma5800-pppoe-access
description: Diagnosticar PPPoE com a EG8145X6-10 roteada como cliente, MA5800-X7 como transporte L2/provisionamento OMCI e ASR1001-X como BNG/AAA.
---

# Acesso PPPoE

## Objetivo

Manter responsabilidades corretas e localizar falha PPPoE por camada.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

VLAN 100 contínua até o BNG; service-port up; WAN route aplicada à ONT de bancada; acesso aos sistemas apropriados.

## Comandos confirmados

- [CONFIRMADO] Na OLT, usar apenas os displays confirmados de ONT, service-port e VLAN deste pacote.

## Comandos de descoberta

- [INFERIDO] Descobrir na R018, usando `?`, como consultar e provisionar a WAN PPPoE da ONT; depois registrar as consultas executadas como [DISCOVERY].
- [DISCOVERY] Qualquer comando PPPoE específico já executado na OLT/BNG deve ser documentado no equipamento correspondente.

## Sintaxe

Arquitetura: EG8145X6-10 (route/NAT/DHCP/Wi-Fi e cliente PPPoE) → GPON → T-CONT → GEM → GEM mapping VLAN/flow → service-port → VLAN → uplink → ASR1001-X (servidor PPPoE/BNG) → AAA/RADIUS. A MA5800 transporta o tráfego e pode provisionar a WAN por OMCI; ela não termina a sessão como cliente.

## Exemplos

Se PADI chega ao BNG mas não há PADO, investigar BNG; se autenticação falha, investigar AAA, não DBA.

## Resultado esperado

Cliente autentica no BNG e recebe IP após todas as camadas anteriores estarem boas.

## Erros conhecidos

Não há erro PPPoE literal fornecido; não fabricar diagnóstico.

## Diagnóstico

Validar WAN/profile na ONT; T-CONT/GEM/mapping/service-port/VLAN/uplink; depois PADI, PADO, PADR/PADS, LCP, PAP/CHAP, IPCP, IP, rota/DNS, NAT/DHCP e LAN/Wi-Fi. Se WAN está `Disconnected`, service-port `up` mas zerado e BNG sem PADI/PADR, verificar primeiro o mapping VLAN/flow do GEM. NAT/CGNAT só é avaliado depois de sessão/IP funcionais.

## Credencial PPPoE no diagnóstico

Quando a validação de autenticação exigir credenciais, `pppoe_username` e
`pppoe_password` podem ser informações operacionais necessárias. A senha atual
deve vir exclusivamente do Source of Truth autorizado do sistema consumidor;
esta Skill não armazena, deduz, gera ou recupera a senha.

Se apenas o username estiver disponível, registrar `UNKNOWN`: a senha PPPoE
atual não foi fornecida pelo Source of Truth. Não inferir a senha nem gerar uma
nova; solicitar ou consultar somente a fonte autorizada conforme a política do
sistema consumidor. Se a credencial for fornecida no contexto autorizado,
registrar `CONFIRMADO` apenas para a disponibilidade e usá-la somente no
escopo autorizado, sem incluí-la na evidência sanitizada. A posse da
credencial não autoriza alteração na OLT, AAA, BNG ou BRAS.

## Dependências

ONT, GPON, GEM, service-port, VLAN, uplink, BNG e AAA.

## Riscos

Credenciais e logs AAA são sensíveis.

## Rollback

Restaurar o baseline bridge da ONT e remover a WAN route com sintaxe previamente validada; mudanças no BNG têm plano próprio.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não fazer a MA5800 atuar como cliente PPPoE. Se OLT/NMS entregar a credencial à ONT por OMCI, usar credencial de teste e canal seguro, mascarar retorno e nunca persistir o segredo em Skills, Git, exemplos ou logs.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
