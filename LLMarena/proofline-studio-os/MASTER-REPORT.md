# PROOFLINE STUDIO OS — Research Mission Report
**Passes covered:** Discovery/Longlist → Selection/Architecture → Repository design → Master-Site V1 blueprint
**Date:** 2026-09-23 · **Operator:** founder-led studio (FR/EU) · **Status:** decision-ready, with named human gates

---

## Zusammenfassung auf Deutsch (kurz)

1. **Das Studio OS ist machbar — aber nicht als Tool-Sammlung.** Der Vorteil liegt in den Gates, Checklisten und wiederverwendbaren Templates (Repository-Teil), nicht in 70 Libraries. V1 = **Astro 7 + Tailwind 4 + Base UI/shadcn-Copy-ins + eigener Form-Endpoint + Plausible + Cloudflare Pages + axe/Lighthouse/Playwright-Gates**.
2. **Harte Lizenz-Funde** (verifiziert): GSAP ist *kein* Open Source, sondern eine kostenlose Webflow-Standardlizenz mit Verbot von visuellen Animations-Buildern; shadcn.io „Pro Blocks" verbietet kommerzielle Nutzung im Individual-Tarif; Vercel Hobby verbietet kommerzielle Nutzung (Client-Arbeit!); Google Fonts vom Google-CDN ist nach LG München I rechtswidrig; Unsplash+ verbietet KI-Training und Template-Weitergabe; Higgsfield erlaubt kommerzielle Nutzung, trainiert aber bei Nicht-Enterprise-Konten weiterhin mit Inputs → **keine Client-Geheimnisse hochladen**.
3. **Rechtlicher Takt (verifiziert):** Mentions légales (LCEN) sind Pflicht, EU-Omnibus verbietet Fake-Testimonials, AI Act Art. 50 gilt seit 02.08.2026, EAA-Status hängt an der Mikrounternehmens-Schwelle — alles als Build-Gate im Repo, keine Rechtsberatung.
4. **Erster Schritt morgen:** Repository anlegen, `docs/00–09` + Launch-Gate-Schablone committen, Astro-Repo aus AstroWind strippen und Token-Switcher als Demo bauen.

---

## 0. Evidence conventions (read this first)

| Marker | Meaning |
|---|---|
| **VERIFIED** | Directly documented by the repository's LICENSE file, package registry, vendor documentation, court/regulator publication or the GitHub API response captured in `research/github-audit.csv` (all API data pulled **2026-09-23**). |
| **INFERRED** | Reasoned from verified evidence, not directly stated by the source. |
| **UNVERIFIED** | Needs a local proof-of-concept, a vendor answer, or a lawyer/privacy review before it becomes a claim. |

Confidence is stated per major recommendation as **high / medium / low**. All licence files referenced below were fetched on 2026-09-23; raw API output is in `research/github-audit.csv`, scored judgements in `research/resource-inventory.csv`.

**Standing disclaimer:** nothing in this document is legal advice. Items marked ⚖️ require a French/EU lawyer or DPO review before we tell a client "we are compliant".

---

## 1. Executive Verdict

### 1.1 Is the proposed Studio OS viable?
**Yes — as a gated delivery system, not as a software platform.** Confidence: **high**.

The evidence base is strong on the parts that matter commercially: every candidate that would end up in *shipped client code* is MIT / ISC / Apache-2.0 (Astro 7, Tailwind 4, Base UI, shadcn/ui, Motion, Lucide, Playwright, Lighthouse), and the three genuinely awkward licences are all *avoidable or containable* — GSAP (free standard licence, not OSS, and forbidden inside animation-builder products), Vercel Hobby (non-commercial only), and premium component registries whose individual tiers forbid client work.

What is **not** viable is the ambition of doing all 22 Studio-OS layers in V1. The failure mode is not legal or technical — it is *attention*: a one-person studio that maintains its own CMS, its own design-system package, a 3D pipeline and an experimentation platform ships slower than a studio with three good templates and hard QA gates.

### 1.2 Smallest high-quality V1
One stack, one template family, one measurement path, three design directions, seven gates:

| Element | V1 decision |
|---|---|
| Framework | **Astro 7.3.x** (MIT, static-first, zero JS by default) |
| Styling | **Tailwind 4.3.x** with CSS-first `@theme` tokens |
| Primitives | **Base UI 1.x** + copy-in **shadcn/ui** components (~8 only) |
| Forms | **Cloudflare Worker + D1** endpoint (+ Tally for intake as fast path) |
| Booking | **Cal.com** free tier, client-owned account |
| Analytics | **Plausible Cloud (EU, €9/mo, client-billed)**; Umami self-hosted for studio-owned sites |
| Hosting | **Cloudflare Pages** on a **client-owned** account, `$0` static / `$5` Workers |
| Assets | Self-hosted OFL fonts (Fontsource) + Lucide SVG + provenance log |
| QA | **axe-core + Playwright + Lighthouse CI** on every PR; manual keyboard/mobile sweep before launch |
| Docs | Markdown in-repo: 12 docs, 7 SKILL.md, 9 templates, 5 JSON schemas |

### 1.3 What we deliberately do NOT build yet
1. Own CMS — Keystatic (MIT) or the client's existing tool covers it.
2. Own component library/package — copy-in components, no internal npm registry.
3. 3D/WebGL/shader pipeline — no conversion case yet; highest CWV risk of all options.
4. A/B testing infrastructure — traffic thresholds (below) make it theatre for the first 12 months.
5. Client portal / agency ERP / CRM — Cloudflare D1 + a spreadsheet beats a home-made tool.
6. Multi-language builds — only when a paying client needs it.
7. Rive/R3F/GSAP production pipelines — one project-scoped exception each, decided in writing.
8. Any AI-generated human imagery used as trust signal (see §9 risk 4/10).

### 1.4 Top 5 risks and reductions

| # | Risk | Why it is top-5 | Reduction |
|---|---|---|---|
| 1 | **Licence drift in shipped code** (GSAP-like "free but not OSS", premium registries, AGPL self-hosting) | A single wrong block can force a rebuild or a licence purchase *after* invoicing | `research/license-register.csv` is a gate artefact: no dependency ships without a row. Quarterly re-check of every "custom" licence row. |
| 2 | **Design-copy / trade-dress exposure** | Our positioning is "we make you credible"; a "clone" accusation ends that instantly | "Do not imitate" policy + reference tagging (§5.9); every concept labelled `Studio Concept — independent demonstration, not client work`. |
| 3 | **Client-confidential data in AI tools** | Higgsfield's own terms: non-Enterprise inputs are used for training by default; indemnification is Enterprise-only | Hard rule: no client assets in any generative tool; intake policy + provenance log + approval record before any AI asset ships. |
| 4 | **Accessibility gap on a paid site** (EAA / WCAG 2.2 AA) | Micro-enterprise exemption protects *small clients*, not us, and vanishes as they grow; €250k ceiling in France | WCAG 2.2 AA gates in CI + manual keyboard/focus sweep + written accessibility statement per site; "we tested" ≠ "we guarantee compliance". ⚖️ |
| 5 | **Founder bandwidth** — 22 layers, 5–14 day delivery, €500–3,000 pricing | The cheapest failure is an over-built OS with no shipped sites | 14-day plan builds the OS *and* the Master Site; every artefact has an owner, a version rule and a "when required" field (§6). |

---

## 2. Studio OS Architecture

`Gate` = the human approval point that cannot be automated away.

