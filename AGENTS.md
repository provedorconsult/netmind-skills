# Regras para agentes — netmind-skills

## Papel deste repositório

- Este repositório é a biblioteca operacional reutilizável dos agentes para acesso, discovery, backup, diagnóstico, configuração, testes, monitoramento e rollback em equipamentos de rede.
- Não armazenar aqui dados específicos de cliente: IPs reais, hostnames, seriais, topologia, credenciais, `.env`, backups brutos ou configurações específicas pertencem ao Source of Truth do projeto correspondente.
- A CLI do equipamento e a documentação oficial compatível com fabricante/modelo/release prevalecem sobre exemplos genéricos.

## Acesso é capacidade básica

- Conectar e autenticar em um equipamento autorizado é uma capacidade básica do agente e não deve ser classificada como mudança de configuração.
- O guardrail deve ser aplicado à classe de comando executado após a conexão, não à abertura da sessão.
- Quando o projeto/Source of Truth disponibilizar `.env` ou `.env.*` como mecanismo autorizado de credenciais, a skill pode orientar seu uso local em memória. Nunca copiar, imprimir, registrar ou versionar valores secretos.
- Se o alvo não resolver por alias, a skill deve permitir endereço de gerenciamento já confirmado pelo Source of Truth ou parâmetro de conexão autorizado; nunca descobrir alvo por varredura ou inferência.

## Modelo de autorização operacional

- `READ/DISCOVERY`: consultas, status, contadores, `show`, `display`, ajuda contextual e `?`. Usar por padrão quando o prompt não autorizar mudança.
- `TEST`: teste controlado conforme a skill e o escopo vigente.
- `WRITE`: criação ou alteração de configuração somente quando o prompt/tarefa vigente autorizar.
- `PERSIST`: persistência global deve ser tratada como ação própria quando aplicável.
- `DESTRUCTIVE/HIGH-IMPACT`: remoção, reload/reset, mudança de gestão, routing, AAA, firewall, ACL/NAT de produção ou equivalente exige autorização e guardrails proporcionais.

A skill nunca amplia o escopo concedido pelo prompt/tarefa/Issue.

## Guardrails

- Antes de escrita: validar alvo, contexto, versão, sintaxe, precheck, impacto, dependências, rollback, abort e pós-validação.
- Não improvisar comando mutável desconhecido; usar discovery seguro ou documentação oficial.
- Em falha de autenticação, bloqueio, host key inesperada ou identidade divergente, interromper repetição automática e devolver evidência sanitizada.
- Nunca registrar secrets em Git, Issues, PRs, logs ou exemplos.

## Qualidade

- Skills devem permanecer parametrizadas e reutilizáveis.
- Exemplos devem usar placeholders ou redes reservadas para documentação.
- Alterações nas skills passam por validação estática e revisão antes de merge.
