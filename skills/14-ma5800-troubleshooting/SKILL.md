---
name: 14-ma5800-troubleshooting
description: Diagnosticar falhas MA5800-X7 em camadas, usando displays e erros literais antes de qualquer alteração.
---

# Troubleshooting MA5800

## Objetivo

Parar no primeiro ponto de falha e produzir hipótese verificável.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Carregar `ma5800-decision-tree` e `15-ma5800-error-database`.

## Comandos confirmados

- [CONFIRMADO] `display ont autofind all`; `display ont info summary 0/1/0`; `display service-port 1000`; `display port vlan 0/1/0`; `display port vlan 0/8/0`.

## Comandos de descoberta

- [DISCOVERY] Usar `?` somente no ponto de falha para ampliar evidência.

## Sintaxe

Executar leitura em ordem física→GPON→profiles→T-CONT→GEM→GEM mapping VLAN/flow→service-port no mesmo GEM→VLAN PON/uplink→BNG→AAA. Em `mapping-mode VLAN`, não inferir que a existência do GEM encaminha tráfego: registrar o mapping explícito e compatível com a VLAN do serviço.

## Exemplos

Service-port down: não alterar AAA; ONT inexistente: não recriar service-port.

## Resultado esperado

Uma primeira falha, evidências, impacto, hipótese e próxima leitura segura.

## Erros conhecidos

Consultar `MA5800-ERROR-DATABASE.md` para os oito erros literais.

## Diagnóstico

Aplicar a árvore de 21 passos e parar. A assinatura ONT online + service-port `up` sem contadores + WAN PPPoE `Disconnected` + BNG sem PADI/PADR exige verificação prioritária do mapping VLAN/flow do GEM. Tratar `Match state: mismatch` como trilha paralela até evidência de impacto no forwarding.

## Dependências

Baseline e acesso a equipamentos das camadas sob análise.

## Riscos

Mudanças simultâneas mascaram causa e ampliam incidente.

## Rollback

Não iniciar mudança sem estado anterior e critério de retorno.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não shotgun troubleshooting; não alterar camadas posteriores.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