| # | Layer | Business purpose | Recommended module(s) | Decision | Why | Main risk | Human gate |
|---|---|---|---|---|---|---|---|
| 1 | Lead qualification & discovery | Stop unprofitable projects before they cost a week | `templates/client-intake.md` + Tally form + scoring rubric | **BUILD** | Nothing off-the-shelf encodes *our* scope limits | Intake becomes a sales barrier if too long | Founder qualifies; no proposal without a completed intake |
| 2 | Positioning & offer analysis | Turn a vague offer into a testable claim | LIFT + MECLABS heuristics (reference), `templates/message-map.md` | **ADOPT (method)** | Proven CRO lenses, free | Framework-worship over customer voice | Founder signs the message map before any design |
| 3 | Conversion copy & message architecture | The actual deliverable clients pay for | `skills/conversion-copy/SKILL.md`, `prompts/copy-message-map.md` | **BUILD** | Copy quality is the differentiator; cannot be licensed | Generic AI copy → "AI slop" positioning risk | Client approves copy freeze (write-protected date) |
| 4 | IA & wireframing | Prevent restructures in week 2 | Section-order spec in `docs/02`, wireframe-in-text discipline | **BUILD** | Cheaper than Figma churn on fixed-price work | Scope creep disguised as "just one section" | Founder freeze after revision round 1 |
| 5 | Creative direction & design systems | Three sellable directions, one codebase | `docs/03-DESIGN-DIRECTIONS.md` + token switcher (demo) | **BUILD** | Directions must be *ours*, legally clean and switchable | Token soup: directions collapse into one look | Founder approves direction brief per client |
| 6 | Reference & inspiration intake | Raise art-direction quality without copying | Controlled intake workflow + tagging schema (§5.9) | **BUILD** | Inspiration is where trade-dress risk enters | Screenshots pasted into client deliverables | Every reference logged + "do-not-imitate" list checked |
| 7 | UI primitives & components | Speed without owning a design system | **Base UI** primitives + **shadcn/ui** copy-ins (MIT) | **ADOPT** | MIT, actively maintained, code ownership | "shadcn look" → undifferentiated output | Component allowlist approval per project |
| 8 | Templates | Compress 3 days into 6 hours | **AstroWind** (MIT) stripped to ~10 sections | **ADAPT** | Active (Astro 7 + TW4), MIT, production-ready | Template familiarity | Founder re-tokens before client sees anything |
| 9 | Motion & micro-interactions | Premium feel without CWV damage | CSS/WAAPI → Motion (islands) → GSAP (exception) | **ADOPT (ladder)** | Motion Budget makes cost explicit | Motion that harms INP/vestibular safety | Motion budget signed per project |
| 10 | Image/video/3D assets | Original, rights-clean visuals | Self-hosted fonts, Lucide, provenance log, Higgsfield for concepts only | **ADAPT + BUILD** | Rights are the only thing that cannot be fixed later | Uploading client assets to AI tools | AI asset approval record before production |
| 11 | Front-end implementation | Predictable 5–14 day delivery | Astro islands + Worker endpoints + Git flow | **ADOPT** | Static-first = fewer failure modes | Framework majors churn annually | Code review by founder; no direct-to-prod pushes |
| 12 | Deployment & hosting | Client owns their site | **Cloudflare Pages** (client account) + GitHub | **ADOPT** | Free tier allows commercial use; €0–5/mo | Client locked out if we hold accounts | Ownership transfer signed before go-live |
| 13 | Forms, CRM, scheduling | Lead flow that cannot silently break | Worker+D1 endpoint, Tally, Cal.com | **ADOPT + BUILD** | EU-friendly, exportable | Deliverability/spam on a home-made endpoint | Test protocol (§4.4) + founder send test |
| 14 | Analytics & measurement | Prove value, not vanity | Plausible (EU cloud) / Umami | **ADOPT** | Cookieless, CNIL-friendly posture | Non-consensual tracking | Privacy review before any tag goes live ⚖️ |
| 15 | SEO & metadata | Baseline quality | Astro metadata + schema (Service/Organization, no self-serving reviews) | **ADOPT** | Documented Google rules | Review-snippet misuse → manual action | QA checklist item signed |
| 16 | Performance | CWV as a delivery guarantee | Lighthouse CI budgets + field check | **ADOPT** | Field thresholds are objective (LCP 2.5s / INP 200ms / CLS 0.1) | Lab-only optimism | Launch gate: budget pass or written waiver |
| 17 | Accessibility | Legal + ethical baseline | axe-core + manual WCAG 2.2 AA checklist | **ADOPT** | Six new AA-relevant criteria are design decisions | Automated-only "compliance" claims | Accessibility sign-off before launch ⚖️ |
| 18 | Privacy / GDPR / France | Avoid creating client liability | Mentions légales + privacy notice templates + CNIL-exemption analytics config | **BUILD (content)** | Only the publisher's data can fill these in | Copy-paste policies | Client signs their entity data; ⚖️ counsel review template |
| 19 | Asset rights & AI transparency | Ship proof, not risk | `templates/asset-provenance-log.csv`, `templates/ai-asset-approval.md` | **BUILD** | AI Act Art. 50 applies since 2026-08-02 | Undisclosed synthetic people | Approval record before asset reaches production |
| 20 | Client QA, review, revision | Scope control | `docs/12-DELIVERY-SOP.md` + QA receipt | **BUILD** | Revision limits protect margin on fixed price | "One more round" | Milestone sign-off per phase |
| 21 | Handover & maintenance | Trust + recurring revenue | Handover packet + ownership checklist | **BUILD** | Client ownership is a sales argument | Unmaintained site → reputation damage | Signed handover + opt-in retainer |
| 22 | Portfolio, sales & learning loop | Fill the pipeline honestly | `docs/13-SALES-AND-PORTFOLIO.md`, case-study template, teardown template | **BUILD** | We have no paid proof yet — honesty is the strategy | Fabricated credibility | Every public claim passes the disclosure checklist |

---

## 3. Research Inventory

Full detail (all 10 score inputs, gaps, risks, integration notes) lives in **`research/resource-inventory.csv`**; licence positions in **`research/license-register.csv`**; raw GitHub evidence in **`research/github-audit.csv`**. Tables below are the decision view: score = Studio Readiness Score (formula in §3.12).

### A. Strategy & copy

| Resource | Licence | Maintenance evidence | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|---|
| MECLABS Conversion Sequence Heuristic [1] | Citation-only framework | Stable, published research method | Weighted prioritisation model for teardowns | Templates, thresholds | 6.60 | REFERENCE |
| LIFT Model (Goward, 2009) [2] | Citation-only framework | Industry standard lens | Six-factor audit structure | Deliverable format | 6.90 | ADOPT (method) |
| NN/g 5-second test [3] | Reference | Continuously published | Cheap clarity/memorability test | Needs ≥5 testers to mean anything | 7.35 | ADOPT (method) |
| TeardownHQ audit checklist [4] | Commercial site, reference | Active 2026 | 21-checkpoint section structure | Reusable text; also a competitor | 5.90 | REFERENCE |
| anthropics/skills (SKILL.md spec + frontend-design) | Apache-2.0 example skills / source-available document skills — **mixed** | 177.8k★, commit 2026-09-22 | Canonical skill format | Studio-specific opinions | 7.85 | ADOPT (format) |

### B. Design intelligence

| Resource | Licence | Maintenance evidence | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|---|
| USWDS [5] | Public domain + mixed notices | pushed 2026-09-23 | Accessible form/error patterns, tokens, content style | US tone; heavy | 7.75 | REFERENCE |
| GOV.UK Frontend [6] | MIT | pushed 2026-09-23 | Best-practice validation/error summary | Editorial/luxury aesthetic | 8.30 | REFERENCE |
| IBM Carbon [7] | Apache-2.0 | pushed 2026-09-23 | Token taxonomy, per-component a11y docs | Enterprise visual language | 7.90 | REFERENCE |
| Adobe React Aria/Spectrum [8] | Apache-2.0 | pushed 2026-09-23 | Headless a11y behaviour | Styling | 8.40 | REFERENCE (fallback primitives) |
| Awwwards / Godly / Mobbin / Land-book | Proprietary ToS, copyrighted screenshots | Live platforms | Pattern vocabulary, art direction | Any right to reuse | 4.75 | REFERENCE (controlled intake) |

### C. UI, components & templates

| Resource | Licence | Maintenance evidence | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|---|
| shadcn/ui [9] | MIT | 124.5k★, pushed 2026-09-21 | Copy-in React components, theming, registry | Astro-native components; design opinion | 8.70 | ADOPT (selective) |
| Base UI [10] | MIT | 11.0k★, pushed 2026-09-23, v1.x stable, shadcn default since Jul 2026 | 35 unstyled a11y primitives | Styling | 8.90 | ADOPT |
| Radix Primitives [11] | MIT | 19.3k★, last push 2026-08-08 — slower cadence | Battle-tested primitives | Component velocity | 8.35 | REFERENCE/fallback |
| Tailwind CSS [12] | MIT | 97.6k★, v4.3.x | Utility CSS + `@theme` tokens | Design taste | 9.00 | ADOPT |
| Astro [13] | MIT | 62.8k★, v7.3.4, Node ≥22.12 | Static-first, islands, images | App-like use cases | 9.30 | **ADOPT (default)** |
| Next.js [14] | MIT | 142.4k★, v16.3.x | SSR/ISR, ecosystem | Weight vs CWV; Vercel Hobby ban | 8.45 | PILOT/fallback |
| AstroWind [15] | MIT | ~6k★, Astro 7 + TW4 rewrite, active 2026 | Production template to strip | Distinctive art direction | 8.45 | ADAPT |
| Magic UI [16] | MIT | 22.4k★, pushed 2026-09-20 | Animated marketing components | Restraint; a11y in some effects | 7.15 | REFERENCE (max 1–2/project) |
| shadcn.io Pro Blocks [17] | Proprietary — **Individual licence forbids commercial use** | Active product | Polished blocks | Legal use for client work without a Team licence | 5.90 | **AVOID** |
| Tailark / Aceternity / Shadcnblocks | Freemium, per-item terms | Active | More patterns | Licence clarity | 5.50 | REFERENCE ONLY |

### D. Motion & creative assets

