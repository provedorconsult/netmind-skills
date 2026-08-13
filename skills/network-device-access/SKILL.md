---
name: network-device-access
description: Preparar, autenticar e validar sessões seguras em equipamentos de rede inventariados usando parâmetros confirmados pelo Source of Truth, inclusive credenciais locais provenientes de .env autorizado, sem ampliar o escopo de comandos permitido pela tarefa.
---

# Acesso seguro a equipamentos de rede

## Objetivo

Estabelecer uma sessão autenticada e validada com o equipamento correto. A conexão é uma capacidade operacional básica; a autorização de leitura, teste, escrita, persistência ou ação destrutiva é decidida separadamente pelo prompt/tarefa vigente.

## Quando usar

Usar antes de qualquer skill que dependa de CLI, SSH, Telnet, API, SNMP ou outro canal de gestão do equipamento.

## Princípios

- Tratar o Source of Truth como autoridade para identidade e endereço do equipamento.
- Não inferir alvo, IP, hostname, credencial ou topologia a partir desta skill.
- Autenticar não significa autorizar mudança.
- `.env`/`.env.*` pode ser usado como fonte local autorizada de parâmetros e credenciais quando o projeto permitir.
- Segredos permanecem em memória e nunca entram em Git, logs, Issues, PRs, relatórios ou respostas.

## Parâmetros

Resolver no Source of Truth ou ambiente autorizado:

- `${DEVICE_NAME}`: nome canônico;
- `${DEVICE_HOST}`: alias, DNS ou endereço de gerenciamento confirmado;
- `${DEVICE_VENDOR}` e `${DEVICE_MODEL}`;
- `${DEVICE_VERSION}` quando conhecida;
- `${ACCESS_PROTOCOL}`: SSH, Telnet, API, SNMP ou outro método autorizado;
- `${USERNAME_VAR}`, `${PASSWORD_VAR}`, `${TOKEN_VAR}` ou outras referências de segredo, quando aplicáveis;
- `${JUMP_HOST}` quando a topologia exigir bastion;
- `${OPERATION_SCOPE}`: `READ`, `DISCOVERY`, `TEST`, `WRITE`, `PERSIST` ou `HIGH-IMPACT` conforme a tarefa.

## Resolução do alvo

Usar esta ordem:

1. nome/alias canônico operacional;
2. configuração SSH/DNS já aprovada;
3. endereço de gerenciamento confirmado no Source of Truth;
4. parâmetro de conexão autorizado no ambiente local.

Falha de resolução de alias não é motivo para abandonar a tarefa quando existir endereço confirmado. Não fazer varredura de rede nem adivinhar endereço.

## Uso de `.env`

Quando permitido pelo projeto:

1. localizar o `.env` no workspace/local seguro;
2. ler somente as variáveis necessárias à sessão;
3. não executar dump, `cat` indiscriminado, debug com expansão de secrets ou eco de credenciais;
4. não exportar variáveis desnecessárias globalmente;
5. usar os valores somente no processo/sessão necessária;
6. nunca copiar o arquivo ou valores para o repositório;
7. registrar apenas que foi usada uma fonte de credencial local autorizada e sanitizada.

A existência da credencial não altera `${OPERATION_SCOPE}`.

## Fluxo

1. **Resolver identidade:** confirmar `${DEVICE_NAME}`, fabricante/modelo e host.
2. **Resolver autorização:** classificar o escopo vigente.
3. **Carregar credencial:** obter somente os valores necessários do mecanismo autorizado.
4. **Conectar:** abrir a sessão pelo protocolo previsto, usando jump host quando exigido.
5. **Validar alvo:** conferir prompt, banner, versão ou outro identificador seguro antes de executar a tarefa principal.
6. **Aplicar guardrail:** carregar a skill específica do fabricante/modelo e executar somente comandos compatíveis com o escopo.
7. **Encerrar/sanitizar:** não persistir secrets e registrar apenas evidência sanitizada.

## Classes de operação

### READ / DISCOVERY

Permitidos quando a tarefa é read-only: consultas, status, contadores, `show`, `display`, ajuda contextual e descoberta de sintaxe segura.

### WRITE

Disponível quando o prompt/tarefa autorizar mudança. Antes de escrever, exigir precheck, sintaxe validada, impacto, rollback, critério de abort e pós-validação proporcionais ao risco.

### PERSIST

Persistência global é uma ação separada quando a plataforma distinguir running state de startup/persistência. Não assumir autorização de persistência apenas porque uma mudança foi autorizada.

### HIGH-IMPACT

Reload/reset, exclusão, alteração de gestão, routing, AAA, firewall, ACL/NAT de produção ou ação com risco material exige autorização explícita e plano seguro.

## Falhas de acesso

Interromper repetição automática quando ocorrer:

- credencial rejeitada;
- bloqueio de usuário/IP;
- host key inesperada;
- banner, prompt, modelo ou identidade divergente;
- salto/bastion diferente do previsto;
- comportamento que sugira alvo incorreto.

Registrar a falha sem segredo e pedir correção do mecanismo de acesso somente quando não houver outra fonte autorizada já definida.

## Resultado esperado

Entregar uma sessão validada ou um diagnóstico sanitizado de acesso contendo: `target_validated`, `protocol`, `scope`, `credential_source_sanitized`, `jump_path_sanitized` e `warnings`.

## Regras de segurança

- Nunca imprimir secrets.
- Nunca commitar `.env*`.
- Nunca usar credencial disponível para extrapolar o prompt.
- Nunca transformar uma falha de alias em varredura de rede.
- Nunca executar comando mutável antes de confirmar o escopo e a skill específica da plataforma.
