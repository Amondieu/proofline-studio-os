# Prompt Library — Build Spec Generation
<!-- v0.1 · owner: founder · input: signed message map + direction brief + tokens -->
## Context
```
Project: <slug>  Tier: <starter|authority|launch_system>
Direction + tokens: <path to tokens.json>
Pages/sections: <list, in order>
Integrations: <form endpoint | tally | cal.com | analytics>
```
## Instruction
Produce a build spec with exactly these sections:
1. **Section list**: id, component name, purpose (one line), tokens used, motion rung (0–5), acceptance criteria.
2. **Component inventory**: which allowlisted primitives are needed (`docs/04`), which exist as copy-ins, which must be built. Max 8 copy-ins.
3. **Asset list**: filename, role (hero/section/decoration), source (own/stock/AI/client), required aspect ratio, weight budget, provenance requirement.
4. **Data & integrations**: endpoints, validation rules, spam controls, event names for the analytics taxonomy, failure behaviour.
5. **Accessibility notes per component**: keyboard behaviour, focus handling, announcements, target sizes, contrast pairs.
6. **Performance plan**: what is static, what is hydrated, image strategy, font strategy, third-party count (max 1).
7. **Build order**: a numbered sequence where every step leaves a deployable page.
8. **Gate checklist**: what must be true before each of the seven gates can be signed.
## Refusals
Refuse to spec: unlicensed dependencies, motion beyond the budget, third-party scripts beyond the approved analytics, or any content that cannot be substantiated.
