---
name: ma5800-decision-tree
description: Conduzir troubleshooting ponta a ponta da MA5800-X7 até PPPoE/AAA, parando obrigatoriamente no primeiro ponto de falha.
---

# Árvore de Decisão MA5800

## Objetivo

Impedir mudanças em camadas posteriores enquanto a anterior está falha.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Baseline, escopo e acessos de leitura.

## Comandos confirmados

- [CONFIRMADO] Usar apenas os displays do pacote em cada nó; os nós sem comando confirmado exigem discovery.

## Comandos de descoberta

- [DISCOVERY] Usar `?` no equipamento responsável pelo nó, sem inferir sintaxe.

## Sintaxe

Sequência fixa de 20 nós documentada em `MA5800-DECISION-TREE.md`. No nó 18, confirmar primeiro WAN route na ONT e depois PADI/PADO/PADR/PADS, LCP, autenticação e IPCP.

## Exemplos

Se a ONT não foi encontrada no nó 4, parar; não criar service-port nem alterar BNG.

## Resultado esperado

Primeira falha isolada, evidência e próxima ação de leitura.

## Erros conhecidos

Erros literais remetem ao banco global.

## Diagnóstico

Responder SIM/NÃO/DESCONHECIDO por nó; DESCONHECIDO exige leitura, não mudança.

## Dependências

Todas as Skills especializadas.

## Riscos

Pular nó causa falso diagnóstico e mudanças desnecessárias.

## Rollback

Nenhuma mudança é autorizada pela árvore; mudanças usam as Skills safe-change/rollback.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não avançar após NÃO/DESCONHECIDO; não confundir OLT L2 com BNG/AAA.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
