# Prompt Library — Higgsfield: Hero Concept Exploration
<!-- v0.1 · owner: founder · NEVER paste client assets, client names, or unreleased product shots. Private workspace only. -->
## Preconditions (all must be true)
- [ ] No client material in the prompt or as input.
- [ ] The output will be reviewed by a human and may be rejected.
- [ ] The asset, if used, gets an `asset-provenance-log.csv` row and (where required) an `ai-asset-approval.md`.
- [ ] Never generate realistic humans for client work (default: off). Abstract, object, texture, environment only.

## Template — abstract hero plate (Precision direction)
> Abstract technical composition for a B2B software landing hero. Flat, quiet, high-contrast on warm off-white (#F7F6F3). Geometric modular grid fragments, thin graphite lines (#14161A), a single electric-blue element (#1B5CFF) as the only saturated accent. No text, no logos, no people, no faces. Studio-lit, matte, editorial restraint. Wide 16:9, generous negative space on the left for a headline overlay.

## Template — cinematic environment (Cinematic direction)
> Cinematic architectural interior, near-black (#0B0B0C) with warm ivory highlights (#F4EFE7) and a single deep-red signal accent (#C8332B). Shallow depth of field, film grain, deliberate shadow, one clear focal plane, no text, no logos, no people, no faces. Wide 21:9. The right third must stay dark and calm for text overlay.

## Template — material macro (Editorial direction)
> Macro photograph of a tactile natural material (paper fibre, unglazed ceramic, brushed brass) in bone, sand and deep-olive tones. Soft directional daylight, fine texture visible, quiet and premium, no text, no logos, no hands, no people. 4:5 and 16:9 variants.

## Iteration discipline
1. Generate 6–10 directions in one batch, then stop; more volume does not improve art direction.
2. Select by *fit to the direction brief*, never by "looks impressive".
3. Re-prompt only on one variable at a time (composition, palette, or medium).
4. Reject immediately: text artifacts, faces, brand-like marks, cluttered backgrounds, colours outside the token palette.
5. Export at the final aspect ratio and optimise outside the tool (AVIF/WebP), then log provenance.

## Required record after selection
`asset_id · tool+plan · model · prompt hash · inputs description · client_material_used:false · output class · disclosure required? · reviewer · approval id`
