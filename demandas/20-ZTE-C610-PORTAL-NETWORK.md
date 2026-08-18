# Demanda — Coleta operacional ZTE C610 — Portal Network

**Prioridade sugerida:** P1

**Status:** PARA ANÁLISE DO CHECKER

**Natureza:** Demanda de coleta de evidência e incorporação de equipamento. Não executar diretamente pelo Maker.

## Contexto

O provedor Portal Network possui uma OLT ZTE C610 que deve ser incorporada ao `netmind-skills` seguindo os padrões consolidados nos equipamentos já tratados no projeto.

A raiz do projeto deverá disponibilizar o arquivo local `.env-portalnetwork`, contendo os dados de acesso à OLT. Todas as variáveis de acesso devem utilizar o prefixo `OLT_ZTE_C610`.

O arquivo `.env-portalnetwork` é exclusivamente local e não deve ser versionado, publicado ou reproduzido em evidências, documentação ou Skills.

## Objetivo

Coletar, em modo estritamente somente leitura, os dados reais da OLT ZTE C610 do Portal Network para identificar:

- identidade, modelo, hardware e versão de software/firmware;
- chassis, placas, slots, interfaces e estado operacional;
- uplinks e interfaces de gerenciamento;
- VLANs, interfaces L3 e demais elementos de transporte relevantes;
- estrutura GPON e portas PON disponíveis;
- perfis e parâmetros DBA;
- line profiles / perfis de linha;
- service profiles / perfis de serviço;
- perfis ou templates utilizados no provisionamento de ONTs;
- service-port, VLAN, GEM, T-CONT e demais associações aplicáveis ao modelo;
- ONTs atualmente provisionadas, preservando identificadores técnicos necessários para reconhecer o padrão sem expor dados desnecessários de clientes;
- padrões de ativação, configuração e provisionamento utilizados pelo provedor;
- comandos e sequência operacional efetivamente utilizados para provisionamento;
- padrões de troubleshooting, consulta e validação identificados na configuração real;
- particularidades da CLI ZTE C610 relevantes para futuras Skills.

## Regra operacional

O Maker deve operar inicialmente **somente em leitura**.

É proibido executar comandos de configuração, alteração, criação, remoção, reboot, reset ou qualquer outra operação que possa modificar o estado da OLT.

O Maker deve primeiro localizar e utilizar o `.env-portalnetwork` para obter os dados de acesso, sem solicitar que credenciais sejam copiadas para o chat ou para arquivos versionados.

Se o acesso não for possível, o Maker deve reportar exatamente o bloqueio e não improvisar credenciais, endereços ou comandos de escrita.

## Coleta mínima esperada

O Maker deve coletar evidências suficientes para permitir ao Checker reconstruir o padrão operacional da C610, incluindo, quando suportado pelo equipamento:

1. identificação do equipamento e versão;
2. inventário de hardware e interfaces;
3. configuração de gerenciamento;
4. VLANs e transporte;
5. uplinks;
6. PON/GPON;
7. DBA profiles;
8. line profiles;
9. service profiles;
10. templates de ONT;
11. service-port/GEM/T-CONT e associações de serviço;
12. ONTs provisionadas e seus padrões;
13. comandos de consulta utilizados;
14. comandos de provisionamento identificados na configuração existente, sem executá-los;
15. evidências de validação do estado atual.

A lista é orientativa: o Checker pode ampliar ou restringir a coleta conforme os dados encontrados na OLT.

## Tratamento de evidências

As evidências devem preservar a fidelidade técnica necessária para futura implementação das Skills, mas devem ser sanitizadas antes de qualquer versionamento.

Não versionar:

- senhas;
- tokens;
- secrets;
- chaves privadas;
- credenciais SNMP;
- conteúdo do `.env-portalnetwork`;
- dados pessoais ou identificadores de clientes que não sejam necessários para demonstrar o padrão técnico.

Valores técnicos necessários para reproduzir o comportamento da plataforma podem ser preservados quando não representarem segredo ou dado pessoal, conforme decisão do Checker.

## Incorporação ao netmind-skills

Após a coleta, o Checker deve avaliar como os dados da C610 devem ser incorporados à estrutura do projeto, seguindo os padrões consolidados nos equipamentos existentes.

A incorporação deve considerar, conforme aplicável:

- `equipment-registry`;
- `compatibility-registry`;
- `capability-registry`;
- `device fingerprint`;
- `command registry`;
- `error registry`;
- `procedure/evidence registries`;
- documentação técnica;
- Skills específicas do fabricante/modelo/versão;
- harness e validações correspondentes.

Não criar uma Skill definitiva apenas com base em documentação genérica do fabricante quando houver evidência operacional real disponível. A configuração real do Portal Network deve ser tratada como fonte primária para os padrões específicos do provedor, mantendo separação entre evidência bruta, evidência sanitizada e conhecimento operacional consolidado.

## Saída esperada do Maker

O Maker deve devolver ao Checker:

- resumo do acesso realizado;
- fingerprint do equipamento;
- versão de software/firmware;
- inventário de hardware;
- dados de gerenciamento e transporte;
- estrutura GPON/PON;
- perfis encontrados;
- padrões de provisionamento observados;
- comandos de consulta utilizados;
- evidências brutas coletadas em local apropriado;
- relação de dados que exigem sanitização;
- lacunas ou informações não disponíveis;
- nenhum comando de escrita executado.

O Maker não deve decidir sozinho quais comandos de alteração serão utilizados e não deve aplicar qualquer mudança na OLT.

## Saída esperada do Checker

O Checker deve revisar a coleta e devolver uma destas decisões:

- `ACCEPT` — evidência suficiente; iniciar incorporação da ZTE C610 ao `netmind-skills`;
- `REWORK` — coleta incompleta ou evidência insuficiente;
- `MERGE_WITH` — combinar com demanda existente relacionada ao mesmo equipamento;
- `DEFER` — adiar a incorporação;
- `REJECT` — não incorporar.

Se `ACCEPT`, o Checker deve definir o Goal formal, o escopo de incorporação e um prompt conciso e direto de execução para o Maker, conforme o padrão consolidado do projeto.

## Critério de conclusão

A demanda somente será considerada concluída quando houver:

1. coleta real da ZTE C610 do Portal Network;
2. evidências suficientes para identificar o padrão de configuração e provisionamento;
3. sanitização concluída;
4. mapeamento para a estrutura de `netmind-skills` aprovado pelo Checker;
5. alterações versionadas com CI e harness válidos;
6. nenhuma credencial ou segredo do Portal Network versionado.
