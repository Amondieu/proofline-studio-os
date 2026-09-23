# 31 — Evidence-Backed Quality Cookbook
<!-- v0.1 · 2026-09-23 · owner: agent drafts, founder approves each rule · every rule needs a source, a test and a gate -->

**What this is.** A working cookbook, not a trend report. Every rule must name its evidence level, its implementation standard, its test, its anti-pattern and its launch gate. Nothing enters this file because it "looks premium", has stars, or won an award.

**Inventory:** 40 pattern cards · 40 anti-pattern rows (severity S1–S3) · 1 must-pass launch checklist (16 items, mapped to test ids) · 13 code-review blockers · 3 tier standards · 1 validation loop · 1 thirty-day calendar · 7 research gaps.

**Related files.** Delivery gates live in `docs/09-LAUNCH-QA.md`; motion budget in `docs/05`; performance numbers in `docs/07`; accessibility method in `docs/06`; asset/AI rules in `docs/08`; client-tier standards in §7 below.

---

## 1. Evidence hierarchy (how much authority a source gets)

| Level | Class | Sources | How we use it | Never used for |
|---|---|---|---|---|
| **1** | **Normative** | W3C WCAG 2.2 (= ISO/IEC 40500:2025 since 2025-10-21), EN 301 549, GDPR/CNIL, French LCEN, EU AI Act Art. 50, Google Search structured-data policies | **Non-negotiable launch gates** | Interpretation of our own legal risk |
| **2** | **Technical** | web.dev / Chrome docs, MDN, framework and browser documentation, Lighthouse docs | **Implementation standards** (how to build it correctly) | Conversion claims |
| **3** | **Research / UX** | Nielsen Norman Group, Baymard, GOV.UK Design System research, academic HCI | **Testable hypotheses** with a local test | Anything normative |
| **4** | **Observational** | Curated galleries and studio portfolios, award sites, SaaS examples | **Visual/pattern vocabulary only** | Causal proof of anything. Never taken as evidence that a pattern converts |

**Citation discipline:** every card below cites its level. Level-1/2 rules are build-blocking. Level-3 rules are *hypotheses we can test locally*. Level-4 material never enters a client deliverable as a claim — and never as a copy-paste.

> Verification note: specific level-3 findings (e.g. exact Baymard percentages) are **not** quoted here unless verified in this session. Where a rule rests on level-3 work, the card says `[verify finding]` and the rule stands on its *test*, not on the statistic.

---

## 2. Source inventory

| Source | Level | Credibility | Use in the cookbook |
|---|---|---|---|
| W3C WCAG 2.2 / ISO/IEC 40500:2025 | 1 | Authoritative standard, now also an ISO/IEC standard | All A11Y-* cards, launch gates |
| CNIL (prospection, audience measurement) | 1 | Regulator guidance | Consent-free analytics config, outreach rules (`docs/30`) |
| EU AI Act Art. 50 + draft labelling code | 1 | Regulation + Commission code | AI-* cards, disclosure duty |
| Google Search structured-data policies | 1 | Platform contract | SEO-003 (self-serving reviews) |
| web.dev / Chrome Core Web Vitals documentation | 2 | Vendor technical documentation | PERF-* cards, `docs/07` budgets |
| MDN Web Docs | 2 | Reference documentation | Implementation specifics |
| GOV.UK Design System (+ Service Manual) | 2/3 | Research-backed, government-grade | FORM-* cards, one-thing-per-page, error summaries |
| Nielsen Norman Group | 3 | Long-standing, published method | HERO-*, NAV-*, TYPE-* hypotheses |
| Baymard Institute | 3 | Large-scale usability research | FORM-* hypotheses `[verify finding]` |
| Tailwind / Astro / Base UI docs | 2 | Framework documentation | Implementation mechanics only |
| Curated galleries (Awwwards, Godly, Land-book, SaaSFrame, Lapa Ninja) | 4 | Curated, taste-driven | Art-direction vocabulary — never claims, never copies |

Not used as evidence: GitHub stars, award counts, "trend" listicles, marketing blog posts without method, screenshots of other people's sites.

---

## 3. Pattern cards

Format (full example shown for the first three; the rest are compressed but carry every required field):

```md
# PATTERN: DOMAIN-NNN — Title
Evidence level · Source (URL) · Problem solved · Required implementation ·
Accessibility impact · Performance impact · Anti-pattern · Test protocol ·
Launch gate · Tier · Evidence status (Approved default / Hypothesis / Conditional)
```

### 3.1 Hero & homepage clarity

#### HERO-001 — State who it is for, what changes, and what to do next (above the fold)
- **Level 2/3** · Source: NN/g first-impression research + our own 5-second test protocol (`docs/02`)
- **Problem:** a first-time visitor cannot repeat the offer back after five seconds.
- **Required implementation:** exactly one `<h1>` naming the outcome; one supporting line naming the buyer or the mechanism; one primary CTA visible without scrolling; no competing second action of equal weight.
- **A11y impact:** none negative — forces one clear heading structure.
- **Perf impact:** neutral (text is the cheapest element you can put there).
- **Anti-pattern:** hero carousel; three equal CTAs; "Welcome to [Company]"; hero image with the text baked into it; leading with a feature grid before the visitor recognises the problem (problem before solution, symptom before treatment).
- **Test:** 5-second test with ≥5 people, unmasked, one question ("what does this company do, and what would you click?"). <4/5 correct → rewrite the hero, not the subhead.
- **Gate:** block if <4/5 testers state the offer.
- **Tier:** all. **Status:** Approved default.

#### HERO-002 — One primary action, repeated in the same words
- **Level 3** · Source: LIFT-style clarity/anxiety lens (see `docs/02`)
- **Problem:** visitors cannot tell which action matters.
- **Implementation:** one CTA wording, identical in hero, mid-page and footer; secondary CTA visually subordinate; sticky mobile CTA after the first viewport.
- **A11y:** sticky bar must not obscure focus (WCAG 2.4.11) and must be dismissible.
- **Perf:** sticky element must not trigger layout shift or scroll listeners.
- **Anti-pattern:** "Learn more" + "Get started" + "Contact us" as peers.
- **Test:** read only the CTAs top-to-bottom — is it one action repeated? Click target ≥24×24 px on mobile.
- **Gate:** block if two CTAs compete above the fold.
- **Tier:** all. **Status:** Approved default.

