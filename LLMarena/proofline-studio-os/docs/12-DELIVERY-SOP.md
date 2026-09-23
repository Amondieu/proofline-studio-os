# 12 — Delivery SOP (5 / 10 / 14 days)
<!-- v0.1 · 2026-09-23 · owner: agent drafts, founder signs · every project copies this file into its repo -->

## Phase gates (identical for all tiers)
`Intake → Message map → Direction brief → Build → QA → Launch → Handover`
Each gate ends with a written artefact and an explicit client sign-off (email is enough).

| Tier | Day plan | Gates | Revision rounds | Content freeze |
|---|---|---|---|---|
| Starter (5 d) | D1 intake + message map · D2 direction brief + build start · D3 build · D4 QA + fixes · D5 launch + handover | message map, direction brief, QA receipt | 1 | end of D2 |
| Authority (10 d) | D1–2 intake, message map, audit · D3 direction brief · D4–6 build · D7 motion + polish · D8 QA · D9 launch · D10 handover + training | + 5-second test before build | 2 | end of D5 |
| Launch System (14 d) | D1–3 discovery + full message architecture · D4–5 IA + direction · D6–10 build (≤5 pages) · D11 CMS + editor training prep · D12 QA · D13 launch · D14 handover + 60-day plan | + CMS test with client editing live | 3 | end of D8 |

## Revision policy
- A revision is a **bounded pass** at agreed sections, within the signed direction, with feedback in writing (one message, consolidated).
- Unlimited micro-tweaks are not revisions; they are change requests (below).
- Feedback received after the content freeze in a way that changes the *offer* restarts the schedule from the message-map gate.
- We do not do unlimited revisions on fixed prices. Ever. It is stated in the proposal, not discovered later.

## Change requests
| CR type | Price |
|---|---|
| Small (copy tweak, image swap, colour token adjustment, one section) | €75 flat or included in the retainer |
| Medium (new section, new page, new integration) | €150–350 |
| Large (new template, CMS model change, multi-language) | Re-quote |

## Acceptance criteria (what "done" means)
Live URL · all cannot-launch items green · launch receipt in the repo · client can log into every account · documentation + training delivered · analytics firing · rollback tested.

## Project folder structure (per project)
```
client-slug/
├── README.md              # scope, stack, who owns what, links to receipts
├── docs/                  # this SOP copy, message map, direction brief, QA receipt, launch receipt
├── src/                   # Astro site
├── public/fonts/          # self-hosted fonts + licences
├── tokens.json            # direction tokens
└── .github/workflows/     # gate + deploy
```

## Naming convention
`<client-slug>_<artefact>_v<major>.<minor>_<YYYY-MM-DD>.<ext>` — e.g. `acme_message-map_v1.0_2026-10-04.md`.
Assets: `<purpose>-<direction>-<nn>.<ext>` — e.g. `hero-cinematic-01.avif`. Never "final_final".

## Versioning
Content artefacts: `vMAJOR.MINOR`; MAJOR = client-visible change. Code: semver tags (`v1.0.0` at launch). Receipts are append-only, never edited after signing.
