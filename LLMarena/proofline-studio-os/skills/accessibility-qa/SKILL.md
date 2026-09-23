---
name: accessibility-qa
description: Run the automated and manual accessibility checks for WCAG 2.2 AA and produce a signed accessibility receipt. Use before every launch, after any component or token change, and whenever a11y is questioned.
---
# accessibility-qa

## Inputs
Preview URL · the list of templates/sections · the token set per direction.

## Procedure
1. **Automated pass:** `npx axe <url>` on every template; require 0 critical / 0 serious. Record the exact command, version and date.
2. **Contrast pass:** per direction, verify body ≥4.5:1, large text ≥3:1, UI/focus ≥3:1. Text over imagery needs a scrim.
3. **Keyboard sweep:** Tab order, focus visible, focus never fully obscured by sticky elements/dialogs, Escape closes overlays, no traps, skip link works.
4. **Switcher check:** change design direction by keyboard only — no focus jump, no reload, single announcement.
5. **Forms:** labels, error summary + field errors, no colour-only signalling, success announced, nothing lost on error, target sizes ≥24×24.
6. **Zoom/reflow:** 200% zoom and 320 px width.
7. **Reduced motion:** OS setting on → all non-essential motion gone in all directions.
8. **Screen-reader spot-check** (VoiceOver/NVDA): hero, one form, one dialog, the switcher.
9. **Content checks:** alt text useful or empty-when-decorative, headings hierarchical, link text meaningful, language declared.

## Output
`templates/qa-launch-checklist.md` filled (accessibility section) + an accessibility receipt block for the project README + wording for the public accessibility statement.

## Refusal conditions
- Any critical/serious finding → block the launch. No waivers for contrast, names, focus visibility or keyboard access.
- Anyone asking to claim "certified accessible"/"fully accessible" → refuse the wording (see `docs/06`).
- An overlay widget proposed as the fix → refuse; fix the source.

## Never
Never test on production data or real client form submissions. Never report a pass when the manual layer was skipped — automated tools catch roughly a third of real problems.
