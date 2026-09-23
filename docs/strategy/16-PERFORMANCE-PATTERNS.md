# 16 — Performance patterns

Performance is measured evidence, not a visual preference. Proofline uses the
Core Web Vitals good thresholds as production targets: LCP ≤ 2.5 s, INP ≤ 200
ms, and CLS ≤ 0.1 at the 75th percentile when field data is available. Lab
measurements are still useful, but they must be labelled as lab evidence.

## Approved V1 rules

1. Identify the likely LCP element before styling the hero.
2. Do not lazy-load the LCP image or video; compress and size it deliberately.
3. Reserve image, video, iframe, and embed dimensions.
4. Self-host a small, licensed font set and verify fallback behavior.
5. Defer non-essential scripts and keep third-party scripts to one by default.
6. Prefer static HTML and small islands over a client-side application shell.
7. Use poster-first video and provide a useful static alternative.
8. Record JS bytes, media bytes, script count, LCP, INP, and CLS in the receipt.

## Test matrix

| Test | Evidence |
|---|---|
| Lab mobile preview | LCP, INP where available, CLS, JS/media size |
| Field data | 75th-percentile Core Web Vitals when traffic exists |
| Slow font/media path | No unreadable flash or layout shift |
| Direction switcher | No reload, no unexpected shift, same content order |
| Long page scroll | No repeated heavy work or hidden controls |

## Anti-patterns

Lazy LCP, unbounded media, six font families, render-blocking analytics,
duplicated trackers, late consent injection, chat before primary content, and
heavy shaders without a fallback are launch blockers until corrected or
explicitly reviewed.
