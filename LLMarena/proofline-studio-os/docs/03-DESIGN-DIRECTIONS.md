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
Accessibility is enforced per direction: body ≥4.5:1, large text ≥3:1, borders/focus ≥3:1 — verified in CI (`tools/check-contrast.mjs`), not by eye.

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
**Do not cross:** decorative gradients, glassmorphism, blobs, more than one accent per viewport, animated counters.

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
**Do not cross:** two accent colours, parallax on every section, autoplay video >2.5 MB, multiple simultaneous focal points, fonts loaded per component.

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
**Do not cross:** sans-serif display type, tight leading, more than two type sizes per section, drop shadows, saturated accents.

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
