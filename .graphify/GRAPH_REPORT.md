# Graph Report - .  (2026-09-23)

## Corpus Check
- 181 files · ~130.090 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 270 nodes · 562 edges · 13 communities detected
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 121 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: contains: 128 · uses: 121 · MODIFIES: 69 · inherits: 61 · calls: 48 · method: 44 · rationale_for: 41 · ON_BRANCH: 21 · PARENT_OF: 19 · imports_from: 10


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 181 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `b04412d`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Contract` - 80 edges
2. `StudioHarnessTests` - 23 edges
3. `LayaAdvisoryTests` - 16 edges
4. `FakeLayaAdapter` - 13 edges
5. `StudioProject` - 11 edges
6. `LayaAdvisoryEngine` - 10 edges
7. `OutboundContractTests` - 9 edges
8. `LayaRequest` - 8 edges
9. `LayaDecision` - 8 edges
10. `ArchetypeTemplateEvaluation` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Dependency-light structural checks for the focused studio repo.` --uses--> `StudioProject`  [INFERRED]
  scripts/validate_studio_contracts.py → studio/models.py
- `Dependency-light structural checks for the focused studio repo.` --uses--> `ArchetypeTemplateEvaluation`  [INFERRED]
  scripts/validate_studio_contracts.py → studio/quality_research.py
- `StudioHarnessTests` --uses--> `StudioProject`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py
- `StudioHarnessTests` --uses--> `PortablePathError`  [INFERRED]
  tests/test_studio_harness.py → studio/portability.py
- `Contracts for the evidence-backed pattern and anti-pattern cookbook.` --uses--> `Contract`  [INFERRED]
  studio/cookbook.py → studio/models.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (27): RuntimeError, Operator CLI for the read-only studio harness., CalibrationStatus, LayaAdvisoryEngine, LayaDecision, LayaEvaluationRecord, LayaModel, LayaPackageAdapter (+19 more)

### Community 1 - "Community 1"
Cohesion: 0.08
Nodes (29): main, 140ed8b feat: adopt research receipts and QA gate, 7bc151b chore: ignore local graphify lifecycle state, cb77a61 feat: create focused landing studio foundation, 140ed8b feat: adopt research receipts and QA gate, 7bc151b chore: ignore local graphify lifecycle state, 80a73c6 chore: separate Graphify profile and code refresh, cb77a61 feat: create focused landing studio foundation (+21 more)

### Community 2 - "Community 2"
Cohesion: 0.10
Nodes (32): BaseModel, Business-archetype contracts and deterministic recommendation helpers., Return a recommendation and confidence without confirming fit or approval., AccessibilityReceipt, AIAssetDetails, ApprovalRecord, ArchetypeRecord, ArchetypeScore (+24 more)

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (19): Contract, AuditFinding, AuditRecord, calculate_prospect_score(), ConversionLeak, OutreachDraft, OutreachState, ProfessionalContact (+11 more)

### Community 4 - "Community 4"
Cohesion: 0.16
Nodes (17): main, 0ecf304 feat: integrate NewLLM prospecting and quality loop, 13df31c feat: add human-gated outbound intelligence module, 142dc46 docs: specify Notion portal and Canva templates, 57970cd feat: add business archetype systems, 5e1626a feat: formalize spec-driven archetype evaluation, 7bf1318 docs: define Notion and Canva integration boundary, 80a73c6 chore: separate Graphify profile and code refresh (+9 more)

### Community 5 - "Community 5"
Cohesion: 0.13
Nodes (18): b89c46f feat: add evidence-backed pattern cookbook, StrEnum, AntiPatternRecord, AntiPatternSeverity, calculate_pattern_readiness(), EvidenceLevel, EvidenceRef, ExperimentRecord (+10 more)

### Community 6 - "Community 6"
Cohesion: 0.16
Nodes (15): 30d83c1 feat: add first archetype readiness audit, b04412d docs: record Austria business readiness gate, ReadinessAuditTests, build_audit(), _catalog(), Category, Check, _contains() (+7 more)

### Community 7 - "Community 7"
Cohesion: 0.13
Nodes (11): ArchetypeTemplateEvaluation, QualityEvidenceLevel, QualityReuseDecision, QualitySourceClass, QualitySourceRecord, Contracts for archetype quality intelligence and template evaluation., A source that can inform a rule without silently becoming a rule., Human-reviewed evaluation; ``gold_candidate`` is never self-approving. (+3 more)

### Community 8 - "Community 8"
Cohesion: 0.20
Nodes (8): artDirection, buttons, directionCta, directionData, previewBody, previewEyebrow, previewTitle, stageLabel

### Community 9 - "Community 9"
Cohesion: 0.73
Nodes (5): audit(), luminance(), main(), parse_tokens(), ratio()

### Community 10 - "Community 10"
Cohesion: 0.90
Nodes (4): check(), main(), markdown(), parse_checklist()

### Community 11 - "Community 11"
Cohesion: 0.90
Nodes (4): check(), main(), markdown(), parse_checklist()

### Community 12 - "Community 12"
Cohesion: 0.50
Nodes (3): Protocol, LayaAdapter, Return the upstream Laya result without granting any authority.

## Knowledge Gaps
- **23 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+18 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Contract` connect `Community 2` to `Community 5`, `Community 0`, `Community 12`, `Community 1`, `Community 3`, `Community 7`?**
  _High betweenness centrality (0.480) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 1` to `Community 4`, `Community 0`, `Community 2`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Why does `StudioHarnessTests` connect `Community 2` to `Community 1`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 57 inferred relationships involving `Contract` (e.g. with `AntiPatternRecord` and `AntiPatternSeverity`) actually correct?**
  _`Contract` has 57 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `StudioHarnessTests` (e.g. with `AccessibilityReceipt` and `AIAssetDetails`) actually correct?**
  _`StudioHarnessTests` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `LayaAdvisoryTests` (e.g. with `CalibrationStatus` and `LayaAdvisoryEngine`) actually correct?**
  _`LayaAdvisoryTests` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `root`, `manifestPath`, `manifest` to the rest of the system?**
  _23 weakly-connected nodes found - possible documentation gaps or missing edges._