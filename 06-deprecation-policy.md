# TASK 06 — Política e Estrutura de Depreciação

## Goal

Implementar a política de depreciação definida no PRD para equipamentos fora de linha, sem excluir documentação histórica.

## Fonte de requisitos

Basear-se exclusivamente em:
- RF08;
- seção 4;
- Fase 3.

## Escopo

1. Definir a estrutura `docs/_deprecated/<fabricante>/<modelo>/`.
2. Definir como documentos deprecated aparecem ou não nos índices, de forma consistente com a navegação AI-Native.
3. Adicionar `status: deprecated` ao Frontmatter dos documentos efetivamente deprecados.
4. Migrar apenas equipamentos que o repositório já identifique claramente como legados/descontinuados.
5. Não classificar um equipamento como deprecated apenas por inferência.
6. Garantir que a movimentação preserve links ou os atualize corretamente.

## Critérios de aceite

- Nenhum documento legado é apagado.
- Equipamentos claramente deprecated ficam sob `docs/_deprecated/`.
- Frontmatter contém `status: deprecated`.
- Links internos são corrigidos.
- O comportamento dos índices é determinístico e documentado.
- `build_indexes.py --check` permanece funcional.

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
