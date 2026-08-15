# TASK 07 — CI/CD: Markdown, Frontmatter e Links

## Goal

Criar a primeira camada de GitHub Actions para validar automaticamente a qualidade da documentação em Pull Requests e Push na `main`.

## Fonte de requisitos

Basear-se em:
- RF07;
- seção 7.2;
- RNF05;
- RNF06.

## Escopo

Criar/ajustar workflows para:
1. checkout;
2. setup Python;
3. instalação das dependências necessárias;
4. validação do Frontmatter;
5. execução de `scripts/build_indexes.py --check`;
6. markdown lint;
7. verificação de links internos.

## Regras

- O workflow deve rodar em Pull Request e Push na `main`.
- Falha em qualquer etapa deve falhar o job.
- Versões de actions e ferramentas devem ser explicitadas de maneira reprodutível.
- Não adicionar ferramentas sem necessidade.
- Se o verificador de links não estiver definido pelo PRD, escolher uma implementação mínima e documentar a escolha.

## Critérios de aceite

- PR de teste executa o workflow.
- Erro proposital em frontmatter é detectado.
- Divergência de índice é detectada.
- Markdown inválido é detectado.
- Link interno quebrado é detectado.
- Correção dos erros faz o pipeline voltar a verde.
- Workflow não modifica o repositório durante validação.

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
