# Laya advisory layer

## Decision

Proofline Studio uses Laya as an optional, advisory-only layer for structured
triage and routing. The integration is implemented in `studio/laya.py`, but it
is disabled by default and does not include model weights. The runtime can be
installed from the pinned `requirements-laya.txt` file when a local operator
wants to run an experiment.

Laya's router exposes structured answers with routing metadata, which makes it
a reasonable fit for a typed recommendation boundary. Its own documentation
also describes meaningful zero-shot, language, and calibration limitations;
therefore Proofline treats every result as an uncalibrated hypothesis until a
separate, labeled evaluation proves otherwise.

References:

- [Laya router API](https://github.com/NandhaKishorM/laya/blob/main/laya/router.py)
- [Laya model and checkpoint notes](https://github.com/NandhaKishorM/laya/blob/main/README.md)
- [Independent evaluation discussion](https://github.com/NandhaKishorM/laya/issues/35)

## Allowed tasks

| Task | Upstream object | Human action after the result |
|---|---|---|
| `prospect_triage` | `ProspectRecord` and `SignalRecord` | Confirm or reject fit before any draft is created. |
| `archetype_fit` | `ClientArchetypeAssessment` | Confirm the archetype during Discovery. |
| `reply_triage` | `ReplyRecord` | Classify, suppress, or respond according to the human-reviewed record. |
| `skill_route` | an internal task brief | Select a suggested wrapper or next step; the operator still owns execution. |
| `qa_review_priority` | `AuditRecord` or QA queue | Prioritize review; never waive a QA or launch gate. |

Laya is forbidden from deciding `SendApproval`, launch approval, legal
approval, client approval, or asset-rights approval. It also never writes to
the prospect list, CRM, Notion, email provider, deployment target, or human
gate ledger.

## Proofline boundary

The flow is deliberately narrow:

```text
evidence-backed record
        |
        v
sanitize -> LayaRequest -> optional Laya adapter -> LayaDecision
                                      |                    |
                                      |                    +--> abstain / human review
                                      +--> no action authority
```

`LayaRequest` requires a task, a named question, and evidence references. The
engine removes obvious secrets and direct contact fields before inference and
records a SHA-256 hash of the sanitized input. A request explicitly marked as
containing sensitive data is rejected instead of being silently cleaned.

`LayaDecision` records the selected option, probabilities, confidence, model,
routing explanation, calibration status, and evidence references. The contract
hard-codes `needs_human_review=true` and `action_authorized=false`. A result
below the configured threshold (currently `0.75`) is an abstention with no
selected option.

`LayaEvaluationRecord` is the only path for turning a recommendation into a
calibration dataset: a human records the correct option, agreement, reviewer,
and calibration bucket. No evaluation record changes a previous decision or
promotes the model automatically.

## Model routing

- English-only inputs may use `english`.
- German, French, or mixed-language inputs should use `multilingual`.
- Explicit typed choice questions use the `typed-decisions` route.
- The selected model and calibration status are always recorded.
- Until a Proofline evaluation says otherwise, calibration is `unknown`.

The adapter always asks Laya for a typed-decision result. This prevents a
free-form model response from being mistaken for a structured approval. Model
selection remains an experiment setting, not a client-facing claim.

## Rollout gates

1. **Implemented:** contracts, sanitizer, adapter, abstention policy, CLI, and
   offline fake-adapter tests are present in this repository.
2. **Offline evaluation:** collect at least 100 representative,
   evidence-backed requests across the allowed tasks. Have a human label each
   one and compare Laya with a deterministic baseline. Track agreement,
   abstention, per-task error, and calibration (for example Brier score or
   expected calibration error).
3. **Restricted pilot:** only if the offline results are acceptable, enable a
   local operator pilot with `calibration_status=uncalibrated` and the same
   human gate. Keep model and language routing observable.
4. **Promotion:** a reviewed change may mark a model calibrated for a specific
   task/language slice. Calibration never removes human review or grants an
   action permission.

The current repository has completed step 1. It intentionally does not claim
that Laya is production-calibrated or ready for autonomous outbound, legal,
client, or launch decisions.

## Operator usage

Install the normal studio dependencies first. For a local experiment, install
the optional pinned adapter and obtain the upstream checkpoint according to
Laya's instructions:

```powershell
python -m pip install -r requirements.txt
python -m pip install -r requirements-laya.txt
python -m studio laya-run path/to/laya-request.json --abstain-below 0.75
```

The command prints a versioned `LayaDecision` JSON record. The operator must
store it with the relevant evidence and later add a human evaluation record;
printing a recommendation is not a send, launch, or approval operation.
