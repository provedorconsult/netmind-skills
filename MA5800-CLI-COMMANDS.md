# MA5800 CLI Commands

Base: MA5800V100R018/SPH507. Os modos abaixo refletem o contexto observado quando conhecido. Onde a transcrição não prova o prompt, o modo é marcado **contexto observado** e deve ser validado com `?`.

## USER VIEW — leitura

| Comando | Finalidade | Status | Saída/erro observado | Risco |
|---|---|---|---|---|
| `display ont-lineprofile gpon all detail` | Detalhar line profiles | [CONFIRMADO] | Profiles/T-CONT/GEM | Baixo |
| `display ont-lineprofile gpon all` | Listar line profiles | [CONFIRMADO] | Inclui default/profile 100 | Baixo |
| `display ont-lineprofile gpon profile-id 0` | Consultar profile | [CONFIRMADO] | line-profile_default_0 | Baixo |
| `display ont-lineprofile gpon profile-id 1` | Consultar profile | [CONFIRMADO] | Executado com sucesso | Baixo |
| `display ont-lineprofile gpon profile-id 2` | Consultar profile | [CONFIRMADO] | Executado com sucesso | Baixo |
| `display ont-lineprofile gpon profile-id 3` | Consultar profile | [CONFIRMADO] | Executado com sucesso | Baixo |
| `display ont-srvprofile gpon all` | Listar service profiles | [CONFIRMADO] | Profile 100 observado | Baixo |
| `display dba-profile all` | Listar DBAs/IDs | [CONFIRMADO] | Usar antes de reutilizar ID | Baixo |
| `display dba-profile all detail` | Detalhar DBAs | [CONFIRMADO] | Valores e bindings | Baixo |
| `display dba-profile profile-id 100` | Consultar DBA | [CONFIRMADO] | Consulta executada | Baixo |
| `display dba-profile profile-id 101` | Consultar DBA | [CONFIRMADO] | Consulta executada | Baixo |
| `display dba-profile profile-id 102` | Consultar DBA | [CONFIRMADO] | `does not exist` em uma tentativa | Baixo |
| `display dba-profile profile-id 200` | Consultar DBA | [CONFIRMADO] | 2048/2048/2048000 | Baixo |
| `display dba-profile profile-id 201` | Consultar DBA | [CONFIRMADO] | 2048/2048/1024000; bind 1 | Baixo |
| `display ont autofind all` | Listar ONTs descobertas | [CONFIRMADO] | Nenhuma; depois uma ONT | Baixo |
| `display ont info summary ?` | Descobrir argumento | [DISCOVERY] | Caminho F/S/P | Baixo |
| `display ont info summary 0/1/0` | Estado da ONT | [CONFIRMADO] | 1 total/online; óptica | Baixo |
| `display ont info 0/1` | Forma rejeitada | [ERRO] | Rejeitado pela CLI | Baixo |
| `display service-port all` | Listar service-ports | [CONFIRMADO] | Inventário | Baixo |
| `display service-port 1000` | Estado do fluxo | [CONFIRMADO] | Admin enable/state up | Baixo |
| `display port vlan 0/1/0` | VLAN da PON | [CONFIRMADO] | 100 | Baixo |
| `display port vlan 0/8/0` | VLAN do uplink | [CONFIRMADO] | 1,10,100; native 1 | Baixo |

## SYSTEM VIEW — leitura de configuração

| Comando | Finalidade | Status | Saída observada | Risco |
|---|---|---|---|---|
| `display current-configuration \| include ont-lineprofile` | Localizar line profiles | [CONFIRMADO] | Configuração relevante | Baixo |
| `display current-configuration \| include ont-srvprofile` | Localizar service profiles | [CONFIRMADO] | Configuração relevante | Baixo |

## CONFIG — configuração global (contexto observado)

