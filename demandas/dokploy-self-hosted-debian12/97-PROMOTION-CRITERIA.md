# Promotion Criteria — Dokploy Self-Hosted

A demanda só avança entre fases quando o Goal anterior estiver `DONE` conforme seu Acceptance Contract.

## Gates
- evidência rastreável;
- testes executados;
- riscos documentados;
- segurança preservada;
- Current/Legacy/Canonical separados;
- nenhuma falha conhecida mascarada;
- artefatos revisáveis pelo Checker.

## Estados
`NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, `READY_FOR_REVIEW`, `APPROVED`, `DONE`.

## Integração
Somente o Checker pode autorizar integração com comentário social literal `approve` no HEAD revisado. CI verde isoladamente não autoriza merge.
