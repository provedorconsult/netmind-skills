# Demanda 21 — ZTE C600 (C610/C650) / TP-Link ONT/ONU — Portal Network

## Estado

`PARA ANÁLISE DO CHECKER`

## Objetivo

Acessar a OLT do Portal Network pertencente à família ZTE C600, abrangendo os modelos C610/C650 conforme a equivalência já estabelecida no projeto, em modo estritamente `READ/DISCOVERY`, para identificar se existem ONTs/ONUs TP-Link provisionadas e determinar o padrão operacional utilizado para esse fabricante.

A evidência deverá servir de base para definir padrões reutilizáveis e, somente após validação do Checker, criar ou atualizar Skills específicas da família ZTE C600.

## Alvo

- Provedor: Portal Network
- Família: ZTE C600
- Modelos de referência: C610 / C650
- Alvo autorizado: equipamento Portal Network já utilizado no G16
- Acesso: arquivo `.env-portalnetwork` na raiz do projeto
- Variáveis: prefixo `OLT_ZTE_C610`
- Operação: exclusivamente `READ/DISCOVERY`

## Critério de identificação TP-Link

Considerar como candidato a TP-Link qualquer ONT/ONU cujo GPON Serial Number tenha prefixo inicial `TPLG`.

O prefixo `TPLG` é um critério de identificação operacional para esta coleta, não uma prova isolada de modelo/chipset. Sempre que possível, correlacionar o SN com fabricante, modelo, OMCI, estado e configuração observada.

## Perguntas que a coleta deve responder

1. Existe pelo menos uma ONT/ONU com GPON SN iniciando em `TPLG`?
2. Quantas foram encontradas?
3. Quais modelos/identificadores são apresentados pela OLT para essas ONTs/ONUs?
4. Em quais PONs estão instaladas?
5. Qual estado operacional apresentam?
6. Como são identificadas/autorizadas na C600?
7. Qual DBA profile é utilizado?
8. Qual line profile é utilizado?
9. Qual service profile/template é utilizado?
10. Qual T-CONT/GEM é utilizado?
11. Como o service-port é criado/associado?
12. Qual VLAN de serviço é utilizada?
13. Existem diferenças de provisionamento em relação às demais ONTs?
14. O padrão depende de OMCI, perfil específico, template, modelo ou firmware?
15. Existem comandos/configurações específicos para TP-Link?
16. Há limitações, incompatibilidades ou erros relacionados a essas ONTs?
17. Qual sequência de provisionamento pode ser reconstruída a partir da configuração existente sem executar nenhum comando de escrita?

## Evidências mínimas

Coletar, quando disponível:

- fingerprint da OLT e versão de software;
- inventário das ONTs/ONUs candidatas;
- GPON SN sanitizado;
- PON/interface;
- estado da ONT;
- modelo/vendor exibido pela OLT;
- ONU/ONT ID;
- DBA profile;
- line profile;
- service profile;
- T-CONT;
- GEM;
- service-port;
- VLAN/service mapping;
- OMCI-related configuration;
- templates ou comandos associados;
- erros/alarms relevantes;
- evidência de comandos de provisionamento existentes na configuração, sem executá-los.

## Regras de segurança

O Maker deve operar somente em `READ/DISCOVERY`.

É proibido executar:

- criação;
- alteração;
- remoção;
- `configure` com alteração efetiva;
- `write`;
- `save`;
- `commit`;
- reboot/reload/reset;
- qualquer operação de alto impacto.

Em caso de dúvida sobre o efeito de um comando, não executar e encaminhar ao Checker.

## Segredos e privacidade

- `.env-portalnetwork` não pode ser versionado.
- Credenciais, tokens, chaves e comunidades SNMP não podem aparecer na evidência versionada.
- Identificadores de clientes devem ser sanitizados quando não forem necessários para demonstrar o padrão técnico.
- O GPON SN pode ser preservado apenas quando necessário para demonstrar o critério `TPLG`; caso contrário, utilizar forma sanitizada/pseudonimizada mantendo o prefixo técnico relevante.
- Evidência bruta deve permanecer fora do Git.

## Classificação da evidência

Cada descoberta deve ser classificada como:

- `CONFIRMADO`
- `DISCOVERY`
- `INFERIDO`
- `ERRO`
- `VERSÃO DIFERENTE`

Com classe operacional:

- `READ`
- `DISCOVERY`
- `TEST`
- `WRITE`
- `PERSIST`
- `HIGH-IMPACT`

Não transformar inferência em padrão confirmado.

## Definição de padrão para Skill

O Checker deverá separar explicitamente:

### Padrão confirmado

Somente comportamento observado na C600/C610/C650 do Portal Network e sustentado por evidência direta.

### Padrão reutilizável

Comportamento que pode ser generalizado para a família ZTE C600 sem depender de um cliente, PON ou instância específica.

### Padrão específico TP-Link

Comportamento observado somente em ONTs/ONUs identificadas pelo critério `TPLG` ou por evidência adicional de fabricante/modelo.

### Skill candidata

Somente criar Skill quando houver evidência suficiente para definir:

- fingerprint/modelo/versão suportados;
- pré-condições;
- comandos READ/DISCOVERY;
- identificação da ONT;
- parâmetros de provisionamento;
- dependências entre DBA/line/service profile/T-CONT/GEM/service-port/VLAN;
- validações pós-provisionamento;
- erros conhecidos;
- limites de aplicabilidade;
- operações WRITE claramente separadas e explicitamente não executadas nesta coleta.

Não criar uma Skill de escrita apenas porque comandos de provisionamento foram encontrados na configuração. A existência do comando deve ser registrada como evidência; autorização de execução pertence a uma etapa posterior.

## Resultado esperado

Ao final da coleta, o Maker deverá entregar:

1. evidência sanitizada das ONTs/ONUs TP-Link encontradas ou evidência de ausência;
2. padrão de provisionamento reconstruído;
3. diferenças em relação ao padrão geral da C600;
4. comandos/configurações relevantes identificados, classificados sem execução;
5. proposta de estrutura para Skill;
6. lacunas e dúvidas para o Checker;
7. PR exclusiva desta demanda.

## Critérios de aceite

- acesso à OLT confirmado ou bloqueio precisamente documentado;
- modelo/versão confirmados;
- presença ou ausência de ONT/ONU `TPLG` comprovada;
- pelo menos uma evidência correlacionando SN, PON, ONT ID, estado e padrão de serviço quando houver candidato;
- padrão de provisionamento reconstruído a partir de evidência real;
- distinção entre padrão geral C600 e comportamento específico TP-Link;
- nenhuma operação WRITE/PERSIST/HIGH-IMPACT executada;
- nenhum segredo versionado;
- evidência sanitizada;
- proposta de Skill baseada em evidência, sem invenção;
- validações do repositório verdes;
- PR exclusiva e aguardando revisão do Checker.

## Próxima etapa

Após a coleta, o Checker deverá revisar o HEAD exato da PR, decidir quais padrões são suficientemente comprovados e definir a estrutura final das Skills antes de qualquer merge.
