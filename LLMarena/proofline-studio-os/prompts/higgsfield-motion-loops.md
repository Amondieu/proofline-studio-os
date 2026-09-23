# Prompt Library — Higgsfield: Short Motion Loops
<!-- v0.1 · owner: founder · Rung 4 of the Motion Escalation Ladder: only where a loop earns its ≥1 MB of budget. -->
## Budget gate before you generate anything
- [ ] The loop replaces something heavier (a 6-image sequence, a 3D scene) **or** carries a real product/film asset.
- [ ] ≤ 6 s, muted, no audio track, poster image planned, `preload="none"`.
- [ ] Target ≤ 2.5 MB; if the loop cannot get under that, it does not ship on mobile.
- [ ] Reduced-motion path: static poster only.
- [ ] No client assets, no client names, no real people.

## Template — abstract background loop (Precision / Editorial)
> Very slow, seamless 6-second abstract loop. Minimal geometric form or soft light sweep across a textured surface in warm off-white / bone tones with one restrained accent. Camera static, no cuts, no text, no logos, no people, no faces. Subtle, near-imperceptible movement suitable as a page background behind text.

## Template — cinematic establishing loop (Cinematic)
> 5-second cinematic establishing shot, near-black interior, single warm ivory light source, slow dolly of a few centimetres only, dust visible in the beam, film grain, no people, no text, no logos. Loopable beginning/end, dark right third for overlay text.

## Post-processing (mandatory before it enters the repo)
1. Trim to ≤6 s and loop-clean; strip audio.
2. Encode H.264 MP4 + WebM/AV1; target ≤2.5 MB total; create a poster frame.
3. Add `poster`, `muted`, `playsinline`, `loop`, `preload="none"`, `autoplay` **only** if above the fold and under 1.5 MB.
4. Under `prefers-reduced-motion: reduce` → poster only (no JS fallback needed).
5. Measure: INP during scroll with the loop playing + LCP unchanged (±100 ms).
6. Log provenance + run the AI asset approval record.
