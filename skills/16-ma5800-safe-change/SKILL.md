---
name: 16-ma5800-safe-change
description: Planejar mudanças seguras e autorizadas na MA5800-X7 com baseline, impacto, validação, janela e rollback.
---

# Mudança Segura MA5800

## Objetivo

Reduzir risco operacional de qualquer comando de configuração.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Autorização explícita; release validada; baseline; dependências; ONT de teste; rollback.

## Comandos confirmados

- [CONFIRMADO] Preferir todos os `display` aplicáveis antes/depois; [DESTRUTIVO] tratar todo comando de configuração como mudança de risco.

## Comandos de descoberta

- [DISCOVERY] Validar sintaxe com `?` se não estiver `[CONFIRMADO]` nesta release.

## Sintaxe

Plano mínimo: alvo, estado anterior, comando, impacto, critério de sucesso, abort e rollback. Para GEM mapping: confirmar `binding times`/escopo do profile, mapping-index livre, VLAN/GEM/service-port coerentes, snapshot sanitizado OLT+BNG, rollback específico e pós-validação ponta a ponta.

## Exemplos

Antes de DBA: listar IDs e bind-times; antes de service-port: listar índice e caminho.

## Resultado esperado

Uma mudança por camada, resultado comparável e nenhuma alteração fora do escopo.

## Erros conhecidos

Em qualquer erro inesperado, parar, registrar literalmente e não tentar variações.

## Diagnóstico

Determinar se falha é de sintaxe, dependência, capacidade ou estado.

## Dependências

Rollback e acesso de gestão resiliente.

## Riscos

Perda de gestão, serviço multi-tenant ou alteração em ONT online. `commit` aplica a mudança no objeto/contexto; `save` global é persistência distinta e nunca é implícito nem executado sem autorização explícita.

## Rollback

Deve ser escrito antes da execução e usar sintaxe confirmada/descoberta.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não executar destrutivo sem confirmação; não alterar gestão/rota; não usar produção como laboratório.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
