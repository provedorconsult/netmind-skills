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
- G15: `DONE / MERGED` in PR #25, approved head
  `23c43d1d7b89ffd4f7294c81b6407e5119458589`, merge commit
  `afafd885c5f7e852a4f85356cd9327b9440758d1`, predecessor G14.
- G16: `DONE / MERGED` in PR #28, approved head
  `7b871b31519a6623cd0cecef65ac89bc084f1255`, merge commit
  `6ad640b6cae88a0b2b0b459ae8f81c6e7ce026c6`, predecessor G15.
- G17: `DONE / MERGED` in PR #31, approved head
  `1ddc124ed2c7aa05caf0d5de7c3df019bd12a30e`, merge commit
  `4117de936136dce7cfdff0a851829c4fc6a3f7c1`, predecessor G16.

## Active Goal

Nenhum Goal está ativo. G17 foi concluído e não há próximo Goal formalmente
promovido; `nextGoal` permanece `null` até decisão posterior do
Harness/Checker.

## G18 and G19 reconciliation

- G18 is formally cataloged with predecessor G17 and PR #35. Its observable
  GitHub PR remains open, but the independent Checker published `blocked`:
  G18 is not yet registered in `main`, and its Acceptance Contract had been
  absent. G19 now supplies that contract without altering G18's technical
  scope; G18 remains `BLOCKED` until G19 is merged with authorization and G18
  receives a new compliant Checker review.
- G19 supersedes the incompatible merge-gate designs in PRs #27 and #33. The
  canonical design keeps a complete, exact one-word Checker verdict and binds
  it to the queried current `headRefOid` by requiring the latest valid verdict
  to be an `approve` created after the current HEAD commit. It also requires a
  non-draft, clean PR and green CI. The multi-line `approvedHead` comment
  format from PR #33 is not retained because it violates the exact-entire-
  comment invariant.
- G19 preserves PR #36's authority separation: the Checker never merges; the
  Maker may merge only after a fresh GitHub-backed `MERGE_AUTHORIZED` result.
- The Checker published `blocked` for PR #37 at
  `2be0f599d2ab929dd2c212b5c0738bc1317af001` because the formal G19 source
  file was absent. That evidence was corrected. The subsequent Checker review
  published `request-changes` because the merge-gate loop command omitted the
  required `--checker-login` argument; G19 is now `CHANGES_REQUESTED` pending
  a new review of the corrective HEAD.
- G10 remains `BLOCKED`: it is a legacy release gate whose predecessor chain
  was superseded during G13 reconciliation. It has no GitHub-confirmed
  successor promotion and cannot be advanced by parallel PR activity.

## Invariants

- Execute one catalog goal at a time and preserve catalog order.
- GitHub PR facts are authoritative; local state is a mirror.
- Only an exact Checker PR comment of `approve` can authorize a merge.
- `request-changes` returns control to the Maker; `blocked` stops the goal.
- Nenhum Goal posterior a G17 está autorizado até nova promoção formal.
