# 30 — Prospecting data sources, signals and send gates

<!-- v0.1 · 2026-09-23 · owner: founder · status: pilot-only -->

This is an internal operating policy, not legal advice. It extends the
human-gated outbound loop in [23–29](23-OUTBOUND-INTELLIGENCE-SYSTEM.md). The
source snapshot that led to this document is preserved in `LLMarena/NewLLM/`;
unverified licence or legal conclusions remain review items.

## Operating rule

The studio may research a small number of companies from permitted public
sources. It may record dated evidence, score fit, prepare a teardown, and draft
a message. It may not guess personal addresses, scrape restricted platforms,
send automatically, or turn an advisory model into a sender.

The V1 sequence is:

`permitted source → dated evidence → prospect record → human review → teardown → exact-message approval → human send`

The canonical contracts remain:

- `schemas/prospect-record.schema.json`
- `schemas/signal-record.schema.json`
- `schemas/suppression-record.schema.json`
- `schemas/send-approval.schema.json`
- `studio/outbound.py`
- `config/studio/outbound-policy.v1.json`
- `config/studio/prospecting-source-policy.v1.json`

## Source boundary

| Source | V1 purpose | Treatment |
|---|---|---|
| Inbound or referral | Respond to an explicit business context | Adopt; record provenance and scope |
| Official company website, blog, pricing or changelog | Human-verified offer and conversion observation | Adopt; date every observation |
| Official jobs or press page | Current, public business signal | Adopt manually; never treat a job as budget proof |
| Official register or API | Entity and firmographic verification | Adopt only within the reviewed terms and retention window |
| Pappers, launch directories, other commercial providers | Conditional enrichment or verification | Human contract/licence review before storage or reuse |
| Google Maps/Places scraping or warehousing | — | Rejected by default; use the official policy as the source of truth |
| LinkedIn scraping, purchased lists, guessed addresses, private channels | — | Rejected |
| Sensitive traits or personal-life inference | — | Rejected |

The source policy is intentionally narrower than what is technically possible.
Each source record needs a URL, collection date, terms-review status, purpose,
and human reviewer. A source being public does not by itself establish a right
to bulk collect, retain, profile, or contact a person.

## Minimal record and retention

Store the organisation, company URL, country, industry, one dated signal, up to
three evidence-backed conversion leaks, and a professional contact route. Do
not store private phone numbers, home addresses, private social profiles,
health, politics, family, finance, date-of-birth, or inferred personal traits.

Default internal retention boundaries are:

- firmographic verification: 12 months;
- current trigger: 90 days;
- post-sequence suppression: 90 days unless a new human-reviewed trigger exists;
- inactive prospect data: review for deletion after 3 years;
- objection, complaint, or data-subject-request suppression: minimal record,
  permanent until a qualified review changes the legal need.

The suppression file is a separate system of record. It is never a campaign
target list and never exported as one. A suppression hit for person, domain, or
company is a hard stop.

## Nine-condition send gate

Do not send unless all nine conditions are true for the exact message:

```text
[ ] 1. Public professional context and source URL are recorded.
[ ] 2. The message relates directly to the recipient's professional role.
[ ] 3. One current, source-linked trigger was observed within 90 days.
[ ] 4. At least one factual website observation was verified by a human.
[ ] 5. Person, domain, and company suppression checks are clear today.
[ ] 6. Sender identity, legal identity, source line, and privacy URL are present.
[ ] 7. A simple, free opt-out is present and tested.
[ ] 8. The exact final message and recipient have human approval.
[ ] 9. Sending-domain authentication and the reply inbox were tested today.
```

The working checklist is [templates/send-gate-checklist.md](../../templates/send-gate-checklist.md).
The review procedure is [skills/outreach-review/SKILL.md](../../skills/outreach-review/SKILL.md).

## Sequence and learning limits

- Maximum three touches in a 21–30 day window.
- Stop immediately on an objection, complaint, or request not to be contacted.
- Never remove or overwrite a suppression record as a convenience.
- Maximum five personalised messages per day during the pilot.
- A teardown is 5–12 minutes, three observations, one possible hero rewrite,
  and one next step. It is not a free redesign, legal audit, or promise.
- Repeated findings become cookbook candidates only after human review and
  enough local evidence; an outreach result is not universal proof.

## Governance gates

| Gate | Evidence | Human decision |
|---|---|---|
| G1 Source admissibility | Source policy row, URL, terms status | May this source be used for this purpose? |
| G2 Record completeness | Prospect, signal, observation and score | Is the record factual and minimised? |
| G3 Legal basis review | Applicable review and information path | Is contact appropriate to this context? |
| G4 Suppression check | Same-day query record | Is there any person/domain/company hit? |
| G5 Exact-message send gate | Nine-condition checklist + approval ID | Send or do not send? |
| G6 Weekly quality review | Replies, objections, complaints, effort | Continue, narrow, or stop the slice? |
| G7 Quarterly source review | Licence/ToS and retention re-check | Keep, restrict, or retire the source? |

## Open review items

Before any production outreach, a qualified reviewer must confirm the concrete
France/EU basis, retention rationale, provider DPAs, provider terms, and the
wording of the privacy/source notice. This document does not make those
decisions on behalf of the founder or counsel.

Official starting points for that review:

- [CNIL: electronic commercial prospecting](https://cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique-sms-mms-et-automate-dappel)
- [CNIL: commercial prospecting theme](https://www.cnil.fr/fr/thematique/commerce-marketing/prospection-commerciale)
- [Google Places policies](https://developers.google.com/maps/documentation/places/web-service/policies)
- [Etalab Open Licence](https://www.data.gouv.fr/pages/legal/licence-ouverte-open-licence/)
