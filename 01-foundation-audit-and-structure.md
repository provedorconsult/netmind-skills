# TASK 01 — Fundação e Estrutura Base

## Goal

Estabelecer a fundação do `provedorconsult/netmind-skills` conforme a arquitetura definida no PRD, sem executar ainda a migração em massa do conteúdo técnico.

## Objetivo operacional

Validar o estado real do repositório e implementar somente a estrutura base necessária para suportar a arquitetura AI-Native:
- diretórios de documentação por fabricante;
- diretórios por modelo/família;
- categorias `cli/`, `config/`, `diag/`, `mon/`, `update/`;
- diretório `templates/`;
- estrutura `.github/`;
- convenções necessárias para os próximos Goals.

## Fonte de requisitos

Basear a implementação no PRD `PRD-NetMind-Skills.md`, especialmente:
- seção 3 — Arquitetura da Informação;
- RF03;
- RF04;
- RF06;
- RNF03;
- Fase 1.

Não inventar conteúdo técnico de equipamentos. Preservar conteúdo existente sempre que possível.

## Escopo

1. Inspecionar a árvore atual antes de alterar arquivos.
2. Identificar arquivos monolíticos e estruturas já existentes.
3. Criar somente diretórios e arquivos-base necessários à fundação.
4. Preservar documentação existente; não apagar conteúdo nesta tarefa.
5. Criar ou ajustar templates definidos pelo PRD:
   - `templates/template-modelo-index.md`
   - `templates/template-modulo-atomic.md`
6. Criar templates de Issue/PR somente se ainda não existirem e somente no escopo especificado pelo PRD.
7. Aplicar kebab-case aos novos caminhos.
8. Documentar claramente qualquer divergência entre a estrutura existente e a estrutura do PRD.

## Fora de escopo

- Migração em massa de documentos.
- Implementação de `build_indexes.py`.
- Implementação de GitHub Actions.
- Alteração de conteúdo técnico dos equipamentos.
- Merge da PR.

## Critérios de aceite

- Estrutura base compatível com o PRD.
- Templates contêm o YAML Frontmatter obrigatório e estrutura coerente com RF04/RF06.
- Nenhum conteúdo técnico existente é perdido.
- Novos nomes seguem kebab-case.
- Não existem arquivos artificiais apenas para preencher diretórios vazios sem justificativa.
- PR contém evidências da inspeção e validação.

# Protocolo Maker / Checker

## Papel do Codex
Atuar exclusivamente como **Maker** nesta tarefa.

## Regra de integração
- O Maker deve implementar apenas o Goal desta tarefa.
- O Maker deve trabalhar em uma branch própria e abrir Pull Request contra `main`.
- O Maker deve executar os testes e validações definidos no arquivo.
- O Maker deve registrar no PR um resumo objetivo do que foi feito e evidências de validação.
- Ao terminar, o Maker deve solicitar explicitamente a revisão do Checker.
- O Maker **não deve fazer merge**, mesmo que os testes estejam verdes.
- O Maker deve aguardar o veredito do Checker em comentário no Pull Request.
- O comentário social `approve` do Checker é a autorização para integração.
- Qualquer outro comentário, inclusive `LGTM`, `looks good`, CI verde ou aprovação informal, **não autoriza merge**.
- Se o Checker solicitar alterações, o Maker deve corrigir na mesma branch/PR, executar novamente as validações e voltar a aguardar novo `approve`.
- Não fechar a PR sem autorização.
- Não alterar escopo de tarefas posteriores para resolver problemas não relacionados.

## Critério de conclusão
A tarefa só é considerada concluída quando:
1. implementação estiver na PR;
2. validações locais/CI estiverem verdes;
3. Checker revisar;
4. Checker publicar o comentário social `approve`.
