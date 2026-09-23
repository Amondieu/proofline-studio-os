# LLMarena research adoption

The snapshot in `LLMarena/proofline-studio-os/` is preserved as a research
bundle from the 2026-09-23 deep-research session. It is evidence and design
input, not a second operational source of truth. It is deliberately outside
the Graphify corpus until individual findings are adopted and reviewed.

## Adopted now

| Research finding | Proofline surface | Decision |
|---|---|---|
| QA must leave a receipt, not only a checkbox | `schemas/studio/qa-receipt.v1.json`, `studio/models.py`, `studio/harness.py` | The pipeline now evaluates an explicit QA gate between Build and Launch. |
| Assets need provenance and an approval trail | `schemas/studio/asset-record.v1.json`, `schemas/studio/approval-record.v1.json` | Rights, AI inputs, allowed uses, and human approval are first-class records. |
| Evidence needs a small, honest vocabulary | `config/studio/evidence-policy.v1.json` | Claims use demonstrated method, stated standard, permissioned quote, or labelled concept work. |
| Performance and motion need measurable budgets | `config/studio/qa-policy.v1.json`, QA receipt contract | The receipt records LCP, INP, CLS, JavaScript, third-party scripts, and reduced-motion review. |
| Client ownership is a delivery gate | QA receipt ownership/rollback sections and existing launch review | A project cannot become ready for human launch review without verified access and restore evidence. |
| Research and legal findings age | this adoption note and the preserved research bundle | Tool, licence, hosting, and legal claims remain dated research; they are not permanent guarantees. |

## Deliberately deferred

- Astro/Tailwind migration of the proof-of-work site. The current static site
  is a low-risk demonstration; a client build can adopt Astro after a project
  brief and stack decision exist.
- Cloudflare Worker/D1, Tally, Cal.com, Plausible, CMS, and other live
  integrations. They require client-owned accounts, data-flow review, and a
  project-specific adapter; this foundation stores no credentials.
- A full `axe`/Lighthouse/Playwright shell. The repository can record the
  evidence now, but it must not pretend that unavailable tooling ran. The
  existing browser QA remains a human/evidence step until a real client build
  supplies a preview server and pinned tools.
- 3D, Rive, GSAP, A/B testing, and a private component package. These remain
  opt-in exceptions with a written decision record.

## Source-of-truth rule

The adopted contracts and policies under `schemas/`, `config/`, `studio/`, and
`docs/` govern current work. The LLMarena bundle is consulted for provenance,
research details, templates, and future pilots. If the two disagree, the
current versioned contract wins until a human records a deliberate change.

## Acceptance check

This adoption is complete when:

1. `python scripts/validate_studio_contracts.py` passes;
2. `python -m unittest discover -s tests -p "test_*.py"` passes;
3. `python scripts/portable_audit.py` passes;
4. a sample QA receipt can be validated without granting launch authority; and
5. no research finding is presented to a client as legal, licence, hosting, or
   conversion advice without a fresh review.
