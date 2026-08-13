# Guardrails de acesso a equipamentos

## Princípio

A biblioteca assume que **acessar o equipamento é parte básica do trabalho do agente**. O acesso autenticado não é, por si só, uma mudança de configuração.

O controle operacional é aplicado ao comando/ação executado após a conexão.

## Hierarquia operacional

1. **Prompt/tarefa/Issue vigente** define o escopo permitido.
2. **Source of Truth** define alvo, topologia, endereços e fatos reais.
3. **Skill aplicável** define procedimento seguro, sintaxe, validações e rollback.
4. **CLI do equipamento** confirma contexto e sintaxe real.

Nenhuma camada inferior amplia uma autorização da camada superior.

## Classes de comando

| Classe | Exemplos conceituais | Regra |
|---|---|---|
| `READ` | status, configuração exibida, contadores | permitido no escopo read-only |
| `DISCOVERY` | ajuda contextual, `?`, inspeção de sintaxe | permitido quando não altera estado |
| `TEST` | teste controlado | conforme prompt e skill |
| `WRITE` | criar/alterar configuração | exige autorização vigente e guardrails |
| `PERSIST` | salvar configuração global | ação separada quando a plataforma distinguir persistência |
| `HIGH-IMPACT` | delete, reload/reset, gestão, routing, AAA, firewall, ACL/NAT de produção | autorização explícita + plano completo |

## Credenciais e `.env`

O `netmind-skills` não armazena `.env` nem credenciais. Entretanto, uma skill pode usar/aceitar credenciais carregadas localmente pelo projeto consumidor quando a política desse projeto permitir.

Requisitos:

- ler somente variáveis necessárias;
- manter secrets fora de stdout/stderr e logs;
- nunca registrar secrets em evidências;
- nunca versionar `.env*`;
- nunca incluir credenciais concretas em exemplos da skill;
- não confundir posse da credencial com autorização para escrita.

## Falha de resolução de nome

Um alias que não resolve não encerra automaticamente a operação. A skill deve aceitar um endereço já confirmado pelo Source of Truth ou parâmetro autorizado do ambiente.

É proibido compensar falta de resolução com varredura de rede ou adivinhação de endereço.

## Escrita segura

Para `WRITE` e acima, confirmar proporcionalmente ao risco:

- alvo e contexto;
- versão/release;
- estado anterior;
- sintaxe descoberta/confirmada;
- impacto e dependências;
- backup pre-change quando aplicável;
- rollback exato;
- critério de abort;
- pós-validação;
- persistência tratada separadamente quando necessário.

## Evidência

A evidência deve mostrar o suficiente para permitir auditoria sem revelar segredo: equipamento canônico, classe da operação, comandos sanitizados, resultados relevantes, horário/janela, validação e warnings.