| Resource | Licence | Maintenance evidence | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|---|
| CSS + Web Animations API | Web standard | Universal | Reduced-motion-safe baseline motion | Timeline orchestration | 9.50 | **ADOPT (default)** |
| Motion (ex-Framer Motion) [18] | MIT | 33.7k★, v13.x, pushed 2026-09-23 | Component/island motion, layout, reduced-motion | React-only | 8.35 | ADOPT (islands) |
| GSAP 3.15 [19] | **Standard "no charge" licence, NOT open source**; commercial sites allowed; visual animation builders prohibited; Webflow-owned, licence can change prospectively | 28.6k★, npm 3.15.0, licence eff. 2025-04-30, amended 2025-05-30 | Timelines, ScrollTrigger, SplitText, MorphSVG | Source freedom; redistribution | 7.65 | PILOT (exception only) |
| Lottie / lottie-web [20] | MIT | **Last push 2025-09-01 — effectively stale** | AE pipeline playback | Performance; maintenance | 6.35 | AVOID (new work) |
| Rive [21] | Runtime MIT; editor SaaS (Free/Cadet $9/Voyager $32 per seat) | rive-react pushed 2026-09-16 | Tiny interactive state-machine animation | Budget (<€2,500 builds) | 7.50 | PILOT |
| Three.js / R3F [22] | MIT | Active 2026-09 | 3D/shaders | CWV, mobile battery, fallback burden | 7.15 | REFERENCE + written justification |
| Lucide [23] | **ISC** (Feather-derived subset, MIT) | 24.7k★, pushed 2026-09-22 | Consistent icon set as inline SVG | Editorial/luxury voice | 8.85 | ADOPT |
| Fontsource / OFL fonts [24] | OFL-1.1 / Apache-2.0 | Actively maintained | Self-hosted, subsetted fonts | — | 8.90 | ADOPT (self-host only) |
| Unsplash / Unsplash+ [25] | Unsplash Licence (commercial OK, no attribution); Unsplash+ adds bans on AI/ML use, digital templates, shared drives | Live platform | Free photography for concepts | Model releases, indemnification ($0 on free tier) | 6.85 | REFERENCE with strict rules |

### E. Build, hosting & deployment

| Resource | Licence | Maintenance evidence | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|---|
| Cloudflare Pages/Workers/D1 [26] | Proprietary service; free tier permits commercial use; Workers Paid $5/mo | Current limits docs 2026 | Unlimited static bandwidth, functions, previews | Not FR-pinned data residency by default | 8.60 | **ADOPT (default host)** |
| Netlify [27] | Proprietary (free 300 credits; Pro ≈$20 flat since Apr 2026) | Live | Static+functions+forms | Credit exhaustion; US | 8.20 | Fallback |
| Vercel [28] | Proprietary; **Hobby = non-commercial only**, Pro $20/seat | Live | Best Next.js DX | Commercial client work on Hobby is a terms breach | 7.65 | AVOID for clients |
| Hetzner/Scaleway/OVH + Coolify [29] | Hosting + Apache-2.0 | Live | EU residency, self-hosting | You are the sysadmin | 7.35 | PILOT (retainer clients) |
| GitHub [30] | Proprietary service, generous free tier | Live | VCS, CI, ownership transfer | — | 8.80 | ADOPT |
| Keystatic [31] | MIT | 2.4k★, pushed 2026-09-08, still 0.x | Git-committed CMS admin | Roles, scheduling, scale | 8.25 | PILOT (default CMS answer) |
| Payload v3 [32] | MIT | 44.9k★, pushed 2026-09-23 | Full CMS in Next.js | Ops/db for small builds | 8.10 | PILOT (>€2,500) |
| Decap CMS | MIT | 19.4k★, low velocity | Git CMS, mature | UX, workflows | 7.85 | REFERENCE |

### F. Forms, CRM & automation

| Resource | Licence | Maintenance evidence | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|---|
| Tally [33] | Proprietary SaaS; Belgian, EU servers; DPA built into ToS (paid tiers strongest) | Active | Fast branded intake/teardown forms | Embed injects third-party scripts | 7.40 | ADAPT (fast path) |
| Cloudflare Worker + D1 endpoint (own) | Our code | Pattern well documented | Zero-vendor forms, honeypot+Turnstile, webhook+D1 | We own spam/deliverability | 8.25 | **BUILD (default)** |
| Formbricks [34] | **AGPL-3.0 core** + `/ee` licence | 13.0k★, pushed 2026-09-23, German vendor | EU/self-hosted surveys | Long intake forms | 7.05 | PILOT (self-host) |
| Cal.com [35] | MIT (cloud plans paid) | 48.6k★, pushed 2026-09-20, free tier 1 user | Booking + qualification | Client needs their own account/domain | 8.30 | ADAPT |

### G. Analytics & CRO

| Resource | Licence | Maintenance evidence | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|---|
| Plausible [36] | AGPL-3.0 self-host; EU cloud from €9/mo | 29.2k★, pushed 2026-09-23 | Cookieless, EU, client-friendly dashboard | Deep funnels | 8.55 | **ADOPT (client-billed)** |
| Umami [37] | MIT | 39.0k★, pushed 2026-09-22; cloud Hobby free (100k events, 3 sites) | Cheapest analytics, event metering | Journey depth | 8.55 | ADAPT (studio sites / self-host) |
| Matomo [38] | GPL-3.0 | 21.9k★, pushed 2026-09-23 | CNIL mode reference implementation | Modern UX, PHP ops | 7.05 | REFERENCE |
| PostHog [39] | MIT core + `/ee`; EU cloud | 39.9k★, pushed 2026-09-23 | Funnels, replay, experiments | Consent burden; cost | 7.50 | PILOT (funded measurement only) |
| Low-traffic testing doctrine [40] | Method (GrowthBook et al.) | 2026 practitioner consensus | "When not to test" decision filter | Traffic | 7.85 | ADOPT (as rules) |

### H. Accessibility, performance & SEO

| Resource | Licence | Maintenance evidence | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|---|
| W3C WCAG 2.2 [41] | W3C document licence | Recommendation; 9 new SC, 4.1.1 removed | Authoritative AA target | Test kit | 9.25 | ADOPT |
| axe-core [42] | MPL-2.0 | 7.5k★, npm 4.13.x | Automated rule engine in CI | Meaning, focus order, real keyboard traps | 8.90 | ADOPT |
| Playwright [43] | Apache-2.0 | 96.6k★, npm 1.63.x | Cross-browser smoke + keyboard sweeps | Visual design judgement | 9.00 | ADOPT |
| Lighthouse CI [44] | Apache-2.0 | 30.8k★ | Budgets/assertions, lab perf | Field truth | 8.95 | ADOPT |
| Core Web Vitals thresholds [45] | Reference | 2026 CrUX: 55.9% of origins pass all three | Objective launch targets | Implementation | 8.75 | ADOPT |
| Google review-snippet rules [46] | Reference | Self-serving rule (2019); fake/incentivised review guidance added 2026-07-24 | Prevents manual actions | — | (part of §9) | ADOPT (as constraint) |

### I. Privacy, AI & legal risk

| Resource | Licence/status | Evidence | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|---|
| CNIL consent exemption [47] | Regulatory guidance (updated 2025-07-04) | Official | Consent-free measurement criteria: aggregate-only, first-party, no cross-site sharing, 13-month tracker limit, 25-month retention | Legal sign-off | 8.40 | ADOPT (as constraint) |
| EU AI Act Art. 50 [48][49] | Regulation (EU) 2024/1689; applicable **2026-08-02**, fines up to €15m/3% | Commission draft labelling code | Deployer disclosure duty for deepfakes/AI content; artistic/fictional attenuation; human editorial responsibility | Whether our specific asset needs a label (case-by-case) ⚖️ | 8.10 | ADOPT (as constraint) |
| EU Omnibus Directive [50] | Directive (EU) 2019/2161, in force 2022-05-28, fines up to 4%/€2m | Legal analyses | Fake/incentivised-undisclosed reviews illegal; must explain verification | How to word testimonials | 8.10 | ADOPT (as constraint) |
| LCEN art. 1-1/1-2 (mentions légales) [51] | French statute; reported exposure up to €75k/€375k | economie.gouv.fr + practitioner summaries | Mandatory publisher, publication director, host, contact details | GDPR notice (separate document) | 8.10 | ADOPT (as build gate) |
| Higgsfield ToS + help centre [52] | Proprietary SaaS, revised Jul 2026 | Official help centre (Aug 2026) | Commercial use allowed, we own outputs, sublicensable to clients, licence ends on deletion | **Non-Enterprise: inputs used for training by default**; IP indemnity Enterprise-only | 6.65 | ADAPT (concept layer, hard gates) |

### J. Client delivery operations
No external dependency is needed: the value is our own SOPs (§6, `docs/12-DELIVERY-SOP.md`). Scoring deliberately not applied to self-authored process documents.

