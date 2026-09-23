# Proofline Studio OS

A research-backed, licence-audited operating system for a one-person premium landing-page studio
(positioning → copy → design direction → build → QA → launch → handover → proof).

<!-- v0.1 · 2026-09-23 · owner: founder · next review: 2026-12-23 -->

## Read in this order
1. `MASTER-REPORT.md` — the research mission, decisions, scores, 14-day plan, risk register.
2. `docs/00-STUDIO-PRINCIPLES.md` — the non-negotiables (read before any client conversation).
3. `docs/03-DESIGN-DIRECTIONS.md` + `demo/direction-switcher.html` — the three sellable directions.
4. `docs/09-LAUNCH-QA.md` — the gate that decides whether anything goes live.
5. `research/resource-inventory.csv` + `research/license-register.csv` — why each tool is (not) allowed.

## The V1 stack (one per slot — no exceptions without an ADR)
Astro 7 · Tailwind 4 · Base UI + selective shadcn/ui copy-ins · Cloudflare Pages (client-owned)
· Cloudflare Worker + D1 form endpoint · Tally (intake) · Cal.com (booking) · Plausible (EU analytics)
· self-hosted OFL fonts + Lucide SVG · axe-core + Playwright + Lighthouse CI.

## The 7 gates (human approval required)
1. **Licence gate** — no dependency ships without a row in `research/license-register.csv`.
2. **Message gate** — no copy without a `templates/message-map.md` and a named evidence type.
3. **Direction gate** — no design without a signed design-direction brief and the "do not imitate" check.
4. **Accessibility gate** — 0 critical/serious axe findings + manual keyboard sweep (WCAG 2.2 AA).
5. **Performance gate** — LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 (p75) with a lab budget assertion.
6. **Asset/provenance gate** — every asset logged; every AI asset approved before production.
7. **Ownership gate** — client owns repo, hosting, domain, analytics before the final invoice.

## What is in here
```text
MASTER-REPORT.md      the full mission report (verdict, architecture, scores, stack, blueprint, plan, risks)
                      + §14 addendum: the Prospecting Evidence & Quality Loop
README.md             this file
docs/00–13            principles · offer/ICP · message architecture · design directions · component allowlist
                      motion budget · WCAG 2.2 · performance budget · privacy/AI/asset policy · launch QA
                      handover · case-study disclosure · delivery SOP · sales & portfolio
docs/30               prospecting data sources, Send Gate (9), hot-signal model, metrics, sequence + suppression, guardrails
docs/31               evidence-backed quality cookbook: evidence ladder, 40 pattern cards, 40 anti-patterns,
                      must-pass checklist, validation loop, 13 code-review blockers, tier standards, gaps
skills/               9 SKILL.md files: studio-research · conversion-copy · creative-direction · landing-page-build
                      accessibility-qa · performance-qa · launch-review · outreach-review · evidence-quality
templates/            client intake · message map · teardown report · direction brief · provenance log · AI asset approval
                      QA receipt · handover packet · case study · send-gate checklist · outreach sequences (3 touches)
                      quick 3-point teardown · LIA for B2B outreach · suppression list · prospect record example
schemas/              7 JSON schemas: project brief · design direction · asset record · QA receipt · approval record
                      prospect record · suppression record
prompts/              Higgsfield hero concepts + motion loops · copy message map · teardown analysis · build spec
                      quality master prompt phase 1 (hero/CTA/forms/a11y/perf) and phase 2 (motion/SEO/AI/portfolio)
research/             github-audit.csv (38 repos, API-verified 2026-09-23) · resource-inventory.csv (61 scored)
                      license-register.csv (51 rows) · rejected-resources.md · poc-backlog.md (POC-01…12)
                      qa-matrix.md (generated) · quality-run-2026-09-23.md (phase-1 run, findings MD-01…MD-13)
demo/                 direction-switcher.html — self-contained, offline-capable proof of the 3 token sets
tools/gate.sh         the one-command QA gate (implemented on day 4 of the plan)
tools/qa_matrix.py    rule → test mapping; `--check` verifies every docs/31 §5 item has a test row
tools/contrast_check.py  token-pair WCAG contrast audit; exit 1 on any failing text pair
```

## The loop in one picture
```text
public signal (official source) → prospect record (8 fields) → Send Gate (9/9) → 3-point teardown
        → ≤3 touches in 21–30 days → reply | opt-out (immediate, permanent suppression)
        → every repeated finding becomes a pattern card → code-review blocker → QA test row
```

## Commands (to be implemented on day 4)
```bash
npm run gate    # lint → axe → Lighthouse budgets → Playwright smoke
python3 research/score_resources.py   # regenerate the scored inventory
```

## Absolute red lines
Never fabricate proof · never clone a brand's expression · never upload client material to a generative tool
· never publish an accessibility or compliance *guarantee* · never hold client accounts hostage.
