# 13 — Conversion pattern cards

These are V1 pilot cards. They define safe starting structures, not guaranteed
conversion outcomes.

## HERO-001 — Outcome + audience + CTA in the first screen

- **Job:** Make what is offered, for whom, the primary outcome, and the next
  action understandable before the visitor scrolls.
- **Use when:** The offer and audience are specific enough to name.
- **Do not use when:** The offer, buyer, or CTA destination is unresolved.
- **Implementation:** Eyebrow/category cue → meaningful outcome headline →
  mechanism/scope line → one primary CTA → one honest risk reducer.
- **Mobile:** Keep the headline and CTA above the first meaningful scroll; crop
  media rather than shrinking text into illegibility.
- **Accessibility/performance:** Real HTML text, accessible CTA name, reserved
  media dimensions, and no lazy-loaded LCP visual.
- **Test:** Five-second test with three target-like reviewers. Ask what is
  offered, for whom, and what happens next.
- **Success/failure:** 2 of 3 answer all three; otherwise rewrite hierarchy
  before styling.

## CTA-001 — One primary action per page

- **Job:** Give the page a clear decision path.
- **Use when:** One conversion event is genuinely primary.
- **Do not use when:** The page is an authenticated product workspace with
  multiple equal workflows.
- **Implementation:** One visually dominant action; secondary action is visibly
  secondary and has a different role.
- **Test:** Hide the labels and ask a reviewer to point to the next action.
- **Success/failure:** Correct action identified without explanation; otherwise
  remove, rename, or re-rank CTAs.

## COPY-001 — Problem → mechanism → benefit → proof → CTA

- **Job:** Make a complex service or product legible without feature dumping.
- **Use when:** The mechanism is real and can be explained in one sentence.
- **Do not use when:** Proof or mechanism is still an assumption.
- **Implementation:** Each section carries claim → evidence type → mechanism →
  next step. Keep one idea per section.
- **Test:** Ask a reviewer to restate the mechanism and intended outcome.

## TRUST-001 — Verifiable proof or labelled proof-pending state

- **Job:** Reduce uncertainty without inventing credibility.
- **Use when:** Proof is permissioned, supplied, or demonstrable in the method.
- **Do not use when:** A logo, quote, metric, or likeness lacks provenance.
- **Implementation:** Show method receipts, supplied evidence, permissioned
  quotes, or an explicit concept/proof-pending label.
- **Test:** Trace every proof item to an asset or approval record.

## FORM-001 — Persistent labels, errors, and success state

- **Job:** Make a lead form understandable and recoverable.
- **Use when:** The form is part of the primary conversion path.
- **Do not use when:** An external flow cannot expose labels, errors, consent,
  or completion state; choose a reviewed alternative.
- **Implementation:** Explicit labels, concise instructions, field-level errors,
  summary where useful, and a clear success confirmation.
- **Test:** Empty, invalid, spam, valid, duplicate, and delivery-failure paths.

## TYPE-001 — Readable type with stable fallbacks

- **Job:** Preserve scanning and layout stability.
- **Use when:** Typography expresses the direction without reducing legibility.
- **Do not use when:** A display face causes overflow, slow loading, or poor
  fallback metrics.
- **Implementation:** Semantic headings, readable measure, self-hosted licensed
  fonts, explicit fallback stack, and reserved font-sensitive layout.
- **Test:** 200% zoom, long words, slow font load, and 320–390 px reflow.

## A11Y-001 — Keyboard, focus, target, and reduced-motion baseline

- **Job:** Keep the interaction model usable without pointer or animation.
- **Use when:** Always.
- **Do not use when:** Never omit it. The visual expression can change; the
  baseline cannot.
- **Implementation:** Skip link, landmarks, semantic controls, visible focus,
  no traps, accessible names, target-size review, and reduced-motion default.
- **Test:** Full keyboard sweep plus reduced-motion and mobile review.

## PERF-001 — LCP-first media and reserved dimensions

- **Job:** Protect perceived speed and visual stability.
- **Use when:** The page has any hero image, video, font, embed, or third-party
  script.
- **Do not use when:** Never treat a Lighthouse score as a substitute for field
  evidence.
- **Implementation:** Prioritise the LCP asset, do not lazy-load it, reserve
  dimensions, defer non-essential work, and record lab versus field data.
- **Test:** Throttled mobile run with LCP/INP/CLS recorded in a QA receipt.

## QA-001 — Preview → E2E test → mobile/keyboard QA → receipt

- **Job:** Turn “finished” into inspectable evidence.
- **Use when:** Every build.
- **Implementation:** Run the available checks, record limitations, attach the
  receipt, and keep human launch approval separate.
- **Test:** Receipt is complete, traceable to a release, and still non-authoritative.

## OWN-001 — Client-owned accounts and exportable handover

- **Job:** Prevent lock-in and make the result maintainable.
- **Use when:** Any external repo, host, domain, analytics, CRM, form, or CMS is
  involved.
- **Implementation:** Client owns accounts; studio receives delegated access;
  exports, restore instructions, and access verification are recorded.
- **Test:** Client logs in and rollback/restore is rehearsed.
