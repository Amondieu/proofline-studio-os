# Component and dependency allowlist

This is the operationally useful part of the LLMarena stack research. It is a
starting policy, not a licence opinion. Every client repository needs its own
version/date check and a human approval record before a dependency ships.

## Default path

| Area | Default | Constraint |
|---|---|---|
| Framework | Astro for client builds | Static-first; no migration of this proof site required. |
| Styling | CSS or Tailwind | Tokens and direction invariants remain the source of design truth. |
| Primitives | Base UI or carefully selected copy-in components | Maximise ownership; record source and licence. |
| Icons | Inline Lucide SVG or an equivalent recorded source | No icon fonts or CDN-only assets. |
| Motion | CSS/Web Animations API | Reduced-motion path is the authored default. |
| Testing | Playwright + axe-core + Lighthouse when a client preview exists | Attach versions and receipts; do not claim a run that did not happen. |
| Fonts | Self-hosted OFL/Apache fonts | Ship the licence file with the project. |

## Conditional exceptions

GSAP, Rive, Three.js/R3F, a CMS, a paid registry, or any package with a
non-standard licence requires a written reason, exact version, licence source,
performance/accessibility impact, rollback path, and human approval. An unclear
licence blocks shipment.

## Forbidden defaults

No accessibility overlay widgets, scroll-jacking, icon fonts, Google Fonts CDN,
unreviewed paid-registry blocks, or animation without a reduced-motion path.
This list does not replace a project-specific legal or licence review.
