# Rejected & Unknown-Licence Resources (with reasons)
<!-- v0.1 · 2026-09-23 · re-checked quarterly · owner: founder -->
## Rejected for commercial studio use
| Resource | Reason | Evidence |
|---|---|---|
| shadcn.io Pro Blocks (Individual tier) | Licence forbids commercial/client use; redistribution restrictions | https://www.shadcn.io/license |
| Vercel Hobby for client work | Fair-use guidelines restrict Hobby to non-commercial personal use; "paid consultant wrote the code" counts as commercial | https://vercel.com/docs/limits/fair-use-guidelines |
| Google Fonts via Google CDN | LG München I (3 O 17493/20, 2022-01-20) ruled the IP transfer unlawful; self-hosting is the fix | court ruling coverage |
| lottie-web for new builds | Last upstream push 2025-09-01; heavy payloads; better options exist | GitHub API 2026-09-23 |
| Accessibility overlay widgets | Do not fix source-level barriers; create false assurance and legal exposure | practitioner consensus |
| Scroll-jacking / section-snap libraries | Break keyboard navigation, INP and reduced-motion expectations | WCAG 2.2 + CWV |
| "Clone this famous site" template packs | Trade-dress exposure by design; incompatible with our positioning | Studio principles |
| Unsplash+ inside templates or AI pipelines | Licence bans digital-template use, AI/ML use, shared-drive storage | https://unsplash.com/plus/terms |
| GA4 as the default analytics | Needs consent; CNIL-compliant aggregate path is unavailable with standard GA4 | CNIL guidance |
| Tailark / Aceternity / Shadcnblocks free tiers (as shipped code) | Per-item licensing unclear; audit cost exceeds value | vendor terms |
## Unknown licence — DO NOT SHIP until confirmed
| Resource | Status | Action |
|---|---|---|
| `coreyhaines31/cro` (agent skill) | No explicit licence found in the listing | Read the repo LICENSE; if absent → reference-only, write our own skill |
| `kjaylee/misskim-skills#anti-slop-design` | No explicit licence found | Same |
| `Leonxlnx/taste-skill`, `openai/frontend-skill`, `garrytan/design-*` | Listed in aggregator; licences vary | Verify per repo before adapting any text |
| Figma Community kits | Community terms vary per file | Never ship assets; styles only, and only after review |
| CodePen / CodeSandbox demos | Default "all rights reserved" on many pens | Re-implement technique from scratch, never copy code |
| Lottie / Rive files from marketplaces | Per-asset licence required | Only with a recorded licence row |
## Note on aggregator lists
`VoltAgent/awesome-agent-skills` and similar registries are excellent for *discovery* and unusable as *licensing evidence*. Treat every entry as unlicensed until its own LICENSE file says otherwise (this is exactly the rule in `docs/00` §5).
