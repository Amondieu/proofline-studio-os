#!/usr/bin/env python3
"""qa_matrix.py — Proofline QA test matrix generator.

Single source of truth for the rule -> test linkage:
  docs/31 (cookbook) §5 checklist  ->  WCAG 2.2 AA criteria  ->  test rows
Each row states: id, criterion, what it protects, automated/manual, tool,
pass condition, block level (A = cannot launch, M = must pass, F = fix when touched).

Usage:
  python3 tools/qa_matrix.py                 # print summary + write research/qa-matrix.md
  python3 tools/qa_matrix.py --check         # verify every docs/31 §5 item has a row
  python3 tools/qa_matrix.py --json          # machine-readable output
"""
from __future__ import annotations
import argparse, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COOKBOOK = ROOT / "docs" / "31-EVIDENCE-BACKED-QUALITY-COOKBOOK.md"
OUT_MD = ROOT / "research" / "qa-matrix.md"

# block: A = cannot launch (no waiver) · M = must pass · F = fix when touched
TESTS: list[dict] = [
    # --- WCAG 2.2 new AA criteria (regression-prone: teams know 2.1, miss 2.2) ---
    dict(id="T-A11Y-201", card="A11Y-001", wcag="2.4.11 Focus Not Obscured (Minimum)", level="A",
         checks="Every focused element is fully visible: sticky header/footer, cookie banner and chat widgets do not cover it; scroll-padding matches sticky height.",
         mode="manual", tool="Keyboard sweep at 375px and 1280px", evidence="waiver", pass_condition="No focused element overlapped by author content."),
    dict(id="T-A11Y-202", card="A11Y-002", wcag="2.5.8 Target Size (Minimum)", level="A",
         checks="All interactive targets >= 24x24 CSS px, or >= 24px diameter non-overlapping spacing.",
         mode="automated+manual", tool="axe-core + devtools measurement", evidence="blocker", pass_condition="0 violations; manual spot-check of icon-only controls."),
    dict(id="T-A11Y-203", card="A11Y-002", wcag="2.5.7 Dragging Movements", level="A",
         checks="Every drag interaction (slider, compare, carousel, reorder) has a single-pointer alternative.",
         mode="manual", tool="Manual interaction test", evidence="blocker", pass_condition="Task completable with buttons/taps only."),
    dict(id="T-A11Y-204", card="A11Y-005", wcag="3.3.7 Redundant Entry", level="A",
         checks="Multi-step flows do not request information already supplied; autofill or 'same as above' offered.",
         mode="manual", tool="Flow walkthrough", evidence="blocker", pass_condition="No repeated field in a live multi-step flow."),
    dict(id="T-A11Y-205", card="NAV-001/A11Y-005", wcag="3.2.6 Consistent Help", level="M",
         checks="Contact/help affordance appears in the same relative order on every template.",
         mode="manual", tool="3-template comparison", evidence="waiver", pass_condition="Same relative position on all templates."),
    # --- accessibility core ---
    dict(id="T-A11Y-101", card="A11Y-001", wcag="2.4.7 Focus Visible", level="A",
         checks="Focus indicator >= 2px with >= 3:1 contrast against adjacent colours; never outline:none without replacement.",
         mode="manual", tool="Keyboard sweep", evidence="blocker", pass_condition="Every focusable element shows a visible indicator."),
    dict(id="T-A11Y-102", card="A11Y-003", wcag="1.4.3 / 1.4.11 Contrast", level="A",
         checks="Text >= 4.5:1 (large >= 3:1); UI components and graphics >= 3:1; text over imagery has scrim/plate.",
         mode="automated+manual", tool="axe-core + token pair script + manual check over imagery", evidence="blocker",
         pass_condition="0 contrast violations; 0 unreadable text over images at 320px."),
    dict(id="T-A11Y-103", card="A11Y-004 / MOT-003", wcag="2.2.2 / 2.3.3 (AAA target)", level="A",
         checks="Static state is default; motion only under prefers-reduced-motion: no-preference; >5s moving content has pause.",
         mode="automated+manual", tool="OS reduced-motion toggle per direction", evidence="blocker",
         pass_condition="All three directions usable with reduced motion on."),
    dict(id="T-A11Y-104", card="FORM-001", wcag="1.3.1 / 3.3.1 / 3.3.2 / 4.1.3", level="A",
         checks="Persistent visible labels, programmatic association, error text linked via aria-describedby, error summary on top for multi-field forms.",
         mode="automated+manual", tool="axe-core + screen reader (VoiceOver/NVDA) + invalid submit", evidence="blocker",
         pass_condition="Every field announced with its label and error; failure never silent."),
    dict(id="T-A11Y-105", card="TYPE-001/002", wcag="1.4.4 / 1.4.10 / 1.3.1", level="A",
         checks="200% zoom and 320px reflow without loss of content or functionality; sequential headings, exactly one h1.",
         mode="manual+automated", tool="Zoom test + heading outline + axe", evidence="blocker",
         pass_condition="No clipping, no horizontal scroll trap, valid heading order."),
    dict(id="T-A11Y-106", card="CTA-001", wcag="2.5.3 Label in Name", level="M",
         checks="Accessible name of every control starts with the visible label text.",
         mode="automated", tool="axe-core label-content-name-mismatch", evidence="blocker", pass_condition="0 violations on interactive controls."),
    # --- forms & conversion path ---
    dict(id="T-FORM-101", card="FORM-001", wcag="3.3.7 flow integrity", level="A",
         checks="End-to-end submission test on mobile: values retained on error, confirmation visible, record/email received.",
         mode="manual", tool="Real device submit x3", evidence="blocker", pass_condition="3/3 received; error path retains input."),
    dict(id="T-FORM-102", card="FORM-004", wcag="3.3.1 n/a (business)", level="A",
         checks="Failure path designed and monitored: fallback contact shown when endpoint is unreachable; alert fires when submissions stop.",
         mode="manual", tool="Endpoint simulation + monitoring check", evidence="blocker", pass_condition="Fallback path works; alerting confirmed."),
    dict(id="T-FORM-103", card="FORM-003", wcag="3.3.8 consider", level="M",
         checks="Spam protection does not require a cognitive test from legitimate users; scripted spam blocked.",
         mode="manual", tool="Turnstile/honeypot + scripted submission", evidence="waiver", pass_condition="Spam blocked; 3/3 legitimate mobile submits pass."),
    dict(id="T-FORM-104", card="FORM-002", wcag="n/a (GDPR)", level="M",
         checks="Every stored field justified in the brief and described in the privacy notice.",
         mode="manual", tool="Field-by-field review against notice", evidence="blocker", pass_condition="No undeclared field."),
    # --- performance ---
    dict(id="T-PERF-101", card="HERO-003/PERF-001", wcag="n/a", level="M",
         checks="LCP <= 2.2s lab baseline; LCP element dimensioned and not lazy-loaded.",
         mode="automated", tool="Lighthouse mobile + devtools LCP element", evidence="waiver", pass_condition="LCP <= 2.2s; element identified in the receipt."),
    dict(id="T-PERF-102", card="PERF-002", wcag="n/a", level="A",
         checks="CLS <= 0.05 after a full scroll on throttled mobile; no late injection above existing content.",
         mode="automated", tool="Lighthouse + throttled scroll test", evidence="blocker", pass_condition="CLS <= 0.05 (never waived above 0.1)."),
    dict(id="T-PERF-103", card="PERF-001", wcag="n/a", level="M",
         checks="Page weights within budget: HTML <= 30KB, CSS <= 50KB, JS <= 60KB, hero <= 180KB, <= 1 third-party script.",
         mode="automated", tool="Build output + network panel", evidence="waiver", pass_condition="All budgets met or a dated fix plan exists."),
    dict(id="T-PERF-104", card="PERF-004", wcag="n/a", level="A",
         checks="Zero third-party font requests; woff2 self-hosted; licence files present; fallback metrics matched.",
         mode="automated", tool="Network panel + repo check", evidence="blocker", pass_condition="0 cross-origin font requests; licences in repo."),
    dict(id="T-PERF-105", card="PERF-003/MOT-001", wcag="n/a", level="M",
         checks="INP <= 150ms target (<=200ms threshold); only transform/opacity animated; no scroll-jacking.",
         mode="automated+manual", tool="Lighthouse + interaction trace", evidence="waiver", pass_condition="No layout-property animation; INP within threshold."),
    # --- proof, trust, AI, legal ---
    dict(id="T-PROOF-101", card="PROOF-001", wcag="n/a (Omnibus/GDPR)", level="A",
         checks="Every public claim maps to a substantiation file; no invented testimonial, logo, metric or award.",
         mode="manual", tool="Claim-by-claim trace", evidence="blocker", pass_condition="100% of claims traceable."),
    dict(id="T-AI-101", card="AI-001/AI-002", wcag="n/a (AI Act Art. 50)", level="A",
         checks="Every AI asset has a provenance row + approval record; realistic synthetic people disclosed at first exposure or absent.",
         mode="manual", tool="asset-provenance-log.csv review", evidence="blocker", pass_condition="No unapproved or undisclosed AI asset."),
    dict(id="T-LEGAL-101", card="SEO-003", wcag="n/a (LCEN/GDPR)", level="A",
         checks="Mentions legales, privacy notice and accessibility statement present, accurate, footer-linked, indexable.",
         mode="manual", tool="Footer click-through on every template", evidence="blocker", pass_condition="1 click from any page; content matches the real entity."),
    dict(id="T-LEGAL-102", card="SEO-002", wcag="n/a (platform policy)", level="A",
         checks="No self-serving review markup; every structured-data fact visible on the page.",
         mode="automated+manual", tool="Rich Results Test + page cross-check", evidence="blocker", pass_condition="0 self-serving review markup."),
    # --- ops / handover ---
    dict(id="T-OPS-101", card="OPS-001", wcag="n/a", level="A",
         checks="Client owns and can log in to repo, hosting, domain, analytics, CMS, calendar before final invoice.",
         mode="manual", tool="Live login on call with the client", evidence="blocker", pass_condition="Client login verified by the client."),
    dict(id="T-OPS-102", card="OPS-002", wcag="n/a", level="M",
         checks="QA receipt reproducible by a second person; rollback rehearsed and timed.",
         mode="manual", tool="Receipt replay + rollback drill", evidence="waiver", pass_condition="All numbers reproducible; rollback <= 15 min."),
    # --- outbound (prospecting loop) ---
    dict(id="T-OUT-101", card="docs/30 §E", wcag="n/a (GDPR/CNIL)", level="A",
         checks="All nine Send Gate items true for the specific message; suppression query run the same day.",
         mode="manual", tool="templates/send-gate-checklist.md (skill: outreach-review)", evidence="blocker", pass_condition="9/9 true, approval id recorded."),
    dict(id="T-OUT-102", card="docs/30 §F", wcag="n/a (GDPR/CNIL)", level="A",
         checks="<=3 touches within 21-30 days; every opt-out suppressed immediately and permanently; list never re-imported.",
         mode="manual", tool="Prospect record log + suppression list review", evidence="blocker", pass_condition="0 contacts after an objection, ever."),
]

