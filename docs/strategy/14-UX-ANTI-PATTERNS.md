# 14 — UX anti-pattern cards

Each item is a review rule, not a claim that every instance has identical legal
effect. The launch rule is deliberately conservative where harm is foreseeable.

## HERO-AP-001 — Meaningless hero

- **Temptation:** Large type and visual drama feel premium.
- **Failure:** A visitor cannot identify the offer, audience, outcome, or action.
- **Detection:** Five-second comprehension test.
- **Replacement:** HERO-001.
- **Severity / launch:** Blocker / block launch.

## TRUST-AP-001 — Fake proof

- **Temptation:** Logos, invented reviews, or synthetic dashboards make an empty
  portfolio look established.
- **Failure:** It misrepresents evidence and damages trust.
- **Detection:** Every proof item must map to a source and permission record.
- **Replacement:** TRUST-001 and method receipts.
- **Severity / launch:** Blocker / block launch.

## RIGHTS-AP-001 — Unclear licence

- **Temptation:** A polished block, font, image, or icon is faster than a clean
  source.
- **Failure:** The asset cannot be defended or handed over safely.
- **Detection:** Missing licence row, version, source, or restriction.
- **Replacement:** Component allowlist and asset-provenance record.
- **Severity / launch:** Blocker / block launch.

## CTA-AP-001 — Equal-priority CTA pile-up

- **Temptation:** Every stakeholder wants their action visible.
- **Failure:** The visitor must resolve internal politics before acting.
- **Detection:** More than one visually dominant action or unclear primary event.
- **Replacement:** CTA-001.
- **Severity / launch:** Blocker / block launch.

## FORM-AP-001 — Silent or unrecoverable form

- **Temptation:** A minimal form looks clean when its states are omitted.
- **Failure:** Users cannot correct errors or know whether the lead arrived.
- **Detection:** Test invalid, spam, valid, and delivery-failure paths.
- **Replacement:** FORM-001.
- **Severity / launch:** Blocker / block launch.

## A11Y-AP-001 — Invisible, trapped, or obscured focus

- **Temptation:** Removing outlines or adding sticky chrome improves a mockup.
- **Failure:** Keyboard users lose orientation or access.
- **Detection:** Tab sweep at mobile widths, including sticky header and dialogs.
- **Replacement:** A11Y-001.
- **Severity / launch:** Blocker / block launch.

## A11Y-AP-002 — Hover/drag/colour-only meaning

- **Temptation:** It reduces visible UI and looks clever.
- **Failure:** Important content disappears for keyboard, touch, zoom, or
  assistive-technology users.
- **Detection:** Keyboard, touch, 200% zoom, and no-colour review.
- **Replacement:** Explicit controls and persistent text alternatives.
- **Severity / launch:** Blocker / block launch.

## PERF-AP-001 — LCP/media budget breach

- **Temptation:** A large video or unoptimised image creates instant drama.
- **Failure:** The page delays usefulness and shifts while loading.
- **Detection:** QA receipt with LCP, CLS, media size, and dimensions.
- **Replacement:** PERF-001.
- **Severity / launch:** Blocker / block launch.

## MOTION-AP-001 — Motion without an authored reduced path

- **Temptation:** Effects are added late as a premium polish pass.
- **Failure:** Reading, orientation, or comfort depends on motion.
- **Detection:** OS reduced-motion setting plus keyboard and mobile test.
- **Replacement:** CSS-first static state and motion budget.
- **Severity / launch:** Blocker / block launch.

## AI-AP-001 — Synthetic people as proof

- **Temptation:** A generated team or customer portrait fills a credibility gap.
- **Failure:** It implies a real identity, relationship, or testimonial.
- **Detection:** Asset provenance and disclosure review.
- **Replacement:** Abstract concept imagery or permissioned real assets.
- **Severity / launch:** Blocker / block launch.

## Additional review-only anti-patterns

Scroll-jacking, autoplay audio, endless marquees, hidden pricing for a fixed
offer, fake urgency, pre-checked consent, duplicate trackers, copied competitor
expression, unbounded client-side JavaScript, and unsupported compliance claims
are recorded as high-risk candidates. They require a card and human decision
before any exception is considered.
