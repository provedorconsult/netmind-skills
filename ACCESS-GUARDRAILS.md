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

## Credencial PPPoE para diagnóstico

A senha PPPoE é uma **credencial operacional**: pode ser necessária quando o
procedimento de diagnóstico precisar validar a autenticação entre serviço,
AAA/RADIUS, BNG/BRAS e sessão PPPoE. Esta regra é multi-fabricante e não
confirma sintaxe, capability ou comando de nenhum equipamento.

O `netmind-skills` define o procedimento; o **Source of Truth autorizado do
projeto consumidor** fornece, quando aplicável, `pppoe_username` e
`pppoe_password`. O agente deve usar a credencial somente dentro do escopo da
tarefa. A disponibilidade da senha não concede `WRITE`, `PERSIST` ou
`HIGH-IMPACT`.

Quando a senha atual não for fornecida pela fonte autorizada, registrá-la como
limitação diagnóstica e não deduzi-la, procurá-la em fontes não autorizadas,
gerar uma nova nem tratar conhecimento histórico como credencial atual. O
repositório não armazena senhas PPPoE; a senha real nunca entra em evidência,
fixtures, exemplos, Skills, Git, PRs, comentários ou logs.

Evidência sanitizada aceitável:

```text
PPPoE username: <pppoe-user>
PPPoE password: PRESENT / AVAILABLE_FROM_SOT
```

O valor da senha não é evidência sanitizada. A presença pode ser reportada sem
revelar o segredo, sempre separando `CONFIRMADO`, `DISCOVERY`, `INFERIDO`,
`ERRO` e `VERSÃO DIFERENTE` conforme a evidência disponível.

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
