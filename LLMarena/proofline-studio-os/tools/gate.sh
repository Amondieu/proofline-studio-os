#!/usr/bin/env bash
# Proofline gate — placeholder to be implemented on day 4 of the 14-day plan.
# Order matters: cheap checks first, expensive last.
set -euo pipefail
echo "1/5 lint + typecheck"
# npm run lint && npx astro check
echo "2/5 build"
# npm run build
echo "3/5 start preview + axe (must be 0 critical / 0 serious)"
# npx start-server-and-test preview http://localhost:4321 "npx @axe-core/cli http://localhost:4321 --exit"
echo "4/5 Lighthouse budgets (perf >= 95, LCP <= 2.0s, TBT <= 200ms)"
# npx lhci autorun
echo "5/5 Playwright smoke (navigation, form submit, keyboard path, mobile viewport)"
# npx playwright test
echo "GATE COMPLETE — attach the output to templates/qa-launch-checklist.md"
