# TASK 02 — Schema e Validação de YAML Frontmatter

## Goal

Implementar a validação automatizada do YAML Frontmatter obrigatório dos arquivos Markdown em `docs/`, preparando uma base confiável para indexação por agentes de IA.

## Fonte de requisitos

Basear-se no PRD:
- RF04 — Padronização de Metadados;
- RNF05 — compatibilidade com parsers Python/PyYAML;
- seção 7.1, etapas 2 e 3.

## Escopo

1. Definir no código o schema obrigatório:
   - `fabricante`
   - `modelo`
   - `categoria`
   - `topicos`
   - `descricao`
   - `versao_firmware_testada`
   - `ultima_atualizacao`
2. Validar presença do frontmatter.
3. Validar YAML com `pyyaml`.
4. Validar tipos e valores necessários sem impor restrições não previstas no PRD.
5. Produzir mensagens de erro úteis contendo caminho do arquivo e campo inválido.
6. Permitir execução automatizada pelo futuro `build_indexes.py`.
7. Criar testes automatizados para casos válidos e inválidos.

## Decisão importante

O PRD não define um schema JSON completo nem enumera todos os valores permitidos para `categoria`. Não criar restrições adicionais que possam bloquear documentação legítima.

## Critérios de aceite

- Arquivos válidos passam.
- Frontmatter ausente falha.
- YAML inválido falha.
- Campo obrigatório ausente falha.
- Tipo estrutural incompatível falha quando isso for necessário para o processamento.
- Mensagens de erro permitem localizar rapidamente a causa.
- Testes cobrem pelo menos sucesso, ausência de frontmatter e YAML inválido.
- Testes executam de forma determinística.

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
