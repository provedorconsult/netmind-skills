# NetMind Harness Working Memory

## Reconciled history

- G11: `DONE / MERGED` in PR #19, merge commit
  `5ba9d398faf35022ea216c72f9f4c42420371261`.
- G12: `DONE / MERGED` in PR #20, approved head
  `20634b6335df02f832f16930c4fb5f2713117082`, merge commit
  `ed3b157c048c0480a01398c7abdf7821148d830f`.
- G13: `DONE / MERGED` in PR #22, approved head
  `0eecaf65149073a5e4b6dbc919c95b7bf4dd9ffb`, merge commit
  `fc88f28038e62d28a0d7381cab5fb20565fa726b`, predecessor G12.
- G14: `DONE / MERGED` in PR #23, merge commit
  `d6cf4f684317810d915a89bd9e03524564e8afa9`, predecessor G13.

## Active Goal

G15 está formalmente definido e promovido para `READY`, com predecessor `G14`.
A fonte canônica é `15-readme-institucional-ai-native.md`.

O objetivo de G15 é reestruturar o `README.md` como porta de entrada
institucional, técnica e operacional do NetMind Skills em Português Brasil,
sem implementar novos registries, Skills ou Goals posteriores.

## Invariants

- Execute one catalog goal at a time and preserve catalog order.
- GitHub PR facts are authoritative; local state is a mirror.
- Only an exact Checker PR comment of `approve` can authorize a merge.
- `request-changes` returns control to the Maker; `blocked` stops the goal.
- G15 é o único Goal autorizado para implementação neste momento.
- G16+ permanecem fora de escopo até nova promoção formal.
