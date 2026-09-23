---
name: performance-qa
description: Measure a page against the Proofline performance budget and Core Web Vitals, then produce a receipt with the exact numbers and any waiver. Use before every launch, after any motion or media change, and at day 7/30/90 post-launch.
---
# performance-qa

## Inputs
Preview or production URL · the page templates in scope · the current motion/media inventory.

## Procedure
1. **Lab pass:** Lighthouse mobile (throttled) — record performance score, LCP, TBT, CLS, and the total transferred JS/CSS/images.
2. **Field pass** where the site is live: LCP/INP/CLS at p75 over ≥28 days (mobile and desktop separately). If it is too new for field data, say so instead of implying field results.
3. **Budget diff:** compare weights to `docs/07` (HTML ≤30 KB, CSS ≤50 KB, JS ≤60 KB, fonts ≤2 families, hero ≤180 KB, third-party ≤1 script).
4. **Motion cost:** interactive measurement (Playwright + trace) of INP on a scripted scroll + form interaction; confirm no motion runs inside the LCP element and no animation runs while hidden.
5. **Regression triage:** for every miss, name the cause (third-party script, unoptimised image, hydration, font loading, layout shift) — the fix must be the *smallest* change that resolves it.
6. **Record** the receipt: command, tool versions, URL, date, device profile, numbers, waiver (if any) with rationale and a fix date.

## Output
`templates/qa-launch-checklist.md` (performance section) + a receipt block + a one-line plain-language summary for the client.

## Refusal conditions
- A miss on a cannot-launch item (CLS/layout stability harming real usage, motion without reduced-motion path) → block the launch.
- A waiver without a named cause and fix date → refuse.
- 3D/WebGL proposed on mobile-critical pages → require a written business case and a static fallback (§11 stop condition).

## Never
Never present lab scores as field performance. Never optimise a number by hiding content. Never add a tag manager "to measure later".
