# TASK 08 — README, CONTRIBUTING e Governança AI-Native

## Goal

Atualizar a documentação de entrada e contribuição do repositório para explicar a arquitetura AI-Native e o fluxo de manutenção.

## Fonte de requisitos

Basear-se em:
- Fase 4;
- RF06;
- RF07;
- objetivos estratégicos do PRD;
- personas Maintainer/Contribuidor e Agente de IA.

## Escopo

Atualizar:
- `README.md`;
- `CONTRIBUTING.md`;
- templates de Issue/PR, quando necessários.

A documentação deve explicar:
1. propósito do repositório;
2. navegação por `INDEX.md`;
3. papel do `llms.txt`;
4. estrutura fabricante/modelo/categoria;
5. Frontmatter obrigatório;
6. limite de documentos atômicos;
7. nomenclatura kebab-case;
8. como executar validações localmente;
9. como gerar/verificar índices;
10. fluxo de Pull Request.

## Regra

Não criar instruções que contradigam o comportamento efetivamente implementado por `build_indexes.py` e CI.

## Critérios de aceite

- Um novo contribuidor consegue entender como adicionar documentação.
- Um agente de IA consegue identificar `llms.txt` e a árvore de índices como pontos de entrada.
- Comandos documentados existem e funcionam.
- Templates são consistentes com o schema real.
- Não há links quebrados.

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
