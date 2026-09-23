# 32 — Archetype quality intelligence

<!-- v0.1 · 2026-09-23 · owner: founder · status: pilot research system -->

Proofline should research all five archetypes explicitly, but it should not
turn a gallery ranking into a universal template. The purpose of this system is
to discover repeatable decision-support patterns, test them in context, and
promote only the ones that survive human review and the existing QA gates.

## The gold standard

There is no single Gold source. A `gold_candidate` template requires a
triangulation:

1. **Normative gates:** accessibility, privacy, rights, claims, and technical
   requirements are checked against authoritative sources.
2. **Method evidence:** a UX or technical research source explains why the
   criterion is meaningful and how it can be tested.
3. **Archetype evidence:** a real, inspectable website or practitioner case
   shows the pattern in a comparable buying situation.
4. **Local proof:** the pattern is implemented in the smallest Proofline
   prototype and tested with a task, not judged only by taste.
5. **Human decision:** the evaluator records fit, limitations, source IDs, and
   whether the pattern is pilot, revise, reject, or a gold candidate.

An award, gallery presence, public score, case-study metric, or forum consensus
can contribute an observation. None can independently establish accessibility,
conversion, legal safety, rights, or universal quality.

## Source hierarchy

| Class | What it can do | Default treatment |
|---|---|---|
| Normative | Define a gate or compliance check | `adopt_as_gate` |
| UX / technical research | Define a testable hypothesis or measurement | `adopt_as_test` |
| Real website | Reveal a pattern in context | `hypothesis_only` |
| Practitioner case study | Explain a shipped decision and tradeoff | `hypothesis_only` until verified |
| Curated award | Provide judged craft and vocabulary signal | `hypothesis_only` |
| Community critique | Supply dissent, failure modes, and questions | `hypothesis_only` |
| Gallery | Supply visual references | `inspiration_only` |

The working registry is `research/archetype-source-register.csv`. Each source
needs a quality signal, limitations, applicable archetypes, reviewer, and
reuse decision. The typed record is `QualitySourceRecord`.

## Criteria for every archetype

Score a candidate template from 0–5 on:

- decision clarity;
- buyer confidence and proof boundary;
- action path and recovery;
- accessibility;
- performance and real-device resilience;
- archetype fit;
- craft and distinctiveness;
- maintainability and ownership.

The score is a comparison aid, not an automatic promotion formula. A low score
on an essential gate cannot be averaged away by visual craft.

## Research cards by archetype

| Archetype | Core question | Evidence to collect | Red-team question |
|---|---|---|---|
| AI / Automation Authority | Can a buyer understand the expensive workflow, mechanism, constraint, and diagnostic next step? | Workflow diagrams, technical proof, risk language, qualified assessment paths | Is technical theatre hiding absent evidence? |
| SaaS Launch & Demand | Can a buyer map a use case to product proof and choose demo or trial? | Use-case pages, product walkthroughs, comparison/fit, demo friction, mobile performance | Is the feature surface clearer than the buying decision? |
| Expert Authority | Can the right buyer distinguish point of view, fit, scope, and first conversation? | Point-of-view writing, method, proof context, application questions | Is personal branding substituting for a specific offer? |
| Creative Portfolio & Inquiry | Can a prospect judge relevance, role, process, constraints, and brief fit? | Curated work, case context, collaborators, credits, inquiry qualification | Is spectacle making the work impossible to compare? |
| High-Trust Lead Engine | Can a cautious visitor understand safety, privacy, expectations, and human response? | Credentials, process, privacy boundary, accessible forms, regulated content | Is reassurance being manufactured with badges or urgency? |

## Evaluation workflow

1. Select 3–5 sources per archetype: at least one normative/technical source,
   one research source where available, and two real or practitioner examples.
2. Record only observable facts and source limitations in a source record.
3. Extract the smallest reusable pattern; do not copy a site's expression,
   assets, code, or copy without rights and permission review.
4. Build a direction-neutral master template with content slots and explicit
   evidence states.
5. Run mobile, keyboard, reduced-motion, performance, form, and claim/rights
   checks. Add an archetype task test such as “state the offer, risk, and next
   action in five seconds”.
6. Review the result with a human and set `candidate`, `pilot`,
   `gold_candidate`, `revise`, or `reject`.

## Repository contracts

- `config/studio/quality-source-policy.v1.json` defines source classes and
  disallowed shortcuts.
- `schemas/quality-source-record.schema.json` records sources and limitations.
- `schemas/archetype-template-evaluation.schema.json` records scored template
  reviews and prevents a gold candidate without human evidence.
- `templates/archetype-quality-review.md` is the manual review form.
- `studio/quality_research.py` provides the typed models.

## Initial high-signal sources

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) for normative accessibility
  gates; it is a Recommendation with testable criteria and explicitly combines
  automated and human evaluation.
- [web.dev Core Web Vitals methodology](https://web.dev/articles/defining-core-web-vitals-thresholds)
  and [field measurement guidance](https://web.dev/articles/vitals-field-measurement-best-practices)
  for performance thresholds and percentile-based real-user evidence.
- [Baymard methodology](https://baymard.com/research/methodology) and the
  [SaaS benchmark overview](https://baymard.com/research-articles/digital-subscriptions-and-saas-2025-benchmark)
  for method-bearing UX research; transfer beyond commerce must be tested.
- [NN/g B2B usability research](https://www.nngroup.com/articles/b2b-usability/)
  for B2B research context; it is older and therefore a hypothesis source,
  not a current benchmark.
- [Awwwards evaluation system](https://www.awwwards.com/about-evaluation/) and
  [Webby judging criteria](https://www.webbyawards.com/judging-criteria/) for
  public judging dimensions, not compliance or conversion truth.
- [Siteinspire](https://www.siteinspire.com/) for visual vocabulary only.
