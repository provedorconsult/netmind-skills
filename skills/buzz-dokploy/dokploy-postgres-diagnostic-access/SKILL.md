---
name: dokploy-postgres-diagnostic-access
description: Diagnosticar, por caminhos autorizados e somente leitura por padrão, o acesso de um deployment Buzz em Dokploy ao PostgreSQL sem expor segredos nem usar a API do Dokploy como shell.
---

# Acesso diagnóstico Dokploy → PostgreSQL para Buzz

## Objetivo

Determinar em qual camada está bloqueado o acesso diagnóstico a um PostgreSQL que suporta uma instalação Buzz em Dokploy: conectividade administrativa, identidade do Compose, privilégio do container ou banco. A skill não faz deploy, restart, migration, alteração de environment ou escrita no banco.

## Quando usar

Use quando uma tarefa `READ` autorizada precisa confirmar saúde, schema, constraints ou uma consulta mínima relacionada ao Buzz. Para mudança de membership, use `$buzz-community-membership` somente com `WRITE` explícito.

## Contexto obrigatório

Obter exclusivamente do Source of Truth ou de ambiente local autorizado:

- `${DOKPLOY_SSH_ALIAS}` ou `${DOKPLOY_HOST}`, `${SSH_PORT}` e `${SSH_USER_VAR}`;
- `${DOKPLOY_API_URL}` e `${DOKPLOY_API_KEY_VAR}`, se a API for autorizada;
- `${COMPOSE_NAME}`, `${POSTGRES_SERVICE_NAME}` e `${DATABASE_NAME}` confirmados;
- `${OPERATION_SCOPE}`, que deve ser `READ` para este procedimento.

Credenciais podem ser lidas em memória do mecanismo autorizado. Não as imprima, expanda em debug, copie para comandos registrados ou versione `.env`.

## Fluxo `READ`

1. Confirme que alias, host e Compose pertencem ao deployment autorizado. Se o alias não resolver e houver host confirmado, use somente esse host; não faça scan nem deduza endereço.
2. Verifique DNS, rota e TCP com timeout limitado. `No route to host` é evidência de rota, gateway, túnel ou host; não justifica alterar rede.
3. Se o host estiver confirmado, valide a host key estritamente. Em divergência de identidade, autenticação ou privilégio, interrompa repetições automáticas e devolva evidência sanitizada.
4. Após login, confirme separadamente o privilégio administrativo necessário para consultar o container. SSH autenticado não comprova acesso ao socket Docker nem a `sudo` não interativo.
5. Use endpoints oficiais documentados do Dokploy apenas para confirmar Compose, serviço, health e logs filtrados. Nunca envie SQL por endpoint não documentado.
6. Identifique PostgreSQL pelo Compose e pelo serviço confirmados, nunca por um nome genérico de container. Confira o health sem despejar environment.
7. Execute `psql` somente em transação `READ ONLY`. Primeiro consulte catálogo/schema e constraints; depois, se a tarefa exigir, use consulta mínima filtrada e sanitizada.
8. Registre camada acessada, health, tipo de consulta, contagem/resultado sanitizado e limitações. Não registre linhas de usuários, eventos ou secrets por padrão.

## Compatibilidade Buzz

O bundle Compose oficial do Buzz usa PostgreSQL, Redis, MinIO e volume de dados Git como dependências. Isso não autoriza assumir nomes de serviços, credenciais, versão de schema ou que um Compose customizado no Dokploy corresponda ao bundle upstream. Confirme a release/imagem e o Compose efetivo antes de interpretar resultados.

## Limites de autorização

- `READ`: consultas, catálogo, constraints, health e logs filtrados.
- `TEST`: não é concedido por esta skill.
- `WRITE`: não é concedido por esta skill; `INSERT`, `UPDATE`, `DELETE`, DDL, migrations e comandos equivalentes exigem tarefa própria, precheck, rollback e pós-validação.
- `PERSIST` e `HIGH-IMPACT`: não são concedidos.

## Resultado esperado

```text
ssh: PASS | FAIL | BLOCKED
dokploy_api: PASS | NOT_USED | FAIL | BLOCKED
compose_identity: PASS | FAIL | BLOCKED
postgres_read: PASS | FAIL | BLOCKED
blocked_layer: route | host-key | authentication | privilege | compose | container | database
secrets: none-disclosed
```

## Fontes

- [Buzz Compose deployment](https://github.com/block/buzz/tree/main/deploy/compose)
- [Buzz architecture](https://github.com/block/buzz#architecture)
