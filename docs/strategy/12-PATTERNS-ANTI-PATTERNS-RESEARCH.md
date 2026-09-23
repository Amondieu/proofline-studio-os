# 12 — Patterns and anti-patterns research system

<!-- v0.1 · 2026-09-23 · owner: founder · status: V1 pilot cookbook -->

This is not a gallery of visual inspiration. It is the operating contract for
turning public evidence, local proofs of concept, QA receipts, and project
outcomes into reusable Proofline rules.

The ten patterns below are **pilot defaults**, not approved causal claims. A
pattern becomes an approved default only after the workflow in this document,
an attached receipt, and a human decision. A public example can inspire a
hypothesis; it cannot prove that the pattern caused conversion.

## Evidence ladder

| Level | Use | Cannot establish |
|---|---|---|
| Authoritative | Standards, browser/framework documentation, verified licence/source code | Business uplift by itself |
| Strong practitioner | Credible UX research, maintained design-system guidance, documented case study | Universal causality |
| Observational | Public website or showcase observation | Conversion impact or permission to copy |
| Inference | Proofline synthesis or hypothesis | A source-backed fact |

The canonical evidence types for client-facing claims remain: demonstrated
method, stated standard, permissioned quote, and labelled concept work. A
pattern card must separate source facts from Proofline inference.

## Provisional taxonomy

Scores are provisional readiness scores, not measured conversion results. The
formula lives in `studio/cookbook.py` and weights clarity, plausibility, trust,
mobile suitability, accessibility, performance, cost, maintenance, legal safety,
and studio fit. For cost and burden, a higher score means easier to deliver and
maintain inside the fixed-scope studio model.

| ID | Pattern | Job | Best fit | Score | Decision |
|---|---|---|---|---:|---|
| HERO-001 | Outcome + audience + CTA in the first screen | Make the offer legible before attention runs out | All | 8.6 | Pilot |
| CTA-001 | One primary action per page | Reduce competing decisions | All | 8.8 | Pilot |
| COPY-001 | Problem → mechanism → benefit → proof → CTA | Explain a complex offer | B2B AI / SaaS | 8.4 | Pilot |
| TRUST-001 | Verifiable proof or labelled proof-pending state | Reduce uncertainty without fabrication | All | 9.4 | Pilot |
| FORM-001 | Persistent labels, errors, and success state | Make lead capture recoverable | All | 9.0 | Pilot |
| TYPE-001 | Readable type with stable fallbacks | Support scanning and stable layout | All | 8.8 | Pilot |
| A11Y-001 | Keyboard, focus, target, and reduced-motion baseline | Keep interaction usable for more people | All | 9.5 | Pilot |
| PERF-001 | LCP-first media and reserved dimensions | Protect perceived speed and CLS | All | 9.3 | Pilot |
| QA-001 | Preview → E2E test → mobile/keyboard QA → receipt | Make “done” auditable | All | 9.6 | Pilot |
| OWN-001 | Client-owned accounts and exportable handover | Prevent lock-in and ambiguity | All | 9.0 | Pilot |

## Ten launch blockers

These are implementation blockers because they undermine clarity, accessibility,
performance, trust, or ownership. They do not claim that every instance has the
same legal consequence; the human/legal review path remains authoritative.

| ID | Anti-pattern | Harm | Launch rule |
|---|---|---|---|
| HERO-AP-001 | Hero does not explain offer, audience, outcome, and action | Conversion / clarity | Block launch |
| TRUST-AP-001 | Fake testimonials, logos, reviews, or metrics | Trust / legal | Block launch |
| RIGHTS-AP-001 | Asset, template, font, or component licence is unclear | Rights / maintenance | Block launch |
| CTA-AP-001 | Primary CTA is hidden or competes with equal-priority CTAs | Conversion | Block launch |
| FORM-AP-001 | Form lacks tested delivery, error recovery, or success state | Conversion / accessibility | Block launch |
| A11Y-AP-001 | Focus is invisible, trapped, or obscured by sticky UI | Accessibility | Block launch |
| A11Y-AP-002 | Key content requires hover, drag, autoplay, colour, or desktop-only interaction | Accessibility | Block launch |
| PERF-AP-001 | Lazy-loaded LCP, oversized hero video, or unreserved media | Performance | Block launch |
| MOTION-AP-001 | Animated UI has no reduced-motion path | Accessibility / trust | Block launch |
| AI-AP-001 | Realistic synthetic people imply real staff, customers, or proof | Trust / legal | Block launch |

