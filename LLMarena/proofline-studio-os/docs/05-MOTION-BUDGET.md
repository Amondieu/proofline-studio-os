# 05 — Motion Budget
<!-- v0.1 · 2026-09-23 · owner: agent drafts, founder approves · per-project budget signed in the direction brief -->

## Motion Escalation Ladder — start at rung 0, justify every step up
| Rung | Technique | Allowed by default? | Typical cost | Justify when |
|---|---|---|---|---|
| 0 | No motion | yes | 0 KB | always acceptable — quiet is a direction |
| 1 | CSS transitions (hover/focus/state) | yes | 0 KB | every interactive element |
| 2 | CSS reveal on scroll (IntersectionObserver + transform/opacity) | yes | ≤1 KB | introducing sections on long pages |
| 3 | Component motion (Motion for React, in an island) | conditional | 15–35 KB | stateful UI: dialog, tabs, switcher, drag alternative |
| 4 | Short video loop (muted, ≤6 s) | conditional | ≤2.5 MB | a real product/film asset exists and mobile data allows |
| 5 | 3D / WebGL / shader | exception | 150 KB–1 MB | written business case + static fallback + mobile opt-out |

## Per-page budgets (V1)
- Home: JS ≤60 KB compressed · motion JS ≤20 KB of it · max 1 rung-3 effect above the fold.
- Any page: max 2 rung-2+ effects · no motion may delay LCP by >100 ms · no motion inside the LCP element.
- Total animation-related main-thread work per interaction <50 ms (measure INP on a throttled Moto-class profile).
- Zero layout-affecting animation (animate `transform`/`opacity` only; `will-change` used sparingly and removed after).

## Reduced motion (mandatory, non-negotiable)
- Author the static state as the default; opt *into* animation with `@media (prefers-reduced-motion: no-preference)`.
- Never ship an animation that can only be reduced by a JS check — CSS must handle it.
- Parallax, autoplay loops, large translations and infinite marquees are disabled entirely under reduced motion.
- WCAG 2.3.3 (AAA) is our internal target even though AA does not require it — vestibular harm is not a nuance.

## Anti-patterns that look premium and hurt
1. Scroll-jacking / section-snapping (breaks INP, keyboard navigation and screen readers).
2. Full-page fade-in on load (feels slow, delays perceived LCP).
3. Parallax on mobile (jank + nausea).
4. Infinite marquees of logos (motion + fake-proof temptation).
5. Animated counters with invented statistics (motion + fabrication).
6. Hero video that autoplays with sound or >2.5 MB on mobile data.
7. Heavy hover choreography on every card (INP death by a thousand transitions).
8. Motion used to disguise a slow page (users notice; Core Web Vitals too).

## Motion QA (in the launch receipt)
- [ ] Reduced-motion path checked on all three directions
- [ ] INP measured on a throttled mobile profile after a full scroll + form interaction
- [ ] No motion element inside the LCP element
- [ ] Autoplay loop ≤6 s, muted, no audio track, poster present
- [ ] No animation runs while the tab is hidden