### K. Portfolio & sales
| Resource | Licence/status | Provides | Does NOT solve | Score | Decision |
|---|---|---|---|---|---|
| Own credibility framework (`docs/13`) | Ours | Labelled concepts, permissioned case studies, substantiation file | Real client outcomes (earned, not designed) | 8.60 | BUILD |
| VoltAgent/awesome-agent-skills (discovery of CRO/design skills) [53] | Mixed/unknown per entry | Radar for community skills | Licence safety of any single entry | 5.65 | REFERENCE ONLY |
| OpenDesign [54] | Apache-2.0 (LICENSE confirmed) | Agent harness for prototypes/landing pages with file output | QA, compliance, production readiness | 6.70 | REFERENCE/PILOT for exploration |

### 3.12 Score transparency
`SRS = .20·license + .10·maintenance + .10·docs + .15·a11y + .10·performance + .10·security + .10·design-adaptability + .05·integration-simplicity + .05·client-suitability + .05·lean-fit`
Reproduce or adjust: `python3 research/score_resources.py`. **Known calibration bias (stated openly):** framework/method resources (LIFT, MECLABS, NN/g) score low because three of ten axes measure shippable artefacts. They are still ADOPT-as-method. Scores are judgements, not measurements.

### 3.13 Rejected list & unknown-licence list
- **Rejected:** shadcn.io Pro Blocks (individual licence), Lottie for new projects (stale), Vercel Hobby for client work (terms), GA4-with-consent-only default (CNIL position), Google Fonts CDN (court ruling), accessibility overlay widgets (no legal effect, documented), FullPage-style scroll-jacking libraries, "clone this famous site" templates.
- **Unknown licence — do not ship until confirmed:** community SKILL.md files from aggregator lists (`VoltAgent/awesome-agent-skills` entries such as `coreyhaines31/cro`, `kjaylee/misskim-skills#anti-slop-design`, `Leonxlnx/taste-skill`), Tailark/Aceternity free tiers, Figma community kits, most Codepen/CodeSandbox demos, Lottie JSON files from third-party marketplaces.

---

## 4. Recommended V1 Stack

