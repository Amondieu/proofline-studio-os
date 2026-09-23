# 30 — Prospecting Data Sources, Signals and Send Gates
<!-- v0.1 · 2026-09-23 · owner: founder (sign-off + ⚖️ review) · review: quarterly, and whenever a source's ToS changes -->

> **Not legal advice.** This document encodes an operating policy with cited sources. Items marked ⚖️ need a French/EU lawyer or DPO before they become client-facing claims. Sources verified 2026-09-23.

---

## A. The legal frame in five lines

| Rule | Source |
|---|---|
| **B2B email prospecting works on opt-out, not opt-in** — but only for a *nominative professional* address, an offer *related to the recipient's function*, and only if the person was informed and can object simply and free of charge. | CNIL guidance on prospection (Art. L.34-5 CPCE / doctrine CNIL) — see §12 [1][2] |
| A nominative professional address (`prenom.nom@societe.fr`) **is still personal data**. The B2B relaxation removes the consent requirement, not the information and objection duties. | CNIL + practitioner analyses [2][3] |
| Legal basis is **legitimate interest (Art. 6(1)(f) GDPR)** → requires a documented balancing test (LIA), information under **Art. 14**, and an **Art. 21** objection that is absolute for direct marketing. | GDPR; template in `templates/lia-b2b-outreach.md` |
| **Retention**: delete/stop using inactive prospect data after ~3 years without contact (CNIL recommendation). Opt-outs are kept **indefinitely** as a suppression record, with minimal data. | CNIL [3][4] |
| Every message: clear sender identity, the **source of the contact**, and a **simple, free opt-out honoured immediately**. Generic addresses (`contact@`, `info@`) fall outside the personal-data regime but are weaker for conversion. | CNIL [1][2] |

**Consequence for the studio:** cold outreach is legal here, so our differentiator is not "we found a loophole" — it is **evidence, restraint and a suppression discipline** a client can audit.

---

## B. Source inventory (what we may use, for what)

Columns: *Permitted purpose* is narrower than *technically possible* on purpose.

