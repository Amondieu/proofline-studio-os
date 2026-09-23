---
name: landing-page-build
description: Build or modify an Astro landing page inside the approved stack and token system, producing a page that passes all seven gates. Use for any client build, template strip-down or component work.
---
# landing-page-build

## Inputs
Signed message map · signed direction brief + `tokens.json` · asset list with provenance rows · stack from `docs/04`.

## Procedure
1. **Confirm the gate inputs exist.** No build starts without message map + direction brief + allowlist check.
2. **Scaffold from the template family** (`AstroWind` stripped to the agreed sections). Delete unused widgets — dead code is a maintenance tax.
3. **Build static-first**: semantic HTML, one `<h1>`, landmark regions, then tokens, then layout, then islands only where interaction is required.
4. **Images:** correct aspect ratio, `width`/`height`, AVIF/WebP, lazy below the fold, `fetchpriority="high"` on the LCP image only.
5. **Forms:** native elements, real labels, inline + summary errors, honeypot + Turnstile, Worker endpoint or Tally; test the failure path, not only the happy path.
6. **Motion:** start at rung 0/1 of the ladder; add rungs only within `docs/05` budget; author the reduced-motion path first.
7. **Run the gate locally**: `npm run gate` (lint → axe → Lighthouse budgets → Playwright smoke). Fix; never suppress a rule without a written waiver.
8. **Write the build receipt**: what was built, what was removed, what deviates from the template, which dependencies were added (with licence rows).

## Output
Working page + gate output + build receipt + updated `license-register.csv` rows for anything new.

## Refusal conditions
- A new dependency without a licence row.
- A design change that breaks the signed direction or a gate.
- A request to install analytics/trackers beyond the one approved tool.

## Never
Never ship an unlicensed asset, a third-party CDN dependency, scroll-jacking, or an animation without a reduced-motion path. Never push directly to production without a green gate on a preview deploy.
