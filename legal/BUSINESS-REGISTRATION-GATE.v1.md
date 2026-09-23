# G-BIZ-001 — Austria business registration gate

Status: required / blocked until human confirmation

This gate prevents Proofline Studio from treating an unconfirmed Austrian
business setup as permission to accept paid work. It is an internal control,
not legal advice and not proof that a specific activity is or is not a Gewerbe.

## Blocks

- paid public offer acceptance;
- binding paid proposal or contract acceptance;
- deposit or other payment collection;
- invoice issuance;
- paid client delivery;
- public checkout for a paid service.

## Required evidence

- [ ] Actual service description written in plain language.
- [ ] Exact Gewerbewortlaut and scope confirmed with the regional WKO or
      competent authority.
- [ ] The combined WITHKODEX/Proofline scope has been checked against the
      proposed `Werbeagentur, Multimediaagentur` and IT-service wordings;
      neither is assumed to cover the full scope without written confirmation.
- [ ] General personal, residence, and eligibility requirements confirmed for
      the actual founder situation.
- [ ] Registration record or documented professional exemption reviewed by a
      human; no assumption based on a price threshold.
- [ ] Free-Gewerbe status is not being confused with an exemption from
      registration or scope limits.
- [ ] `Unternehmensberatung einschließlich Unternehmensorganisation` is not
      used as a public umbrella claim without a separate qualification review.
- [ ] Business identity, contact address, and invoice profile prepared.
- [ ] Tax, VAT, SVS, and WKO follow-up questions assigned to a qualified
      reviewer for the actual personal situation.
- [ ] Austrian website information/disclosure requirements reviewed.
- [ ] Privacy/data-flow map and form retention decision reviewed.
- [ ] SOW/contract reviewed before paid acceptance.
- [ ] Asset rights, AI disclosure, ownership, and handover records prepared.

## Human decision

- Decision: `[blocked | approved for paid preflight | superseded]`
- Reviewer: `[name / role]`
- Date: `[YYYY-MM-DD]`
- Evidence links: `[registration / written WKO answer / review record]`
- Scope covered: `[exact services and jurisdiction]`
- WKO contact and response date: `[record]`
- Limitations and follow-up: `[record here]`

Automated audits may keep this gate blocked when evidence is absent. They may
not change it to approved.