| # | Source / API | Best use | Fields we take | Permitted purpose | Retention | Licence / ToS status | Cost | Legal review | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **INSEE SIRENE API** (api.insee.fr, V3.x) | French company verification | SIREN/SIRET, legal form, NAF/APE, HQ location, creation date, status | Firmographic verification + ICP filtering | Firmographics cached **12 months**, re-verified before use | **Licence Ouverte 2.0 (Etalab)** — commercial reuse allowed; must credit `www.insee.fr` + date of last update | Free (30 calls/min) | Not required (open licence); keep attribution | **V1 — ADOPT** |
| 2 | **Annuaire des Entreprises** (annuaire-entreprises.data.gouv.fr) | Human cross-check of #1 | Same as SIRENE + public contacts published by the company | Verification, manual research | 12 months | Open data (Etalab) | Free | None | **V1 — ADOPT (manual)** |
| 3 | **Pappers API** | FR company verification + BODACC-level events | Register data, filings, officers, BODACC notices | Verification, change signals | Events as *signals* 90 days; firmographics 12 months | Commercial API, credits; data re-published from INSEE/INPI/BODACC. **ToS/redistribution must be read before storing beyond internal use** ⚖️ | €20/mo (500 credits) → pay-as-you-go | Yes: contract + redistribution clause | **V1 — ADOPT with contract review** |
| 4 | **BODACC / INPI open data** | Change signals (creation, modification, filings, IP events) | Notice type, date, entity | Hot-signal detection | 90 days as signal | Open data (Etalab) for BODACC; INPI has its own open-data licence — verify per dataset | Free | Light | **V1 — ADOPT (signals only)** |
| 5 | **Companies House API (UK)** | UK entity + officer verification | Company profile, officers, filing history, PSC | Verification, ICP filtering | 12 months | Free public REST API, registration for key; **directors' DoB is month+year only**; ECCTA identity verification rolling through 2026 | Free | Light (UK GDPR) | **V1 — ADOPT for UK slice** |
| 6 | **OpenCorporates API** | International entity resolution | Registry records across 140+ jurisdictions | Verification (later stage) | n/a in V1 | **ODbL share-alike** for permitted users; **commercial use requires a paid non-share-alike licence** (from £2,250/yr, 500 calls/mo); "Permitted Users" excludes corporations | £2,250+/yr | Yes: share-alike trap | **NOT V1 — reference only** |
| 7 | **Crunchbase API** | Startup/funding signals | Funding, investors, categories | Signal enrichment (later) | n/a in V1 | **Free API tier discontinued**; Basic/Pro plans or enterprise licensing, quote-only | $49–99/mo → enterprise | Yes | **NOT V1 — reference only** |
| 8 | **Official company website / blog / changelog / pricing page** | The *only* source for concrete website diagnoses | Public offer, CTA, proof, launch posts | Manual diagnosis (human reads it) | Observation kept with URL + date; page copy quoted **≤25 words** | Public content; we read it manually. No automated bulk extraction ⚖️ | Free | Light: quoting limits | **V1 — ADOPT (manual)** |
| 9 | **Official job page / careers page** | Growth signal | Open roles (growth/sales/marketing/product) | Signal only — never "proof of budget" | 90 days | Public page; read manually | Free | None | **V1 — ADOPT (manual)** |
| 10 | **Company press page / LinkedIn *posts* (public, read manually)** | Launch & positioning signals | Public announcement + date | Signal + personalisation context | 90 days | Manual reading only. **No scraping, no automation, no export** — platform ToS + our own rule | Free | Light | **V1 — ADOPT (manual, read-only)** |
| 11 | **Product Hunt / app stores / accelerator directories** | Early SaaS launch signals | Launch date, category, public page | Signal only, only where the platform's terms permit | 90 days | **Per-platform ToS must be checked before any programmatic use** | Free/varies | Yes if automated | **Pilot — manual until checked** |
| 12 | **Self-declared inbound forms / referrals** | The highest-priority leads | Whatever the person submitted + consent/source | Direct response to their request | Per privacy notice (12 months) | Their own submission = strongest basis | Free | None | **V1 — ADOPT (priority 1)** |
| 13 | **Paid data providers with DPA + provenance + suppression support** | Scaling after ICP validation | Business contact data | Only after a signed DPA, provenance record and suppression-list integration | Per contract, ≤12 months | Contract review mandatory ⚖️ | Varies | Yes | **Later — only after ≥20 validated conversations** |
| ✗ | **Google Maps / Places scraping or warehousing** | — | — | **Rejected** | — | Maps Platform ToS prohibits export/extract/scrape and caching outside narrow exceptions (place IDs storable; coordinates ≤30 days) [5] | — | — | **AVOID** |
| ✗ | **LinkedIn scraping / automation** | — | — | **Rejected** | — | Platform terms prohibit automated collection; we treat it as prohibited by default (UNVERIFIED in detail, conservative) | — | — | **AVOID** |
| ✗ | **Purchased contact lists without provenance/DPA** | — | — | **Rejected** | — | No lawful basis we could defend (Art. 14 information impossible to satisfy) | — | — | **AVOID** |
| ✗ | **Enrichment of private/sensitive traits** (health, politics, finances, family) | — | — | **Rejected** | — | Incompatible with minimisation and Art. 9 exposure | — | — | **AVOID** |

**V1 rule of thumb:** registry data tells us *whether the company fits*; the company's own public pages tell us *whether we have something useful to say*. Neither tells us *how to reach someone privately* — and we never look for that.

---

## C. V1 stack (the six moves, and nothing else)

