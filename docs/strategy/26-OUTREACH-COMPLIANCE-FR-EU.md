# 26 — Outreach compliance boundary for France / EU

<!-- Internal control document; not legal advice. Obtain qualified review before any real campaign. -->

This document defines a conservative operational gate. It does not determine
the lawful basis for a particular campaign, country, recipient, provider, or
data source.

The CNIL states that electronic commercial prospecting requires prior
information, and that professional B2B prospecting may in some circumstances
rely on legitimate interest when the solicitation relates to the person’s
professional activity; the person must be informed and able to object simply
and freely. See the [CNIL electronic prospecting guidance](https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique)
and the [CNIL objection-list guidance](https://cnil.fr/fr/comment-utiliser-une-liste-repoussoir-pour-respecter-lopposition-la-prospection).
Re-check the current official guidance before implementation.

## No-send conditions

Hold or reject when:

- the professional relevance of the offer to the recipient role is unclear;
- the source, collection date, or permitted use is unclear;
- the recipient is private, sensitive, or not a role-relevant professional
  contact;
- a lawful-basis assessment and transparency path are missing;
- an opt-out or suppression record exists;
- sender identity, privacy notice, or free objection mechanism is missing;
- the message uses deceptive subject lines or fabricated personalisation;
- the audit contains unsupported performance, legal, health, finance, or other
  sensitive claims;
- the exact recipient and exact final message have not been human-approved.

## Required record before send

```text
[ ] professional context and relevance documented
[ ] source URL, source type, and collection date recorded
[ ] source terms / permitted use reviewed
[ ] data minimised to necessary fields
[ ] concrete legal-basis assessment completed by a responsible human
[ ] suppression and opt-out lists checked
[ ] sender identity and business contact details present
[ ] privacy information linked
[ ] simple free objection route in the message
[ ] no deceptive subject or invented personalisation
[ ] factual observations have evidence URLs
[ ] exact recipient reviewed
[ ] exact message reviewed
[ ] sending domain authentication tested
```

The checklist is a block, not a legal certification. `SendApproval` stores the
decision and exact message hash; it does not replace counsel, controller
documentation, or provider obligations.

## Internal suppression rule

An opt-out must stop future outreach and be retained only as needed to prevent
re-contact. A suppression record must not be repurposed for another marketing
purpose. The period and implementation must be reviewed for the specific
setup; the repository’s 90-day sequence rule is only an internal operating
limit, not a legal retention rule.

## Minimal transparent footer draft

Have the concrete wording reviewed before use:

```text
You are receiving this message because I believe this may be relevant to your
professional role at [Company]. I used publicly available business information
to identify the fit.

[Legal business name], [business address], [privacy URL].
To stop future messages, reply “no” or use [objection URL].
```

## Sources and prohibited collection

Use permitted public company sources, official APIs, permitted directories,
inbound/referral data, and sources with documented terms. Do not bypass access
controls, scrape Google Maps or professional platforms outside permitted
interfaces, guess addresses, collect private emails, or gather sensitive data.

This repository does not store a live prospect list, personal contact database,
or sending credentials.
