# Proofline Studio

Proofline Studio is a human-governed operating system for professional
websites and conversion landing pages. It combines a repeatable studio method,
scope-aware offers, creative direction systems, implementation checklists, and
a read-only launch harness.

The public `site/` is an interactive proof-of-work master site. The `studio/`
package is the operational core. It evaluates a project manifest through:

`Discovery -> Message -> Direction -> Build -> QA -> Launch`

The evaluator can block and explain missing work. It cannot approve, publish,
deploy, or assert that a legal or factual claim is true. A human owns every
meaningful sign-off.

The six-gate pipeline now includes a machine-readable QA receipt between Build
and Launch. Asset provenance and detailed human approvals are separate,
versioned records; they supplement the append-only gate ledger.

## What this repo is for

- productized landing-page delivery for B2B AI/automation, micro-SaaS, and
  premium service offers;
- strategy, copy, art direction, implementation, accessibility, performance,
  tracking, and handover as one controlled service;
- a reusable harness that prevents scope drift, fabricated proof, and premature
  launch;
- a master site that demonstrates three controlled creative directions without
  changing the underlying information architecture or conversion path.

## Quick start

```powershell
python -m pip install -r requirements.txt
python scripts/validate_studio_contracts.py
python -m unittest discover -s tests -p "test_*.py"
python -m studio validate tests/fixtures/studio/blocked-project.v1.json
python scripts/portable_audit.py
```

Laya is an optional advisory layer, disabled by default. Its contracts and
offline boundary tests are included; install `requirements-laya.txt` only for
a local, human-reviewed inference experiment. See
[`docs/architecture/LAYA-ADVISORY-LAYER.md`](docs/architecture/LAYA-ADVISORY-LAYER.md).

Open `site/index.html` directly for the local proof-of-work site. It has no
network dependency and its teardown form is a local demonstration only.

## Repository map

- `docs/strategy/` — studio positioning, offers, creative directions, and
  client-facing operating recipes.
- `docs/architecture/` — authority model and harness design.
- `docs/architecture/NOTION-CANVA-INTEGRATION.md` — deferred Notion/Canva roles,
  ownership boundaries, and adapter backlog.
- `docs/operations/` — reusable briefs and checklists for client work.
- `docs/operations/NOTION-CLIENT-PORTAL-V1.md` and
  `CANVA-SALES-TEMPLATES-V1.md` — later-build specifications for the client
  portal and the five sales/delivery templates.
- `studio/` — typed project contracts, deterministic gate evaluator, portable
  path helpers, QA receipt, provenance records, explicit human-gate ledger
  writer, and the optional Laya advisory adapter.
- `schemas/studio/` — versioned JSON contracts.
- `templates/studio/` — portable QA and asset-provenance starting templates.
- `templates/` — pattern cards, test plans, evidence log, and launch receipt.
- `docs/strategy/12–18` — the evidence-backed pattern and anti-pattern cookbook.
- `docs/strategy/19–22` — business archetypes, selection rubric, blueprints, and sales playbook.
- `docs/strategy/23–29` — human-gated outbound intelligence, scoring, teardown,
  compliance, messaging, and reply learning.
- `docs/strategy/30–31` — NewLLM-derived source policy, suppression boundary,
  send gate, and evidence-backed quality standard.
- `docs/strategy/32-ARCHETYPE-QUALITY-INTELLIGENCE.md` — source hierarchy,
  archetype research protocol, and master-template evaluation rules.
- `.specify/` and `specs/` — lightweight project-local specification workflow,
  constitution, plan, tasks, and convergence evidence.
- `templates/archetypes/` and `research/archetype-template-evaluations/` — five
  direction-neutral master templates and their deliberately human-gated
  candidate evaluations.
- `docs/architecture/LAYA-ADVISORY-LAYER.md` — optional model routing,
  abstention, calibration, and authority boundaries.
- `LLMarena/` — preserved deep-research bundle; see
  `docs/architecture/LLMARENA-ADOPTION.md` for what is operational.
- `config/studio/` — profile, offers, creative directions, archetypes, and QA policy.
- `site/` — Proofline Studio master-site proof of work.
- `skills/landing-studio/` — agent execution envelope for studio tasks.
- `skills/` — local Proofline wrappers around selected external references;
  wrappers preserve evidence, privacy, and human-send boundaries.

## Deliberately outside this repo

There is no social publishing, content persona engine, viral cookbook, Ruflo
swarm, live provider credential, scheduler authority, or autonomous client
deployment. Laya is present only as an optional, non-authoritative advisory
adapter; its weights and runtime state are outside the repository. Those other
capabilities were part of the source project's AI-media scope and would make
this studio's responsibilities less clear.

See [MIGRATION-MAP.md](docs/MIGRATION-MAP.md) for the full adoption decision.
