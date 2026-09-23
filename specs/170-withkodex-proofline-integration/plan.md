# Plan — WITHKODEX × Proofline integration

## Design choice

Treat this as a parent-site route and content-governance change first. Keep the
existing Proofline repository as the source of truth for Proofline method,
archetypes, QA, legal gates, and portfolio honesty. Do not create a second
runtime or copy the external WITHKODEX site into this repository.

## Minimal implementation sequence

1. Confirm parent-site ownership, current capabilities, route conventions, and
   legal operator with a human.
2. Approve the route map and message boundary in `spec.md`.
3. Produce `/proofline` content from the existing Proofline message map,
   archetype catalog, offer catalog, and quality standards.
4. Add cross-links from the parent capabilities only after each link target and
   CTA has an owner.
5. Keep teardown interaction interest-only until privacy/data-routing and
   `G-BIZ-001` are cleared.
6. Run the acceptance and QA receipt; record unresolved facts rather than
   filling them with generated copy.

## Files and ownership

| Artifact | Repository role | Owner |
|---|---|---|
| `spec.md` | route and boundary contract | founder |
| `acceptance.md` | human-readable acceptance matrix | founder + reviewer |
| `traceability.json` | requirement-to-evidence map | studio system |
| `qa-receipt.md` | implementation evidence and blockers | builder + QA reviewer |
| `legal/` | jurisdiction and paid-work gates | founder + qualified reviewer |
| external WITHKODEX site | deployment surface | WITHKODEX owner |

## Explicit non-goals

- no automatic external-site scraping or mirroring;
- no automatic publication;
- no new CRM, analytics, calendar, payment, or hosting adapter;
- no brand split decision based on aesthetic preference;
- no claim that the current external pages were verified by this repository.
