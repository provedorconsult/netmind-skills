# MA5800 Error Database

Base: MA5800V100R018/SPH507. Preservar mensagens literalmente.

| Erro literal | Diagnóstico observado | Ação segura |
|---|---|---|
| `Failure: OMCI must not use type4 DBA-profile` | OMCI T-CONT não aceita Type 4 neste cenário. | Usar DBA compatível; Type 5 foi testado. |
| `Failure: The bandwidth of OMCI can't be less than 1Mbps` | OMCI exige ao menos 1 Mbps neste contexto. | Usar ≥1024 kbps; baseline conservador testado 2048/2048. |
| `Failure: The DBA-profile has already existed` | Pode haver estado/ID inconsistente. | `display dba-profile all`; não assumir objeto funcional. |
| `Failure: The DBA-profile does not exist` | ID ou contexto não consultável. | Confirmar lista, ID e contexto. |
| `Failure: The line profile does not exist` | Profile/ID/contexto não encontrado. | `display ont-lineprofile gpon all`. |
| `Failure: No service virtual port can be operated` | Nenhum service-port corresponde à operação. | `display service-port all`. |
| `Failure: The ONT does not exist` | F/S/P ou ONT-ID incorreto/ausente. | `display ont info summary <F/S/P>`. |
| `Failure: The maximum bandwidth of the referenced DBA profile exceeds the limitation` | DBA Max/profile/T-CONT incompatível com capacidade ou ONT type. | Investigar DBA Max, ONT, line profile, T-CONT, GEM e referências; não reduzir às cegas. |
| `Failure: The automatically found ONTs do not exist` | Nenhuma ONT está no resultado de autofind. | Conferir enable, PON, ODN, energia e óptica. |

## Inconsistência confirmada do ID 102

`dba-profile add profile-id 102 ...` retornou `Failure: The DBA-profile has already existed`, mas `display dba-profile profile-id 102` retornou `Failure: The DBA-profile does not exist`. Logo, a mensagem de criação não substitui a listagem e consulta.

## Regra para novos erros

Registrar release, patch, modo, comando literal, cursor `^` se houver, retorno literal, estado anterior e leitura seguinte. Classificar o comando como `[ERRO]`; só criar ação corretiva depois de evidência.

