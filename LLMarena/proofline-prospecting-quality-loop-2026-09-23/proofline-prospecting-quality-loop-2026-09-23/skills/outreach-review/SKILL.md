---
name: outreach-review
description: Review a draft outbound message for a specific prospect against the Proofline Send Gate (docs/30 §E). Checks evidence, compliance and quality before any send; refuses to approve incomplete or unsupported messages.
---

# Skill: Outreach Review

## When to use
Before **any** outbound message leaves the drafts folder, and again after an opt-out, complaint or bounce.

## Inputs required (refuse to proceed without them)
1. The prospect record (`schemas/prospect-record.schema.json`) — valid JSON, all required fields.
2. The exact final email text, including the footer.
3. The suppression-list query result and its timestamp (same day).
4. The approval context: account, sending domain, reply inbox, and who is approving.
5. The evidence for the trigger: source URL and observation date.

## Procedure
1. **Mechanical schema check** — validate the record; flag any missing `compliance`, `public_signal` or `website_observations` entries.
2. **Trigger freshness** — `observed_at` within 90 days and the URL actually supports the claim in the message. No URL → fail.
3. **Observation integrity** — at least one observation, `verified_by_human: true`, reproduced at the stated device width, quoted accurately in the email (no rephrasing into speculation).
4. **Role fit** — does the message speak to the recipient's *professional function*? If it could be sent unchanged to a marketing manager, a founder and an accountant, fail.
5. **Data minimisation** — no private or unnecessary personal data; nothing beyond the eight-field V1 set; no inferred budget/revenue/health/political content.
6. **Footer completeness** — sender identity, legal business identity, source-of-contact statement, privacy URL, and a **working** opt-out link (test it) plus a reply-based opt-out sentence.
7. **Suppression** — person, domain and company checked; any hit → hard refuse, no exceptions.
8. **Sequence state** — touch number ≤3, within the 21–30 day window, and a touch log entry exists for each earlier touch.
9. **Tone and claim audit** — no fake familiarity, no insult, no "just following up", no invented numbers, no guarantee words (`rechtssicher`, `WCAG-konform garantiert`, `Conversion garantiert`), no claims about the recipient's internal situation.
10. **Verdict** — issue one of: `APPROVED` (with the Send Gate checklist completed and an `AP-xxxx` id) · `NEEDS_EDIT` (list the exact failing items) · `REFUSE` (hard stop with a reason).

## Output
- Verdict + item-by-item Send Gate table (all nine).
- The exact edited lines when `NEEDS_EDIT`.
- The approval id to store in the prospect record.
- A one-line log entry for the weekly review.

## Refusal conditions (hard stop, no negotiation)
- Suppression hit for the person, domain or company.
- Non-public data source, purchased list, scraped contacts, or guessed email address.
- Missing source URL for the trigger, or an observation not verified by a human.
- A prior opt-out, a complaint, or silence that followed a request to stop.
- Sensitive-context signals (insolvency proceedings, illness, political or health information).
- Any message claiming a guaranteed result, legal compliance, or a fabricated metric.
- Send volume for the day already at the ≤5 limit, or the sending domain failing SPF/DKIM/DMARC.

## Never
- Never approve "just this once" without the evidence.
- Never remove or overwrite a suppression entry.
- Never let the review be done by the same model output that wrote the email without a fresh check against the source URLs.
- Never export the suppression list into any campaign tool as a target list.
