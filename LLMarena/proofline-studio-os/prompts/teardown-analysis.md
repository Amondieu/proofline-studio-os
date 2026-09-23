# Prompt Library — 3-Point Teardown Analysis
<!-- v0.1 · owner: founder · public pages only · never analyse a page behind a login or a private client asset -->
## Context
```
URL: <public page>
Audience it targets: <best guess + why>
Primary action the page appears to want: <click | book | subscribe | buy>
Device reality: <we check desktop AND mobile; mobile first>
```
## Instruction (produce exactly this structure)
1. **One-sentence summary** of what the page is trying to do and the single biggest constraint on doing it.
2. **Three findings, ranked**, each as: Observation (quote the exact text/element) → Why it matters (visitor behaviour) → Severity (high/medium/low) → One-variable fix → Signal to watch.
   - Finding 1 must come from *clarity* (headline, offer, first 5 seconds).
   - Finding 2 from *proof* (what evidence is shown, and whether it is credible/verifiable).
   - Finding 3 from *path* (CTA visibility, friction, form, mobile reachability).
3. **What we deliberately do not change** — remaining issues ranked, with the reason for leaving them.
4. **One-variable next test** with an honest traffic estimate before it becomes measurable.
5. **Rule out**: do not recommend adding testimonials/logos/numbers unless the client can substantiate them; do not suggest copying a competitor; do not estimate conversion uplifts — say "unknown" rather than guessing.
## Output format
Exactly the structure of `templates/teardown-report.md`, ≤2 pages, no adjectives doing the work of evidence.