CHECKLIST_ITEM_TO_TEST = {
    1: "T-A11Y-202", 2: "T-A11Y-201", 3: "T-A11Y-203", 4: "T-A11Y-205", 5: "T-A11Y-204",
    6: "T-A11Y-103", 7: "T-PERF-104", 8: "T-PERF-102", 9: "T-PERF-103", 10: "T-FORM-101",
    11: "T-PROOF-101", 12: "T-LEGAL-102", 13: "T-LEGAL-101", 14: "T-AI-101", 15: "T-OPS-101", 16: "T-OPS-102",
}


def parse_checklist() -> dict[int, str]:
    text = COOKBOOK.read_text(encoding="utf-8")
    block = re.search(r"## 5\. Must-pass launch checklist.*?```(.*?)```", text, re.S)
    if not block:
        return {}
    items = {}
    for line in block.group(1).splitlines():
        m = re.match(r"\s*\[ \]\s*(\d+)\s+(.*)", line)
        if m:
            items[int(m.group(1))] = m.group(2).strip()
    return items


def check() -> int:
    items = parse_checklist()
    if not items:
        print("FAIL: could not parse docs/31 §5 checklist")
        return 1
    missing = [n for n in items if n not in CHECKLIST_ITEM_TO_TEST]
    orphan = [t for t in CHECKLIST_ITEM_TO_TEST.values() if t not in {x['id'] for x in TESTS}]
    print(f"checklist items parsed: {len(items)}")
    print(f"items without a test row: {missing or 'none'}")
    print(f"rows referencing unknown tests: {orphan or 'none'}")
    ok = not missing and not orphan
    print("RESULT:", "OK" if ok else "MISMATCH")
    return 0 if ok else 1