| Comando | Finalidade | Status | Saída/erro observado | Risco |
|---|---|---|---|---|
| `ont-lineprofile gpon profile-id ?` | Descobrir ID/sintaxe | [DISCOVERY] | Preservar `?` | Baixo |
| `dba-profile add profile-id ?` | Descobrir faixa/opções | [DISCOVERY] | Preservar `?` | Baixo |
| `dba-profile add profile-id 200 profile-name "TESTE" type5 fix ?` | Descobrir Fix | [DISCOVERY] | Preservar `?` | Baixo |
| `dba-profile add profile-id 101 profile-name "DBA-OMCI-2G" type5 fix 128 ?` | Descobrir próximo token | [DISCOVERY] | `assure` etc. | Baixo |
| `dba-profile add profile-id 101 profile-name "DBA-OMCI-2G" type5 fix 128 assure ?` | Descobrir Assure | [DISCOVERY] | Preservar `?` | Baixo |
| `dba-profile add profile-id 101 profile-name "DBA-OMCI-2G" type5 fix 128 assure 128 ?` | Descobrir Max | [DISCOVERY] | Preservar `?` | Baixo |
| `dba-profile add profile-id 101 profile-name "DBA-OMCI-2G" type5 fix 128 assure 128 max 2000000` | Criar DBA | [CONFIRMADO][DESTRUTIVO] | Profile 101 criado | Alto |
| `dba-profile add profile-id 102 profile-name "DBA-OMCI-2G" type5 fix 1000 assure 1000 max 2000000` | Criar DBA | [CONFIRMADO][DESTRUTIVO] | Também houve `already existed` | Alto |
| `dba-profile add profile-id 103 profile-name "DBA-OMCI-2G" type5 fix 2048 assure 2048 max 2048000` | Criar DBA | [CONFIRMADO][DESTRUTIVO] | Executado | Alto |
| `dba-profile add profile-id 200 profile-name "TESTE" type5 fix 2048 assure 2048 max 2048000` | Criar DBA | [CONFIRMADO][DESTRUTIVO] | Executado; nome final divergiu | Alto |
| `dba-profile delete profile-id 100` | Excluir DBA | [CONFIRMADO][DESTRUTIVO] | ID deixou de aparecer | Crítico |
| `dba-profile delete profile-id 101` | Excluir DBA | [CONFIRMADO][DESTRUTIVO] | ID deixou de aparecer | Crítico |
| `vlan 10 smart` | Criar VLAN gestão | [CONFIRMADO][DESTRUTIVO] | Baseline atual | Crítico |
| `vlan 100 smart` | Criar VLAN cliente | [CONFIRMADO][DESTRUTIVO] | Baseline atual | Alto |
| `vlan desc 10 description "gerencia"` | Descrever VLAN | [CONFIRMADO][DESTRUTIVO] | Baseline atual | Alto |
| `port vlan 10 0/8 0` | Associar gestão ao uplink | [CONFIRMADO][DESTRUTIVO] | Baseline atual | Crítico |
| `port vlan 100 0/8 0` | Associar cliente ao uplink | [CONFIRMADO][DESTRUTIVO] | Baseline atual | Alto |
| `service-port 1000 vlan 100 gpon 0/1/0 ont 0 gemport 1 multi-service user-vlan 100 tag-transform translate` | Criar fluxo | [CONFIRMADO][DESTRUTIVO] | Criado; state up | Alto |

## GPON INTERFACE — `interface gpon 0/1`

