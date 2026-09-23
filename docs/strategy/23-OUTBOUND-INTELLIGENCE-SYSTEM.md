# 23 — Outbound intelligence system

<!-- v0.1 · 2026-09-23 · owner: founder · status: pilot-only, no automated send -->

Proofline Studio may use outbound research to find a small number of companies
with a visible, expensive conversion leak. It must not become a
`scrape → AI-mail → mass-send` machine.

The operating loop is:

`Allowed source → Candidate → Public evidence → ICP/score → Human research review → 3-point teardown → Human send approval → Send → Reply/opt-out → Learning`

Research and drafting can be assisted. Final recipient selection, legal review,
exact-message approval, and sending remain human actions.

## V1 offer and ICP

Start with:

- AI / automation consultants with a specific technical service;
- micro-SaaS or AI tools with a live product and a concrete launch/use case.

The matching Proofline archetypes are `ai-automation-authority` and
`saas-launch-demand`. The first offer hypothesis is the `authority-sprint` or
`launch-system` tier, subject to Discovery and evidence.

Do not optimize for “no website”. A business with an existing offer, demand,
and an observable conversion gap is a better fit than a business with no
digital presence and no evidence of budget or intent.

## System boundaries

### Allowed assistance

- discover candidate companies from permitted public sources;
- record dated evidence URLs and source terms;
- score fit and confidence;
- draft a small audit and a message;
- classify replies and record learning.

### Never automated

- guessing personal email addresses;
- bypassing logins, CAPTCHAs, robots, rate limits, or platform terms;
- collecting sensitive personal data;
- ignoring opt-outs or suppression records;
- sending messages;
- asserting legal compliance;
- inventing personalisation, metrics, proof, or business facts.

## Repository contracts

- `schemas/prospect-record.schema.json` — candidate and evidence record.
- `schemas/signal-record.schema.json` — dated trigger or change signal.
- `schemas/audit-record.schema.json` — maximum three evidence-backed findings.
- `schemas/outreach-draft.schema.json` — draft that cannot approve itself.
- `schemas/send-approval.schema.json` — exact recipient/message human gate.
- `schemas/reply-record.schema.json` — outcome, reply, and suppression record.
- `config/studio/outbound-policy.v1.json` — thresholds and forbidden actions.
- `studio/outbound.py` — typed models and score validation.

## External skill adoption

The following nine upstream skills were installed as references from
`coreyhaines31/marketingskills` at commit
`5b2c0007766c6a1cf1d53fd8fc73e979e0821022`:

`product-marketing`, `prospecting`, `customer-research`,
`competitor-profiling`, `cro`, `copywriting`, `cold-email`, `revops`, and
`analytics`.

They are not Proofline policy. Local wrappers in `skills/` add the studio’s
archetype, evidence, rights, privacy, and human-send boundaries. Upstream
content must be reviewed again when the pin changes.

## V1 capacity

- 20 manually researched candidates for the first pilot;
- at most 10 audits per week;
- only prospects with a score of 70/100 or higher receive a manual audit;
- at most three messages per prospect in a 21–30 day sequence;
- 90-day internal suppression after the sequence unless an explicit human
  decision changes the state;
- no message is sent without a `SendApproval` for the exact recipient and
  exact message hash.

These are conservative internal operating limits, not legal advice or a claim
that a particular sending volume is safe.

## First controlled test

Use the Proofline master site as the offer and run a research-only pilot:

1. collect 20 candidates from permitted sources;
2. record one current signal and up to three website observations each;
3. reject all records below 70 or with unclear provenance;
4. manually review the five strongest records;
5. draft three-point teardowns and messages;
6. stop before send unless the full compliance and human approval gates pass.

The pilot is not executed by this repository change. No prospect data,
personal contacts, or outbound messages are committed here.
