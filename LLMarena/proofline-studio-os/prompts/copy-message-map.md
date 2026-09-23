# Prompt Library — Message Map Drafting (input for `skills/conversion-copy`)
<!-- v0.1 · owner: founder · output goes into templates/message-map.md, never straight to a client -->
## Context block to fill
```
Audience: <ICP + trigger>
Offer (client's words): "
Real evidence available: <list>
Competitors/alternatives the visitor considers:
Constraints: <regulated sector? claim limits? language?>
Direction: precision | cinematic | editorial
Page type: <landing | service | teardown report | proposal>
```
## Instruction
1. Write the offer in one sentence (who + outcome + mechanism + constraint). If you cannot, list exactly what information is missing instead of inventing it.
2. Produce the claim table: for every section in the fixed order, give a claim of ≤12 words, exactly one evidence type, a one-sentence mechanism, and a next step.
3. Mark every claim you could not substantiate with `[NEEDS EVIDENCE]` — do not soften it into a vague benefit.
4. List the top 5 objections in the audience's own language and the answer in ≤25 words.
5. List every claim you deleted because it was unverifiable, and why.
6. Do not use: revolutionary, world-class, cutting-edge, best-in-class, guaranteed, trusted by, as seen in, limitless, unleash.
## Output format
The filled `message-map.md` sections + a "NEEDS EVIDENCE" list + a banned-claim audit table.
## Hard refusals
Fabricated testimonials, logos, metrics, awards, client names, or any guarantee of results/rankings/compliance.
