# TASK 09 — Validação Ponta a Ponta AI-Native

## Goal

Validar o fluxo completo de navegação AI-Native definido no PRD, desde o `llms.txt` até um documento atômico específico.

## Fonte de requisitos

Basear-se em:
- objetivos estratégicos;
- persona Agente de IA;
- RF01;
- RF02;
- RF03;
- KPI de redução de tokens;
- Fase 4.

## Escopo

Criar um teste ou harness reproduzível que demonstre:
1. entrada pelo `llms.txt`;
2. seleção de fabricante;
3. seleção de modelo;
4. seleção de categoria;
5. seleção do documento atômico;
6. obtenção do conteúdo técnico final.

## Métricas

Medir, quando os dados do repositório permitirem:
- quantidade de arquivos consultados;
- linhas lidas;
- tamanho aproximado do contexto;
- comparação entre fluxo monolítico e fluxo modular.

Não afirmar redução de 75% sem medição. Se não houver baseline histórico disponível, registrar a limitação e criar somente a instrumentação necessária.

## Critérios de aceite

- Fluxo reproduzível.
- Caminhos usados são reais.
- Índices e `llms.txt` são suficientes para encontrar o documento escolhido.
- Resultado pode ser auditado pelo Checker.
- Métricas e limitações estão registradas.

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
