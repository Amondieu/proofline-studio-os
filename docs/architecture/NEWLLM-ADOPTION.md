# NewLLM adoption map

<!-- v0.1 · 2026-09-23 · source: LLMarena/NewLLM -->

The NewLLM snapshot contains useful operating material, but its report also
describes files and fixes from a separate bundle. This map records what is
actually adopted in this repository and keeps the source session reviewable.

## Adopted now

| Finding | Repository implementation |
|---|---|
| Prospecting needs a source boundary | `config/studio/prospecting-source-policy.v1.json` and `docs/strategy/30-PROSPECTING-DATA-SOURCES.md` |
| Suppression must be a separate, minimal system of record | `SuppressionRecord`, `schemas/suppression-record.schema.json`, and the empty CSV template |
| Every send needs nine explicit conditions | `templates/send-gate-checklist.md`, `skills/outreach-review/SKILL.md`, existing `SendApproval` |
| Outreach should feed a quality loop | `templates/teardown-quick-audit.md`, `templates/outreach-email-sequences.md`, `docs/strategy/31-EVIDENCE-BACKED-QUALITY-COOKBOOK.md` |
| Quality rules need a machine-checkable mapping | `tools/qa_matrix.py` and `research/qa-matrix.md` |
| Reduced motion must be the default-safe path | `site/styles.css` keeps transitions and smooth scrolling inside the no-preference branch |

## Adapted, not copied

- The incoming prospecting policy is merged with the existing typed outbound
  contracts in `docs/strategy/23–29`; no second prospect model is introduced.
- The incoming cookbook is consolidated with existing pattern families in
  `docs/strategy/12–18`; the repository does not create a duplicate 40-card
  authority or silently promote observational research to proof.
- The incoming Phase-1 run remains evidence about its own demo artifact. It is
  not presented as a passed QA report for `site/index.html`.
- Contrast checking is adapted to the current CSS token shape and is a report,
  not a launch authority.

## Deliberately held back

- `tokens.json`: first resolve the human decision about spec-versus-demo token
  ownership.
- Production form endpoint and delivery evidence.
- Automated collection, CRM export, campaign sending, and external adapters.
- Legal conclusions about a provider's licence, redistribution, retention, or
  a concrete France/EU outreach case. Those remain counsel/founder review.

## Source record

The incoming snapshot is preserved at `LLMarena/NewLLM/`. The selected archive
is treated as research input, not as an executable policy. A future update
should add a dated entry here, state the evidence used, and run the contracts,
unit tests, portability audit, QA tools, and Graphify checks before promotion.
