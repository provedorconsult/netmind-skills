---
name: 19-ma5800-production-checklist
description: Validar ponta a ponta um provisionamento MA5800-X7 antes de liberar produção, sem executar testes locais ou mudanças não autorizadas.
---

# Checklist de Produção MA5800

## Objetivo

Dar aceite operacional reproduzível para ONT e PPPoE.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Mudança autorizada e concluída; dados do assinante tratados fora das Skills.

## Comandos confirmados

- [CONFIRMADO] `display ont info summary 0/1/0`; `display service-port 1000`; `display port vlan 0/1/0`; `display port vlan 0/8/0`.

## Comandos de descoberta

- [DISCOVERY] Para qualquer outro estado, usar `?` e registrar a release.

## Sintaxe

Checklist completo no README: board/PON, profiles/DBA, ONT, GEM, service-port, VLAN, uplink, BNG, AAA e IP.

## Exemplos

Aceite do baseline: ONT online, service-port up, VLAN100 nos dois lados, PPPoE no BNG.

## Resultado esperado

Todos os itens aprovados com evidência e responsável.

## Erros conhecidos

Qualquer item falho interrompe o aceite; usar banco de erros.

## Diagnóstico

Voltar à primeira camada falha na decision tree.

## Dependências

Equipes OLT, transporte/BNG e AAA.

## Riscos

Aceite parcial pode ocultar perda de redundância ou gestão.

## Rollback

Se critério de abort ocorrer, seguir `17-ma5800-rollback`.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não declarar sucesso apenas pelo estado online da ONT.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

