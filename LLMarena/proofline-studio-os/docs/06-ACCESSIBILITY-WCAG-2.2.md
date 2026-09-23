# 06 — Accessibility: WCAG 2.2 AA standard and method
<!-- v0.1 · 2026-09-23 · owner: agent drafts, founder signs · review: on any W3C update -->

## Standard
Target: **WCAG 2.2 Level AA** (W3C Recommendation). WCAG 2.2 adds nine success criteria and removes 4.1.1 Parsing.
Relevant for us and **new since 2.1**: 2.4.11 Focus Not Obscured (Minimum, AA) · 2.5.7 Dragging Movements (AA) · 2.5.8 Target Size Minimum (AA, 24×24 CSS px) · 3.2.6 Consistent Help (A) · 3.3.7 Redundant Entry (A) · 3.3.8 Accessible Authentication (Minimum, AA).

## What automated tools can and cannot do
`axe-core` catches roughly a third of realistic issues (contrast, names, roles, target size, some structure). It cannot judge meaning, alt-text quality, reading order, focus order, or whether a keyboard trap exists in practice. **Automated pass ≠ accessible page.** Both layers are required; the manual layer is not optional.

## Canonical manual test script (≤45 min per page)
1. **Keyboard sweep:** Tab through the whole page. Every interactive element reachable, focus always visible, focus never fully hidden by the sticky header or a dialog, order matches reading order. Escape closes overlays. No traps.
2. **Focus + switcher:** switch design direction by keyboard only — focus must not jump, the page must not reload, the change is announced once.
3. **Forms:** labels programmatically associated · errors announced in a summary and at the field · no error relies on colour · success is announced · nothing is lost on error.
4. **Zoom/reflow:** 200% zoom and 320 px width — no horizontal scroll, no clipped content, no overlap.
5. **Contrast:** verify each direction's token pairs (body ≥4.5:1, large ≥3:1, UI/focus ≥3:1). Text over imagery gets a scrim, not luck.
6. **Motion:** set OS "reduce motion" — all non-essential motion gone (see `docs/05`).
7. **Media:** every image has an alt that serves its purpose (or `alt=""` when decorative); video has captions if it carries words.
8. **Screen reader spot-check** (VoiceOver or NVDA): hero, one form, one dialog, the switcher.
9. **Touch targets:** ≥24×24 CSS px with spacing; thumb-reach check on the actual mobile layout.
10. **Help consistency:** the same help affordance in the same relative place on every page (3.2.6).

## Automation (CI, every PR)
```
npx playwright test            # smoke + keyboard path
npx axe <preview-url>          # 0 critical, 0 serious to merge
```
Attach both outputs to the launch receipt. A waiver is only possible for a *moderate/minor* finding, must name the reason, the affected users and the fix date — never for contrast, names, focus visibility or keyboard access.

## Wording rules (avoid legal exposure)
- ✅ "Built to WCAG 2.2 AA; tested with axe-core and a documented manual keyboard/zoom review on <date>."
- ❌ "Fully accessible", "certified accessible", "accessible for everyone".
- Publish an **accessibility statement** per site: standard, method, known limitations, contact, review date.
- Note for clients: the European Accessibility Act applies to many consumer-facing digital services from 28 June 2025, with a micro-enterprise exemption (<10 employees **and** ≤€2 M) for services only — and it disappears as a client grows. We are not their legal advisor; we hand them the evidence and the wording. ⚖️
