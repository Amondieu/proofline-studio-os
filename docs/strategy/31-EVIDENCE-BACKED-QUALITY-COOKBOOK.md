# 31 — Evidence-backed quality cookbook

<!-- v0.1 · 2026-09-23 · owner: founder · status: pilot standard -->

This document consolidates the new LLMarena quality strand with the existing
pattern system in `docs/strategy/12–18`. It is a decision boundary, not a
replacement for the detailed cards. A check may block work; only a human may
approve a direction, release, or launch.

## 1. Evidence ladder

| Level | May establish | May not establish |
|---|---|---|
| Normative | A standard or policy requirement | Business uplift |
| Technical | An implementation constraint or browser behaviour | Universal conversion impact |
| Research | A hypothesis worth testing locally | A guarantee for this studio |
| Observational | A visual or interaction vocabulary | Permission to copy or causal proof |

Every public claim needs a substantiation path. A public example can inspire a
pattern, but it cannot prove that the pattern caused a result or that its
expression is available for reuse.

## 2. Rule → card → blocker → test

The reusable loop is:

`candidate → evidence log → pattern card → smallest local proof → human review → QA receipt → approve, revise, or retire`

The existing detailed card families remain canonical:

- conversion and messaging: `13-CONVERSION-PATTERNS.md`;
- UX failure modes: `14-UX-ANTI-PATTERNS.md`;
- motion: `15-MOTION-BUDGET.md`;
- performance: `16-PERFORMANCE-PATTERNS.md`;
- accessibility: `17-ACCESSIBILITY-PATTERNS.md`;
- trust, proof and AI disclosure: `18-TRUST-AND-PROOF-STANDARDS.md`.

The executable mapping is `tools/qa_matrix.py`. It intentionally keeps the
quality run separate from the launch decision.

## 3. Three delivery tiers

| Tier | Required baseline | Controlled enhancement | Forbidden shortcut |
|---|---|---|---|
| Starter | Clarity, one CTA, readable type, form state, accessibility baseline, QA receipt | One static visual system | Unbounded integrations or animation-led IA |
| Authority | Starter + message mechanism, proof boundary, performance receipt | One direction pass and a short demo | Unsupported result claims or silent scope expansion |
| Launch System | Full baseline + ownership, experiment record, rollback evidence | Approved CMS or custom asset when scoped | Client-data AI uploads or autonomous publishing |

## 4. Blocker families

The following are implementation blockers until a human records a waiver or a
fix: unclear hero or CTA; fabricated proof; unclear asset/font rights; missing
form recovery; invisible or obscured focus; desktop-only or colour-only
interaction; unbounded LCP media; no reduced-motion path; undeclared realistic
synthetic people; missing legal/privacy pages; self-serving review markup;
missing client ownership; and an unreproducible QA or rollback receipt.

## 5. Must-pass launch checklist

The checklist is deliberately explicit so every item maps to at least one test
row in `tools/qa_matrix.py`.

```text
[ ] 1 Interactive targets are at least 24×24 CSS px or have an equivalent exception.
[ ] 2 Focus is visible and not obscured by sticky or fixed UI.
[ ] 3 Drag interactions have a non-drag alternative.
[ ] 4 Help and support mechanisms remain consistent across the flow.
[ ] 5 Information already supplied is not redundantly requested.
[ ] 6 Reduced motion preserves comprehension and interaction.
[ ] 7 Fonts and third-party assets have an explicit licence and fallback.
[ ] 8 CLS meets the project budget and no late content shifts above the fold.
[ ] 9 Third-party scripts stay within the project budget and purpose.
[ ] 10 Forms have labels, errors, recovery, spam handling, and notification evidence.
[ ] 11 Every public claim maps to substantiation or is labelled as concept work.
[ ] 12 Structured data does not create self-serving review or invisible claims.
[ ] 13 Legal, privacy, and accessibility pages are accurate and reachable.
[ ] 14 AI assets have provenance, rights, and disclosure treatment where needed.
[ ] 15 Client ownership of code, hosting, domain, analytics, and accounts is verified.
[ ] 16 QA evidence is reproducible and rollback has been rehearsed.
```

These are gates for readiness, not an automated launch approval. A project can
be shown as a concept while still being blocked from launch.

## 6. Current run boundary

The LLMarena Phase-1 report was executed against its own demo artifact, not the
current `site/index.html`. Its observations are therefore research inputs. In
particular, the current master site must still be checked for reduced motion,
contrast, legal pages, form delivery, and production ownership before any
public launch. The incoming report also identifies token drift and a future
`tokens.json` proof-of-concept; this repository records those as decisions, not
as silently generated authority.

## 7. Human decisions still required

1. Choose whether the current site or a future token specification is the
   source of truth before introducing `tokens.json`.
2. Run the second quality phase against the real master site once a production
   form endpoint exists.
3. Have legal/counsel review public legal text, AI disclosure, and rights.
4. Promote the new QA tooling only after a second project supplies evidence.
