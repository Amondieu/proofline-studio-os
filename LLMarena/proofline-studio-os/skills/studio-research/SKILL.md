---
name: studio-research
description: Research a tool, library, vendor, font, image source or AI service for commercial studio use and produce an evidence-backed adoption decision. Use when anyone says "can we use X", "find a tool for Y", "is this licence OK", or before adding any dependency to a client project.
---
# studio-research

## When to use
Any new dependency, vendor, asset source, AI service or font. Any doubt about a licence.

## Inputs
Resource URL(s) or name · the layer it belongs to (see MASTER-REPORT.md §2) · the project it is for.

## Procedure
1. **Identify the licence from the source of truth**, not from a blog post: `LICENSE`/`LICENSE.md` file, package registry metadata (`npm view <pkg> license`), vendor terms page. Record the exact URL you read.
2. **Collect maintenance evidence:** last commit/release date, release cadence, open issues trend, whether it is archived or a fork, who maintains it and whether that entity was recently acquired. Use the GitHub API, never memory.
3. **Check the four risk axes:** dependency weight (install size + transitive deps), security posture (npm audit / advisories), accessibility maturity (does it claim and test a11y?), performance cost (runtime JS, layout work).
4. **Score it** with the Studio Readiness Score in `research/score_resources.py` (10 axes, weighted). Add a row to `research/resource-inventory.csv` and `research/license-register.csv`.
5. **Test integration cost honestly:** >2 hours of integration without a measurable delivery benefit = reject.
6. **Write the decision** as ADOPT / ADAPT / REFERENCE / AVOID / BUILD, with the boundaries ("we use it for X, never for Y").

## Output
A completed row in both CSVs + a 5-line summary: decision, licence, maintenance signal, main risk, integration note. Plus a POC entry in `research/poc-backlog.md` if anything is unverified.

## Refusal conditions (stop and escalate to the human)
- Licence missing, ambiguous, "free for personal use", or a custom licence that changed after acquisition.
- Inputs would be used for model training and client material is involved.
- The resource is a visual clone of a recognisable brand.
- Integration would require >2 h without a measurable benefit.

## Never
Never recommend something because of stars, a demo, or social attention. Never state "GDPR compliant", "accessible" or "production-ready" without evidence. Never copy code before the licence row exists.
