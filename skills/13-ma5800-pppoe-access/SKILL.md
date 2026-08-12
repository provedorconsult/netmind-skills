---
name: 13-ma5800-pppoe-access
description: Diagnosticar a arquitetura PPPoE em redes MA5800-X7 separando OLT L2, ONT cliente PPPoE e ASR1001-X BNG/AAA.
---

# Acesso PPPoE

## Objetivo

Manter responsabilidades corretas e localizar falha PPPoE por camada.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

VLAN 100 contínua até o BNG; service-port up; acesso aos sistemas apropriados.

## Comandos confirmados

- [CONFIRMADO] Na OLT, usar apenas os displays confirmados de ONT, service-port e VLAN deste pacote.

## Comandos de descoberta

- [DISCOVERY] Qualquer comando PPPoE específico da OLT/BNG deve ser descoberto/documentado no equipamento correspondente.

## Sintaxe

Arquitetura: EG8145X6-10 (cliente PPPoE) → GPON → GEM1 → service-port1000 → VLAN100 → uplink0/8/0 → ASR1001-X (BNG) → AAA/RADIUS.

## Exemplos

Se PADI chega ao BNG mas não há PADO, investigar BNG; se autenticação falha, investigar AAA, não DBA.

## Resultado esperado

Cliente autentica no BNG e recebe IP após todas as camadas anteriores estarem boas.

## Erros conhecidos

Não há erro PPPoE literal fornecido; não fabricar diagnóstico.

## Diagnóstico

Captura/contador no ponto autorizado: CPE, VLAN no BNG, sessão PPPoE e RADIUS, nessa ordem.

## Dependências

ONT, GPON, GEM, service-port, VLAN, uplink, BNG e AAA.

## Riscos

Credenciais e logs AAA são sensíveis.

## Rollback

Alterações PPPoE pertencem ao CPE/BNG e exigem plano próprio.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não configurar usuário/senha PPPoE do assinante na MA5800; não armazenar credenciais.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