#### HERO-003 — The LCP element must be text or a dimensioned image, never a video
- **Level 2** · Source: web.dev LCP guidance; `docs/07` budget
- **Problem:** hero video/undimensioned images destroy LCP and shift layout.
- **Implementation:** LCP candidate is HTML text where possible; if an image, it is `fetchpriority="high"`, preloaded, correctly sized, AVIF/WebP, ≤180 KB; video only with `poster`, `preload="none"` and a static fallback.
- **A11y:** the video must never carry information that is not also text.
- **Perf:** no `lazy` on the LCP image; no font-blocking of the LCP text.
- **Anti-pattern:** autoplaying hero video with a text overlay baked into the video.
- **Test:** Lighthouse mobile LCP ≤2.0 s lab; CLS ≤0.05 in the field.
- **Gate:** cannot-launch: LCP element undimensioned or lazy-loaded.
- **Tier:** all. **Status:** Approved default.

#### HERO-004 — Say what happens after the click
- **Level 3** · Source: GOV.UK "start page" practice (expectation setting)
- **Problem:** visitors hesitate because they do not know what they are committing to.
- **Implementation:** one microcopy line under the CTA: what is required, how long it takes, when they hear back.
- **A11y:** microcopy must not be the only place the requirement exists.
- **Perf:** none.
- **Anti-pattern:** "Book a call" with no indication of duration, cost or next step.
- **Test:** 5-second test follow-up: "what happens if you click that?"
- **Gate:** recommended; blocks only if the CTA leads to a paid or account-creating flow.
- **Tier:** all. **Status:** Approved default.

### 3.2 Information architecture & navigation

#### NAV-001 — Persistent, order-stable navigation
- **Level 1/3** · Source: WCAG 3.2.3 (consistent navigation) + 3.2.6 (consistent help, new in 2.2)
- **Problem:** users lose orientation when navigation moves between templates.
- **Implementation:** same landmark order on every page; help/contact affordance in the same relative place; no hamburger-only desktop nav; current page indicated programmatically (`aria-current`).
- **A11y:** keyboard order follows visual order; skip link present and visible on focus.
- **Perf:** nav is static HTML, not hydrated.
- **Anti-pattern:** mobile-only menus on desktop; nav that reorders per page. *Conditional:* campaign landing pages may drop the full nav for logo + one CTA — never the legal/privacy/contact links.
- **Test:** keyboard sweep across three pages — same order, same help location; `aria-current` correct.
- **Gate:** cannot-launch if navigation order differs between major templates without a stated reason.
- **Tier:** all. **Status:** Approved default.

### 3.3 Message hierarchy (B2B service & SaaS)

#### MSG-001 — Claim → Evidence type → Mechanism → Next step, per section
- **Level 3** · Source: our own message architecture (`docs/02`), built on LIFT/MECLABS heuristics
- **Problem:** sections contain claims no visitor can evaluate.
- **Implementation:** every section carries a ≤12-word claim, one named evidence type, a one-sentence mechanism, and a next step.
- **A11y:** claims are text, not images of text (WCAG 1.4.5).
- **Perf:** none.
- **Anti-pattern:** adjective stacks ("innovative, cutting-edge, world-class").
- **Test:** message-map audit — any claim without an evidence type is deleted.
- **Gate:** block if a section has no evidence type.
- **Tier:** all. **Status:** Approved default.

#### MSG-003 — Objection handling is a section, not a hope
- **Level 3** · Source: practitioner consensus across CRO literature; our objection map
- **Problem:** unaddressed objections silently stop action.
- **Implementation:** a dedicated block with the 5 real objections in the visitor's own language, each answered in ≤25 words, including the price/ownership/edit-it-later concerns.
- **A11y:** use a definition-style structure (heading + answer) so screen-reader users can skim.
- **Perf:** none.
- **Anti-pattern:** hiding pricing and ownership questions until the sales call.
- **Test:** compare against actual sales-call objections logged in the last 10 conversations.
- **Gate:** block if pricing or ownership is never addressed anywhere on the site.
- **Tier:** all. **Status:** Approved default.

### 3.4 CTA, forms and booking flows

#### CTA-001 — Verb + object, and never the word "Submit"
- **Level 2/3** · Source: GOV.UK button guidance (clear action labels) + our CTA plan
- **Problem:** generic labels force the user to work out what happens.
- **Implementation:** CTA text states the outcome ("Get the 3-point teardown"); button labels match the destination page's heading (no surprise after the click).
- **A11y:** accessible name = visible label (WCAG 2.5.3 label in name).
- **Perf:** none.
- **Anti-pattern:** "Submit", "Click here", "Learn more" for a conversion action.
- **Test:** keyboard + screen reader: does the accessible name match the visible label?
- **Gate:** blocks on the label-in-name failure.
- **Tier:** all. **Status:** Approved default.

#### FORM-001 — Persistent visible labels with accessible validation
- **Level 1/2** · Source: WCAG 1.3.1, 3.3.1, 3.3.2, 3.3.3, 4.1.3 (ARIA status messages) · GOV.UK error-summary pattern
- **Problem:** placeholder-as-label disappears on input and blocks error recovery.
- **Implementation:** visible `<label for>` per field; help text before the input where needed; error text linked via `aria-describedby`; an error summary at the top of the form on multi-field submissions; success confirmed after a *server* response; autocomplete attributes set for known fields.
- **A11y impact:** this is the single highest-value form pattern; screen-reader users get the field purpose and the error in context.
- **Perf impact:** none.
- **Anti-pattern:** placeholder-only labels; colour-only error signalling; silent failure; more than one decision on the same screen (newsletter + booking + survey).
- **Test:** (1) keyboard-only completion, (2) invalid input submission, (3) screen-reader check on the error, (4) mobile completion, (5) end-to-end email/record receipt.
- **Gate:** **cannot-launch** if any field lacks a persistent accessible label or if submission can fail silently.
- **Tier:** all. **Status:** Approved default.

#### FORM-002 — Ask only what you will use, and say why
- **Level 1/3** · Source: GDPR data minimisation (Art. 5(1)(c)) + Art. 13/14 information
- **Problem:** unnecessary fields raise friction *and* legal exposure.
- **Implementation:** every field has a purpose sentence in the internal brief; a short privacy microcopy line beside the submit button linking to the notice; no "phone" field unless a human calls.
- **A11y:** pairing purpose text to fields helps cognitive accessibility.
- **Perf:** none.
- **Anti-pattern:** asking company size, budget and timeline on an unqualified first contact.
- **Test:** field-by-field justification review; privacy notice matches actual fields.
- **Gate:** blocks if a stored field is not described in the privacy notice.
- **Tier:** all. **Status:** Approved default.

