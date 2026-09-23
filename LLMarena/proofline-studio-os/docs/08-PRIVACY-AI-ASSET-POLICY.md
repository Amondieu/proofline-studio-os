# 08 — Privacy, AI and Asset Policy
<!-- v0.1 · 2026-09-23 · owner: founder (sign-off) · ANY change requires ⚖️ counsel review + re-brief of active projects -->
> Not legal advice. This is an operating policy that keeps us out of avoidable trouble.

## 1. Data we process (and why)
| Data | Purpose | Legal basis (assumed) | Retention | Where |
|---|---|---|---|---|
| Contact/teardown form data | Answer the request, qualify | Legitimate interest / pre-contractual steps | 12 months in the shared inbox, then delete | Cloudflare Worker + D1 (or Tally, EU) + email provider |
| Booking data | Schedule the call | Pre-contractual steps | Until the call + 3 months | Cal.com |
| Analytics | Aggregate site measurement | Consent-exempt only if configured aggregate/first-party/cookieless; otherwise consent | 25 months max | Plausible / Umami |
| Client project files | Deliver the project | Contract | Handover + retention window stated in the contract | Client repo + our working copy |

**Rules:** data minimisation (no field we cannot justify) · no cross-site tracking · no advertising pixels · no session replay without signed consent and masking · export and deletion paths documented for every tool we install for a client.

## 2. Analytics configuration (consent management)
Default: cookieless, first-party, aggregate-only measurement (Plausible or Umami). Where it meets the criteria, French rules allow audience measurement without a consent banner — aggregate purposes only, no cross-site tracking or data pooling, limited tracker lifetime (13 months where a tracker exists), 25-month retention, IP truncation/anonymisation, publisher-only use, and a documented self-evaluation. If a client insists on Google Analytics or advertising tags, we require a compliant consent banner **first**, and we do not push the decision to the client's lawyer for free. Any new tag = privacy review + documented decision before deploy. ⚖️

## 3. AI tool policy (hard rules)
1. **No client material in any generative tool.** No client photos, copy, unreleased product shots, screenshots, credentials, NDAs or personal data — regardless of the vendor's commercial-use terms.
2. **No client names in prompts.** Describe the category, not the client.
3. Generative tools are used for: moodboards, hero concepts, texture/background plate exploration, internal pitch visuals in the *concept* stage.
4. Generative tools are **not** used for: production code as-is, legal pages, accessibility statements, client claims, or anything a human has not reviewed line by line.
5. Vendor assessment before use: commercial-use rights, input-use for training, indemnification, deletion behaviour, data residency. Record each vendor's status in `research/license-register.csv` (AI vendors included).
6. **Higgsfield specifics (as researched):** commercial use of outputs is permitted and our outputs remain ours (Terms §§4.2–4.4, July 2026 revision), rights survive cancellation and may be sublicensed to clients — **but** non-Enterprise accounts still allow input use for model training by default, IP indemnification is Enterprise-only, and outputs are explicitly non-exclusive. Consequence: client-confidential material never goes in; use the private workspace only; never submit work to public showcases unless the client permits it.
7. Disclosure: any realistic synthetic person, or a synthetic asset presented as documentary, gets a visible human-readable label at first exposure — nothing buried in metadata. AI Act Article 50 transparency obligations have applied since 2 August 2026 (deplyer duty for deepfake-like content; attenuated treatment for evidently artistic/fictional work with appropriate disclosure; human editorial responsibility matters for text). ⚖️

## 4. Asset rules
| Source | Rule |
|---|---|
| Own photography/illustration | Preferred. Log creator + licence (usually: ours/work-for-hire), release for identifiable people. |
| Client assets | Only with written permission; log the permission; never re-upload to a generative tool. |
| Stock (free tier) | Commercial use may be granted but indemnification is often $0 and model releases are unverified → never for claims about people/products; log URL + download date. |
| Stock (paid, e.g. Unsplash+) | Extra restrictions apply (no AI/ML use, no digital templates, no shared drives) → never in templates we redistribute, never in AI tools. |
| AI-generated | Always `templates/asset-provenance-log.csv` + `templates/ai-asset-approval.md` before production. |
| Fonts | OFL/Apache only, self-hosted, licence file shipped. Never a third-party font CDN. |
| Icons | Lucide (ISC) inline SVG. |

## 5. Red-flag → human/legal review matrix
| Signal | Action |
|---|---|
| Client asks to use their customer photos/testimonials without written permission | Refuse; request permission; document |
| Client wants "trusted by" logos they cannot evidence | Refuse; offer method-based proof instead |
| Request to describe a site as "GDPR/accessibility compliant" | Refuse the wording; offer evidence-based wording ⚖️ |
| Client wants synthetic people presented as staff/customers | Refuse ⚖️ |
| Client asks to upload their CRM export / NDA'd material into an AI tool | Refuse ⚖️ |
| Client wants tracking without consent | Refuse or require a compliant CMP first ⚖️ |
| Client is in a regulated sector (health, finance, legal) | Extra review before any claim or data flow ⚖️ |
| Client domain/hosting must stay in our accounts "for simplicity" | Refuse — ownership gate |
