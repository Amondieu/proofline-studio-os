# Verification — run on 2026-09-23 (captured from the live repository)

## `python3 tools/qa_matrix.py --check`
```
checklist items parsed: 16
items without a test row: none
rows referencing unknown tests: none
RESULT: OK
```

## `python3 tools/contrast_check.py demo/direction-switcher.html`
```

[cinematic]
  PASS  17.19:1  --ink-strong on --bg-base (text, needs 4.5:1) — headings and body on page background
  PASS   9.37:1  --ink-muted on --bg-base (text, needs 4.5:1) — muted paragraphs, meta, labels
  PASS   8.76:1  --ink-muted on --card-bg (text, needs 4.5:1) — muted text inside cards
  PASS  16.07:1  --ink-strong on --card-bg (text, needs 4.5:1) — headings inside cards
  PASS    5.0:1  --accent-ink on --accent (text, needs 4.5:1) — button label on primary button
  PASS   3.71:1  --accent on --bg-base (ui, needs 3.0:1) — accent used as BORDER/ICON only — never as body text
  PASS   14.0:1  --signal on --bg-base (ui, needs 3.0:1) — focus ring / signal colour, non-text
  MANUAL  gradients need human verification: --hero-bg

[editorial]
  PASS  15.55:1  --ink-strong on --bg-base (text, needs 4.5:1) — headings and body on page background
  PASS   5.86:1  --ink-muted on --bg-base (text, needs 4.5:1) — muted paragraphs, meta, labels
  PASS   6.17:1  --ink-muted on --card-bg (text, needs 4.5:1) — muted text inside cards
  PASS  16.39:1  --ink-strong on --card-bg (text, needs 4.5:1) — headings inside cards
  PASS   7.39:1  --accent-ink on --accent (text, needs 4.5:1) — button label on primary button
  PASS   7.14:1  --accent on --bg-base (ui, needs 3.0:1) — accent used as BORDER/ICON only — never as body text
  PASS   4.03:1  --signal on --bg-base (ui, needs 3.0:1) — focus ring / signal colour, non-text
  MANUAL  gradients need human verification: --hero-bg

TEXT failures: 0
```

## Structural counts
```
pattern cards: 40 · anti-pattern rows: 40
cards unique: True
send-gate conditions: 9
JSON schemas valid: 7
external requests in demo: 0
```
