---
name: 22-zte-c600-ont-correlation
description: Correlacionar, somente em READ/DISCOVERY, GPON SN, ONU, T-CONT, GEM, vport, service-port e VLAN em ZTE C600/C650. Usar ao investigar ONUs por prefixo de serial, inclusive TPLG, sem pressupor fabricante ou modelo.
---

# Correlação de ONUs ZTE C600/C650

## Escopo confirmado

Usar esta Skill somente depois de confirmar `ZXA10 C650` e `ZTE ZXA10 Software
V1.1.2`, o único contexto de CLI observado. Tratar C600/C650 como escopo de
navegação, não como compatibilidade comprovada entre modelos ou releases.

Esta Skill é exclusivamente `READ` e `DISCOVERY`. Ela não autoriza
provisionamento, criação de ONU/perfil/VLAN/GEM/T-CONT/service-port, `configure`,
`commit`, `write`, `save`, reload ou reset.

## Fluxo de correlação

1. Confirmar o fingerprint com `show software`.
2. Listar estados com `show gpon onu state` e obter referências `gpon_olt-`
   confirmadas pela própria CLI.
3. Consultar `show gpon onu baseinfo <gpon_olt-confirmada>` para localizar o
   prefixo solicitado no GPON SN. Preservar seriais completos somente fora do
   conteúdo versionado.
4. Para cada referência autorizada, correlacionar estado e atributos com
   `show gpon onu detail-info <gpon_onu-confirmada>`.
5. Consultar, para a mesma PON confirmada:

   ```cli
   show gpon onu tcont <gpon_olt-confirmada>
   show gpon onu gemport <gpon_olt-confirmada>
   show gpon onu vport <gpon_olt-confirmada>
   ```

6. Correlacionar o objeto de serviço com:

   ```cli
   show service-port interface <gpon_onu-confirmada>
   ```

7. Quando a interface de transporte já estiver confirmada pelo Source of Truth
   ou pela CLI, consultar a associação de VLAN com:

   ```cli
   show vlan port <xgei-confirmada>
   ```

Usar `show ?` como `DISCOVERY` quando uma referência ou sintaxe não for aceita.
Não adivinhar PON, ONU, vport ou interface.

## Prefixo TPLG

`TPLG` é um **fingerprint de descoberta de GPON SN**, não uma confirmação de
fabricante, modelo ou chipset. Registrar o resultado como:

```text
GPON SN prefix: TPLG
Fabricante/modelo: desconhecido; não confirmado pela coleta
```

Não atribuir fabricante à ONU, nem promover esse prefixo a uma regra de
compatibilidade, sem identificação explícita fornecida pela OLT.

## Interpretação

- Tratar T-CONT, GEM, vport, service-port e VLAN como objetos distintos e
  correlacionar somente referências do mesmo contexto PON/ONU.
- Separar estado administrativo de `working`, `OffLine`, `LOS` e `DyingGasp`.
- Registrar valores de DBA, OMCI, criptografia OMCC, line profile e service
  profile somente quando a resposta realmente expuser esses campos.
- Manter `CONFIRMADO` para consultas aceitas e resultados observados;
  `DISCOVERY` para ajuda e prefixos; `ERRO` para resposta literal rejeitada;
  e `INFERIDO` para uma sequência lógica que não foi vista como comando.

## Limitações e sanitização

- Não assumir que um padrão de T-CONT, GEM, VLAN, OMCI ou service-port é
  universal para C600/C650, outro release ou outro ambiente.
- Não versionar serial completo, LOID, senha, IP, descrição de circuito,
  identificador de assinante, contagem de ONUs ou configuração bruta.
- Não converter relações observadas em comandos de provisionamento ou Skill de
  escrita. A sequência de provisionamento só pode ser descrita como inferência
  até haver evidência e autorização específicas.
