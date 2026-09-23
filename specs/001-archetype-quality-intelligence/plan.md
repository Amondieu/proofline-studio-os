# Implementation plan

## Minimal design

Use existing `config/studio/archetypes.v1.json` IDs. Add only two typed
research contracts, five Markdown template skeletons, five JSON evaluation
fixtures, a source registry, and a repository-local workflow record. Do not
introduce a database, scraper, external connector, or new rendering runtime.

## File map

| Concern | File or directory |
|---|---|
| Constitution | `.specify/memory/constitution.md` |
| Source policy and register | `config/studio/quality-source-policy.v1.json`, `research/archetype-source-register.csv` |
| Typed contracts | `studio/quality_research.py`, `schemas/quality-source-record.schema.json`, `schemas/archetype-template-evaluation.schema.json` |
| Master templates | `templates/archetypes/*-master.v1.md` |
| Evaluations | `research/archetype-template-evaluations/*.json` |
| Verification | `tests/test_archetype_evaluations.py`, `scripts/validate_studio_contracts.py` |

## Verification strategy

- Schema and Pydantic validation catch malformed source/evaluation records.
- The evaluation test enforces exact five-archetype coverage.
- The model validator blocks unsupported `gold_candidate` records.
- Existing QA, contrast, portability, and Graphify checks cover the broader
  studio invariants.
