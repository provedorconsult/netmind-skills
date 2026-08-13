# Auditoria de valores concretos

Data: 12-08-2026

## Escopo

Revisão manual dos 11 arquivos sinalizados na `main` por uma varredura conservadora de endereços IPv4 privados e identificadores hexadecimais longos. A sinalização automática não prova origem ou sensibilidade.

## Resultado

| Arquivo | Classificação manual | Ação |
|---|---|---|
| `README.md` | Continha dados concretos de uma sessão de laboratório e falsos positivos em URLs oficiais | Parametrizar valores operacionais; preservar URLs |
| `MA5800-CLI-COMMANDS.md` | Continha identificador concreto de ONT | Parametrizar |
| `skills/01-ma5800-baseline/SKILL.md` | Continha endereçamento concreto | Parametrizar |
| `skills/02-ma5800-cli-discovery/SKILL.md` | Continha identificador concreto de ONT | Parametrizar |
| `skills/06-ma5800-ont-autofind/SKILL.md` | Continha identificadores concretos de ONT | Parametrizar |
| `skills/07-ma5800-ont-provisioning/SKILL.md` | Continha identificador concreto de ONT | Parametrizar |
| `skills/08-ma5800-ont-status/SKILL.md` | Continha identificador concreto de ONT | Parametrizar |
| `skills/12-ma5800-uplink/SKILL.md` | Continha gateway concreto | Parametrizar |
| `skills/cisco-asr1001x/28-ma5800-access/SKILL.md` | Continha usuário e endereço concretos | Parametrizar |
| `skills/cisco-asr1001x/CISCO-ASR1001X-COMMANDS.md` | Continha usuário e endereço concretos | Parametrizar |
| `skills/cisco-asr1001x/README.md` | Continha usuário e endereço concretos | Parametrizar |

## Limites

- Não foi inferida relação entre os valores e qualquer rede de cliente.
- URLs oficiais com identificadores numéricos foram preservadas; eram falsos positivos do critério hexadecimal.
- IDs, VLANs, slots, portas e nomes de perfis existentes fora do critério original exigem auditoria semântica separada antes de serem classificados como exemplos reutilizáveis ou dados específicos.
- A parametrização não promove comandos a `[CONFIRMADO]` para outros equipamentos ou releases.
