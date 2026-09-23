# QA receipt — first archetype portfolio preflight

## Receipt status

`STATIC / CONCEPT RECEIPT — not a production release`

This receipt points to repository evidence and records what is still missing.
It must not be used as a launch approval or a claim of field performance.

## Evidence available

- Contract validation: `python scripts/validate_studio_contracts.py`
- Unit tests: `python -m unittest discover -s tests -p "test_*.py"`
- QA matrix: `python tools/qa_matrix.py --check`
- Contrast check: `python tools/contrast_check.py`
- Portability: `python scripts/portable_audit.py`
- Browser evidence retained in `LLMarena/NewLLM/quality-run-2026-09-23.md`.
- Focused page receipt: `pending focused-page implementation`.

## Known static behavior

- [x] Direction switcher has a local persistence path.
- [x] Reduced-motion rules and focus-offset handling are represented in the
      current master site.
- [x] Current concept work is labelled as concept or independent redesign.
- [x] The form copy says that no data is sent.
- [ ] Focused-page keyboard sweep recorded.
- [ ] Focused-page 390px review recorded.
- [ ] Focused-page performance metrics recorded.
- [ ] End-to-end form, error, spam, and notification paths tested.
- [ ] Legal, ownership, rollback, and production accessibility evidence
      recorded.

## Human record

- Tester: `[human reviewer required]`
- Commit: `[attach focused-page commit]`
- Waivers: `[none recorded]`
- Sign-off: `pending`
