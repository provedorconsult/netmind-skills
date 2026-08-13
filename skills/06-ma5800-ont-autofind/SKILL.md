---
name: 06-ma5800-ont-autofind
description: Descobrir ONTs GPON na MA5800-X7, habilitar autofind de modo controlado e validar SN, modelo e porta antes do provisionamento.
---

# Autofind de ONT

## Objetivo

Localizar e identificar uma ONT sem confundi-la com outra PON.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

ODN conectado; PON correta; autorização para habilitar autofind.

## Comandos confirmados

- [CONFIRMADO] `display ont autofind all`
- [CONFIRMADO][DESTRUTIVO] `interface gpon 0/1`
- [CONFIRMADO][DESTRUTIVO] `port 0 ont-auto-find enable`

## Comandos de descoberta

- [DISCOVERY] Usar `port ?` no contexto GPON se a release divergir.

## Sintaxe

O enable ocorre em `config-if-gpon-0/1`, porta 0.

## Exemplos

ONT observada: 0/1/0, SN 4857544354ABCFB2, HWTC, EG8145X6-10, MAC AC5E-143C-EB3E, NNI 2.5G/1.25G.

## Resultado esperado

`display ont autofind all` retorna a ONT correta; inicialmente retornou ausência.

## Erros conhecidos

[ERRO] `Failure: The automatically found ONTs do not exist` significa nenhum resultado, não falha de sintaxe.

## Diagnóstico

Checar enable, PON/ODN, energia, laser, alcance e SN; usar guia oficial Huawei de falha de autodiscovery.

## Dependências

Board H907CGHF no slot 0/1 e PON 0.

## Riscos

Autofind pode expor ONTs não autorizadas; habilitar não as provisiona.

## Rollback

Se exigido pela política, descobrir e validar com `?` o comando de disable antes de executar.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não adicionar uma ONT somente por ter aparecido; validar SN e localização.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

