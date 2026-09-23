# 17 — Accessibility patterns

The target is WCAG 2.2 AA practice with automated evidence and human review.
The cookbook must never turn an automated pass into a blanket accessibility
guarantee.

## Interaction baseline

- Semantic landmarks and heading hierarchy.
- Skip link and keyboard-complete navigation.
- Visible focus with no sticky element obscuring the focused control.
- Explicit accessible names for controls and direction-switcher state.
- Persistent form labels, instructions, text errors, and success feedback.
- No keyboard traps; Escape closes dismissible overlays.
- Target-size review and 200% zoom / 320 px reflow review.
- Reduced-motion default and a no-motion comprehension path.
- Meaningful text alternatives for informative media; decorative media ignored.

## Direction switcher protocol

1. Reach all direction controls by keyboard.
2. Activate each with Enter/Space.
3. Confirm focus does not jump and the document does not reload.
4. Announce only the direction name once.
5. Confirm DOM order, copy, CTA destination, and legal content are unchanged.
6. Repeat with reduced motion and narrow viewport.

## Form protocol

Test empty, malformed, invalid, spam, valid, duplicate, and delivery-failure
states. Each error identifies the field in text, does not rely on colour alone,
and preserves recoverable user input where appropriate.
