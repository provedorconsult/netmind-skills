# G19 — Reconciliação da colisão de design do Merge Gate e registro de G18

## Predecessor

`G17`

## Contexto

PRs #27, #33 e #36 alteravam de modo incompatível o contrato de aprovação do
Checker para o HEAD revisado. A PR #27 vinculava o veredito ao `headRefOid` e
ao tempo do commit; a PR #33 exigia `approvedHead: <SHA>` no corpo do
comentário; e a PR #36 separava Maker e Checker, mas sobre o contrato v1.

G18 também tinha uma PR aberta (#35) sem registro no catálogo formal. G10
permanece `BLOCKED`: seu caminho legado foi superseded na reconciliação G13 e
não existe promoção de sucessor confirmada no GitHub.

## Objetivo

Produzir um único contrato canônico que vincule a aprovação ao HEAD revisado,
preserve a separação de autoridade Maker/Checker e registre G18 formalmente.

## Decisão canônica

O contrato adota `headRefOid` atual mais veredito cronológico literal:

- a PR deve estar aberta, não ser Draft e ter estado de merge `CLEAN`;
- o `headRefOid` atual deve estar disponível na evidência GitHub;
- a CI consultada deve estar verde para a PR atual;
- o último veredito válido do Checker deve ser o comentário inteiro, exato e
  sensível a maiúsculas/minúsculas `approve`; o mesmo Checker deve ter um
  review nativo `APPROVED` cujo commit OID seja exatamente o `headRefOid`
  atual, e o comentário não pode preceder esse review;
- `request-changes` ou `blocked` posterior invalida autorização anterior.

O formato multi-linha `approve\napprovedHead: <SHA>` da PR #33 não é adotado:
ele viola o requisito de que todo o comentário do Checker seja apenas um dos
vereditos previstos em `checker.json`.

O Maker é o único executor de merge, somente após nova consulta GitHub gerar
`MERGE_AUTHORIZED`. O Checker nunca executa merge, não pode auto-merge e não
pode burlar o gate. O Maker não pode se autoaprovar nem mergear sem autorização.

## Escopo

- Consolidar `merge-policy.json`, `merge-gate.json`, template de revisão,
  scripts de gate/validação/teste e fixtures em uma mudança coerente.
- Reaproveitar o vínculo de HEAD e as fixtures da PR #27.
- Reaproveitar a separação de papéis da PR #36.
- Registrar G18 com predecessor G17, arquivo formal e PR #35, sem modificar
  seu conteúdo técnico.
- Atualizar a memória de trabalho e encerrar as PRs concorrentes #27, #33 e
  #36 após a abertura da PR canônica.

## Fora de escopo

- Corrigir o comentário já publicado em PR #35.
- Implementar Device Fingerprint, Compatibility Registry, Capability Registry
  ou Skill Router.
- Promover G10 ou Goals posteriores.
- Alterar Skills, registries de equipamento ou `demandas/`.

## Critérios de aceite

- Há uma única definição canônica de política, gate e script de merge.
- Nenhuma PR aberta concorrente reescreve esse contrato de forma incompatível.
- G18 está registrado no catálogo com seu estado observável.
- G10 continua documentado como `BLOCKED`.
- A validação estrutural passa; a suíte dinâmica é responsabilidade da CI/VPS,
  pois a política do repositório não autoriza executá-la localmente.

## Estado atual

`CHANGES_REQUESTED` — o bloqueio inicial por ausência do artefato formal e a
inconsistência de `--checker-login` foram corrigidos. O segundo
`request-changes` confirmou que comparar o comentário com `committedDate` não
provava que o SHA era o HEAD revisado. O gate agora exige review nativo
`APPROVED` vinculado exatamente ao `headRefOid` atual; este novo HEAD aguarda
re-review e novo veredito literal.
