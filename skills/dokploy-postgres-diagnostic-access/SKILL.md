---
name: dokploy-postgres-diagnostic-access
description: Diagnosticar acesso SSH/Dokploy e consultar PostgreSQL em containers autorizados com evidência sanitizada, separando read-only de alterações transacionais explícitas.
---

# Acesso diagnóstico Dokploy → PostgreSQL

## Objetivo

Encontrar um caminho autorizado e reproduzível para consultas PostgreSQL sem
confiar cegamente em alias SSH, sem transformar a API do Dokploy em shell e
sem expor credenciais.

## Parâmetros do Source of Truth

- `${DOKPLOY_SSH_ALIAS}`, `${DOKPLOY_HOST}` e `${SSH_PORT}` confirmados;
- referências locais de `${SSH_USER_VAR}` e `${SSH_PASSWORD_VAR}` quando
  autorizadas;
- `${DOKPLOY_API_URL}` e `${DOKPLOY_API_KEY_VAR}` apenas para API documentada;
- `${COMPOSE_NAME}`, `${POSTGRES_SERVICE_PATTERN}` e `${DATABASE_NAME}`;
- `${OPERATION_SCOPE}`: `READ` por padrão, `WRITE` somente por autorização.

Leia `.env` somente em memória, pelo menor privilégio. Nunca imprima ou grave
os valores, nem os passe em argumentos visíveis.

## Observação de SSH (READ)

1. Verifique o alias sem despejar sua expansão; compare internamente seu destino
   com `${DOKPLOY_HOST}` inventariado.
2. Confira DNS, rota e conexão TCP de forma limitada. `No route to host` pode
   indicar destino antigo, gateway/túnel ausente ou host inacessível; não faça
   varredura nem altere rede para contornar.
3. Se o endereço inventariado alcançar SSH mas o alias não, trate o alias como
   divergente e valide host key estritamente no destino confirmado.
4. Em falha de autenticação, pare a repetição automática. Diferencie rota,
   host key, usuário, credencial e privilégio pós-login.
5. Registre apenas `alias configurado`, `host remoto` e camada de falha; não
   registre IP, usuário ou caminho de chave.

## Dokploy API

Use somente endpoints oficiais documentados para identificar Compose, serviços,
status e logs filtrados. API acessível não equivale a terminal, Docker socket ou
acesso PostgreSQL. Não use endpoints não documentados e não envie SQL pela API.

## PostgreSQL por container (READ)

Depois de SSH autenticado:

1. confirme a autorização para `sudo`/Docker; acesso SSH não garante acesso ao
   socket Docker;
2. identifique o container PostgreSQL pelo Compose e serviço confirmados, nunca
   por um nome genérico de outro stack;
3. confirme health sem despejar environment;
4. execute `psql` pelo container em transação `READ ONLY`;
5. consulte primeiro schema, Community/tenant e contagens; só depois dados
   mínimos necessários, sempre filtrados;
6. valide PK/unique/FK via catálogo e registre resultado sanitizado.

## Alterações posteriores (WRITE explicitamente autorizado)

Diagnóstico não autoriza escrita. Para uma alteração futura, crie um ciclo
separado com precondições, transação curta, abort, rollback específico e
pós-validação independente. Não reutilize permissões de acesso para ampliar o
escopo da tarefa.

## Classificação

- **ACCESS RESTORED:** SSH e consulta `READ ONLY` ao container PostgreSQL
  confirmados.
- **ACCESS BLOCKED:** informe destino sanitizado, erro literal sanitizado,
  teste feito, camada bloqueadora e a autorização/rota necessária.

## Incidente consolidado

**Causa confirmada:** um alias SSH pode apontar para destino divergente enquanto
o host inventariado está alcançável; também é possível autenticar em SSH sem
permissão ao socket Docker.

**Prevenção:** valide destino, host key, autenticação e privilégio Docker como
gates independentes antes de declarar acesso PostgreSQL restaurado.