### 4.1 Default V1 path (exactly one)
| Slot | Choice | Licence | Why this and not the alternative |
|---|---|---|---|
| Framework | **Astro 7.3.x** | MIT | Zero-JS default protects LCP/INP; Next.js reserved for app-like clients |
| Styling | **Tailwind 4.3.x** (`@tailwindcss/vite`, CSS-first `@theme`) | MIT | One styling system; `@astrojs/tailwind` is deprecated — the Vite plugin is the supported path |
| Components | **Base UI 1.x primitives + shadcn/ui copy-ins** (~8 components max) | MIT | Active maintenance (v1 Dec 2025, shadcn's default since Jul 2026) + we own the code |
| Forms | **Cloudflare Worker + D1** endpoint; **Tally** for intake/teardown | own code / SaaS | No vendor in the critical path; Tally covers non-technical flows fast |
| Analytics | **Plausible Cloud (EU)** client-billed €9/mo | AGPL (service) | Cookieless, EU-resident, client can own the account; GA4 fails the CNIL posture |
| Hosting | **Cloudflare Pages** on client-owned account | Service | Commercial use allowed on free tier; Vercel Hobby forbids it |
| Deployment | GitHub → Pages build, PR previews, `main` = production | Service | Preview-to-prod is the release process, no custom CI to maintain |
| Asset workflow | Repo `/assets` → AVIF/WebP + `<Picture>`; fonts self-hosted (Fontsource); icons inline SVG (Lucide) | OFL/ISC/MIT | Everything first-party: faster *and* GDPR-clean |
| QA tools | axe-core + Playwright + Lighthouse CI (`npm run gate`) | MPL/Apache | One command, three gates, all CI-able |
| Docs system | Markdown in-repo + ADRs + launch receipts | ours | No wiki to maintain; handover = repo transfer |
| Folder structure | §6.13 | — | — |
| Recurring monthly cost | **Studio: €0–5** (Cloudflare free→Workers Paid) + **€9/client** Plausible + ~€12/yr domain per client | — | Total client-facing stack can ship at €0/month if client declines analytics |
| Build hours, Master Site V1 | **34–40 h** across 14 days (7 focused workdays feasible at 5–6 h/day) | — | Budgeted in §7 |

### 4.2 Alternative A — low-code path (when the founder is the bottleneck)
AstroWind template (MIT, un-stripped) + **Tally** (EU) for every form + **Cal.com** free + **Plausible** + Cloudflare Pages. No Worker, no copy-in components, no custom motion beyond CSS. Trade-off: less distinctive output, third-party embeds on page, ~4–6 h saved per project. Use for Starter Conversion Page (€500–750) only.

### 4.3 Alternative B — self-hosted / open-source-first path
Astro build + **Hetzner/OVH VPS (~€5–7/mo)** with Coolify (Apache-2.0) running: static site, **Umami** (MIT) analytics, optional **Cal.com** (MIT) and **Formbricks** (AGPL, unmodified). Trade-off: 2–4 h/month ops per client; sell only with a maintenance retainer (≥€60/mo). Note AGPL/GPL boundaries: run unmodified or keep modifications private to your own infrastructure.

### 4.4 Non-negotiable operational rules for the stack
1. One framework, one styling system, one primitive layer, one form path, one analytics tool per project. No second tool without a written ADR.
2. No dependency enters a client repo without a row in `research/license-register.csv`.
3. Every client project has **its own** repository and **client-owned** hosting/domain accounts; we get delegated access, never ownership.
4. `npm run gate` (lint + axe + Lighthouse budget + Playwright smoke) must pass before any deploy to `main`.

---

## 5. Proofline Master-Site Blueprint

### 5.1 Page map (V1 — deliberately small)
```
/                     Master site (the first case study: "this site is the demo")
/directions           The three design directions, live-switchable on one page  → secondary CTA lives here
/teardown             Primary conversion: request the 3-point teardown
/work                 Portfolio: concept work + (later) permissioned client work
/work/master-site     Case study of this site: the build, the gates, the receipts
/offer                Packaging + prices + what is not included
/about                Who, why, standards (accessibility, honesty, ownership)
/legal/mentions-legales · /legal/privacy · /legal/accessibility-statement · /legal/cookies (only if needed)
```
A "design direction" is **not** a separate site: one route, three token sets, switched via a sticky control (`?d=precision|cinematic|editorial`), so the positioning and IA cannot drift apart.

### 5.2 Section order (home) — the conversion spine
1. `Hero` — one-sentence offer + primary CTA + secondary CTA + honest status line ("Studio concept work shown — first client slots open").
2. `Problem framing` — 3 bullets naming the real failure modes of weak landing pages (clarity, proof, path).
3. `What you get` — the 3-point teardown, concretely: what the three points are, what arrives, when.
4. `How it works` — 3 steps, each with a promise and a time stamp (form → within 48h → 20-minute call).
5. `Proof by method` — the gates we publish (a11y, performance budget, provenance, ownership transfer) with links to the policy pages. **This replaces fake logos.**
6. `Directions preview` — three cards, each switching the live token set inline; secondary CTA "Explore our creative directions".
7. `Packaging` — Starter / Authority / Launch System with prices, deliverables, timeline, what's excluded.
8. `Objections` — 5 honest answers (I have no traffic yet / can I edit it later / do I own it / who writes copy / what if I hate the direction).
9. `Process & ownership` — revision limits, content freeze, handover.
10. `Final CTA` — the teardown request, restated in one line, with a fallback (email) and privacy microcopy.
11. `Footer` — mentions légales, privacy, accessibility statement, contact, no third-party trackers.

### 5.3 CTA architecture
- **Primary:** "Get a 3-point landing page teardown" — appears at sections 1, 6, 10 and in the sticky mobile bar. One wording everywhere (no A/B variants in V1).
- **Secondary:** "Explore our creative directions" — sections 1 and 6 only, routes to `/directions`.
- **Tertiary (low intent):** email link in footer; email address is *never* the primary path.
- Form fields (V1, 4 required): name · work email · URL to review · one-line goal. Everything else is asked on the call.

### 5.4 Copy architecture (four building blocks, reused on every page)
`Claim → Evidence type → Mechanism → Next step`
- **Claim:** ≤12 words, specific outcome, no superlatives.
- **Evidence type:** only one of — *demonstrated method*, *stated standard*, *permissioned client quote*, *labelled concept work*. No claim may exist without a named evidence type (this is the anti-fabrication rule in practice).
- **Mechanism:** the sentence that explains *why* it works (this is where a studio looks senior instead of loud).
- **Next step:** one verb, one object, one friction expectation ("takes 2 minutes; you get a reply within 48 h").

### 5.5 Three design-direction token systems
Tokens are the **only** sanctioned difference between directions. All values are CSS custom properties, generated from one `tokens.json`.

| Token | **A. Precision System** | **B. Cinematic Authority** | **C. Editorial Luxury** |
|---|---|---|---|
| Primary audience | B2B SaaS / AI / automation | launches, creative brands | premium consultants, high-ticket services |
| `--bg-base` | `#F7F6F3` warm off-white | `#0B0B0C` near-black | `#F1EBE1` bone |
| `--bg-elevated` | `#FFFFFF` | `#141416` | `#E7DFD2` sand |
| `--ink-strong` | `#14161A` graphite | `#F4EFE7` warm ivory | `#15140F` ink |
| `--ink-muted` | `#5A6068` | `#A9A29A` | `#5B5A50` |
| `--accent` | `#1B5CFF` electric blue | `#C8332B` signal red | `#6B6B3A` deep olive |
| `--accent-signal` | `#B8F24A` acid-lime (micro only) | `#C9CDD2` chrome (gradient, 1 use/page) | `#9A7B4F` muted brass |
| `--border` | `1px solid rgba(20,22,26,.10)` | `1px solid rgba(244,239,231,.14)` | `1px solid rgba(21,20,15,.16)` |
| Radius | `6px` | `2px` | `4px` |
| Type scale | 1.200 minor-third, tight tracking, sans display | 1.333 perfect-fourth, oversized display, condensed caps | 1.250 major-third, high-contrast serif display |
| Display font (OFL, self-hosted) | e.g. Inter + IBM Plex Mono for data | e.g. Archivo/Bebas-class condensed + Inter | e.g. Fraunces/Freight-class serif + Inter |
| Grid | 12-col, 24px gutter, strict | 12-col, 40px gutter, asymmetric spans | 12-col editorial, 2-col text measure, wide margins |
| Motion | 120–200ms, opacity + 4px rise, no parallax | 400–700ms reveal, one loop ≤6 s, cinematic easing | 200–300ms, fades and 1px hairlines, no bounce |
| Imagery treatment | diagrams, UI crops, flat data | full-bleed, high-contrast, one hero composition | material/texture detail, generous whitespace |
| Section rhythm | dense, modular, repeating modules | sparse, large, one idea per viewport | quiet, columnar, typographic |
| Danger zone (what breaks the direction) | decorative gradients, soft blobs | more than one accent, parallax everywhere | sans-serif display, tight leading |

### 5.6 What the switcher changes / what it must never change
**Changes:** tokens (colour, radius, borders, elevation), display/body font pairing, type scale and leading, grid gutters and max-width, imagery treatment and aspect ratios, motion durations/easings within the Motion Budget, section backgrounds and dividers.
**Never changes:** positioning, page map, information architecture, section order, offer structure and prices, CTA wording and flow, form fields, claim wording and evidence type, reading order, focus order, alt text intent, contrast minimums, target sizes, reduced-motion behaviour, legal pages.

### 5.7 Accessibility behaviour (per direction)
- Contrast is enforced per token pair: body text ≥ 4.5:1, large text ≥ 3:1, UI borders/focus ≥ 3:1 — checked in CI, not by eye. Cinematic's dark theme is fully re-checked, not assumed.
- Focus is always visible: ≥2 px indicator, 3:1 against both adjacent colours (supports WCAG 2.2 focus criteria); sticky header never fully hides a focused element (`scroll-padding-top` + test).
- Targets ≥24×24 CSS px (WCAG 2.5.8) — including the direction switcher and footer legal links.
- `prefers-reduced-motion: reduce` = the default code path: motion is opt-in via `@media (prefers-reduced-motion: no-preference)`, never opt-out.
- Keyboard-only path through the direction switcher is a required test: switching directions must not move focus or re-announce the whole page (aria-live announcement of the direction name only).
- One help affordance in a consistent place (WCAG 3.2.6); form errors announced with a summary + in-field message (GOV.UK pattern).

### 5.8 Performance rules
- Budget (field targets): **LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at p75**; lab gate: Lighthouse mobile perf ≥ 95, LCP ≤ 2.0 s, TBT ≤ 200 ms on a throttled run.
- Per-page weights: HTML ≤ 30 KB compressed, CSS ≤ 50 KB, JS ≤ 60 KB compressed on the home page (islands only), fonts ≤ 2 families / ≤ 4 files, hero image ≤ 180 KB AVIF, no autoplaying video above 2.5 MB.
- Motion: transform/opacity only; no layout-affecting animation; no scroll-jacking; `content-visibility` for long pages; images always dimensioned.
- Third-party budget: **zero** third-party scripts on the Master Site except analytics (one, async, deferred, cookieless). One exception needs a written note in the QA receipt.

### 5.9 Reference & inspiration rules (the "do not imitate" policy)
1. Research **patterns, structure and technique** — never a brand's expression: no logos, product UI screenshots, illustration style, mascots, copy, or "inspired by <brand>" wording.
2. Every intake reference is tagged: `layout · typography · hero · proof · CTA · motion · forms · pricing · navigation · footer · mobile · accessibility`.
3. A reference is logged with URL, date, what we take (pattern level) and what we explicitly do **not** take.
4. Concept work is always labelled: **"Studio Concept — independent demonstration, not client work."**
5. If a direction starts to resemble a recognisable brand, the direction brief is reworked — not "adjusted slightly".

### 5.10 Disclosure & proof rules
- Concept projects: visible label (not only in a footnote) + no brand names in titles/slugs.
- Redesign studies: same label + "not affiliated with the referenced brand" + no use of the brand's assets beyond what we have rights to.
- Client work: only with written permission (project + logo + quote) recorded in the approval record; quotes are verbatim, and we explain how reviews were obtained (Omnibus requirement).
- Metrics: only client-supplied or client-approved numbers, with the measurement window and tool named.
- Synthetic imagery: never presented as staff/customers; disclosure line attached when a realistic synthetic person is used, plus AI Act Art. 50 considerations. ⚖️
- Structured data: no review/AggregateRating markup for our own business (Google's self-serving review rule) — proof lives in HTML, not in stars.

---

## 6. Reusable Internal Assets

Owner column: `F` = founder (only human), `A` = agent may draft, `F★` = founder signs off, agent never publishes.
Versioning: all files carry `<!-- v0.1 · 2026-09-23 · owner: F · next review: … -->` front-matter; `docs/` files are versioned **vMAJOR.MINOR** with an entry in `CHANGELOG.md`; templates use `vX.Y` and never change silently after a client project started (a change mid-project creates a new minor version and is logged in the project's approval record).

| # | Path | Purpose | Minimum fields / sections | Owner | Versioning rule | Becomes required when |
|---|---|---|---|---|---|---|
| 1 | `README.md` | Orientation + first-five-minutes path | What the OS is, stack, the 7 gates, how to run `npm run gate`, decision log link | F | vX.Y | Immediately |
| 2 | `docs/00-STUDIO-PRINCIPLES.md` | The non-negotiables | Truthfulness, ownership, accessibility, performance, licences, no-clone, human gates, honest pricing | F★ | vX.Y, change = ADR | Before any client work |
| 3 | `docs/01-OFFER-AND-ICP.md` | What we sell to whom | 3 ICPs, pains, triggers, disqualifiers, offer ladder + prices, capacity, proof position | F★ | vX.Y | Before outbound |
| 4 | `docs/02-MESSAGE-ARCHITECTURE.md` | Reusable claim hierarchy | Claim/evidence/mechanism/CTA blocks, objection map, page-type message maps, banned words list | F★ | vX.Y | Before first client copy |
| 5 | `docs/03-DESIGN-DIRECTIONS.md` | The three directions as spec | Token table, type, grid, imagery, motion, do-not-cross rules, switcher invariants | F★ | vX.Y | Before Master Site build |
| 6 | `docs/04-COMPONENT-ALLOWLIST.md` | What may enter a client repo | Allowed list w/ licence + version, forbidden list, review trigger, update policy | A → F★ | vX.Y per dependency change | Immediately |
| 7 | `docs/05-MOTION-BUDGET.md` | Motion as a budgeted resource | Ladder (0→CSS→component→video→3D), per-page budgets, MP4/loop limits, reduced-motion rules, anti-patterns | A → F★ | vX.Y | Before first motion work |
| 8 | `docs/06-ACCESSIBILITY-WCAG-2.2.md` | AA standard + method | 6 new AA criteria, manual test script, keyboard sweep, focus rules, evidence format | A → F★ | vX.Y, review per W3C update | Immediately |
| 9 | `docs/07-PERFORMANCE-BUDGET.md` | Objective launch targets | Field + lab budgets, per-asset weights, third-party budget, measurement instructions | A → F★ | vX.Y | Immediately |
| 10 | `docs/08-PRIVACY-AI-ASSET-POLICY.md` | Data + AI + asset rules | Data map, legal bases, AI tool policy, provenance record, prohibited uploads, red-flag matrix | F★ (+⚖️) | vX.Y, **any change = re-brief** | Before first form + any AI asset |
| 11 | `docs/09-LAUNCH-QA.md` | The launch gate | 60-item checklist, automated vs manual, cannot-launch-until list, waiver procedure | A → F★ | vX.Y | Before every launch |
| 12 | `docs/10-CLIENT-HANDOVER.md` | Ownership transfer | Account list, credentials process, backups, docs, training, retainer options | A → F★ | vX.Y | At first handover |
| 13 | `docs/11-CASE-STUDY-DISCLOSURE.md` | Honest proof rules | Concept/redesign/client labels, quote rules, metric rules, permission workflow | F★ | vX.Y | Before publishing `/work` |
| 14 | `docs/12-DELIVERY-SOP.md` | 5/10/14-day delivery | Phase gates, revision policy, content freeze, change requests, folder + naming conventions | A → F★ | vX.Y | Before first paid project |
| 15 | `docs/13-SALES-AND-PORTFOLIO.md` | Pipeline without fake proof | Portfolio IA, prospect scoring, 30-prospect workflow, outreach + teardown-led audit, proposal structure, objection handling | A → F★ | vX.Y | Before outbound |
| 16 | `skills/*/SKILL.md` (7 files) | Repeatable agent behaviours | YAML frontmatter (name, description), triggers, inputs, steps, outputs, refusal conditions, gates | A → F★ | vX.Y, spec-compatible | Immediately |
| 17 | `templates/client-intake.md` | Qualification | 18 fields incl. scope, budget band, deadline, legal entity, data owner, decision maker | A → F★ | vX.Y | Before every proposal |
| 18 | `templates/message-map.md` | Copy spine | Audience, job, objection, claim, evidence type, mechanism, proof asset, CTA, measurement | A → F★ | vX.Y | Every copy project |
| 19 | `templates/teardown-report.md` | The primary offer deliverable | 3 ranked findings (clarity/proof/path), severity, evidence, redacted screenshot, 1-variable next step, disclosure footer | A → F★ | vX.Y | Every teardown |
| 20 | `templates/design-direction-brief.md` | Art direction contract | Direction, references (tagged), do-not-imitate list, tokens, imagery brief, motion budget, acceptance criteria | A → F★ | vX.Y | Before design work |
| 21 | `templates/asset-provenance-log.csv` | Rights trail | asset_id, source_type (own/stock/AI/client), source_url, licence, licence_file, date, creator, AI_tool+model, prompt_hash, human_reviewer, approval_id, allowed_uses, restrictions | A → F★ | append-only | First asset of any kind |
| 22 | `templates/ai-asset-approval.md` | AI release gate | Tool+plan, inputs used (assert no client assets), output class, disclosure decision, label placement, reviewer, date | F★ | append-only, never edited | Any AI asset before production |
| 23 | `templates/qa-launch-checklist.md` | Launch receipt | a11y automated + manual, perf, SEO/meta, forms test matrix, legal pages, backups/rollback, sign-off | A → F★ | per project, frozen at launch | Every launch |
| 24 | `templates/handover-packet.md` | Client ownership | Accounts, access model, DNS, repo, hosting, analytics, CMS, credentials protocol, backup/restore proof, training recording, support window | A → F★ | per project | At handover |
| 25 | `templates/case-study.md` | Proof artefact | Client/permission status, context, constraint, approach, artefacts, measured outcome (or "not measured"), disclosure line | A → F★ | per project | On permission |
| 26 | `schemas/*.schema.json` (5) | Machine-checkable discipline | project-brief, design-direction, asset-record, qa-receipt, approval-record | A → F★ | semver per schema | Immediately |
| 27 | `prompts/*.md` (5) | Reusable prompt library | Higgsfield hero concepts, Higgsfield motion loops, copy message map, teardown analysis, build spec | A → F★ | vX.Y | Before first AI/creative use |
| 28 | `research/*.csv` + `poc-backlog.md` | Evidence base | github-audit, resource-inventory, license-register, rejected-resources, poc-backlog | A | quarterly refresh | Immediately |
| 29 | `tools/gate.sh` (or npm `gate`) | One-command QA | lint → axe → Lighthouse budget → Playwright smoke | A | vX.Y | Immediately |

**The 10 highest-priority files, written out copy-paste-ready in this repository:** `README.md`, `docs/00`, `docs/03`, `docs/04`, `docs/05`, `docs/06`, `docs/08`, `docs/09`, `templates/client-intake.md`, `templates/teardown-report.md`. (All others exist as structured stubs with their required sections and owners, so nothing is a mystery later.)

---

## 7. 14-Day Build Plan

Assumes one focused operator, 4–7 h/day. Each day has a **deliverable**, an **acceptance gate**, a **failure condition** and a **fallback**. Rule: a failed gate stops the day — it never gets carried silently.

| Day | Objective | Deliverable | Time | Acceptance gate | Failure condition | Fallback |
|---|---|---|---|---|---|---|
| 1 | Freeze decisions + repo skeleton | `proofline-studio-os` repo, README, `docs/00`, `license-register.csv` seeded | 5 h | Repo builds; licence register has a row for every candidate | Cannot state the V1 stack in 5 lines | Cut to §4.1 verbatim; defer all "nice" tools |
| 2 | Offer + message architecture | `docs/01`, `docs/02`, intake template, teardown template | 5 h | Teardown template can be executed on a real stranger's page in ≤45 min | Copy still says "we help brands grow" | Rewrite only the claim + mechanism blocks |
| 3 | Design directions as spec + live switcher | `docs/03` + `demo/direction-switcher.html` with 3 token sets | 6 h | Switcher changes tokens only; IA/CTA/copy identical; contrast passes per pair | Directions look like 3 skins of one look | Reduce differences to typography + grid + motion, re-decide colour later |
| 4 | Stack setup + gates | Astro 7 project, Tailwind 4, Base UI, `npm run gate` (axe + Lighthouse + Playwright) | 6 h | `gate` runs green on a placeholder page; fails loudly when a contrast/target is broken | Cannot reproduce the CI gate locally | Ship axe + Lighthouse only; Playwright smoke on day 6 |
| 5 | Template strip-down | AstroWind stripped to 10 sections, re-tokenised to direction A | 6 h | Home page ≤ 60 KB JS, LCP ≤ 2.0 s lab on throttled mobile | Stripping takes longer than rebuilding | Rebuild the 10 sections by hand from `docs/03` |
| 6 | Copy + content for the Master Site | All section copy, message map per section, objection section, legal page stubs | 6 h | Every claim has a named evidence type; zero unverifiable numbers | Copy sounds like everyone else's studio | Re-run `prompts/copy-message-map.md` with a stricter voice brief |
| 7 | Form path + booking | Worker+D1 endpoint, Turnstile, validation, email routing, Cal.com link, test protocol | 5 h | End-to-end test: submit → record in D1 → notification → confirmation page; spam attempt blocked | Deliverability fails in test | Switch notification to Tally (EU) and keep D1 as the record |
| 8 | Directions B + C implemented | Full token sets, imagery treatment, motion budgets applied | 6 h | All three directions pass contrast, target-size and reduced-motion checks | Direction C looks like a tinted Direction A | Cut to two directions for V1; keep the third as a spec only |
| 9 | Proof pages + disclosure | `/work`, concept labels, `/work/master-site` case study, accessibility statement, privacy notice, mentions légales template | 5 h | Concept labels visible without scrolling; no fabricated proof anywhere | Cannot fill mentions légales (missing entity data) | Publish legal pages as "in preparation" — never fake them |
| 10 | Analytics + measurement plan | Plausible, event taxonomy, KPI dashboard spec, banner decision documented | 4 h | No cookies before consent analysis; no third-party script besides analytics | Analytics fails the privacy review | Ship without analytics on V1; measure with the form's own records |
| 11 | Full QA sweep #1 | axe (0 critical/serious), keyboard sweep, mobile matrix, CWV field check on preview | 6 h | QA receipt signed, or waiver written with rationale | Critical a11y or CLS failure | Fix or remove the offending section — never waive a11y |
| 12 | Content + SEO + polish | Metadata, OG images, sitemap, robots, schema (no self-serving reviews), 404, redirects | 5 h | Rich Results Test clean; OG preview correct | OG images look like templates | Use typographic OG images only |
| 13 | Launch + rollback drill | Client-side deploy, DNS, backups, rollback rehearsal, launch receipt | 5 h | Rollback executed once on purpose and timed (<15 min) | Rollback untested | Do not launch |
| 14 | Handover packet + first outbound | Handover docs, 30-prospect list, 10 personalised teardown-led outreach drafts, POC backlog triage | 6 h | Handover packet complete; 10 outreach messages reference *specific* observations | Only generic outreach possible | Send 3 excellent messages instead of 10 mediocre ones |

**Definition of done for the 14 days:** Master Site live, 7 gates enforced, 10 priority files real (not stubs), one full teardown delivered to a real prospect, and a written list of what V1 deliberately left out.

---

## 8. Validation Experiments

Discipline first: **below 1,000 monthly visits to the test page we do not run formal A/B tests** (documented consensus: <1,000 → skip formal testing; <5,000 → results take months and are unreliable; a 3% baseline with a 15% relative MDE needs ≈10,000 visitors *per variant*). Under threshold we use qualitative evidence and one-variable sequential changes, and we label them as *not* statistically validated.

| # | Hypothesis | Variable | Control | Metric | Sample threshold | Decision rule | Next step |
|---|---|---|---|---|---|---|---|
| 1 | Design-direction preference is not uniform across ICPs | Direction tokens on `/directions` (A/B/C) | No change (all three live) | (a) which card is opened first; (b) self-reported fit via 1-question micro-survey; (c) 5-second test recall | ≥40 sessions + ≥12 survey answers | If one direction gets >60% "fits my business", it becomes the default for that ICP in outreach | Adjust offer copy per ICP, not the tokens |
| 2 | CTA wording changes qualified submissions, not just clicks | Primary CTA copy ("Get a 3-point teardown" vs "See what's broken on your page") | Current wording, 2 weeks | qualified submissions / sessions (a submission with a real URL and a real goal counts) | ≥400 sessions per arm-equivalent window | Predefine: adopt the wording that wins on *qualified* submissions; if unmeasurable in 4 weeks, choose on the 5-second test | Re-test only after traffic doubles |
| 3 | Teardown-form friction is the bottleneck | Form length (4 fields vs 7 fields incl. budget band + deadline) | 4-field version | form starts → submissions (completion rate), plus abandonment reasons from exit survey | ≥150 form starts | If the longer form keeps completion within 20% while improving qualification, adopt it | Never add a field without removing one |
| 4 | Mobile clarity is weaker than desktop | Mobile hero: shorter headline + tighter sub-copy vs desktop version | Desktop copy | 5-second-test comprehension (can the tester state the offer?) + mobile scroll-to-CTA rate | 5 testers (per direction of testing, small but directional) | If <4/5 testers state the offer correctly, the mobile hero copy is wrong regardless of metrics | Re-run with new testers after the rewrite |
| 5 | Perceived trust rises when standards are published (not when logo strips appear) | `/work/master-site` proof-by-method section: present vs absent in the scroll path | Present version | "would you book a call?" (1–5) + CTA click rate from that section | ≥60 sessions on each path within 4 weeks | If trust scores are equal, keep the section (it costs nothing and is honest) — do not add fake proof | Re-test quarterly with client-call recordings as the qualitative input |

**Rules of engagement:** one variable per test · pre-written decision rule before launch · no stopping early on a p-value (Bayesian reading only, and only as *directional*) · no test may violate accessibility or privacy · a test that cannot change a decision is not run.

---

## 9. Compliance and Risk Register

Likelihood/impact: L/M/H. Owners are humans (F = founder) or named external roles.

| # | Risk | Likelihood | Impact | Early signal | Prevention | Human owner | Escalation trigger |
|---|---|---|---|---|---|---|---|
| 1 | **Licence conflict** (custom "free" licences, premium registries, AGPL/GPL boundaries) | M | H | A dependency with no SPDX licence; "free for personal use" wording; a licence not re-checked after an update | `license-register.csv` as a ship gate; quarterly re-check; only MIT/ISC/Apache/MPL/LGPL/GPL/AGPL-with-understood-obligations in client code | F | Any new dependency whose licence is not in the register → stop the build |
| 2 | **Copied design / trade dress / brand look-alike** | M | H | A concept that "looks like <brand>"; reference logged without tags; screenshots in client files | Do-not-imitate policy, tagged intake, mandatory concept labels, art-direction review | F | Direction resembles a recognisable brand → rework before client sees it ⚖️ |
| 3 | **Client confidential data in AI tools** | M | H | Someone uploads a client screenshot/photo to a generative tool; prompts containing client names | AI policy in `docs/08`: no client assets in any generative tool, no client names in prompts; provenance + approval records; private workspace only | F | Any client asset in an AI tool → delete, disclose, log, re-review |
| 4 | **Fake proof** (testimonials, logos, metrics, AI people as staff/customers) | L | H | A quote with no permission record; a number nobody can point to; a "customer photo" with no release | Omnibus ban + Google's fake/incentivised-review rules + our six evidence types; every claim needs substantiation on file | F | Any unverified claim found live → remove within 24 h, log the incident |
| 5 | **Inaccessible interaction** (focus hidden, contrast, target size, drag-only) | M | H | axe findings; can't tab through the direction switcher; sticky header hides focus | WCAG 2.2 AA checklist (6 new AA-relevant criteria), CI axe, manual keyboard sweep, per-token contrast checks | F | A critical/serious axe finding or a failed keyboard sweep → no deploy |
| 6 | **Motion / performance harm** (layout shift, janky scroll, vestibular triggers) | M | M | INP > 200 ms, CLS > 0.1, motion with no reduced-motion path | Motion Budget + Escalation Ladder; CSS-first; transform/opacity only; reduced-motion as default path; CWV budget gate | F | Budget miss at launch → fix or written waiver; a11y-related motion → always fix |
| 7 | **Broken form / data routing** (leads silently lost) | M | H | No test submission in 30 days; notification spam-flagged; D1 rows without notifications | Weekly automated test submission + alerting; D1 as source of truth; documented test protocol; honeypot + Turnstile | F | Two failed tests in a row → disable the form and publish a direct email fallback |
| 8 | **Non-consensual analytics / tracking** | L | H | A third-party script on the page; a cookie set before interaction; GA4 added by a vendor | Cookieless analytics (Plausible/Umami) configured CNIL-style: aggregate-only, first-party, no cross-site, no sharing, 13-month tracker limit (not applicable where no cookies are set), 25-month retention; explicit "no GA4/pixels" rule | F (+⚖️) | Any new tag → privacy review and documented decision before deploy |
| 9 | **Missing client ownership transfer** | M | H | Client has no admin access; site depends on our account; domain in our name | Ownership model in every proposal; handover packet; repo/org transfer; credentials protocol; verified by the client logging in themselves | F | Before final invoice: client must prove access |
| 10 | **AI-generated realistic person misuse** (undisclosed synthetic humans) | L | H | A "team" or "customer" image that is synthetic; no disclosure line; no approval record | Never present synthetic people as real staff/customers; AI Act Art. 50 (applicable since 2026-08-02) disclosure at first exposure; approval record mandatory; realistic-human imagery is default-off for client work | F | Any request to present an AI person as real → refuse and document ⚖️ |
| 11 | **Unsupported legal / SEO / conversion claims** ("WCAG compliant", "GDPR compliant", "guaranteed conversions", "top ranking") | M | H | Marketing copy containing guarantees; a compliance badge with no audit behind it | Banned-words list; substantiation file; wording "we build to WCAG 2.2 AA and document the evidence" instead of "we are compliant" | F | Any guarantee wording reaching a public page ⚖️ |
| 12 | **Sub-processor / transfer risk** (US-run tools with client data) | M | M | A US-only vendor in the lead path; no DPA on file; team-shared drive with client assets | Prefer EU-hosted basics (Tally, Plausible, Cal.com EU/self-host, Cloudflare with DPA); DPA + TOM note per vendor in the project's data map | F (+⚖️) | New vendor touching personal data → DPA check before integration |

Explicit non-claim: this register is a working method, not a compliance certification. Items 1, 2, 4, 8, 10 and 11 are the ones a French/EU lawyer should review before we market compliance to clients.

---

## 10. Final Decision Memo

### 10.1 The 10 modules to adopt first
1. **Astro 7 + Tailwind 4** — static-first delivery core (MIT).
2. **Base UI + selective shadcn/ui copy-ins** — accessible primitives we own (MIT).
3. **Cloudflare Pages + Workers/D1** — hosting and the form endpoint (commercial use allowed, €0–5/mo).
4. **axe-core + Playwright + Lighthouse CI** — the three automated gates.
5. **WCAG 2.2 AA checklist + manual keyboard sweep** — the standard behind the gates.
6. **Plausible (EU) / Umami** — cookieless measurement with a defensible posture.
7. **Fontsource self-hosted OFL fonts + Lucide** — first-party, licence-clean assets.
8. **Tally (EU forms) + Cal.com** — intake and booking without building a CRM.
9. **Keystatic** — the default answer when a client asks "can I edit it?".
10. **The artefact system itself** (12 docs, 7 skills, 9 templates, 5 schemas, provenance + approval logs).

### 10.2 The 5 modules to pilot before adoption
1. **GSAP 3.15** — powerful and free for commercial sites, but a non-OSS licence that can change; pilot on one project behind a wrapper module.
2. **Rive** — great output, paid editor per seat; pilot only where interactivity is the point.
3. **Payload CMS** — correct answer for content-heavy clients, but brings a database and ops; pilot on a >€2,500 build.
4. **Keystatic in GitHub mode** with a non-technical client — pilot the editor experience before promising it.
5. **Higgsfield as concept layer** — pilot with *no* client assets, one hero concept, full provenance + approval records.

### 10.3 The 5 things to avoid
1. **Vercel Hobby for client work** (non-commercial terms) and shadcn.io Pro Blocks on an Individual licence.
2. **Google Fonts CDN / any third-party CDN for fonts or JS** (court ruling + performance).
3. **Lottie for new projects**, 3D/WebGL without a written business case, scroll-jacking, and animation libraries without a `prefers-reduced-motion` path.
4. **Accessibility overlay widgets** marketed as compliance, and reward badges we cannot substantiate.
5. **Building our own CMS, component package, CRM or experimentation platform** in year one.

### 10.4 The first repository structure to create
The tree in this workspace (see `README.md` for the annotated version):
```text
proofline-studio-os/
├── MASTER-REPORT.md            ← this document
├── README.md
├── docs/       00–13
├── skills/     studio-research · conversion-copy · creative-direction · landing-page-build
│               accessibility-qa · performance-qa · launch-review
├── templates/  client-intake · message-map · teardown-report · design-direction-brief
│               asset-provenance-log.csv · ai-asset-approval · qa-launch-checklist
│               handover-packet · case-study
├── schemas/    project-brief · design-direction · asset-record · qa-receipt · approval-record
├── prompts/    higgsfield-hero-concepts · higgsfield-motion-loops · copy-message-map
│               teardown-analysis · build-spec
├── research/   github-audit.csv · resource-inventory.csv · license-register.csv
│               rejected-resources.md · poc-backlog.md · score_resources.py · gh_audit.py
└── demo/       direction-switcher.html
```

### 10.5 The first task to execute tomorrow morning
**09:00 — create the repo, commit `docs/00`, `docs/04`, `docs/06` and `research/license-register.csv`, then run `python3 research/score_resources.py` once to confirm the inventory regenerates.** Then open `demo/direction-switcher.html`, pick the two directions you would actually defend in a client call, and delete the third from V1 scope. That single decision unblocks day 3–8 of the plan.

---

## 11. Stop Conditions Triggered by This Research (for the founder's decision)

1. **Licence divergence with material consequences (STOP):** GSAP's standard licence is free for commercial sites but is *not* open source and prohibits visual animation-builder products; shadcn.io Pro Blocks' Individual tier prohibits client work. Decision needed: accept GSAP as a documented exception, or standardise on Motion + CSS only. **Recommendation: standardise on Motion + CSS for V1; keep GSAP as a named exception.**
2. **Unclear licences in the wider ecosystem (STOP):** the most-recommended community "anti-slop"/CRO skills have no explicit licence. **Recommendation: write our own SKILL.md files (done here) and keep aggregator lists as discovery only.**
3. **AI data-use conflict with client confidentiality (STOP):** Higgsfield permits commercial use, but non-Enterprise accounts still train on inputs by default, and IP indemnification is Enterprise-only. **Recommendation: Higgsfield stays a concept/asset layer for non-client material, with the provenance and approval gates in `docs/08`.**
4. **Legal requirements needing counsel (STOP):** mentions légales content, privacy notice, accessibility statements, AI disclosure wording, and any client-facing claim of compliance. **Recommendation: budget one lawyer review (~2–4 h) before the first paid launch; ship a template that is explicit about needing review.**

## 12. Open evidence gaps (honest limits of this research)
1. **Cloudflare D1 data-residency guarantees for EU clients** — must be verified against Cloudflare's current DPA/regional documentation before promising residency (UNVERIFIED).
2. **EU transactional email provider** for the Worker endpoint (deliverability + residency + DPA) — POC-04 in `research/poc-backlog.md` (UNVERIFIED).
3. **Rive editor commercial terms on the free tier** — sources conflict; confirm with the vendor before relying on free-tier commercial use (UNVERIFIED).
4. **Zeitzone/Rechtsprechung drift:** the French transposition details of the EAA and AI Act enforcement practice are still evolving in 2026 (INFERRED from regulatory publications).
5. **Field traffic data** for the Master Site once live — the only way to validate §8 experiments (UNVERIFIED until measured).

## 13. Sources
[1] MECLABS Conversion Sequence Heuristic — https://content.marketingsherpa.com/data/public/LP-Exercise-WS.pdf · [2] LIFT Model — https://umbrex.com/resources/frameworks/marketing-frameworks/lift-model-for-conversion-value-relevance-clarity-anxiety-distraction-urgency/ · [3] NN/g 5-second testing — https://www.nngroup.com/articles/five-second-testing/ · [4] TeardownHQ audit checklist — https://teardownhq.com/insights/landing-page-audit-checklist · [5] USWDS — https://github.com/uswds/uswds · [6] GOV.UK Frontend — https://github.com/alphagov/govuk-frontend · [7] Carbon — https://github.com/carbon-design-system/carbon · [8] React Aria/Spectrum — https://github.com/adobe/react-spectrum · [9] shadcn/ui — https://github.com/shadcn-ui/ui (MIT licence statement: https://www.shadcndesign.com/blog/is-shadcn-ui-free) · [10] Base UI v1 — https://www.infoq.com/news/2026/02/baseui-v1-accessible/ · [11] Radix — https://github.com/radix-ui/primitives · [12] Tailwind — https://github.com/tailwindlabs/tailwindcss · [13] Astro — https://github.com/withastro/astro · [14] Next.js — https://github.com/vercel/next.js · [15] AstroWind — https://github.com/arthelokyo/astrowind · [16] Magic UI — https://github.com/magicuidesign/magicui · [17] shadcn.io licence — https://www.shadcn.io/license · [18] Motion — https://github.com/motiondivision/motion · [19] GSAP standard licence — https://gsap.com/community/standard-license/ · [20] lottie-web — https://github.com/airbnb/lottie-web · [21] Rive runtimes/pricing — https://github.com/rive-app/rive-react · [22] R3F/three — https://github.com/pmndrs/react-three-fiber · [23] Lucide — https://github.com/lucide-icons/lucide · [24] Fontsource — https://fontsource.org/ · [25] Unsplash licence — https://unsplash.com/license · [26] Cloudflare limits — https://developers.cloudflare.com/pages/platform/limits/ · [27] Netlify pricing — https://www.netlify.com/pricing/ · [28] Vercel fair use — https://vercel.com/docs/limits/fair-use-guidelines · [29] Hetzner cloud — https://www.hetzner.com/cloud/ · [30] GitHub pricing — https://github.com/pricing · [31] Keystatic — https://github.com/Thinkmill/keystatic · [32] Payload — https://github.com/payloadcms/payload · [33] Tally — https://tally.so/ · [34] Formbricks — https://github.com/formbricks/formbricks · [35] Cal.com — https://github.com/calcom/cal.com · [36] Plausible — https://github.com/plausible/analytics · [37] Umami — https://github.com/umami-software/umami · [38] Matomo — https://github.com/matomo-org/matomo · [39] PostHog — https://github.com/PostHog/posthog · [40] When not to A/B test — https://www.growthbook.io/insights/when-not-to-run-test-product-leader-takeaways · [41] WCAG 2.2 — https://www.w3.org/TR/WCAG22/ · [42] axe-core — https://github.com/dequelabs/axe-core · [43] Playwright — https://github.com/microsoft/playwright · [44] Lighthouse — https://github.com/GoogleChrome/lighthouse · [45] Core Web Vitals — https://web.dev/articles/vitals · [46] Google review snippets (self-serving + 2026-07-24 update) — https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful · https://searchenginecore.com/google-quietly-updated-review-snippet-schema-heres-what-changed/ · [47] CNIL audience measurement exemption — https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies-solutions-pour-les-outils-de-mesure-daudience · [48] AI Act Art. 50 application date — https://bratby.law/ai-act-transparency-obligations-2026/ · [49] Draft labelling code — https://www.jonesday.com/en/insights/2026/01/european-commission-publishes-draft-code-of-practice-on-ai-labelling-and-transparency · [50] Omnibus Directive / fake reviews — https://www.lexology.com/library/detail.aspx?g=929020b0-ff28-4964-a6fa-ad7f6edd2475 · [51] Mentions légales (FR) — https://www.economie.gouv.fr/entreprises/developper-son-entreprise/innover-et-numeriser-son-entreprise/mentions-sur-votre-site-internet-les-obligations-respecter · [52] Higgsfield terms/ownership — https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially · [53] Agent-skills registry — https://github.com/VoltAgent/awesome-agent-skills · [54] OpenDesign — https://github.com/nexu-io/open-design

*GitHub metadata for all repositories cited above was captured live on 2026-09-23 and is stored in `research/github-audit.csv`; npm versions in the same session (Astro 7.3.4, Next 16.3.6, Tailwind 4.3.3, React 19.3.0, Motion 13.4.1, GSAP 3.15.0, three 0.186.0, @base-ui/react 1.8.0, radix-ui 1.6.7, axe-core CLI 4.13.0, Playwright 1.63.0).*
