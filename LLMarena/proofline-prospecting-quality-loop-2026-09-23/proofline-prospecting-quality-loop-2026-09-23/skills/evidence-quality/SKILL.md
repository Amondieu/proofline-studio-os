---
name: evidence-quality
description: Turn a claim, a design idea or a research finding into a Proofline pattern card with an evidence level, implementation standard, anti-pattern, test and launch gate — or mark it as hypothesis only. Use before any rule enters the cookbook, a client deliverable or a code review.
---

# Skill: Evidence & Quality

## When to use
- A pattern is proposed for a client build, a design direction, or the cookbook.
- A research finding, a competitor teardown or a gallery screenshot is being used as an argument.
- Before a code review, to confirm the rule being enforced is a *rule* and not a style preference.

## Procedure
1. **Classify the evidence** (docs/31 §1): 1 normative (WCAG/ISO/EN/legal) · 2 technical (web.dev/MDN/framework docs) · 3 research (NN/g, Baymard, GOV.UK research, HCI) · 4 observational (galleries, portfolios, awards). Level 4 can never justify a claim, a gate, or a client-facing assertion.
2. **Separate the claim types** the finding can support: implementation requirement · testable hypothesis · visual reference · nothing. State which one applies.
3. **Write the pattern card** with all fields: evidence level + source URL · problem solved · required implementation · accessibility impact · performance impact · anti-pattern · test protocol · launch gate · tier · evidence status.
4. **Convert the rule into three artefacts:**
   - *Pattern card* in `docs/31 §3`.
   - *Code-review blocker* (one line: what the reviewer fails the PR for, with the criterion id).
   - *QA test* in `tools/qa_matrix.py` (id, level A/M/F, automated or manual, pass condition).
5. **Check the licence/rights dimension** when the pattern involves code, assets, fonts, illustrations or layout inspiration. Record the source and licence; missing/ambiguous licence → `DO NOT SHIP UNTIL CONFIRMED`.
6. **Decide the status** honestly: `Approved default` (level 1/2 or a repeatedly validated local test) · `Hypothesis` (level 3, needs a per-project test) · `Conditional` (allowed only with a stated constraint) · `Deprecated` (with date and reason).
7. **Recheck before reuse** if the card is older than 12 months, if WCAG/platform policy changed, or if a client incident was traced to it.

## Output
- Completed pattern card text, ready to append to `docs/31`.
- The blocker line for the code review.
- The test row for `tools/qa_matrix.py`.
- An explicit status and, for level-3 cards, the local test that would promote or kill it.

## Refusal conditions (these never become rules)
- "It looks premium", "our competitors do it", awards, or gallery presence as justification.
- Star counts, download counts or a polished demo as a maintenance signal.
- Any claim that a pattern improves conversion without a test design.
- Any pattern whose implementation we cannot verify ourselves in ≤4 hours.
- Any pattern requiring copying protected expression (code, assets, copy, screenshots, logos, trade dress).
- Any pattern that cannot state its accessibility impact or its performance cost.

## Never
- Never promote a level-3 hypothesis to a launch gate without a documented local test.
- Never cite a statistic that was not verified at its primary source in this session (`[verify finding]` otherwise).
- Never let a pattern card exist without a test and an anti-pattern.
- Never sell a rule as a compliance guarantee; WCAG conformance depends on the complete project and its testing.