```text
1. Web search + manual research          → 30-name longlist for one ICP slice
2. Public company site / blog / changelog → one concrete, quotable observation per prospect
3. INSEE SIRENE (FR) or Companies House (UK) → entity verification before any contact
4. Official job / press / launch pages   → one *current* trigger, source-linked
5. Notion prospect database (controlled) → one record per prospect, exportable CSV
6. Human approval before every send      → the Send Gate in §E, signed per message
```
No Maps scraper. No LinkedIn automation. No bought lists. No "AI enrichment" of anything we did not read ourselves.

---

## D. Data model and minimisation

Machine-readable definition: `schemas/prospect-record.schema.json` · filled example: `templates/prospect-record.example.json`.

| Field group | Why it exists | Minimisation rule |
|---|---|---|
| `prospect_id`, `company_name`, `country`, `company_url` | Identification of the *organisation* | No private data about individuals |
| `source_record` | Art. 14 transparency: where the data came from | Exactly one primary source + URL + `collected_at` + `terms_checked` |
| `public_signal` | The reason we are writing *now* | One signal only, with `evidence_url`, `observed_at`, confidence, and a ≤25-word factual claim |
| `website_observations[]` | The substance of the mini-value | 1–3 items, each with `evidence_url` and `verified_by_human: true` |
| `contact_route` | How we reach the person **in their professional function** | `public_professional_email` (nominative) or `contact_form` or `inbound`. Never guessed addresses, never private channels |
| `compliance` | Proof we can defend the send | `lawful_basis`, `opt_out_status`, `suppression_checked`, `send_status`, `retention_delete_on` |
| `outreach_log[]` | Sequence discipline + evidence | Date, template id, touch number, outcome; append-only |

**Never stored:** personal phone numbers, home addresses, private social accounts, date of birth, family information, health/political/financial inferences, or any scraped personal profile data.

**Verification rule:** every `contact_route` needs a URL showing the address publicly **in a professional context** (contact page, imprint, team page). If it only exists inside a third-party database → not V1.

---

## E. Send Gate (all nine, or the message does not go)

```
DO NOT SEND unless all are true:
[ ] 1. Public professional context and its source URL are recorded in the prospect record.
[ ] 2. The message relates directly to the recipient's professional role.
[ ] 3. One real, source-linked current trigger exists, observed within the last 90 days.
[ ] 4. At least one factual website observation, verified by a human, with a URL.
[ ] 5. No opt-out / suppression record for this person, domain or company.
[ ] 6. Sender identity, legal business identity, source-of-contact line and privacy URL are in the footer.
[ ] 7. A simple, free opt-out is present (reply "no" AND a working link).
[ ] 8. The exact final email + recipient list has explicit human approval (AP-xxxx record).
[ ] 9. Sending domain authentication (SPF/DKIM/DMARC) and the reply inbox have been tested today.
```
Checklist file: `templates/send-gate-checklist.md` · review skill: `skills/outreach-review/SKILL.md`.

**Hard stops (escalate to human, never "handle it later"):** any insolvency/legal-procedure signal, any indication of illness or personal crisis, any request to discuss a competitor's confidential data, any prospect who is a public official or in a regulated sector, any prospect under 18 contact context, any list we did not build ourselves.

---

## F. Sequence and suppression discipline

| Rule | Value |
|---|---|
| Touches per prospect | **Max 3** (initial + 2 follow-ups) |
| Window | 21–30 days, then stop |
| Follow-up timing | +5–7 working days, then +7–10 working days |
| After sequence ends | **Suppression for at least 90 days**; reactivation only with a *new, verifiable* trigger from an official source |
| On any objection ("no", "unsubscribe", "stop", silence-with-request) | **Immediate, permanent suppression**; no follow-up, no "just confirming", no re-import ever |
| Inactive prospects | Deleted after **3 years** without contact (CNIL recommendation) |
| Cross-file safety | The suppression list is a **separate system of record**; it is never used as a source for new outreach and is never exported to a campaign tool as a *target* list |
| Volume | ≤5 personalised messages per day. If quality drops, volume drops — not the reverse |

