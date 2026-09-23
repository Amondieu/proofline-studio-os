# 04 — Component Allowlist
<!-- v0.1 · 2026-09-23 · owner: agent drafts, founder approves · every dependency change = new minor version -->

## Rule
A dependency may enter a client repository only if (a) it is on the allowlist below, (b) it has a row in `research/license-register.csv`, and (c) the row is younger than 90 days.

## Allowed (V1)
| Area | Package / source | Licence | Version pin rule | Notes |
|---|---|---|---|---|
| Framework | `astro` | MIT | pin minor (`7.3.x`) | upgrade only after a green `npm run gate` on a preview |
| Styling | `tailwindcss`, `@tailwindcss/vite` | MIT | pin minor | `@astrojs/tailwind` is deprecated — do not use |
| React islands | `react`, `react-dom` | MIT | pin minor | islands only, never a full React shell |
| Primitives | `@base-ui/react` | MIT | pin minor | Dialog, Popover, Tabs, Select, Accordion, Tooltip |
| Components (copy-in) | `shadcn` CLI registry items | MIT | record the registry URL + fetch date in the project README | max 8 components; edit the file, don't wrap it blindly |
| Icons | `lucide-*` (inline SVG) | ISC | pin minor | no icon fonts, no CDN |
| Motion | `motion` | MIT | pin minor | islands only |
| Analytics | Plausible snippet or `umami` script | service / MIT | version-less script, record the source URL | one analytics tool per project |
| Forms | Cloudflare Worker (our code) + `zod` | ours / MIT | pin minor | validation shared between Worker and client |
| Testing | `@playwright/test`, `@axe-core/playwright`, `@lhci/cli` | Apache-2.0 / MPL-2.0 | pin minor | dev-only dependencies |

## Conditional (requires a written justification in the project README)
`gsap` (standard "no charge" licence, not OSS) · `@rive-app/*` (MIT runtime, paid editor) · `three` + `@react-three/fiber` (CWV risk) · `payload` + a database (only >€2,500 with CMS scope) · `keystatic` (0.x — pin exactly).

## Forbidden
`lottie-web` (stale since 2025-09) · any animation library without a reduced-motion path · accessibility overlay widgets · jQuery-era carousel/slider plugins · scroll-jacking libraries · icon fonts · Google Fonts CDN · anything with no LICENSE file · paid-registry blocks under an Individual licence (e.g. shadcn.io Pro) · AGPL/GPL code that we modify and serve for clients without a written analysis.

## Component ownership & update policy
1. Copy-in components are **ours from the moment they land** — we adapt them; we do not track upstream PRs.
2. Update cadence: quarterly, on a preview branch, with the QA gate as the acceptance test.
3. Every custom component carries a header comment: purpose, direction(s) it supports, a11y notes, last review date.
4. Components are deleted when unused for two consecutive projects (dead code is a maintenance tax).
