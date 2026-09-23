# Graph Report - .  (2026-09-23)

## Corpus Check
- Corpus is ~7.206 words - fits in a single context window. You may not need a graph.

## Summary
- 61 nodes · 78 edges · 10 communities detected
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: contains: 33 · uses: 13 · rationale_for: 10 · inherits: 9 · calls: 6 · method: 4 · imports_from: 3


## Input Scope
- Requested: all
- Resolved: all (source: cli)
- Included files: 32 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed
## God Nodes (most connected - your core abstractions)
1. `StudioHarnessTests` - 12 edges
2. `StudioProject` - 9 edges
3. `Contract` - 8 edges
4. `PortablePathError` - 6 edges
5. `evaluate_project()` - 3 edges
6. `DiscoveryBrief` - 3 edges
7. `MessageMap` - 3 edges
8. `DesignDirection` - 3 edges
9. `BuildChecklist` - 3 edges
10. `LaunchReview` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Dependency-light structural checks for the focused studio repo.` --uses--> `StudioProject`  [INFERRED]
  scripts/validate_studio_contracts.py → studio/models.py
- `StudioHarnessTests` --uses--> `BuildChecklist`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py
- `StudioHarnessTests` --uses--> `DesignDirection`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py
- `StudioHarnessTests` --uses--> `DiscoveryBrief`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py
- `StudioHarnessTests` --uses--> `LaunchReview`  [INFERRED]
  tests/test_studio_harness.py → studio/models.py

## Communities

### Community 5 - "Community 5"
Cohesion: 0.40
Nodes (4): root, manifestPath, manifest, normalized

### Community 7 - "Community 7"
Cohesion: 0.67
Nodes (1): Check the focused repo for unsafe absolute project references.

### Community 6 - "Community 6"
Cohesion: 0.67
Nodes (3): _load(), validate(), Dependency-light structural checks for the focused studio repo.

### Community 0 - "Community 0"
Cohesion: 0.20
Nodes (8): directionData, buttons, stageLabel, previewEyebrow, previewTitle, previewBody, directionCta, artDirection

### Community 1 - "Community 1"
Cohesion: 0.27
Nodes (8): Proofline Studio's human-governed delivery harness., _result(), evaluate_project(), record_human_gate(), Read-only gate evaluation and explicit human gate recording.  The evaluator is i, Return a deterministic, non-authoritative project readiness report., Append one explicit human decision to a hash-chained local ledger., StudioProject

### Community 8 - "Community 8"
Cohesion: 0.67
Nodes (1): Operator CLI for the read-only studio harness.

### Community 2 - "Community 2"
Cohesion: 0.36
Nodes (8): Contract, BaseModel, DiscoveryBrief, MessageMap, DesignDirection, BuildChecklist, LaunchReview, Versioned, provider-neutral contracts for a landing-page project.

### Community 9 - "Community 9"
Cohesion: 1.00
Nodes (2): Stage, StrEnum

### Community 3 - "Community 3"
Cohesion: 0.43
Nodes (6): PortablePathError, ValueError, normalize_relative_path(), safe_project_path(), Cross-platform project-relative reference rules., Raised when a contract reference is not portable or project-bounded.

### Community 4 - "Community 4"
Cohesion: 0.33
Nodes (2): make_project(), StudioHarnessTests

## Knowledge Gaps
- **16 isolated node(s):** `root`, `manifestPath`, `manifest`, `normalized`, `Check the focused repo for unsafe absolute project references.` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 7`** (1 nodes): `Check the focused repo for unsafe absolute project references.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 8`** (1 nodes): `Operator CLI for the read-only studio harness.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 9`** (2 nodes): `Stage`, `StrEnum`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 4`** (2 nodes): `make_project()`, `StudioHarnessTests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `StudioHarnessTests` connect `Community 4` to `Community 2`, `Community 1`, `Community 3`?**
  _High betweenness centrality (0.251) - this node is a cross-community bridge._
- **Why does `StudioProject` connect `Community 1` to `Community 6`, `Community 8`, `Community 2`, `Community 4`?**
  _High betweenness centrality (0.249) - this node is a cross-community bridge._
- **Why does `PortablePathError` connect `Community 3` to `Community 4`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `StudioHarnessTests` (e.g. with `BuildChecklist` and `DesignDirection`) actually correct?**
  _`StudioHarnessTests` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `StudioProject` (e.g. with `Dependency-light structural checks for the focused studio repo.` and `Operator CLI for the read-only studio harness.`) actually correct?**
  _`StudioProject` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `root`, `manifestPath`, `manifest` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._