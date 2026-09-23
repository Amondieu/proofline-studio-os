# Convergence report

Status: converged for the candidate-quality system; not a Gold promotion.

## Evidence

- Five evaluation files cover all five configured archetypes.
- Every evaluation is explicitly `candidate` with human test and review pending.
- The Pydantic validator rejects a Gold candidate without all required gates.
- Source records preserve quality signals, limitations, and reuse decisions.
- The master templates are content skeletons, not copied client designs.

## Commands to run at handoff

```text
python scripts/validate_studio_contracts.py
python -m unittest discover -s tests -p "test_*.py"
python tools/qa_matrix.py --check
python tools/contrast_check.py site/styles.css
python scripts/portable_audit.py
npm run graph:validate
npm run graph:update
npm run graph:status
npm run graph:portable
git diff --check
git status --short --branch
```

## Human follow-up

Run one representative task test per archetype, review rights and claims, and
only then decide whether any candidate should move to `pilot` or
`gold_candidate`. No current record makes that decision automatically.
