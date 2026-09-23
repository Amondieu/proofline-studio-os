# Outreach Email Sequences (3 touches, then stop)
<!-- v0.1 · 2026-09-23 · owner: founder · every send passes templates/send-gate-checklist.md · sources in docs/30 §12 -->

**Non-negotiable mechanics**
- Max **3 touches** in 21–30 days, then suppression ≥90 days.
- Every message: sender identity, legal business identity, **source of the contact**, privacy URL, and a simple free opt-out that works (reply "no" **and** a link).
- Personalisation must reference something *public and current* (≤90 days), quoted factually, never insinuating.
- No fake familiarity, no compliments-as-filler, no urgency theatre, no invented numbers.
- Personal data rule: a nominative professional address is personal data → info + objection duties apply even though consent is not required (B2B opt-out regime).

---

## Personalisation block (fill before anything else)
```text
Trigger (official source, date, URL):            ________________________________
Observation (what the visitor cannot do, ≤25 words, verified by me): _______
Role relevance (why this person owns this):      ________________________________
Evidence class used in message 1:                demonstrated method | stated standard | labelled concept
Private teardown link (no client data, public page only): ______________________
```
If any line is empty → no send. There is no "I'll personalise later".

---

## Touch 1 — the observation (day 0)

**Subject:** `One conversion observation on [Company]`

```text
Hi [First name],

I saw [specific, factual trigger from an official source — e.g. your new
[service / launch / product update] announced on [source, month]].

I checked the landing page on mobile and found one clear friction point:
a first-time visitor can see [what is currently clear], but cannot quickly
see [missing buyer / outcome / next step].

I put together a short 3-point teardown with:
- the exact message gap,
- one proof element worth surfacing,
- a suggested hero rewrite.

Here it is: [private link, unlisted]

I run fixed-scope landing-page sprints for [specific ICP] that combine message,
conversion copy, visual direction, build and launch QA.

Would a 15-minute fit check be useful, or should I send the notes as plain text?

Best,
[Name] — Proofline Studio
[website] · [legal business name + address]
Privacy: [privacy URL]
I contacted you because this may be relevant to your role at [Company],
using your publicly listed business address from [source].
To opt out of future messages, reply "no" or use [unsubscribe URL].
```

**Why this shape works (and what it deliberately avoids):** the opener is a verifiable public fact instead of a pleasantry; the observation is non-insulting and checkable; the value is small enough to be produced in 5–12 minutes; the CTA offers a lower-commitment alternative; nothing claims a result.

---

## Touch 2 — sharpen the value (day +5–7 working days, only if no reply and no opt-out)

**Subject:** `Re: One conversion observation on [Company]`

```text
Hi [First name],

Closing the loop on the teardown.

The first change I would test is moving
"[specific outcome for specific buyer]" into the hero,
followed by "[specific CTA]".

That makes the offer understandable before a visitor has to interpret the
rest of the page — which is usually where mobile visitors drop out.

If a page sprint is not relevant now, no reply is needed.
If you would like the plain-text notes, reply "notes".

Best,
[Name]
[identity · source line · privacy URL · opt-out line]
```

---

## Touch 3 — close it out (day +7–10, final touch)

**Subject:** `Should I close this out?`

```text
Hi [First name],

I have not heard back, so I will close this out after this message.

The teardown stays here: [link]

If it becomes relevant later, reply "audit" and I will send the three
recommendations in a short written version.

To opt out, reply "no" or use [unsubscribe URL].

Best,
[Name]
[identity · source line · privacy URL · opt-out line]
```

**After touch 3:** sequence ends. Suppression for ≥90 days. Reactivation only with a **new** verifiable trigger.

---

## Objection / reply handling (short, non-defensive)

| Reply | Response | Internal action |
|---|---|---|
| "No thanks" / "Unsubscribe" / "Stop" | One line: "Understood — you're removed, you won't hear from me again." | **Immediate permanent suppression** (person + domain scope). No further contact, ever. |
| "Not now" | "Understood — I'll close it out. Happy for me to check back in three months?" Only if they say yes. | Suppress unless explicit consent to re-contact; log the consent. |
| "Send the notes" | Send the plain-text teardown, then stop. | Log delivery, no follow-up sequence. |
| "Who gave you my address?" | Name the exact source and URL, state the legal basis and their rights. | Log; consider removing the source if this repeats. |
| "How much?" | Give the tier + price band + exclusions publicly stated on the site. | Log as qualified. |
| Hostile complaint | Apologise once, remove immediately, do not defend. | Suppress; review the signal quality for that ICP slice. |
| Auto-reply / out of office | Note the return date; send **one** follow-up afterwards, counted as a touch. | Log. |

---

## Volume and quality rules
- ≤5 personalised messages/day. If a day produces fewer than 5 *good* observations, send fewer.
- Before any batch: all nine Send Gate items true for each message.
- Weekly review (20 min): reply rates, opt-outs honoured, any complaint traced to root cause, and whether the *signal source* is still producing usable triggers.

## Prohibited
Bought lists · scraped contacts · generic `info@` blasts · guessing email addresses · "just checking in" nudges · fake replies to your own email · pre-ticked consent · hidden unsubscribe · sending from a domain without SPF/DKIM/DMARC.