Suppression record (minimal fields, kept indefinitely): `email_or_domain`, `suppressed_at`, `reason`, `source`, `scope` (person/domain/company), `note`.
Schema: `schemas/suppression-record.schema.json` · file: `templates/suppression-list.csv`.

---

## G. Hot-signal model

The best prospect is **not** "has no website". It is:

```
Fit  +  current change impulse  +  visible conversion leak  +  reachable decision maker
```

| Priority | Signal | Observable evidence | Why now | Pitch angle | Reject if… |
|---|---|---|---|---|---|
| 1 | Product/service launch | Changelog, press page, new URL | New traffic needs explanation | Launch & Demand System | Launch is >6 months old |
| 2 | New AI/automation service line | New service page, webinar, sales post | Complex offer needs trustworthy explanation | AI / Automation Authority | We cannot verify the service exists |
| 3 | Funding / accelerator | Official announcement | GTM phase likely | SaaS Landing Sprint | Only a rumour or a scraped database entry |
| 4 | New sales/growth/marketing role | Official job page | Demand focus rising | Content-to-conversion leak | We treat it as budget proof (it is not) |
| 5 | Rebrand / repositioning | Brand or web announcement | Decision window open | Message + Visual Direction Sprint | It is only a logo refresh we assume |
| 6 | New case study / logos | Own news/case page | Proof exists but is often badly integrated | Proof Architecture Audit | The client cannot substantiate the claims |
| 7 | Strong social momentum, weak CTA | Public posts + own site | Attention leaking | Audience-to-lead flow | Numbers are unverifiable |
| 8 | Hero without buyer/outcome/CTA | Public website | Immediately demonstrable | 3-point teardown | It is only an aesthetic opinion |
| 9 | Mobile form/booking defect | Manually verified on our own test | Direct lead loss | Mobile lead-flow fix | We have not reproduced it ourselves |

**Rejected as signals (never used):** "design looks old" · "no Instagram" · unverified revenue/budget/conversion guesses · personal life events · insolvency/health/political situations · generic company lists with no trigger.

---

## H. Mini-value: the 3-Point Conversion Teardown

Deliverable: **90-second Loom or 150–250 words of text** · built in **5–12 minutes** · three observations, one hero rewrite, one next step.
Scripts and the text version: `templates/teardown-quick-audit.md` · full report format for *paying* teardown requests: `templates/teardown-report.md`.

| Metric | Definition | V1 internal target |
|---|---|---|
| Audit completion rate | finished audits / qualified prospects | ≥80% |
| Positive reply rate | "yes", question, interest, referral | ≥8% (highly personalised only) |
| Audit-to-call rate | booked calls / delivered audits | ≥3% |
| Qualified call rate | calls with fit + budget + decision access / calls | ≥40% |
| Opt-out rate | opt-outs / delivered emails | <2% |
| Negative reply rate | complaints / delivered emails | <5% |
| Meeting-to-proposal rate | proposals / qualified calls | ≥50% |

These are **internal experiment thresholds, not market guarantees**. At low volume, read trends across ≥20 sends; never react to a single reply.

---

## I. Governance and human gates

| Gate | Who approves | What is checked | Artefact |
|---|---|---|---|
| G1 Source admissibility | Founder | Source licence/ToS, purpose, retention for the source used | row in §B + `license-register.csv` |
| G2 Record completeness | Founder | Schema valid, signal ≤90 days, observation URL human-verified | `prospect-record.json` |
| G3 LIA + basis | Founder (⚖️ once for the template, then per-material-change) | Legitimate interest balance, Art. 14 information, absolute objection | `templates/lia-b2b-outreach.md` |
| G4 Suppression check | Founder (or script, with human confirmation) | No suppression hit for person/domain/company | suppression list query logged |
| G5 Send gate | Founder | All nine items in §E | `templates/send-gate-checklist.md` + `AP-xxxx` approval record |
| G6 Weekly review | Founder | Opt-outs honoured, negative replies analysed, volume vs quality | 20-minute log entry |
| G7 Quarterly source review | Founder | Every source re-checked: licence, ToS, price, data freshness | updated §B + changelog entry |

