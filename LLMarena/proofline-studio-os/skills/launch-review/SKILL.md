---
name: launch-review
description: Perform the final go/no-go review before production: verify every gate, assemble the launch receipt, rehearse rollback and confirm client ownership. Use on the launch day of every project.
---
# launch-review

## Inputs
Preview build with a green `npm run gate` · completed QA receipts (accessibility, performance) · legal page content from the client · account/ownership plan.

## Procedure
1. **Gate audit:** walk `docs/09` section A (cannot-launch list). Any single red item = no launch, full stop.
2. **Proof audit:** no fabricated proof, every concept asset labelled, every quote/metric has a permission or substantiation record.
3. **Legal page audit:** mentions légales complete with the client's real entity data, privacy notice matching the actual data flows, accessibility statement dated, cookie/analytics behaviour matching the documented decision. ⚖️ (counsel review flagged where required)
4. **Form audit:** end-to-end test (submission → record → notification → confirmation), spam attempt blocked, notification reaches a *different* domain, error path tested.
5. **Rollback rehearsal:** deploy the previous version once, time it (<15 min), then restore. Record both timings.
6. **Ownership check:** client logs into repo, hosting, domain, analytics *themselves* while we watch.
7. **Launch receipt:** write the single artefact containing gates, numbers, dates, waivers, ownership status, and the first post-launch check dates (day 7/30/90).
8. **Announce only what we can evidence** — no compliance claims, no conversion promises.

## Output
Signed launch receipt in the project repo + go/no-go decision + scheduled post-launch checks.

## Refusal conditions
- Any cannot-launch item unresolved.
- Client cannot access their own accounts.
- Rollback untested.
- A public claim without substantiation.

## Never
Never launch on a Friday afternoon without a rollback rehearsal and a documented owner for the weekend. Never let "we'll fix it after launch" apply to accessibility, legal pages, or the form path.
