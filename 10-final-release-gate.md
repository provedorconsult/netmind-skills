# TASK 10 — Release Gate e Auditoria Final

## Goal

Executar a auditoria final do repositório contra todos os requisitos verificáveis do PRD e preparar a versão candidata para lançamento, sem realizar o merge.

## Fonte de requisitos

Revisar integralmente:
- RF01–RF08;
- RNF01–RNF06;
- Fases 1–4;
- KPIs;
- critérios de aceite distribuídos nas Tasks 01–09.

## Escopo

1. Executar toda a suíte de testes.
2. Executar `build_indexes.py --check`.
3. Verificar frontmatter.
4. Verificar limite de 150 linhas.
5. Verificar kebab-case.
6. Verificar blocos de código com linguagem.
7. Verificar links internos.
8. Verificar workflows.
9. Verificar README/CONTRIBUTING/templates.
10. Verificar estrutura deprecated.
11. Verificar `llms.txt`.
12. Medir tempos do pipeline/build quando possível.
13. Produzir relatório de conformidade no PR.

## Regra de release

Se houver requisito não atendido:
- não mascarar a falha;
- não alterar o escopo silenciosamente;
- registrar exatamente o requisito, evidência e impacto;
- corrigir somente o que estiver dentro desta tarefa ou devolver para uma Task específica.

## Critérios de aceite

- Todos os requisitos verificáveis possuem status PASS, FAIL ou N/A justificado.
- Nenhuma falha conhecida fica escondida.
- CI verde.
- Árvore de documentação consistente.
- `llms.txt` e índices sincronizados.
- PR pronta para decisão do Checker.

## Condição de encerramento

O Maker deve parar após solicitar o Checker. O release só pode prosseguir depois do comentário social `approve` do Checker.

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