| Comando | Finalidade | Status | Saída observada | Risco |
|---|---|---|---|---|
| `port 0 ont-auto-find enable` | Habilitar autofind | [CONFIRMADO][DESTRUTIVO] | Uma ONT encontrada | Médio |
| `ont add ?` | Descobrir PortID | [DISCOVERY] | `portid<U><0,15>` | Baixo |
| `ont add 0 ?` | Descobrir autenticação | [DISCOVERY] | loid/ontid/password/protect/sn... | Baixo |
| `ont add 0 0 sn-auth ?` | Descobrir SN | [DISCOVERY] | `sn-value` | Baixo |
| `ont add 0 0 sn-auth 4857544354ABCFB2 ?` | Descobrir protocolo | [DISCOVERY] | omci/password-auth/snmp | Baixo |
| `ont add 0 0 sn-auth 4857544354ABCFB2 omci ?` | Descobrir profiles/desc | [DISCOVERY] | desc, line/srv profile, ont-type | Baixo |
| `ont add 0 0 sn-auth 4857544354ABCFB2 omci ont-lineprofile-id 100 ont-srvprofile-id 100 desc "EG8145X6-10-TESTE"` | Adicionar ONT | [CONFIRMADO][DESTRUTIVO] | 1 permitida, 1 sucesso | Alto |

## LINE PROFILE — profile 100

| Comando | Finalidade | Status | Saída observada | Risco |
|---|---|---|---|---|
| `ont-lineprofile gpon profile-id 100 profile-name "LINE-OMCI-VLAN-100"` | Criar/entrar no profile | [CONFIRMADO][DESTRUTIVO] | Profile 100 | Alto |
| `tcont 0 ?` | Descobrir T-CONT | [DISCOVERY] | Preservar `?` | Baixo |
| `tcont 0 dba-profile-id 200` | Associar DBA | [CONFIRMADO][DESTRUTIVO] | Associação inicial | Alto |
| `tcont 0 dba-profile-id 201` | Trocar associação | [CONFIRMADO][DESTRUTIVO] | Estado final | Alto |

Nenhum comando de criação GEM foi fornecido como confirmado. O GEM 1 foi observado no profile; qualquer sintaxe de GEM deve ser redescoberta.

## SERVICE PROFILE — profile 100

| Comando | Finalidade | Status | Saída observada | Risco |
|---|---|---|---|---|
| `ont-srvprofile gpon profile-id 100 profile-name "SRV-OMCI-VLAN-100"` | Criar/entrar no profile | [CONFIRMADO][DESTRUTIVO] | Profile 100 | Alto |
| `ont-port ?` | Descobrir grupo | [DISCOVERY] | Preservar `?` | Baixo |
| `ont-port eth ?` | Descobrir ETH | [DISCOVERY] | Preservar `?` | Baixo |
| `port ?` | Descobrir port | [DISCOVERY] | Preservar `?` | Baixo |
| `port vlan ?` | Descobrir VLAN | [DISCOVERY] | Preservar `?` | Baixo |
| `port vlan eth ?` | Descobrir seleção ETH | [DISCOVERY] | Preservar `?` | Baixo |
| `port vlan eth 1-4 ?` | Descobrir argumento | [DISCOVERY] | Exigiu `100` | Baixo |
| `port vlan eth 1-4 100 ?` | Descobrir opções | [DISCOVERY] | `<cr>`, TLS, priority, prival | Baixo |
| `port vlan eth 1 translation 100 user-vlan 100` | Mapear ETH1 | [CONFIRMADO][DESTRUTIVO] | Aplicado | Alto |
| `port vlan eth 2 translation 100 user-vlan 100` | Mapear ETH2 | [CONFIRMADO][DESTRUTIVO] | Aplicado | Alto |
| `port vlan eth 3 translation 100 user-vlan 100` | Mapear ETH3 | [CONFIRMADO][DESTRUTIVO] | Aplicado | Alto |
| `port vlan eth 4 translation 100 user-vlan 100` | Mapear ETH4 | [CONFIRMADO][DESTRUTIVO] | Aplicado | Alto |
| `port vlan eth 1-4 vlanid100` | Forma inválida | [ERRO] | Rejeitado | Nenhum se rejeitado |

## Regra de execução

Este catálogo documenta evidência; não é um script. Mesmo `[CONFIRMADO]` precisa de validação de versão, modo, alvo, dependências, impacto e autorização. Comandos `[DESTRUTIVO]` nunca são executados automaticamente.