Detailed cards live in [13-CONVERSION-PATTERNS.md](13-CONVERSION-PATTERNS.md),
[14-UX-ANTI-PATTERNS.md](14-UX-ANTI-PATTERNS.md),
[15-MOTION-BUDGET.md](15-MOTION-BUDGET.md),
[16-PERFORMANCE-PATTERNS.md](16-PERFORMANCE-PATTERNS.md),
[17-ACCESSIBILITY-PATTERNS.md](17-ACCESSIBILITY-PATTERNS.md), and
[18-TRUST-AND-PROOF-STANDARDS.md](18-TRUST-AND-PROOF-STANDARDS.md).

## Three direction rules

| Direction | Allowed emphasis | Forbidden default | Budget posture |
|---|---|---|---|
| Precision System | diagrams, structured proof, explicit mechanism, calm signal motion | decorative gradients, dense card grids, counters without evidence | CSS motion first; one restrained interactive system |
| Cinematic Authority | one strong composition, short product/brand demonstration, editorial pacing | autoplay sound, heavy parallax, multiple focal points | static poster first; media must not delay LCP |
| Editorial Luxury | typography, whitespace, material detail, selective proof | saturated accents, tight leading, shadow-heavy cards | quiet transitions; no effect is required to understand the page |

Direction switching may change tokens only. It must not change information
architecture, copy, CTA destination, focus order, legal content, or the
reduced-motion path.

## Project-tier rules

| Tier | Must have | Permitted enhancement | Forbidden complexity |
|---|---|---|---|
| Starter (€500–750) | HERO-001, CTA-001, TYPE-001, A11Y-001, FORM-001, QA-001 | CSS state changes and one static visual | custom 3D, multi-step form, unbounded integrations |
| Authority (€1,250–1,750) | Starter set plus COPY-001, TRUST-001, PERF-001 | one controlled direction pass, short demo loop with poster | A/B infrastructure, bespoke CMS, animation-led IA |
| Launch System (€2,500–3,000) | full default set plus OWN-001 and documented experiment | approved custom asset or CMS when scoped | silent scope expansion, client-data AI uploads, unsupported result claims |

All tiers use the same evidence and launch gates. Price changes scope, not the
standard of honesty, accessibility, ownership, or QA.

## QA protocol

### Automated evidence

- Validate project, pattern, anti-pattern, experiment, and QA JSON contracts.
- Run axe where a real preview exists; investigate all serious/critical findings.
- Measure LCP, INP, and CLS with a pinned tool and record lab versus field data.
- Verify metadata, link targets, form routes, and direction-switcher invariants.
- Run the portability audit and keep paths project-relative.

### Manual evidence

- Read the first viewport at mobile width and state the offer, audience,
  outcome, and action.
- Tab through navigation, switcher, form, and footer; inspect focus visibility,
  order, escape behavior, and sticky-element overlap.
- Test 200% zoom and 320–390 px widths.
- Enable reduced motion and confirm that comprehension and interaction remain
  intact.
- Check every proof item, asset, font, quote, and claim against provenance.
- Confirm the client can access the accounts and that rollback/restore was
  actually rehearsed.

### Low-traffic test rule

Use a directional test only when the page has enough qualified traffic and a
decision can be made without manufacturing certainty. Otherwise use a
structured 5-second comprehension test, task walkthrough, or expert review and
label the result as qualitative evidence.

## Research-to-cookbook workflow

```text
candidate → evidence log → card → local proof of concept → human review
         → pilot / block → QA receipt + outcome data → approve / revise / retire
```

1. Add a candidate to `templates/pattern-evidence-log.csv` with context, source
   level, exact URL, observation, and the claim it can support.
2. Write a pattern or anti-pattern card. Include a use boundary, implementation
   mechanism, mobile behavior, accessibility behavior, budget, and test.