#### FORM-003 — Spam protection that does not punish humans
- **Level 2/3** · Source: our own Worker pattern; WCAG 3.3.8 (accessible authentication — don't add cognitive tests)
- **Problem:** naive protection (hard puzzles) costs real submissions and excludes people.
- **Implementation:** honeypot field hidden from users, Cloudflare Turnstile (non-interactive where possible), server-side rate limit, and a silent-fail + logged event — never a CAPTCHA the user must solve unless risk demonstrably requires it.
- **A11y:** no cognitive function test for legitimate users (3.3.8).
- **Perf:** one extra script maximum; must not block the form render.
- **Anti-pattern:** image-grid CAPTCHAs in front of a €600 page.
- **Test:** scripted spam attempt blocked; real submission passes three times in a row on mobile.
- **Gate:** blocks if spam protection can reject a legitimate mobile submission.
- **Tier:** all. **Status:** Approved default.

#### FORM-004 — The failure path is a designed screen
- **Level 1/2** · Source: WCAG 3.3.1/3.3.3, GOV.UK validation practice
- **Problem:** failed submissions lose the user's work or hide why it failed.
- **Implementation:** values are preserved on error; error message names the problem and the fix in the field context; a fallback email address is shown if the endpoint is unreachable; a monitoring alert fires when submissions stop.
- **A11y:** errors announced (`role="alert"` or a focus-moved summary).
- **Perf:** none.
- **Anti-pattern:** "Something went wrong" with no retained data and no alternative contact.
- **Test:** submit empty, submit invalid, kill the endpoint (simulate) and verify the fallback path.
- **Gate:** **cannot-launch** without a verified failure path and monitoring.
- **Tier:** all. **Status:** Approved default.

### 3.5 Trust, proof and claim substantiation

#### PROOF-001 — Four evidence types, and nothing else
- **Level 1/3** · Source: EU Omnibus Directive (fake/incentivised reviews banned; verification must be described) + our `docs/02`
- **Problem:** invented proof is now a legal risk, not only an ethical one.
- **Implementation:** every proof element is one of: demonstrated method · stated standard · permissioned quote (verbatim, permission recorded, procurement described) · labelled concept work. No logo walls without written permission.
- **A11y:** quote text must be real text, not an image.
- **Perf:** none.
- **Anti-pattern:** "trusted by 100+ companies" with no named company; anonymised "a happy client said"; comparison numbers rendered without units, baseline or window ("3× faster").
- **Test:** every public claim traced to a file in the project's substantiation folder.
- **Gate:** **cannot-launch** if any claim lacks substantiation.
- **Tier:** all. **Status:** Approved default.

#### PROOF-002 — Show the method when you cannot show the clients
- **Level 3** · Source: our own positioning strategy; testable in validation experiment #5
- **Problem:** a new studio has no logo wall and must not fake one.
- **Implementation:** publish the gates, budgets, receipts and provenance rules as the proof surface; link the artefacts.
- **A11y:** the proof section must be readable at 200% zoom (it is dense).
- **Perf:** none.
- **Anti-pattern:** stock-photo "team" or AI-generated people presented as staff/customers (also an AI Act disclosure issue).
- **Test:** trust question in validation experiment #5 ("would you book a call?").
- **Gate:** recommended; blocks if any visual on the page could be mistaken for a real employee or customer.
- **Tier:** all. **Status:** Hypothesis.

#### PROOF-003 — Pricing and ownership stated on the page
- **Level 3** · Source: B2B buyer research; our own objection map
- **Problem:** hidden pricing shifts work to the call and filters out the wrong people late.
- **Implementation:** publish price bands, delivery windows, revision counts, exclusions and the ownership model.
- **A11y:** price tables must reflow at 320 px (WCAG 1.4.10) — use lists, not wide tables.
- **Perf:** none.
- **Anti-pattern:** "contact us for pricing" on every tier.
- **Test:** 320 px reflow check on the pricing block; count of "how much?" questions on calls.
- **Gate:** blocks if the pricing block breaks reflow.
- **Tier:** all. **Status:** Approved default.

#### PROOF-004 — A case study states what we cannot claim as clearly as what we can
- **Level 1/3** · Source: EU Omnibus Directive (claim substantiation, reviews) + our permission workflow (`docs/11`)
- **Problem:** case studies inflate ("+37 % conversions") in ways nobody can verify; that is both a legal and a credibility risk.
- **Required implementation:** four blocks per case — context, constraint, what we changed, and a **span** section listing the permission status of every asset and metric ("client-approved quote, dated", "metric measured by the client's analytics, window stated, written approval on file", "no metric permissioned — none shown"), labelled concept work clearly.
- **A11y impact:** the case must be readable as text; screenshots need descriptive alt text; before/after images need a text equivalent of the difference.
- **Perf impact:** case-study media is the heaviest content on most studio sites — budget it (≤3 images, compressed, dimensioned).
- **Anti-pattern:** anonymised "a client said…"; percentage claims with no tool, window or approval; screenshots of another studio's design.
- **Test:** every published number and quote traces to a permission record; no metric appears without its window and source.
- **Gate:** **cannot-launch** if a metric or quote has no permission record.
- **Tier:** Authority/Launch (Starter: method as proof instead). **Status:** Approved default.

### 3.6 Responsive typography and scanning

#### TYPE-001 — Measure, leading and scale before font choice
- **Level 2/3** · Source: typographic best practice + NN/g readability research `[verify finding]`
- **Problem:** long lines and tight leading slow reading on desktop and mobile.
- **Implementation:** body measure 45–75 characters (`max-width` in `ch`), line-height 1.5–1.7 for body, scale ratio from tokens (1.2 / 1.333 / 1.25 per direction), display type locked to a token ceiling per direction.
- **A11y:** text must reflow at 320 px and 200% zoom (WCAG 1.4.4, 1.4.10); never fix text in px-only containers that clip.
- **Perf:** one or two font families; subset; `font-display: swap`; metric-compatible fallback to prevent CLS.
- **Anti-pattern:** 100+ character lines; all-caps paragraphs; fonts loaded from a third-party CDN.
- **Test:** zoom 200% + 320 px width; measure characters per line with a ruler in devtools; check fallback metrics for CLS.
- **Gate:** blocks on reflow failure.
- **Tier:** all. **Status:** Approved default.

#### TYPE-002 — Headings carry the argument
- **Level 1/2** · Source: WCAG 1.3.1 (structure) + scanning behaviour
- **Problem:** sections that only make sense if you read the paragraph.
- **Implementation:** one `<h1>`; sequential heading levels; each section heading states the claim, not the topic ("Find the three things costing you conversions", not "Our approach").
- **A11y:** screen-reader users navigate by headings — this is their primary map.
- **Perf:** none.
- **Anti-pattern:** styling a `<div>` as a heading; skipping levels for visual reasons.
- **Test:** read only the headings; then check the heading outline in devtools.
- **Gate:** blocks on skipped levels or non-semantic headings.
- **Tier:** all. **Status:** Approved default.

### 3.7 Accessibility (WCAG 2.2 AA)

#### A11Y-001 — Focus is always visible and never fully obscured
- **Level 1** · Source: WCAG 2.4.11 Focus Not Obscured (Minimum, **AA, new in 2.2**), 2.4.7, 2.4.13 (AAA as our internal target)
- **Problem:** sticky headers, cookie banners and chat widgets hide the focused element; keyboard users lose their place.
- **Implementation:** `:focus-visible` ring ≥2 px with 3:1 contrast against both adjacent colours; `scroll-padding-top` matching the sticky header height; no full-width overlay that can cover focus; dialogs trap focus intentionally and restore it on close.
- **A11y impact:** direct WCAG 2.2 AA criterion.
- **Perf:** none.
- **Anti-pattern:** `outline: none` without a replacement; sticky bars without scroll offset.
- **Test:** keyboard sweep with the sticky header present; focus a link near the top while the bar is visible; open and close a dialog and verify focus restoration.
- **Gate:** **cannot-launch.**
- **Tier:** all. **Status:** Approved default.

#### A11Y-002 — Touch and pointer targets ≥24×24 CSS px
- **Level 1** · Source: WCAG 2.5.8 Target Size (Minimum, **AA, new in 2.2**); 2.5.7 Dragging Movements (AA)
- **Problem:** small or drag-only controls exclude users with motor impairments and cause mobile mis-taps.
- **Implementation:** all interactive controls ≥24×24 px with spacing, or a 24 px circle that does not overlap another target; any drag interaction has a single-pointer alternative (buttons) — including any before/after slider or carousel.
- **A11y:** two new AA criteria; also reduces accidental taps for everyone.
- **Perf:** none.
- **Anti-pattern:** 16 px icon-only buttons; drag-only image comparison; swipe-only galleries.
- **Test:** measure every control in devtools at mobile viewport; perform the compare/reorder task with buttons only.
- **Gate:** **cannot-launch.**
- **Tier:** all. **Status:** Approved default.

#### A11Y-003 — Contrast is a token property, verified per direction
- **Level 1** · Source: WCAG 1.4.3 (4.5:1), 1.4.11 (3:1 for UI), 1.4.1 (use of colour)
- **Problem:** cinematic and editorial palettes tempt low-contrast accents; text over imagery fails unpredictably.
- **Implementation:** every text/background pair in the token set is verified; accent colours used for text must pass 4.5:1; text over images gets a scrim or a solid plate; error/success never signalled by colour alone.
- **A11y:** core AA requirement; also the most common automated finding.
- **Perf:** none.
- **Anti-pattern:** light-grey "muted" text on white below 4.5:1; thin accent text on photo backgrounds.
- **Test:** automated contrast check per token pair + manual check of text over imagery at 320 px.
- **Gate:** **cannot-launch.**
- **Tier:** all. **Status:** Approved default.

#### A11Y-004 — Motion is opt-in, not opt-out
- **Level 1** · Source: WCAG 2.3.3 Animation from Interactions (AAA) + 2.2.2 Pause/Stop/Hide (A); our `docs/05`
- **Problem:** vestibular harm and distraction from decorative animation.
- **Implementation:** author the static state as default; enable animation only under `@media (prefers-reduced-motion: no-preference)`; any auto-playing/moving content >5 s offers pause/stop; no infinite marquees behind text; no motion that cannot be disabled in CSS.
- **A11y:** protects vestibular and attention-impaired users; also improves INP.
- **Perf:** reduces main-thread work.
- **Anti-pattern:** JS-only motion guards; "reduce motion" implemented as a slow version of the same movement.
- **Test:** OS reduced-motion on → verify every direction; check pause control on any >5 s moving element.
- **Gate:** **cannot-launch.**
- **Tier:** all. **Status:** Approved default.

#### A11Y-005 — Redundant entry and consistent help
- **Level 1** · Source: WCAG 3.3.7 Redundant Entry (**A, new in 2.2**), 3.2.6 Consistent Help (**A, new in 2.2**)
- **Problem:** multi-step flows re-ask information; help moves around the site.
- **Implementation:** autofill/select already-provided values in multi-step forms (or allow "same as above"); keep contact/help affordances in the same relative position on every template.
- **A11y:** two new criteria in 2.2 that teams routinely miss.
- **Perf:** none.
- **Anti-pattern:** a two-step form asking for the email twice; help link appearing in the header on one page and the footer on another.
- **Test:** walk the multi-step flow and count re-entry; compare help location across three templates.
- **Gate:** **cannot-launch** on redundant entry in a live multi-step flow.
- **Tier:** Authority/Launch (Starter: only if a multi-step flow exists). **Status:** Approved default.

### 3.8 Performance / Core Web Vitals

#### PERF-001 — Budgets before beauty
- **Level 2** · Source: web.dev Core Web Vitals thresholds (LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 at p75) + `docs/07`
- **Problem:** pages optimised by feel miss the thresholds that users feel.
- **Implementation:** per-page weight budgets (HTML ≤30 KB, CSS ≤50 KB, JS ≤60 KB, hero ≤180 KB, fonts ≤2 families, ≤1 third-party script) enforced in CI.
- **A11y:** no trade-off — fast pages benefit assistive-tech users too.
- **Perf:** this is the rule.
- **Anti-pattern:** adding a chat widget, a heatmap and three analytics tags "for measurement".
- **Test:** Lighthouse CI assertions; weight diff in the QA receipt.
- **Gate:** waiver-eligible **only** with cause + fix date; CLS-related misses are never waived.
- **Tier:** all (budgets tighten by tier). **Status:** Approved default.

#### PERF-002 — Reserve space for everything that loads late
- **Level 2** · Source: web.dev CLS guidance
- **Problem:** late-loading images, ads or embeds shove content and cause mis-clicks.
- **Implementation:** `width`/`height` (or aspect-ratio) on every image/video/iframe; font fallbacks with matched metrics; no content injected above existing content after load; reserved slots for any dynamic block.
- **A11y:** layout stability reduces mis-activation for motor-impaired users.
- **Perf:** CLS requires this, not "minimises" it.
- **Anti-pattern:** banner/notification injected at the top after hydration.
- **Test:** CLS measured on a throttled mobile run after a full scroll; field check at day 7.
- **Gate:** **cannot-launch** if CLS >0.1; target ≤0.05.
- **Tier:** all. **Status:** Approved default.

#### PERF-003 — Static first, islands second, hydration last
- **Level 2** · Source: Astro framework documentation (zero-JS default; islands); general hydration-cost research `[verify finding]`
- **Problem:** shipping a framework shell for a marketing page costs INP and bytes for nothing.
- **Implementation:** static HTML by default; hydrate only the components that need state (switcher, accordion, dialog, form validation); no client-side routing; no state library.
- **A11y:** less JS = fewer hydration-induced focus jumps.
- **Perf:** direct INP and JS-budget effect.
- **Anti-pattern:** hydrating the whole page to animate one card.
- **Test:** audit `npx astro build` output: bytes of JS shipped per page against the budget.
- **Gate:** blocks if JS exceeds budget without a written justification.
- **Tier:** all. **Status:** Approved default.

#### PERF-004 — Fonts: self-hosted, subset, preloaded once, with a matched fallback
- **Level 1/2** · Source: LG München I ruling on Google Fonts CDN (unlawful IP transfer without a basis) + web.dev font guidance
- **Problem:** third-party font CDNs leak IP addresses to a third country *and* cost a connection round-trip.
- **Implementation:** woff2 files self-hosted with their licence files; subset to the character set actually used; `preload` only the display font; `font-display: swap` with size-adjusted fallback; never `@import` from a CDN.
- **A11y:** `swap` avoids invisible text; user font-size preferences must still work (no fixed px-only scaling).
- **Perf:** removes a blocking cross-origin request; the single easiest LCP win.
- **Anti-pattern:** `<link href="fonts.googleapis.com">`; icon fonts; 5 weights of 3 families.
- **Test:** devtools network — zero third-party font requests; CLS after font swap ≤0.05; check licence files present in the repo.
- **Gate:** **cannot-launch** on any third-party font request.
- **Tier:** all. **Status:** Approved default.

### 3.9 Motion and reduced motion

#### MOT-001 — The Motion Escalation Ladder is a budget, not a menu
- **Level 2/3** · Source: our `docs/05`; web.dev animation performance guidance
- **Problem:** motion is added for taste and paid for in INP.
- **Implementation:** start at rung 0/1 (CSS only); rung 2 for scroll reveals within 1 KB; rung 3 (component motion) only for stateful UI inside an island; rungs 4–5 need written justification and a static fallback.
- **A11y:** pairs with A11Y-004.
- **Perf:** animate `transform`/`opacity` only; never layout properties.
- **Anti-pattern:** scroll-jacking; parallax on mobile; animated counters. *Sequencing rule:* a fast, readable first paint beats any entrance animation — prioritise instant readable text and <100 ms interaction feedback over decorative reveals.
- **Test:** INP after scroll + interaction on a throttled profile; verify no layout-property animation in devtools.
- **Gate:** blocks if INP >200 ms or if motion exceeds the budget without justification.
- **Tier:** all (rung ceiling varies by tier). **Status:** Approved default.

#### MOT-003 — Motion must not be the only carrier of meaning
- **Level 1** · Source: WCAG 1.3.3 (sensory characteristics), 2.2.2, 4.1.3
- **Problem:** "the price slides in" or "the error shakes" is invisible to some users and to reduced-motion users.
- **Implementation:** state appears in text and semantics (live region for changes); motion is decoration on top of an already-correct static state.
- **A11y:** core requirement.
- **Perf:** none.
- **Anti-pattern:** animation-only validation feedback; hover-only affordances.
- **Test:** reduced-motion + screen-reader combination: is every state still perceivable?
- **Gate:** **cannot-launch.**
- **Tier:** all. **Status:** Approved default.

#### MOT-004 — Scroll-linked effects show progress, they never reveal content
- **Level 1/3** · Source: WCAG 2.2.2 / 2.4.11 / 1.3.3 + our `docs/05`
- **Problem:** scroll-triggered reveals hide content from keyboard users, reduced-motion users and anyone whose JS fails.
- **Required implementation:** content is in the DOM and readable without any scroll event; scroll motion is decorative (progress bar, sticky section label); no `opacity:0` default state waiting for an observer; no scroll-jacking; no "scroll to continue".
- **A11y impact:** protects keyboard and screen-reader users, and prevents the classic "invisible content" defect with `IntersectionObserver` reveals.
- **Perf impact:** a scroll listener that writes layout properties destroys INP — animate only `transform`/`opacity`, or use CSS scroll-driven animations with a static fallback.
- **Anti-pattern:** sections that are blank until scrolled into view; horizontal scroll hijacks; progress bars that also gate the CTA.
- **Test:** disable JavaScript → all content readable in order; keyboard tab through the whole page without scrolling mouse; reduced-motion run; INP after a full scroll.
- **Gate:** **cannot-launch** if any content depends on a scroll event to become visible.
- **Tier:** all. **Status:** Approved default.

### 3.10 SEO, metadata and structured data

#### SEO-001 — Metadata is content, not decoration
- **Level 2** · Source: search-engine documentation (titles/descriptions are inputs, not guarantees) + our `docs/02`
- **Problem:** templated titles and duplicate descriptions devalue every page.
- **Implementation:** unique `<title>` (≤60 chars, offer-led) and meta description (≤155 chars, benefit + next step) per page; one `<h1>`; canonical URL; OG/Twitter image (1200×630) with alt; sitemap + robots correct; no template filler.
- **A11y:** page title is the first thing a screen reader announces.
- **Perf:** OG images must be compressed and not block render.
- **Anti-pattern:** "Home | Company | We do great things" titles; the same description sitewide.
- **Test:** crawl the sitemap and diff titles/descriptions for uniqueness; test OG preview in two clients.
- **Gate:** blocks on duplicate or missing titles on indexable pages.
- **Tier:** all. **Status:** Approved default.

#### SEO-002 — Structured data only where it is true and eligible
- **Level 1** · Source: Google Search structured-data policies
- **Problem:** decorative schema creates eligibility problems and, for reviews, is not shown at all.
- **Implementation:** `Organization`/`LocalBusiness` (real data: legal name, address, contact), `Service` where it matches a real service, `BreadcrumbList` where navigation exists, `FAQPage` only for genuinely visible Q&A. **Never** `AggregateRating`/`Review` for our own business on our own site (self-serving review rule), and never reviews that are incentivised without disclosure.
- **A11y:** schema is not an accessibility feature; do not use it instead of real markup.
- **Perf:** inline JSON-LD only, no blocking scripts.
- **Anti-pattern:** star markup on the homepage; `Product` schema on a service.
- **Test:** Rich Results Test + manual cross-check that every marked-up fact is visible on the page.
- **Gate:** blocks on self-serving review markup.
- **Tier:** all. **Status:** Approved default.

#### SEO-003 — Legal and trust pages are indexable and linked
- **Level 1** · Source: French LCEN (mentions légales) + GDPR (privacy notice) + accessibility statement practice
- **Problem:** unlinked legal pages are both a legal and a credibility problem.
- **Implementation:** mentions légales (publisher identity, publication director, host name/address/phone, contact), privacy notice, accessibility statement — each linked in the footer of every page, reachable in one click, indexable.
- **A11y:** these pages are frequently the most poorly structured pages on a site; they get the same treatment as the rest.
- **Perf:** see weight budgets; `noindex` is *not* used to dodge work.
- **Anti-pattern:** privacy policy only inside a cookie modal; "last updated" with no date.
- **Test:** click-through from every template; check content against the client's real entity data and actual data flows.
- **Gate:** **cannot-launch** (see `docs/09`). ⚖️ counsel review for wording.
- **Tier:** all. **Status:** Approved default.

#### SEO-004 — One canonical page per offer, no orphan pages, honest dates
- **Level 2/3** · Source: search-engine documentation on canonicalisation and duplication (L2) + content architecture practice
- **Problem:** the same offer described on four URLs splits signals and confuses the visitor about which page is the offer.
- **Required implementation:** one indexable page per service with a canonical URL; internal links from the homepage, pricing and at least one proof page into it; every page reachable in ≤3 clicks from home; "last updated" dates that are real (and only shown when the content actually changed); no near-duplicate city/market variants.
- **A11y impact:** clear, single-topic pages help cognitive load; breadcrumbs give orientation when implemented with semantics.
- **Perf impact:** fewer near-duplicate pages = fewer assets to keep within budget.
- **Anti-pattern:** eight "landing pages" for the same service targeting keyword variants; orphaned blog posts; dates updated automatically to look fresh.
- **Test:** crawl the sitemap — every page has one canonical, is internally linked, and any date matches real edits (git log).
- **Gate:** blocks if an indexable page is orphaned or duplicates another's intent.
- **Tier:** Authority/Launch. **Status:** Approved default.

### 3.11 AI assets, provenance and transparency

#### AI-001 — No client material in generative tools, ever
- **Level 1/2** · Source: vendor terms analysis (Higgsfield: commercial use permitted, but non-Enterprise inputs are used for training by default; IP indemnity Enterprise-only) + our `docs/08`
- **Problem:** uploading client assets can put confidential material into a training pipeline with no indemnity.
- **Implementation:** generative tools are used with *our own* or category-level prompts only; private workspace; no client names in prompts; an approval record before any AI asset reaches production.
- **A11y:** AI-generated imagery still needs meaningful alt text and contrast checks.
- **Perf:** generated imagery is heavier — it goes through the same compression budget as photography.
- **Anti-pattern:** "just try it with the client's screenshots".
- **Test:** provenance log entry + approval record for every AI asset; a spot-check that no client asset appears in the prompt history.
- **Gate:** **cannot-launch** for any unapproved AI asset.
- **Tier:** all. **Status:** Approved default.

#### AI-002 — Realistic synthetic people are default-off; disclosure otherwise
- **Level 1** · Source: EU AI Act Article 50 (applicable since 2026-08-02; deployer duty to disclose deepfake-like content; attenuated treatment for evidently artistic/fictional work; human editorial responsibility) + our internal influencer-content rule
- **Problem:** undisclosed synthetic humans as staff/customers is both deceptive and now a regulatory exposure.
- **Implementation:** never present AI people as real employees/customers; if a realistic synthetic person is used, a visible human-readable disclosure appears at first exposure (not only in metadata); never use a real person's likeness without written authorisation.
- **A11y:** the disclosure must itself be accessible (text, contrast, not only an icon).
- **Perf:** none.
- **Anti-pattern:** AI "team photos" on an About page; an AI-generated customer quote illustration.
- **Test:** asset inventory review; verify the label renders at first exposure on mobile.
- **Gate:** **cannot-launch** on any undisclosed realistic synthetic person. ⚖️
- **Tier:** all. **Status:** Approved default.

#### AI-003 — AI-assisted copy is still authored, and every sentence has a human owner
- **Level 1/2 (disclosure) + process rule** · Source: EU AI Act Art. 50 (transparency for AI-generated content; attenuated for evidently artistic work, human editorial responsibility remains) + GDPR (no client data in tools) + our `docs/08`
- **Problem:** AI drafts are cheap; unsourced claims, invented proof and generic filler are the expensive part.
- **Required implementation:** AI output is a draft only; a named human verifies every factual claim against the source, removes anything unverifiable, and owns the final text; no client documents, transcripts or confidential data in the tool; any AI-generated **image** follows AI-002's disclosure rule; the message map (`docs/02`) is written before prompting, not extracted afterwards.
- **A11y impact:** AI drafts frequently produce vague link text and decorative headings — the TYPE-002 and CTA-001 checks still apply.
- **Perf impact:** none directly; generic copy tends to add sections, which adds bytes.
- **Anti-pattern:** shipping generated claims ("industry-leading"), generated testimonials, generated case-study numbers, or a generated privacy notice.
- **Test:** every claim in the final copy traces to a substantiation file; prompt log shows no client material.
- **Gate:** **cannot-launch** if any factual claim cannot be traced or any client data entered a prompt.
- **Tier:** all (the rule is about the process, not the tier). **Status:** Approved default. ⚖️ for disclosure wording in client contracts.

### 3.12 Handover, ownership and launch QA

#### OPS-001 — The client can log in to everything before the invoice
- **Level 1/3** · Source: GDPR controller/processor boundaries + our ownership gate
- **Problem:** client data and infrastructure held in a studio account is a contractual and trust failure.
- **Implementation:** repo, hosting, domain, analytics, CMS, booking and form records live in client-owned accounts; we hold delegated access; credentials exchanged via the client's password manager.
- **A11y:** documentation is written to be readable (plain language, headings, short steps).
- **Perf:** none.
- **Anti-pattern:** "we'll transfer it after the final payment".
- **Test:** client logs in themselves, on a call, before the final invoice.
- **Gate:** **cannot-launch / cannot-invoice.**
- **Tier:** all. **Status:** Approved default.

#### OPS-002 — Every launch carries a receipt
- **Level 2/3** · Source: our QA receipts (`templates/qa-launch-checklist.md`) + `docs/09`
- **Problem:** "we tested it" is unverifiable and cannot be handed over.
- **Implementation:** one receipt per release: axe output, keyboard sweep result, contrast values, Lighthouse numbers, weights, form test IDs, rollback timing, ownership status, waivers with fix dates.
- **A11y:** the receipt includes the manual layer, not only automated output.
- **Perf:** numbers are the receipt.
- **Anti-pattern:** screenshots of a green Lighthouse score with no date, URL or tool version.
- **Test:** a second person can reproduce every number from the receipt alone.
- **Gate:** blocks the launch.
- **Tier:** all. **Status:** Approved default.

---

## 4. Anti-pattern cards (40, with severity and replacement)

Severity: **S1** = never ship · **S2** = fix before launch · **S3** = fix when touched.

| # | Anti-pattern | Sev | Why it fails (evidence level) | Replace with |
|---|---|---|---|---|
| 1 | Placeholder-only form labels | S1 | WCAG 1.3.1/3.3.2 (L1) | FORM-001 persistent labels |
| 2 | `outline: none` with no replacement | S1 | WCAG 2.4.7/2.4.11 (L1) | A11Y-001 focus ring |
| 3 | Sticky header hiding the focused element | S1 | WCAG 2.4.11 (L1) | `scroll-padding-top` + tested offset |
| 4 | Icon-only buttons under 24 px | S1 | WCAG 2.5.8 (L1) | A11Y-002 |
| 5 | Drag-only comparison/carousel | S1 | WCAG 2.5.7 (L1) | Button-based alternative |
| 6 | Text contrast below 4.5:1 | S1 | WCAG 1.4.3 (L1) | Token contrast check |
| 7 | Error signalled by colour only | S1 | WCAG 1.4.1 (L1) | ICON + TEXT + ARIA |
| 8 | Third-party font CDN | S1 | Court ruling (L1) + privacy | PERF-004 self-host |
| 9 | Google Maps/Places data warehoused as a list | S1 | ToS §3.2.3 (L1) | Registry data + manual research (`docs/30`) |
| 10 | Fake or incentivised-undisclosed testimonials | S1 | EU Omnibus (L1) | PROOF-001 evidence types |
| 11 | AI people presented as staff/customers | S1 | AI Act Art. 50 (L1) | AI-002 disclosure or removal |
| 12 | `AggregateRating` for your own business on your own site | S1 | Google policy (L1) | SEO-002 compliant markup |
| 13 | "GDPR compliant" / "fully accessible" claims | S1 | Unsubstantiable claim | Evidence-based wording (`docs/06`) |
| 14 | Client assets uploaded to a generative tool | S1 | Vendor terms + confidentiality | AI-001 rules |
| 15 | Legal pages unreachable from the footer | S1 | LCEN/GDPR (L1) | SEO-003 |
| 16 | Silent form failure / no monitoring | S1 | WCAG 3.3.1 + business risk | FORM-004 |
| 17 | Hero carousel | S2 | HERO-001 test | One static hero |
| 18 | Autoplaying hero video with baked-in text | S2 | PERF + a11y | HERO-003 + real text |
| 19 | LCP image lazy-loaded | S2 | web.dev (L2) | `fetchpriority="high"` |
| 20 | Images without dimensions | S2 | CLS guidance (L2) | PERF-002 |
| 21 | Scroll-jacking, section snapping, or parallax on mobile | S2 | INP, vestibular harm, keyboard traps | MOT-001 / MOT-004 static content |
| 22 | Infinite marquee behind text | S2 | WCAG 2.2.2 | Pausable or removed |
| 23 | Animated counters with invented statistics | S2 | Fabrication + motion | Real numbers or none |
| 24 | Multiple equal CTAs above the fold | S2 | HERO-002 | One primary action |
| 25 | Pricing pages that break at 320 px | S2 | WCAG 1.4.10 | PROOF-003 reflow |
| 26 | Hidden pricing on every tier | S3 | PROOF-003 | Price bands published |
| 27 | "Learn more" as the primary CTA label | S3 | CTA-001 | Verb + object |
| 28 | Duplicate `<title>` across pages, or near-duplicate pages for the same offer | S2 | SEO-001 / SEO-004 | Unique offer-led titles; one canonical page per offer |
| 29 | Product schema on a service page | S3 | SEO-002 policy | `Service` or nothing |
| 30 | Third-party chat/heatmap/analytics pile-on | S2 | Budgets + consent | ≤1 third-party script |
| 31 | "We'll keep an eye on it" — no alert route, no incident rule | S2 | OPS-003 | Alert route + written incident definition |
| 32 | Cookie banner that blocks the primary CTA | S2 | Focus + conversion | Non-blocking, dismissible consent |
| 33 | Analytics requiring consent when aggregate-only would do | S3 | CNIL exemption (L1) | Plausible/Umami configured per `docs/08` |
| 34 | Long text lines (>75 chars) | S3 | TYPE-001 | `max-width` in `ch` |
| 35 | Headings used for styling, not structure | S2 | WCAG 1.3.1 | TYPE-002 |
| 36 | Two-step form asking the same data twice | S2 | WCAG 3.3.7 (L1) | A11Y-005 |
| 37 | Help link in different places per page | S2 | WCAG 3.2.6 (L1) | NAV-001 |
| 38 | Image-of-text headlines | S2 | WCAG 1.4.5 | Real text |
| 39 | Client accounts held by the studio "for convenience" | S1 | OPS-001 | Ownership transfer |
| 40 | Launch without a receipt or rollback rehearsal | S2 | OPS-002 | Cant-launch gate |

---

## 5. Must-pass launch checklist (the compressed gate)

Beyond `docs/09-LAUNCH-QA.md`, the cookbook adds these **non-negotiable** items:

```
[ ] 1  Every interactive target ≥24×24 px, with a 24 px non-overlapping circle where smaller (WCAG 2.5.8)
[ ] 2  Focus visible with 3:1 contrast and never fully obscured by author content (WCAG 2.4.11)
[ ] 3  Any drag interaction has a single-pointer alternative (WCAG 2.5.7)
[ ] 4  Help affordance in the same relative place on every template (WCAG 3.2.6)
[ ] 5  No re-entry of previously supplied information in multi-step flows (WCAG 3.3.7)
[ ] 6  Reduced-motion path verified in every design direction (WCAG 2.3.3 as internal target)
[ ] 7  Zero third-party font requests; every font licence file in the repo
[ ] 8  CLS ≤0.05, LCP ≤2.2 s, INP ≤150 ms targets met or waivered with cause + date
[ ] 9  ≤1 third-party script, documented
[ ] 10 Every form: persistent labels, error summary, retained values, tested failure path, monitoring
[ ] 11 Every claim has an evidence type and a substantiation file
[ ] 12 No self-serving review markup; all structured data visible on the page
[ ] 13 Legal pages present, accurate, footer-linked, indexable
[ ] 14 Every AI asset has a provenance row + approval record; realistic synthetic people disclosed or absent
[ ] 15 Client owns and can access repo, hosting, domain, analytics, CMS
[ ] 16 Launch receipt reproducible by a second person; rollback rehearsed <15 min
```

---

## 6. Pattern validation loop

```
candidate  →  evidence  →  local proof-of-concept  →  human review  →  pilot  →  QA receipt  →  approved / deprecated
```

| Stage | Entry criteria | Exit criteria | Artefact |
|---|---|---|---|
| **Candidate** | Something we want to use (from research, a client need, or a project post-mortem) | Named evidence level + source URL | entry in `research/poc-backlog.md` |
| **Evidence** | Level 1/2 source exists, or a level-3 hypothesis with a test | Card drafted with all fields | draft pattern card |
| **Local PoC** | The card can be built in ≤4 h | Built into `demo/` or a client preview | branch + screenshots |
| **Human review** | PoC exists | Founder signs or rejects; a11y + perf checks run | `AP-xxxx` approval record |
| **Pilot** | One real project uses it | No gate failures in that project | QA receipt referencing the pattern |
| **Receipt** | Pilot complete | Numbers recorded (perf/a11y/test results) | receipt entry |
| **Approved / Deprecated** | Receipt exists | Card marked Approved default / Conditional / Deprecated with date | this file + changelog |

**Deprecation triggers:** a WCAG or platform-policy change; a performance regression in two consecutive projects; the underlying dependency changing licence or becoming unmaintained; a client incident traced to the pattern.

### 6.1 Code-review blockers (the literal lines a PR fails on)

Every confirmed rule exists in three places: a pattern card above, one blocker line here, and a test row in `tools/qa_matrix.py`. A rule that is missing any of the three is not a rule — it is an opinion.

| Blocker line (reviewer fails the PR) | Card | Test |
|---|---|---|
| `outline` removed without a ≥2 px, ≥3:1 replacement — or focus hidden by sticky chrome | A11Y-001 | T-A11Y-101 / T-A11Y-201 |
| Any interactive target below 24×24 px, or a drag-only interaction without a button alternative | A11Y-002 | T-A11Y-202 / T-A11Y-203 |
| A text/background pair that has not been run through `tools/contrast_check.py`, or accent/signal used as body text | A11Y-003 | T-A11Y-102 |
| Motion outside `@media (prefers-reduced-motion: no-preference)` — transitions, animations or smooth scrolling | A11Y-004 / MOT-001 | T-A11Y-103 |
| Labels missing/null `for` ids, error text not linked, or a failure path that silently drops input | FORM-001 / FORM-004 | T-A11Y-104 / T-FORM-101 / T-FORM-102 |
| New client JS pushing the page over the budget (JS ≤60 KB, third-party ≤1) without a written justification | PERF-001 / PERF-003 | T-PERF-103 |
| An image, video or iframe without dimensions, or content injected above existing content after load | PERF-002 | T-PERF-102 |
| A font request to a third-party origin, or a font file without its licence in the repo | PERF-004 | T-PERF-104 |
| A public claim without a substantiation file, or any invented metric/proof element | PROOF-001 | T-PROOF-101 |
| AI-generated asset without a provenance row + approval record, or a realistic synthetic person without disclosure | AI-001 / AI-002 | T-AI-101 |
| Legal/trust pages missing, inaccurate, unlinked or `noindex`-ed | SEO-003 | T-LEGAL-101 |
| Self-serving review markup, or structured data marking up anything not visible on the page | SEO-002 | T-LEGAL-102 |
| Client accounts (repo, hosting, domain, analytics, CMS) held by the studio | OPS-001 | T-OPS-101 |

---

## 7. Tier standards (what the price actually buys)

| Quality area | €500–750 Starter | €1,250–1,750 Authority Sprint | €2,500–3,000 Launch System |
|---|---|---|---|
| **Message** | Hero + CTA + core sections | Full message map + objection handling | Positioning memo + a documented test hypothesis |
| **Design** | One direction, tokens applied | Custom direction + asset system + token audit | Direction alternatives explored + motion system |
| **Build** | Responsive one-pager | Component + token system, islands where needed | Multi-page or multi-flow, variants, CMS-ready content model |
| **Forms** | Contact/quote form with accessible validation | Routing, confirmation page, tested failure path | CRM/calendar integration + event tracking on every action |
| **Accessibility** | Automated axe pass + contrast check | WCAG 2.2 AA-oriented **manual** QA (keyboard, zoom, focus) | Plus a documented QA receipt and a remediation list for known limits |
| **Performance** | Optimised media, budget-aware build | Explicit budget + Lighthouse/field baseline | Performance plan + monitoring + a 30-day check |
| **Proof** | Real, substantiable proof assets only | Proof architecture (evidence types mapped to sections) + rights log | Public case-study/proof system + permission workflow |
| **Legal/rights** | Legal pages correct, asset provenance logged | Above + licence register per dependency | Above + accessibility statement + AI disclosure decisions documented |
| **Handover** | Access + export | Documentation + ownership matrix | Launch packet + 14-day support window |
| **Receipt** | One-page QA receipt | Full QA receipt | Full receipt + post-launch monitoring plan |

**What we never sell as a tier difference:** compliance guarantees, conversion guarantees, "we'll fix everything later", or unlimited revisions.

**Wording rule (all tiers):** "built to WCAG 2.2 AA and tested with the documented method on <date>" — never "compliant", never "certified". WCAG 2.2 is an ISO/IEC standard (ISO/IEC 40500:2025) and conformance depends on the complete implementation and testing of the specific project, which is why we ship the receipt instead of a badge. ⚖️

---

## 8. Research gaps needing human / legal / specialist review

1. **Level-3 statistics** (Baymard/NN-g specific percentages) are deliberately not quoted; if we want to cite them in client-facing material, verify the primary source first. `[VERIFY]`
2. **EN 301 549 update** referencing WCAG 2.2 is expected; until it lands, the EAA's harmonised standard still points at WCAG 2.1 AA — clarify per client sector. ⚖️
3. **Accessibility statement wording** and the precise claims we may make in a client contract. ⚖️
4. **AI disclosure wording** for client sites using realistic synthetic imagery (Art. 50 deployer duty + draft labelling code practice). ⚖️
5. **Consent-banner necessity** per client configuration (CNIL aggregate exemption vs necessary consent). ⚖️
6. **Structured-data eligibility for service pages** — Google's support for `Service` review snippets is less direct than for `Product`; do not promise stars. `[VERIFY]`
7. **Sector-specific rules** (health, finance, education) where claims and data flows need specialist input before we accept the project. ⚖️

#### OPS-003 — The page is watched after launch, by the client, with rules agreed in advance
- **Level 2/3** · Source: our `docs/07` (day 7/30/90 ritual) + `docs/10` (Care plans) + monitoring practice
- **Problem:** "handover" without monitoring means defects are discovered by the client's customers.
- **Required implementation:** agreed thresholds (form submissions stop, error rate, LCP/CLS regression, certificate/domain lapse), an alert route that reaches a human, a written incident definition ("what counts, who acts, by when"), and a 30-day report that states numbers, not adjectives. Care plans cover it contractually; without a care plan, the alert route is the client's and is documented as such.
- **A11y impact:** monitoring catches regressions that silently break assistive-tech use (e.g. a plugin re-introducing focus traps).
- **Perf impact:** the day-7 and day-30 field checks are the only way our lab budgets become real numbers.
- **Anti-pattern:** "we'll keep an eye on it"; dashboards nobody reads; alerts sent to an unmonitored inbox.
- **Test:** simulate a form failure and a 5xx; verify the alert reaches a human within the agreed time. Re-run the QA matrix subset on the live site at day 7.
- **Gate:** blocks the *handover* (not the launch) if no alert route and incident rule exist.
- **Tier:** Authority/Launch (Starter: documented client-side alert route). **Status:** Approved default.