**Never automated:** sending, suppression removal, list export to a campaign tool, or the decision that a signal is real.

---

## J. What would make us stop entirely

- A platform term change that makes our *manual* reading of public pages a breach (we would restrict to search + registry only).
- Any indication that our outreach volume is being experienced as spam (negative reply rate >5% or opt-out >2% for two consecutive weeks).
- A CNIL/EDPB position that narrows the B2B opt-out regime for one-person service providers ⚖️.
- Client pressure to use bought lists or scraping — we decline, in writing.

---

## K. Open items requiring human/legal review

1. **LIA wording** for our specific B2B outreach (template ready; needs review once). ⚖️
2. **Pappers API redistribution clause** — confirm we may store its derived data in our own CRM beyond internal verification. ⚖️
3. **Platform ToS for Product Hunt / accelerator directories** before any automated collection.
4. **Suppression-list retention** on GDPR grounds (we keep it "indefinitely" as necessary for objection compliance — document the reasoning). ⚖️
5. **Notion as CRM**: whether the workspace is EU-hosted for our plan, and what the DPA covers. ⚖️
6. **Email-sending infrastructure**: which EU transactional provider and whether it signs a DPA (POC-04 in `research/poc-backlog.md`).

---

## 12. Sources
[1] CNIL — Prospection commerciale par courrier électronique, SMS/MMS et automate d'appel: https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique-sms-mms-et-automate-dappel · [2] CNIL — RGPD en pratique: maîtrisez votre relation client (opt-in vs opt-out par canal, B2B email = opt-out): https://www.cnil.fr/fr/rgpd-en-pratique-maitrisez-votre-relation-client · [3] Practitioner summary of the CNIL B2B regime (3 cumulative conditions, nominative pro address = personal data, 3-year retention, simple opt-out): https://www.ediware.net/email-marketing-b2b/cold-emailing-b2b-cadre-legal/ and https://kohenavocats.fr/2026/06/14/prospection-commerciale-email-sms-cnil-consentement-2026/ · [4] CNIL retention/opt-out practice overview: https://agentco.fr/actualites/prospection-commerciale-cnil · [5] Google Maps Platform ToS §3.2.3 + Service Specific Terms and Places policies (no scraping/export; place IDs storable, coordinates ≤30 days): https://bizcollect.dev/blog/google-places-api-terms · [6] INSEE SIRENE API terms + Licence Ouverte 2.0 and the 30 calls/minute limit: https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee and https://www.data.gouv.fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret and https://github.com/etalab/licence-ouverte/blob/master/LO.md · [7] Pappers data sources, free interface vs credit-priced API: https://www.pappers.fr/fonctionnalites and https://hayot-expertise.fr/en/blog/pappers-company-data-tool-review · [8] Companies House API surface, free access, partial DoB, ECCTA identity verification: https://dev.to/openregistry/uk-companies-house-post-eccta-reality-and-the-actual-api-surface-3737 and https://www.kyckr.com/blog/how-to-search-companies-house-uk-company-register-2025 · [9] OpenCorporates pricing + ODbL share-alike and non-share-alike licensing: https://opencorporates.com/pricing/ and https://savvyiq.ai/compare/opencorporates · [10] Crunchbase API: free tier discontinued, Basic/Pro/Enterprise, quote-only: https://pipeline.zoominfo.com/sales/crunchbase-api · [11] GDPR Art. 21 (right to object; direct marketing) and Art. 6(1)(f)/Art. 14 (information duties): EUR-Lex, Regulation (EU) 2016/679 — see `templates/lia-b2b-outreach.md` for the practical test.
