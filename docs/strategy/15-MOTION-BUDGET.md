# 15 — Motion patterns and budget

Motion is a communication aid, not a proof of quality. The static state is the
default; animation opts in only when it helps orientation, feedback, or
comprehension.

## Escalation ladder

| Rung | Technique | Default | Limit |
|---:|---|---|---|
| 0 | No motion | Yes | Always acceptable |
| 1 | CSS hover/focus/state transition | Yes | Transform/opacity preferred |
| 2 | Small reveal using IntersectionObserver | Yes, selective | No reading obstruction |
| 3 | Component motion in an island | Conditional | One stateful effect above fold |
| 4 | Short muted loop | Conditional | Poster, ≤6 s, ≤2.5 MB |
| 5 | 3D/WebGL/shader | Exception | Business case, fallback, mobile opt-out |

## Direction limits

- Precision: signal movement only; no counters without real data.
- Cinematic: one focal loop or reveal; no parallax-everywhere composition.
- Editorial: opacity and hairline shifts; motion never carries the meaning.

## Required checks

- `prefers-reduced-motion: reduce` preserves content, focus, and interaction.
- No motion inside the LCP element and no layout-affecting animation.
- Keyboard users receive the same state change as pointer users.
- A loop has a poster, is muted, and does not autoplay audio.
- Interaction work remains within the project performance budget.
