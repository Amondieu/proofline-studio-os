# Feature specification: archetype quality intelligence

Status: implemented as a candidate-quality system; human promotion remains open.

## Why

Proofline needs a repeatable way to research all five business archetypes and
evaluate reusable master templates without confusing visual popularity with
quality, accessibility, conversion evidence, or rights.

## Scope

In scope: source hierarchy, evidence records with limitations, five
direction-neutral master templates, machine-readable evaluations, and a
verification trail. Out of scope: scraping, automatic site copying, live
client templates, production forms, award-based approval, and autonomous
source promotion.

## Assumptions and decisions

- “Master template” means a content-and-decision skeleton in Markdown first;
  it is not a finished client website or visual direction.
- Current evidence is sufficient to create candidates, not to declare any
  template Gold. Human task tests and review are intentionally false/pending in
  the initial evaluation records.
- The five catalog IDs are the source of truth in
  `config/studio/archetypes.v1.json`.
- Existing QA, accessibility, performance, proof, rights, and human-gate
  rules remain authoritative; this feature adds evidence organization only.

## Functional requirements

- **FR-001 Source records:** Every source records class, evidence level,
  quality signal, limitations, applicable archetypes, and reuse decision.
- **FR-002 Five coverage:** Each catalog archetype has one master-template
  artifact and one machine-readable evaluation.
- **FR-003 Template boundaries:** Templates include evidence slots, CTA/action
  logic, accessibility/performance requirements, and explicit no-fabrication
  boundaries.
- **FR-004 Gold safety:** `gold_candidate` is invalid unless normative gates,
  functional gates, a human test, and human review are all recorded.
- **FR-005 Workflow:** The implementation is traceable through this spec,
  `plan.md`, `tasks.md`, and `converge.md`.
- **FR-006 Verification:** Contracts, unit tests, QA matrix, contrast check,
  portability audit, and Graphify checks pass before commit.

## Acceptance criteria

1. Exactly five evaluation files validate against the evaluation contract and
   cover every archetype ID.
2. All five evaluations are `candidate`, not falsely promoted to Gold.
3. Every evaluation references at least two registered source IDs.
4. All five templates are direction-neutral and contain a primary decision,
   proof boundary, evidence slots, and QA requirements.
5. A test fails when an archetype evaluation is missing or when an unqualified
   Gold candidate is introduced.
6. The convergence commands and their results are recorded in `converge.md`.
