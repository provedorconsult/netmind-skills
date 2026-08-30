# G20 — Remediação dos achados da auditoria de repositório

## Predecessor

`G18`

G19 permanece uma reconciliação retrospectiva do merge gate com predecessor
G17; ele não promoveu um novo Goal operacional no estado corrente.

## Contexto

A auditoria de 29 de agosto de 2026 não identificou credenciais, chaves
privadas, IPs de cliente, links Markdown quebrados ou falhas nos guardrails
operacionais. Ela identificou três pontos de manutenção:

1. o catálogo do Harness lista G19 como concluído, enquanto
   `.harness/state/current.json` termina em G18 e não espelha G19;
2. os validadores de frontmatter, Equipment Registry e índices requerem
   PyYAML, mas não há artefato versionado para preparar esse ambiente local;
3. `.vscode/extensions.json` é configuração local não rastreada e não é
   explicitamente ignorada.

## Objetivo

Eliminar as ambiguidades de governança e tornar a validação estática local
reproduzível, sem ampliar o escopo para equipamentos, clientes ou mudanças de
rede.

## Escopo

- Definir e documentar a representação canônica de G19 no catálogo e no
  estado corrente do Harness. A solução deve deixar explícito por que G18
  continua ou deixa de continuar como `completedGoal` sequencial.
- Atualizar os validadores e fixtures do Harness para verificar essa regra,
  impedindo nova divergência silenciosa entre catálogo e estado.
- Versionar uma dependência exclusiva de desenvolvimento para PyYAML na mesma
  versão já usada na CI, e documentar o preparo mínimo para executar os
  validadores estáticos localmente.
- Tratar `.vscode/` como configuração local: ignorá-la, salvo se houver uma
  decisão documentada de compartilhar uma configuração de equipe.
- Atualizar a documentação de tarefas para refletir G20 como demanda formal
  planejada, sem promovê-lo a `READY` ou alterar `activeGoal`.

## Fora de escopo

- Alterar Skills de equipamento, comandos operacionais, registries técnicos
  ou regras de autorização de rede.
- Instalar dependências de produção, executar containers, deploys, migrações
  ou qualquer acesso a equipamento.
- Executar suítes de teste locais; testes dinâmicos continuam responsabilidade
  da CI/VPS conforme `AGENTS.md`.
- Promover automaticamente G20, fazer merge ou alterar histórico remoto.

## Critérios de aceite

- Catálogo, estado corrente, memória de trabalho, validador e fixture usam a
  mesma regra explícita para G18 e G19.
- Um teste/validação estática falha se G19 voltar a divergir do estado que a
  política determinar.
- Existe um arquivo de dependências de desenvolvimento versionado que fixa
  `PyYAML==6.0.3`, sem alterar dependências de runtime.
- README ou documento de contribuição informa um comando reproduzível para os
  validadores estáticos após instalar as dependências de desenvolvimento.
- `.vscode/` não aparece como arquivo não rastreado após a aplicação da regra
  escolhida.
- Lint Markdown, links internos, validação de repositório, frontmatter,
  Equipment Registry e verificação de índices passam no ambiente preparado.
- A CI executa a mesma versão de PyYAML declarada no repositório.

## Prompt para o Maker

```text
Você é o Maker do G20 — Remediação dos achados da auditoria de repositório.

Leia integralmente AGENTS.md, README.md, HARNESS.md, README-TASKS.md,
20-auditoria-repositorio-remediacao.md e os arquivos do Harness antes de
editar. Crie o Goal G20 com a ferramenta Goal; trabalhe em uma branch curta
docs/g20-audit-remediation ou fix/g20-audit-remediation e não altere o estado
para READY sem a promoção formal exigida pelo Harness.

Implemente somente o escopo do G20:
1. Reconcilie a representação de G19 entre o catálogo e o estado corrente.
   Preserve a semântica de G18 como último Goal sequencial apenas se isso for
   documentado e validado explicitamente. Atualize memória, validadores e
   fixtures para que a regra não volte a divergir silenciosamente.
2. Adicione uma dependência de desenvolvimento versionada com PyYAML==6.0.3,
   alinhada à CI. Documente o preparo e os comandos de validação estática
   local; não adicione dependências de produção.
3. Trate .vscode/ como configuração local por meio de .gitignore, salvo se
   encontrar uma decisão versionada e atual que justifique compartilhá-la.
4. Atualize README-TASKS.md para registrar G20 como demanda planejada, sem
   mudar activeGoal, nextGoal ou executar promoção automática.

Preserve dados sanitizados: não inclua credenciais, tokens, IPs/hostnames de
clientes, backups ou configurações reais. Não execute testes locais, Docker,
deploy, migração ou ação de rede. Pode executar somente validações estáticas
leves depois que o ambiente de desenvolvimento estiver preparado.

Antes de abrir a PR, revise git diff e execute as validações estáticas
aplicáveis. Relate os arquivos alterados, a regra canônica escolhida para
G18/G19, as validações executadas, as limitações e os testes pendentes na CI.
Abra uma PR; aguarde o Checker. Não faça merge sem um comentário social
literal `approve` no HEAD efetivamente revisado.
```