3. Build the smallest local proof of concept. Do not upload client material or
   copy a public site's expression.
4. Run the relevant automated and manual checks. Attach a QA receipt.
5. A human reviewer records `pilot`, `approved`, `reference_only`, `avoid`, or
   `superseded`. The cookbook never authorizes launch.
6. After a client project, record measured or client-supplied outcomes only with
   permission. “Not measured” is a valid result.
7. Retire a rule when evidence weakens, maintenance cost rises, a standard
   changes, or two projects show the pattern fails its stated job.

## Repository deliverables

| File | Purpose | Approval |
|---|---|---|
| `docs/strategy/12-PATTERNS-ANTI-PATTERNS-RESEARCH.md` | System rules and decision log | Founder |
| `docs/strategy/13-CONVERSION-PATTERNS.md` | Initial pattern cards | Founder for promotion |
| `docs/strategy/14-UX-ANTI-PATTERNS.md` | Initial blockers and replacements | Founder; legal review where applicable |
| `docs/strategy/15-MOTION-BUDGET.md` | Interaction budget and direction limits | Founder |
| `docs/strategy/16-PERFORMANCE-PATTERNS.md` | Core Web Vitals and media rules | Founder + QA evidence |
| `docs/strategy/17-ACCESSIBILITY-PATTERNS.md` | WCAG-oriented interaction rules | Founder; specialist review where needed |
| `docs/strategy/18-TRUST-AND-PROOF-STANDARDS.md` | Proof, disclosure, and rights | Founder; legal review where needed |
| `templates/pattern-card.md` | Copy-ready pattern record | Founder |
| `templates/anti-pattern-card.md` | Copy-ready blocker record | Founder |
| `templates/pattern-test-plan.md` | Controlled test plan | Founder |
| `templates/pattern-evidence-log.csv` | Research backlog and source log | Researcher drafts; founder reviews |
| `templates/launch-receipt.md` | Human-readable release receipt | Founder / named human reviewer |
| `schemas/pattern-record.schema.json` | Pattern contract | Founder |
| `schemas/anti-pattern-record.schema.json` | Anti-pattern contract | Founder |
| `schemas/experiment-record.schema.json` | Experiment contract | Founder |
| `schemas/qa-receipt.schema.json` | Compatibility entry point | Founder |

The machine-readable contracts are versioned with `v1`; changes that alter
required fields require a new major contract or an explicit migration.

## First decisions

### Encode this week

HERO-001, CTA-001, COPY-001, TRUST-001, FORM-001, TYPE-001, A11Y-001,
PERF-001, QA-001, and OWN-001.

### Block in code review

Fake proof, unclear rights, CTA ambiguity, silent form failure, invisible or
obscured focus, hover-only content, lazy LCP/oversized hero media, missing
reduced motion, misleading synthetic people, and unsupported outcome claims.

### First five tests on the Master Site

1. 5-second first-viewport comprehension test.
2. Keyboard path through navigation, direction switcher, and form.
3. 320/390 px reflow and sticky-focus overlap check.
4. Reduced-motion switcher and animation-path check.
5. Form validation, success, and local-only data-handling check.

### Smallest defensible V1

Ten pilot cards, ten blocker cards, one evidence log, one test-plan template,
the existing QA receipt, and a human promotion decision. Do not write 25 cards
per category until the research pass has evidence worth preserving.

## Source notes

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the normative accessibility
  reference; it is testable but does not address every user need.
- [W3C form labels tutorial](https://www.w3.org/WAI/tutorials/forms/labels/)
  supports persistent, programmatically associated form labels.
- [web.dev Core Web Vitals](https://web.dev/articles/vitals), [LCP](https://web.dev/articles/lcp),
  [INP](https://web.dev/articles/inp), and [CLS](https://web.dev/articles/optimize-cls)
  provide metric definitions and field-oriented thresholds.
- [`prefers-reduced-motion` on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
  documents the platform signal used by the motion rules.
- The LLMarena archive contains the broader source inventory and research
  backlog. Its dated vendor/legal findings require fresh review before client
  communication.
