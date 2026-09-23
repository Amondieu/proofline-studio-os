# 07 — Performance Budget
<!-- v0.1 · 2026-09-23 · owner: agent drafts, founder signs · measured on every preview deploy -->

## Field targets (the promise) — Core Web Vitals at the 75th percentile
| Metric | Good threshold | Our launch target | Measure with |
|---|---|---|---|
| LCP (Largest Contentful Paint) | ≤ 2.5 s | **≤ 2.2 s mobile** | CrUX / field RUM or Vercel/Cloudflare analytics + Lighthouse lab as a proxy |
| INP (Interaction to Next Paint) | ≤ 200 ms | **≤ 150 ms** | field data; lab proxy via throttled Lighthouse + Playwright traces |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | **≤ 0.05** | field + `PerformanceObserver` in the QA run |

Reality check for expectation-setting: only ~56% of origins pass all three (May 2026 CrUX). Passing is a *differentiator*, not a baseline — say so, honestly.

## Lab gates (blocking, in CI)
- Lighthouse mobile: performance ≥ 95, accessibility = 100 (or the documented waiver), LCP ≤ 2.0 s, TBT ≤ 200 ms.
- Page weights (compressed): HTML ≤ 30 KB · CSS ≤ 50 KB · JS ≤ 60 KB (home) · fonts ≤ 2 families / 4 files.
- Images: AVIF or WebP only · hero ≤ 180 KB · every image with width/height · `loading="lazy"` below the fold · no layout shift on load.
- Video: `preload="none"`, poster present, ≤ 2.5 MB, no autoplay with sound.
- Third-party: **one** script maximum (analytics). Each additional one needs a written note in the QA receipt and a re-measured budget.

## Implementation rules
1. Static-first: no client-side routing, no hydration of static sections, islands only for interactive parts.
2. Fonts self-hosted, subsetted, `woff2`, `<link rel="preload">` for the display font only, `font-display: swap` + metric-compatible fallback to avoid CLS.
3. Critical CSS inline where practical; everything else deferred.
4. `content-visibility: auto` for long below-fold sections; `fetchpriority="high"` on the LCP image only.
5. No layout-affecting animation, no synchronous third-party <script> in <head>, no tag managers.
6. Cache everything static; long-lived hashed assets; HTML revalidated.

## Measurement ritual
- Every preview deploy: Lighthouse CI assertions (`npm run gate`).
- Before launch: one throttled mobile run + one real-device run (iPhone Safari, mid-range Android Chrome).
- After launch: field check at day 7, 30 and 90; if a metric regresses, it becomes the next single change — not a redesign.
