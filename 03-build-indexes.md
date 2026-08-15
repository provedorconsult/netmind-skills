# TASK 03 — Build de Índices e llms.txt

## Goal

Implementar `scripts/build_indexes.py` para construir e verificar a árvore de índices e o `llms.txt` conforme o PRD.

## Fonte de requisitos

Basear-se em:
- RF01;
- RF02;
- RF05;
- seção 7.1;
- RNF06;
- RNF02.

## Modos obrigatórios

Implementar:
- `--build`: gera/atualiza os artefatos;
- `--check`: valida se os artefatos existentes estão sincronizados sem modificá-los.

## Escopo

O script deve:
1. Percorrer recursivamente `docs/`.
2. Encontrar Markdown técnico.
3. Ler e validar YAML Frontmatter.
4. Gerar índices de equipamento.
5. Gerar índices de fabricante.
6. Gerar `/INDEX.md`.
7. Gerar `/llms.txt`.
8. Utilizar links relativos.
9. Produzir saída determinística.
10. Informar claramente divergências no modo `--check`.
11. Retornar código de saída diferente de zero quando houver divergência ou erro.
12. Evitar modificar arquivos fora dos artefatos gerados.

## Regras

- Não depender de ordenação do sistema de arquivos.
- Ordenar fabricantes, modelos e documentos de forma determinística.
- Não incorporar conteúdo técnico completo nos índices; usar metadados enxutos.
- Respeitar o objetivo AI-Native de navegação em árvore.
- O script deve ser seguro para execução repetida.

## Critérios de aceite

- `--build` produz os índices esperados.
- Uma segunda execução de `--build` sem mudanças não gera diff.
- `--check` retorna sucesso quando tudo está sincronizado.
- `--check` detecta índice alterado ou ausente.
- `llms.txt` lista fabricantes e rotas relativas.
- Testes automatizados cobrem geração e detecção de divergência.
- Desempenho é medido e documentado; para até 1.000 arquivos, buscar conformidade com o limite de 10 segundos do RNF02.

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
