# G15 — README institucional AI-Native em Português Brasil

## Predecessor

`G14`

## Objetivo

Transformar o `README.md` na porta de entrada institucional, técnica e operacional do NetMind Skills, apresentando o projeto como um **Network Equipment Skill Registry AI-Native** para operação segura, reutilizável e multi-fabricante de equipamentos de rede.

O README deve orientar rapidamente sobre o que o projeto é, para que serve, como está organizado, como um agente deve navegar e quais são os limites de segurança.

## Escopo

Reestruturar o `README.md` em Português Brasil para cobrir, de forma concisa e factual:

1. título e posicionamento institucional;
2. missão e finalidade operacional;
3. o que o projeto é e o que não é;
4. modelo conceitual `Target → Device Fingerprint → Equipment Registry → Compatibility Registry → Capability Registry → Skill Router → Skill/Command/Procedure/Error → Validation/Evidence`;
5. arquitetura atual e papéis de `docs/`, `registries/`, `skills/`, `.harness/`, `scripts/` e `tests/`;
6. registries atuais, em evolução e planejados, sem apresentar roadmap como implementação existente;
7. navegação AI-Native e uso de `llms.txt`/`INDEX.md` conforme o estado real do repositório;
8. cobertura atual de Huawei MA5800-X7 e Cisco ASR1001-X;
9. separação entre evidência técnica e classe operacional;
10. ordem de autoridade e regra de não promover inferência a comando confirmado;
11. acesso a equipamentos e separação entre sessão e mudança de configuração;
12. segurança operacional e limites de dados armazenados;
13. fluxo Maker/Checker e regra de que CI verde não autoriza merge;
14. estado atual e roadmap, distinguindo claramente implementado, em evolução e planejado;
15. exemplo conceitual pequeno e sanitizado de uso por agente;
16. links para documentação complementar e Quick Start.

## Regras editoriais

- O idioma institucional é Português Brasil.
- Nomes técnicos, comandos, caminhos, identificadores, estados do Harness e nomes próprios de tecnologias podem permanecer no idioma original.
- Huawei e Cisco devem aparecer como cobertura atual, não como identidade do projeto.
- Não inventar registries, capabilities, Skill Router ou outros componentes ainda não implementados.
- Não apresentar roadmap como funcionalidade existente.
- Não apagar conhecimento técnico existente sem preservar seu acesso por documentação específica.
- O README principal não deve funcionar como manual completo de um fabricante.
- Não armazenar no README dados reais de clientes, credenciais, `.env`, backups reais, topologia real ou outros dados operacionais sensíveis.

## Evidência e segurança

Separar visualmente evidência técnica de classe operacional.

Evidência técnica:

- `CONFIRMADO`
- `DISCOVERY`
- `INFERIDO`
- `ERRO`
- `VERSÃO DIFERENTE`

Classe operacional:

- `READ`
- `DISCOVERY`
- `TEST`
- `WRITE`
- `PERSIST`
- `HIGH-IMPACT`

Ordem de autoridade:

1. CLI real do equipamento;
2. evidência do mesmo modelo/versão;
3. discovery no alvo;
4. documentação oficial compatível;
5. evidência de outra versão;
6. inferência.

Regra obrigatória: **nunca promover inferência a comando confirmado**.

## Governança

O README deve representar o fluxo:

`Goal → Maker → PR → CI → Checker → approve → merge`

A CI verde não autoriza merge. O comentário social literal `approve` autoriza somente o HEAD revisado pelo Checker.

## Fora de escopo

- alterar Skills;
- alterar registries;
- implementar Skill Router;
- implementar novos registries;
- alterar o Harness além da promoção/estado necessária para este Goal;
- executar G16 ou qualquer Goal posterior;
- migrar integralmente a documentação de equipamentos para novos diretórios;
- transformar o README em manual operacional de Huawei, Cisco ou outro fabricante.

## Critérios de aceite

- O README identifica o projeto como infraestrutura de conhecimento operacional AI-Native multi-fabricante.
- Huawei e Cisco aparecem como cobertura atual, não como identidade principal.
- O leitor consegue distinguir implementação existente de roadmap.
- O modelo de navegação para agentes está explícito.
- Os limites de segurança e de Source of Truth estão explícitos.
- Evidência técnica e classe operacional estão separadas.
- O fluxo Maker/Checker e a regra do `approve` estão claros.
- O README aponta para documentação específica sem duplicar integralmente os manuais dos equipamentos.
- Todos os links e referências utilizados existem no repositório.

## Condição de conclusão

O Maker deverá abrir uma PR exclusiva de G15, executar as validações do repositório e solicitar revisão do Checker. A integração depende exclusivamente de um comentário social literal `approve` no HEAD revisado.
