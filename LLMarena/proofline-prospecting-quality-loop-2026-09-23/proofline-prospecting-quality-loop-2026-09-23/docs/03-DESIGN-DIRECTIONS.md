# 03 — Design Directions
<!-- v0.1 · 2026-09-23 · owner: founder (sign-off) · source of truth for tokens.json -->

Tokens live in `tokens.json` and are emitted as CSS custom properties. **Switching direction may change tokens only** — never IA, section order, CTA wording, claim wording, legal content or accessibility behaviour.

## Token contract (all three directions)
```
--bg-base --bg-elevated --ink-strong --ink-muted --accent --accent-signal
--border-color --border-width --radius --shadow
--font-display --font-body --font-mono --scale-ratio --leading-tight --leading-body --tracking-display
--grid-cols --grid-gutter --container-max
--motion-fast --motion-base --motion-ease --motion-reveal-distance
--image-treatment --divider-style --section-padding-block
```
Accessibility is enforced per direction: body ≥4.5:1, large text ≥3:1, borders/focus ≥3:1 — verified by `python3 tools/contrast_check.py demo/direction-switcher.html` (exit 1 on any text failure), not by eye. Measured 2026-09-23 on the demo token set (T-A11Y-102): ink-strong 16.76 / 17.19 / 15.55 · ink-muted 5.87 / 9.37 / 5.86 · accent-ink on accent 5.22 / 5.00 / 7.39 · accent on bg-base 4.83 / **3.71** / 7.14 · signal on bg-base 5.87 / 14.0 / **4.03**. Bold values are below 4.5:1 — see the usage constraints in each direction's *do not cross* list.

---

## A · Precision System (B2B SaaS, AI, automation)
Quiet, structured, technical, high-trust.
```
--bg-base:#F7F6F3  --bg-elevated:#FFFFFF  --ink-strong:#14161A  --ink-muted:#5A6068
--accent:#1B5CFF  --accent-signal:#B8F24A (micro-signals only: focus dots, small ticks)
--border:1px solid rgba(20,22,26,.10)  --radius:6px
--font-display: Inter (OFL)  --font-body: Inter  --font-mono: IBM Plex Mono (OFL)
--scale-ratio:1.200  --leading-tight:1.15  --leading-body:1.55  --tracking-display:-0.01em
--grid:12col/24px  --container-max:1180px  --section-padding-block:88px
--motion:120–200ms opacity + 4px rise  --image-treatment: flat UI crops, diagrams, data
```
**Do not cross:** decorative gradients, glassmorphism, blobs, more than one accent per viewport, animated counters, `--accent` or `--accent-signal` used as body text, **`--accent-signal` (#B8F24A) on `--bg-base`** — it measures 1.23:1 there (WCAG 1.4.11 fails); it is a dark-ink-only micro-signal (13.66:1 on #14161A).

## B · Cinematic Authority (launches, creative brands)
Dramatic, editorial, premium, one idea per viewport.
```
--bg-base:#0B0B0C  --bg-elevated:#141416  --ink-strong:#F4EFE7  --ink-muted:#A9A29A
--accent:#C8332B  --accent-signal:#C9CDD2 chrome gradient (one use per page)
--border:1px solid rgba(244,239,231,.14)  --radius:2px
--font-display: Archivo-class condensed (OFL)  --font-body: Inter  --font-mono: none
--scale-ratio:1.333  --leading-tight:1.02  --leading-body:1.6  --tracking-display:0.02em (caps)
--grid:12col/40px asymmetric  --container-max:1440px  --section-padding-block:140px
--motion:400–700ms reveals, one loop ≤6s  --image-treatment: full-bleed, high-contrast, single hero composition
```
**Do not cross:** two accent colours, parallax on every section, autoplay video >2.5 MB, multiple simultaneous focal points, fonts loaded per component, `--accent` (#C8332B) as body text on `--bg-base` (3.71:1 — borders, icons and button fills only).

## C · Editorial Luxury (premium consultants, high-ticket services)
Quiet, cultivated, typographic, generous whitespace.
```
--bg-base:#F1EBE1  --bg-elevated:#E7DFD2  --ink-strong:#15140F  --ink-muted:#5B5A50
--accent:#6B6B3A (deep olive)  --accent-signal:#9A7B4F (muted brass, hairlines only)
--border:1px solid rgba(21,20,15,.16)  --radius:4px
--font-display: Fraunces-class serif (OFL)  --font-body: Inter  --font-mono: none
--scale-ratio:1.250  --leading-tight:1.1  --leading-body:1.65  --tracking-display:-0.005em
--grid:editorial 2-column measure, 24px gutter  --container-max:1240px  --section-padding-block:120px
--motion:200–300ms fades, 1px hairline shifts  --image-treatment: material/texture detail, wide crops
```
**Do not cross:** sans-serif display type, tight leading, more than two type sizes per section, drop shadows, saturated accents, `--accent-signal` (#9A7B4F) as anything but hairlines/borders (3.33:1 on `--bg-base` — passes the 3:1 non-text bar, fails as text).

---

## Switcher invariants (must hold for every direction)
- Identical DOM order, identical section copy, identical CTA wording and destination.
- Focus order unchanged by switching; the switcher announces only the direction name (`aria-live="polite"`).
- Reduced-motion path is the default code path in all three (`@media (prefers-reduced-motion: no-preference)` opts in).
- Contrast, target size (≥24×24) and focus visibility are re-verified per direction, every build.
- Switching never triggers a page reload or a layout shift >0.1 CLS.

## Direction selection rule (per client)
| Signal | Direction |
|---|---|
| Complex, technical, procurement-driven offer | A |
| Launch moment, entertainment/creative brand, needs impact | B |
| Advisory, high price point, relationship-led sale | C |
Choose one. The other two are *not* shown to the client as "options" — they are internal alternates if the brief changes.

---

## Spec ↔ artefact divergences (open — needs a human decision)
Found by the Phase-1 quality run (2026-09-23, `research/quality-run-2026-09-23.md`, MD-11/MD-12). This file is the token *spec*; `demo/direction-switcher.html` is an artefact built earlier from an earlier draft. They disagree in places, and **`tokens.json` referenced above does not exist yet**.

| Token / value | This spec | Demo | Note |
|---|---|---|---|
| Container max (A / B / C) | 1180 / 1440 / 1240 px | 1100 / 1240 / 1160 px | Demo is narrower; spec values were never implemented |
| Section padding-block (A / B / C) | 88 / 140 / 120 px | 80 / 120 / 104 px | Same pattern |
| C · `--accent` | #6B6B3A | #4F4F28 | Different olive; both pass as UI, spec value also passes as text (4.67:1) |
| C · `--accent-signal` | #9A7B4F | #8A6E45 | Both hairline-only |
| B · `--ink-muted` | #A9A29A | #B9B2A9 | Both pass ≥4.5:1 |
| Token names | `--bg-elevated`, `--border-color`, `--font-mono`, `--motion-fast` … | `--bg-elev`, `--border`, `--font-label`, `--reveal` … | Demo uses shorter local names; a mapping is required before generation |
| Precision `--accent-signal` | #B8F24A (intended "micro-signal") | same value, unused | Spec addition: dark-ink only (1.23:1 on `--bg-base`) |

**Decision required (human):** (a) reconcile the demo to this spec and generate both from a single `tokens.json`, or (b) amend this spec to the demo's values and declare the demo canonical. Until then, treat this file as intent and the demo as a standalone proof — never cite the demo as evidence that this spec is implemented.
