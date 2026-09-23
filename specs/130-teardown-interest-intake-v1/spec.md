# Feature 130 — teardown interest intake V1

Status: `proposed / privacy-gated`

Define a minimal, interest-only teardown request route that can be shown in the
vertical slice without payment, booking, hidden tracking, or an unreviewed
external data processor.

## Requirements

- FR-130-01: Request copy does not promise delivery or response time.
- FR-130-02: Fields are minimal and mapped before a provider is selected.
- FR-130-03: No submission leaves the browser until privacy, retention,
  routing, business, and human gates are approved.
- FR-130-04: Labels, validation, error, success, and no-send states are
  accessible.
- FR-130-05: Privacy and legal links exist as reviewed routes/placeholders.
- FR-130-06: No payment, calendar, CRM, analytics, or session replay is V1.
- FR-130-07: Provider and retention decisions are recorded separately.

The default is a local/non-sending demo or disabled request, not a fake
successful delivery.
