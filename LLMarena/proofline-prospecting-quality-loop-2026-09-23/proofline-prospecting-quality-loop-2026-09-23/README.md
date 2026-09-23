# Proofline — Prospecting & Quality Loop · 2026-09-23

**What this bundle is.** One self-contained folder with everything produced by the *Prospecting Evidence & Quality Loop* session: the prospecting/compliance operating policy, the evidence-backed quality standard, the reusable prompt pair, the executable QA tooling, and the executed Phase-1 quality run with its real findings and fixes.

**Why this folder name.** `proofline-prospecting-quality-loop-2026-09-23` — brand, the two strand names, ISO date for sortability. Lowercase, hyphens only, no spaces or umlauts, so it survives every OS, zip tool, network share and URL.

---

## Reading order (30–45 minutes)

| # | File | Why |
|---|---|---|
| 1 | `README.md` (this file) | Scope, verification, open items |
| 2 | `docs/30-PROSPECTING-DATA-SOURCES.md` | How prospects may be found, contacted and suppressed — with the 9-condition Send Gate |
| 3 | `docs/31-EVIDENCE-BACKED-QUALITY-COOKBOOK.md` | The quality standard: evidence ladder, 40 pattern cards, 40 anti-patterns, must-pass checklist, code-review blockers, tier standards |
| 4 | `research/quality-run-2026-09-23.md` | The Phase-1 run **actually executed** on `demo/direction-switcher.html`: findings MD-01…MD-13, what was fixed, what stayed open |
| 5 | `verification/RESULTS.md` | Captured command output proving the checks (matrix, contrast, counts) |
| 6 | `context/MASTER-REPORT.md` §14 | The addendum that places this loop inside the v1 mission report |

---

## Contents

```text
docs/         30 prospecting data sources · 31 quality cookbook (both new)
              03 design directions (updated: measured contrast + divergence table)
templates/    send-gate checklist · 3-touch email sequences · quick teardown · LIA · suppression list · prospect record example
schemas/      prospect-record · suppression-record   (JSON Schema, valid)
skills/       outreach-review · evidence-quality     (SKILL.md with refusal conditions)
prompts/      quality master prompt phase 1 · phase 2 (+ consolidation step)
tools/        qa_matrix.py · contrast_check.py       (both runnable, no dependencies)
research/     quality-run-2026-09-23.md · qa-matrix.md (generated) · poc-backlog.md
demo/         direction-switcher.html                (the reviewed artefact, 0 external requests)
context/      MASTER-REPORT.md · README.md           (mission v1, for orientation)
verification/ RESULTS.md                             (captured evidence)
MANIFEST.csv  every file: size, purpose, sha256 prefix
```

## Verification (reproduce in 10 seconds)

```bash
python3 tools/qa_matrix.py --check                        # → 16/16 checklist items mapped · RESULT: OK
python3 tools/contrast_check.py demo/direction-switcher.html   # → 21 pairs PASS · TEXT failures: 0 · exit 0
```

Structural counts, checked when the bundle was built: **40 pattern cards · 40 anti-pattern rows · 9 Send Gate conditions · 7 JSON schemas valid · 0 external requests in the demo.** Full output in `verification/RESULTS.md`.

## What is genuinely new here (versus mission v1)

1. **A compliant prospecting path that does not depend on scraping:** registry verification (INSEE SIRENE / Companies House), manually read public pages, an 8-field record, and a nine-condition gate that must be 100 % true before any message leaves the drafts folder.
2. **Suppression as an engineering discipline:** minimal record, immediate and permanent effect, never exported as a target list, with the sequence capped at 3 touches in 21–30 days.
3. **A quality standard with an evidence ladder** where normative and technical sources become launch gates, research becomes a testable hypothesis, and galleries are vocabulary only — never proof.
4. **Rules as a triple:** every rule exists as a pattern card → a code-review blocker line → a QA test row, verified by `qa_matrix.py --check`.
5. **Real defects found and fixed** in the studio's own demo: sticky-chrome focus obscuring (WCAG **2.4.11**, new in 2.2), motion running despite `prefers-reduced-motion`, post-paint direction restore, and a token that measured **1.23:1** on the light background.
6. **One structural gap made explicit:** `tokens.json` does not exist yet, and the spec (`docs/03`) and the demo disagree on several values — documented with a decision request instead of silently reconciled.

## Open items / human decisions (unchanged, waiting for you)

1. **Token decision:** does the spec (`docs/03`) win over the demo on container widths, section padding and two editorial colour values? → then generate `tokens.json` (POC-11).
2. **Run Phase 2** on the studio's own site once the form endpoint exists (POC-04), so motion/SEO/AI rules are validated against a complete page.
3. **Promote or hold** `contrast_check.py` and `qa_matrix.py` as *Approved default* (needs a second project).
4. **Legal wording** for mentions légales, privacy notice, accessibility statement — before any public launch. ⚖️
5. **Publish `docs/31` as the public quality standard**, or keep it internal until the first paid project validates it?

## Honest limits of this bundle

- Not legal advice. Every legal statement is an operating policy with cited sources; ⚖️ marks what needs counsel review (LIA, Pappers redistribution clause, Notion EU hosting/DPA, disclosure wording).
- Level-3 research findings (Baymard/NN-g percentages) are **not** quoted; the rules stand on their own tests. `[VERIFY]` marks anything that needs primary-source confirmation.
- Phase 2 of the quality prompt (motion, SEO, AI assets, portfolio) is written but **not yet executed** against a real artefact.
- Metrics in `docs/30 §H` are internal experiment thresholds — never presented to a client as promises.
