# 09 — Launch QA (cannot-launch-until checklist)
<!-- v0.1 · 2026-09-23 · owner: agent drafts, founder signs · attach to templates/qa-launch-checklist.md as a receipt -->

## A. Cannot launch until passed (no waiver possible)
- [ ] axe: **0 critical, 0 serious** findings on every template
- [ ] Keyboard sweep passed on home + form + legal pages (focus visible, never fully obscured, no traps)
- [ ] Contrast verified per design direction (body ≥4.5:1, large ≥3:1, UI/focus ≥3:1)
- [ ] Target size ≥24×24 CSS px for all interactive controls (incl. switcher, footer links)
- [ ] Reduced-motion path verified (OS setting on, all three directions)
- [ ] Form end-to-end test passed (submit → record → notification → confirmation → GDPR-conform storage)
- [ ] Spam protection active (honeypot + Turnstile) and tested with a scripted attempt
- [ ] Privacy notice + mentions légales published and accurate (client data filled in, not placeholders) ⚖️
- [ ] Concept-work labels render on every concept asset ("Studio Concept — independent demonstration, not client work")
- [ ] No fabricated proof anywhere (no logos, quotes, metrics, team photos without permission records)
- [ ] Client owns repo, hosting, domain, analytics (verified by the client logging in themselves)
- [ ] Rollback rehearsed once and timed (<15 min)
- [ ] Backups exist and a restore has been proven (not just configured)
- [ ] Accessibility statement published with method + date

## B. Must pass or a written waiver is required
- [ ] Lighthouse mobile: perf ≥95, LCP ≤2.0 s, TBT ≤200 ms
- [ ] Field/lab CLS ≤0.05, JS ≤60 KB, fonts ≤2 families
- [ ] One third-party script maximum (analytics) — each extra one justified in writing
- [ ] Metadata: title/description/OG/canonical/sitemap/robots correct; Rich Results Test clean
- [ ] No review/AggregateRating markup for our own business (Google self-serving review rule)
- [ ] 404 page, redirects from the old site (if any), and links checked
- [ ] Analytics events fire once per action (no duplicates), and the taxonomy matches `docs/07` of the measurement plan

## C. Manual checks most teams skip
- [ ] Longest German/French word in the nav does not break the layout
- [ ] Zoom 200% + 320 px width: no horizontal scroll
- [ ] Form error state tested with a real broken submission (empty, invalid, honeypot-tripped)
- [ ] Email notification tested on a *different* domain than sender (deliverability reality)
- [ ] Timezone in booking confirmations correct for the client's audience
- [ ] Legal pages reachable from every page footer and not hidden behind a "more" menu
- [ ] Contrast of focus ring on the darkest and lightest token pair per direction

## D. Release procedure
1. Merge to `main` only via PR with a green `npm run gate`.
2. Deploy to the preview URL → run QA receipt → founder signs.
3. Promote to production; tag the release (`v1.0.0`); write the launch receipt into the project repo.
4. Day-7 field check; if the budget regresses, the next change is a single fix, not a redesign.
