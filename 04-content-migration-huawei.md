# TASK 04 — Migração Inicial de Conteúdo Huawei

## Goal

Migrar uma primeira fatia controlada do conteúdo Huawei existente para a arquitetura modular, validando na prática o modelo de documentação atômica antes de ampliar a migração para todos os fabricantes.

## Fonte de requisitos

Basear-se em:
- RF02;
- RF03;
- RF04;
- RF08;
- RNF01;
- RNF03;
- RNF04;
- Fase 3.

## Escopo

1. Mapear o conteúdo Huawei existente.
2. Identificar documentos monolíticos que possam ser divididos sem perda de informação.
3. Migrar somente uma amostra representativa.
4. Organizar por fabricante/modelo e categoria.
5. Inserir YAML Frontmatter em cada documento migrado.
6. Manter cada documento abaixo de 150 linhas quando tecnicamente possível.
7. Preservar comandos e sintaxes existentes.
8. Não inventar comandos, parâmetros ou resultados.
9. Usar blocos de código com linguagem apropriada.
10. Atualizar índices através do `build_indexes.py --build`.

## Critério de seleção

Priorizar uma amostra que contenha pelo menos:
- um procedimento `cli`;
- um `config`;
- um `diag`;
- um `mon` ou equivalente existente;
- um procedimento de `update`, se houver conteúdo correspondente.

Se algum desses conteúdos não existir no repositório, registrar a ausência em vez de fabricar documentação.

## Critérios de aceite

- Conteúdo original relevante está preservado.
- Documentos migrados são atômicos.
- Frontmatter válido em 100% da amostra.
- Nomes seguem kebab-case.
- Índices apontam corretamente para os documentos.
- Não há links internos quebrados introduzidos pela migração.
- O Checker consegue comparar origem e destino da amostra.

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
