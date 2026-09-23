# Quality Master Prompt — Phase 2 (motion, discoverability, AI assets, credibility)
<!-- v0.1 · 2026-09-23 · run after Phase 1 · this run also consolidates both phases into one cookbook -->

## How to run this
- **Phase 2 domains:** motion & interaction feel · SEO / metadata / structured data · AI assets & disclosure · portfolio & case-study credibility (proof).
- Same constraints as Phase 1 — restate them in the prompt, do not assume the model remembers.
- This run **completes** the card set to 40 patterns + 40 anti-patterns, produces the tier standards (E) and the 30-day calendar (G) if Phase 1 left them thin, and performs the consolidation step (§I below).
- Phase 2 is where the temptation to be decorative is highest. The rule: a motion, SEO or AI-asset rule only exists if it changes what we build, test or gate.

---

## PROMPT (copy from here)

You are continuing a two-phase quality audit inside `proofline-studio-os/`. Phase 1 covered hero clarity, CTA, forms, accessibility and performance and produced `research/quality-run-<phase1-date>.md`. You are now auditing the **remaining domains** and then consolidating everything.

**Phase scope (this run):**
`motion & interaction · SEO / metadata / structured data · AI assets & provenance / disclosure · portfolio & case-study credibility`
Artefacts in scope: `{FILES_OR_URLS}` · tier context: `{TIER}` · audience: `{ICP}`

### Non-negotiable constraints (restated, not inherited)
1. **Evidence ladder:** Level 1 normative → gate · Level 2 technical → implementation · Level 3 research → testable hypothesis + the local test that settles it · Level 4 observational → visual vocabulary only, never a gate, never causal proof.
2. **Cite or drop.** `[VERIFY]` instead of any unverified number. Mark `VERIFIED` / `INFERRED` / `UNVERIFIED` per statement.
3. **No fabrication.** Particularly strict here: motion showcases, "awards", engagement metrics and case-study results are the easiest things to invent. Nothing goes in a deliverable that a client could not audit.
4. **No protected expression.** Motion techniques, layouts and structure may be studied; assets, code, copy and trade dress may not be reproduced. Independent-concept labelling stays on every demonstration artefact.
5. **Licence awareness.** Every runtime, animation file, icon set, font, image and model output carries a licence/provenance entry; unknown → `DO NOT SHIP UNTIL CONFIRMED`.
6. **Motion is accessibility work**, not decoration: vestibular safety, reduced-motion as the default state, pause controls, and meaning never carried by motion alone.
7. **AI transparency is a duty, not a preference:** never present synthetic people as real staff or customers; realistic synthetic imagery is disclosed human-readably at first exposure; no client material in generative tools. ⚖️ for any sector-specific question.
8. **Never promise rankings, compliance or conversion.** We publish method, tests and receipts.
9. **No trend reporting.** Galleries and award sites are vocabulary sources only.

### Required output — produce A through H in this order

**A. Verdict + evidence map.** What the artefact does well (with proof), what is decorative, what is risky (especially: undisclosed AI content, unlicensed assets, motion that harms, schema that is not eligible), what is missing. Table of sources: level, URL, what it justifies, and which sources you rejected.

**B. Must-pass checklist** for the phase domains only (motion, SEO, AI assets, portfolio credibility), same format as Phase 1: criterion id, reference, automated/manual, tool, pass condition, block level.

**C. 20 pattern cards** completing the set to 40, in the identical format. Every card names its local test and its anti-pattern.

**D. 20 anti-pattern cards** completing the set to 40 (S1/S2/S3 + reason + replacement). Include the reputational/legal ones: undisclosed synthetic imagery, unlicensed animation files, invented case-study numbers, self-serving review markup, SEO claims we cannot substantiate.

**E. Price-tier standards.** Complete/refresh the table for all four phase-2 domains across the three tiers, with explicit exclusions and the "next sprint" boundary.

**F. Validation loop.** Confirm or refine `candidate → evidence → PoC → human review → pilot → QA receipt → approved/deprecated`, including deprecation triggers specific to this phase (a runtime changing licence, a platform policy change on AI disclosure or structured data, a motion pattern causing reported discomfort).

**G. 30-day calendar.** Day-by-day, including: motion audit on real devices, schema validation after the first content change, AI-asset provenance reconciliation, and the day-30 decision on which patterns get promoted from Hypothesis.

**H. Research gaps + refusals.** Open questions with ⚖️ where law is involved; explicit refusals.

### I. Consolidation (phase 2 only)
1. Merge Phase 1 + Phase 2 cards into one file (`docs/31-…`): no duplicates, cross-references where two domains collide (e.g. motion ∩ accessibility ∩ performance), and a single set of ids (`HERO-`, `NAV-`, `MSG-`, `CTA-`, `FORM-`, `PROOF-`, `TYPE-`, `A11Y-`, `PERF-`, `MOT-`, `SEO-`, `AI-`, `OPS-`).
2. Verify: 40 pattern cards, 40 anti-pattern cards, one must-pass checklist, tier table, validation loop, 30-day calendar, gaps — all present, nothing padded.
3. Ensure every card maps to (a) a code-review blocker line and (b) a test row in `tools/qa_matrix.py`; run `python3 tools/qa_matrix.py --check` and report the result.
4. Report conflicts between the two phases explicitly (e.g. a performance budget fighting an animation pattern) and resolve them with a stated priority: **accessibility > correctness > performance > motion > aesthetics**.

### Hard refusals
Refuse to: treat an award-winning or gallery-featured site as evidence; recommend motion that cannot be disabled in CSS; recommend AI imagery pretending to be documentary photography of real people; recommend buying review or engagement metrics; write SEO advice that promises rankings; or mark a card `Approved default` without a human owner and a test.

### Run mechanics
- Update `docs/31-…`, write `research/quality-run-<phase2-date>.md`, update `tools/qa_matrix.py`, and note in the run file what changed and what stayed open.
- End with "Human decisions required:" listing the ≤5 decisions only a person can make — including which patterns to publish as the studio's public quality standard.

## PROMPT (to here)

---

## Post-run merge check (human)
- [ ] 40 + 40 cards, no duplicates, no padding, every id resolvable.
- [ ] No level-4 (observational) item acting as a gate anywhere.
- [ ] Motion rules all name their reduced-motion behaviour.
- [ ] AI rules all reference a provenance record and a disclosure decision.
- [ ] `python3 tools/qa_matrix.py --check` returns OK.
- [ ] The cookbook can be handed to a client as our method — and contains no claim we could not defend in a room with their lawyer. ⚖️