def markdown() -> str:
    items = parse_checklist()
    out = ["# QA test matrix (generated)", "",
           "Generated by `tools/qa_matrix.py`. Edit the script, never this file. "
           "Block levels: **A** = cannot launch (no waiver) · **M** = must pass · **F** = fix when touched.", "",
           f"- Tests: {len(TESTS)} · automated: {sum(1 for t in TESTS if t['mode'] == 'automated')} · "
           f"manual: {sum(1 for t in TESTS if t['mode'] == 'manual')} · mixed: {sum(1 for t in TESTS if '+' in t['mode'])}", "",
           "## Cookbook checklist → test mapping", "",
           "| checklist item (docs/31 §5) | test id |", "|---|---|"]
    for n, text in sorted(items.items()):
        out.append(f"| {n}. {text} | `{CHECKLIST_ITEM_TO_TEST.get(n, 'MISSING')}` |")
    out += ["", "## Tests", "", "| id | card | criterion | block | mode | pass condition | tool |", "|---|---|---|---|---|---|---|"]
    for t in TESTS:
        out.append(f"| `{t['id']}` | {t['card']} | {t['wcag']} | {t['level']} | {t['mode']} | {t['pass_condition']} | {t['tool']} |")
    out += ["", "## Pre-launch coverage", "",
            f"- Cannot-launch tests: {sum(1 for t in TESTS if t['level'] == 'A')}",
            f"- Manual-only tests (cannot be automated away): {sum(1 for t in TESTS if t['mode'] == 'manual')}",
            "- Every row feeds `templates/qa-launch-checklist.md` and the QA receipt (`schemas/qa-receipt.schema.json`).", ""]
    return "\n".join(out)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    if a.check:
        return check()
    if a.json:
        print(json.dumps({"tests": TESTS, "checklist": parse_checklist(),
                          "mapping": CHECKLIST_ITEM_TO_TEST}, indent=2, ensure_ascii=False))
        return 0
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(markdown(), encoding="utf-8")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"tests: {len(TESTS)} | cannot-launch: {sum(1 for t in TESTS if t['level']=='A')} "
          f"| manual: {sum(1 for t in TESTS if t['mode']=='manual')}")
    print("checklist items:", len(parse_checklist()), "| mapped:", len(CHECKLIST_ITEM_TO_TEST))
    return check()


if __name__ == "__main__":
    sys.exit(main())
