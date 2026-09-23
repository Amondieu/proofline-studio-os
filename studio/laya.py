"""Optional Laya advisory layer with hard Proofline authority boundaries."""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any, Literal, Protocol

from pydantic import Field, model_validator

from .models import Contract


class LayaTask(StrEnum):
    prospect_triage = "prospect_triage"
    archetype_fit = "archetype_fit"
    reply_triage = "reply_triage"
    skill_route = "skill_route"
    qa_review_priority = "qa_review_priority"


class LayaModel(StrEnum):
    english = "english"
    multilingual = "multilingual"
    typed_decisions = "typed-decisions"


class CalibrationStatus(StrEnum):
    unknown = "unknown"
    uncalibrated = "uncalibrated"
    calibrated = "calibrated"


class LayaRequest(Contract):
    """A sanitized, typed request. It contains no permission to perform an action."""

    schema_version: Literal["studio.laya-request.v1"] = "studio.laya-request.v1"
    request_id: str = Field(pattern=r"^laya_req_[a-z0-9_-]{4,80}$")
    task: LayaTask
    question_id: str = Field(pattern=r"^[a-z][a-z0-9_-]{1,80}$")
    state: dict[str, Any]
    questions: dict[str, dict[str, Any]] = Field(min_length=1, max_length=32)
    language: str | None = Field(default=None, min_length=2, max_length=20)
    requested_model: LayaModel | None = None
    evidence_refs: list[str] = Field(min_length=1, max_length=30)
    contains_sensitive_data: bool = False

    @model_validator(mode="after")
    def requested_question_exists(self) -> "LayaRequest":
        if self.question_id not in self.questions:
            raise ValueError("question_id must refer to a question in questions")
        return self


class LayaDecision(Contract):
    """A recommendation record. It can never authorize a downstream action."""

    schema_version: Literal["studio.laya-decision.v1"] = "studio.laya-decision.v1"
    decision_id: str = Field(pattern=r"^laya_dec_[a-z0-9_-]{4,80}$")
    request_id: str = Field(pattern=r"^laya_req_[a-z0-9_-]{4,80}$")
    task: LayaTask
    model: LayaModel
    provider: str = Field(min_length=2, max_length=120)
    input_sha256: str = Field(pattern=r"^[a-f0-9]{64}$")
    selected_option: str | None = None
    probabilities: dict[str, float] = Field(default_factory=dict, max_length=32)
    confidence: float = Field(ge=0, le=1)
    abstained: bool = False
    abstention_reason: str | None = None
    calibration_status: CalibrationStatus = CalibrationStatus.unknown
    routing_reason: str = Field(min_length=3, max_length=500)
    evidence_refs: list[str] = Field(min_length=1, max_length=30)
    needs_human_review: bool = True
    action_authorized: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @model_validator(mode="after")
    def enforce_advisory_boundary(self) -> "LayaDecision":
        if not self.needs_human_review:
            raise ValueError("Laya decisions always require human review")
        if self.action_authorized:
            raise ValueError("Laya decisions cannot authorize actions")
        if self.abstained and not self.abstention_reason:
            raise ValueError("abstained decisions require a reason")
        if self.abstained and self.selected_option is not None:
            raise ValueError("abstained decisions cannot select an option")
        if not self.abstained and self.abstention_reason is not None:
            raise ValueError("non-abstained decisions cannot have an abstention reason")
        if self.probabilities:
            if any(value < 0 or value > 1 for value in self.probabilities.values()):
                raise ValueError("probabilities must be between 0 and 1")
            total = sum(self.probabilities.values())
            if abs(total - 1.0) > 0.02:
                raise ValueError("probabilities must sum to approximately 1")
        return self


class LayaEvaluationRecord(Contract):
    """Human-labelled feedback used to measure agreement and calibration."""

    schema_version: Literal["studio.laya-evaluation-record.v1"] = "studio.laya-evaluation-record.v1"
    evaluation_id: str = Field(pattern=r"^laya_eval_[a-z0-9_-]{4,80}$")
    decision_id: str = Field(pattern=r"^laya_dec_[a-z0-9_-]{4,80}$")
    human_option: str = Field(min_length=1, max_length=160)
    agrees_with_model: bool
    reviewer: str = Field(min_length=2, max_length=160)
    reviewed_at: datetime
    calibration_bucket: str = Field(min_length=2, max_length=120)
    notes: str | None = None


class LayaAdapter(Protocol):
    provider: str
    model: LayaModel
    calibration_status: CalibrationStatus

    def predict(self, request: LayaRequest) -> dict[str, Any]:
        """Return the upstream Laya result without granting any authority."""


class LayaUnavailableError(RuntimeError):
    """Raised when optional Laya runtime dependencies are not installed."""


class LayaPackageAdapter:
    """Lazy adapter for the optional `laya` package and its Router API."""

    provider = "laya-package"
    calibration_status = CalibrationStatus.unknown

    def __init__(
        self,
        model: LayaModel = LayaModel.english,
        device: str | None = None,
        max_loaded: int = 1,
        preload: bool = False,
    ) -> None:
        try:
            import laya  # type: ignore[import-not-found]
        except ImportError as exc:  # pragma: no cover - depends on optional runtime
            raise LayaUnavailableError(
                "Optional Laya runtime is unavailable. Install requirements-laya.txt and model weights separately."
            ) from exc
        self.model = model
        self._router = laya.Router(
            device=device,
            max_loaded=max_loaded,
            default=model.value,
            preload=preload,
        )

    def predict(self, request: LayaRequest) -> dict[str, Any]:
        return self._router.predict(
            request.state,
            request.questions,
            model=request.requested_model.value if request.requested_model else None,
            task="typed_decisions",
            lang=request.language,
        )


def sanitize_state(state: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    """Remove obvious secrets and direct contact fields before model inference."""

    blocked = {
        "password",
        "token",
        "auth_token",
        "secret",
        "api_key",
        "access_token",
        "refresh_token",
        "professional_email",
        "contact_email",
        "email_address",
        "email",
        "phone",
        "phone_number",
        "contact_phone",
        "telephone",
        "authorization",
        "session_id",
    }
    redacted: list[str] = []

    def walk(value: Any, path: str) -> Any:
        if isinstance(value, dict):
            result: dict[str, Any] = {}
            for key, item in value.items():
                normalized_key = (
                    "".join(("_" + char.lower()) if char.isupper() else char for char in str(key))
                    .lstrip("_")
                    .replace("-", "_")
                )
                if normalized_key in blocked or normalized_key.endswith(("_token", "_secret", "_password", "_api_key")):
                    redacted.append(path + key)
                    continue
                result[key] = walk(item, path + key + ".")
            return result
        if isinstance(value, list):
            return [walk(item, path + "[]") for item in value]
        return value

    return walk(state, ""), redacted


def request_hash(request: LayaRequest, sanitized_state: dict[str, Any]) -> str:
    canonical = json.dumps(
        {
            "request_id": request.request_id,
            "task": request.task.value,
            "question_id": request.question_id,
            "state": sanitized_state,
            "questions": request.questions,
            "language": request.language,
            "requested_model": request.requested_model.value if request.requested_model else None,
        },
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _normalise_answer(answer: dict[str, Any]) -> tuple[str | None, dict[str, float], float]:
    answer_type = answer.get("type")
    if answer_type == "choice":
        return answer.get("choice"), answer.get("probabilities", {}), float(answer.get("confidence", 0))
    if answer_type == "noul":
        probability = float(answer.get("noul", 0))
        return ("true" if probability >= 0.5 else "false"), {"true": probability, "false": 1 - probability}, float(answer.get("confidence", 0))
    if answer_type == "score":
        return None, answer.get("probabilities", {}), float(answer.get("confidence", 0))
    raise ValueError("unsupported Laya answer type")


class LayaAdvisoryEngine:
    """Runs Laya only for allowlisted advisory tasks and abstains conservatively."""

    def __init__(self, adapter: LayaAdapter, abstain_below: float = 0.75) -> None:
        if not 0 <= abstain_below <= 1:
            raise ValueError("abstain_below must be between 0 and 1")
        self.adapter = adapter
        self.abstain_below = abstain_below

    def advise(self, request: LayaRequest) -> LayaDecision:
        sanitized, redacted = sanitize_state(request.state)
        if request.contains_sensitive_data:
            raise ValueError("Laya advisory requests must not be marked as containing sensitive data")
        safe_request = request.model_copy(update={"state": sanitized})
        raw = self.adapter.predict(safe_request)
        answers = raw.get("answers", {})
        if request.question_id not in answers:
            raise ValueError(f"Laya result did not contain question {request.question_id!r}")
        selected, probabilities, confidence = _normalise_answer(answers[request.question_id])
        abstained = confidence < self.abstain_below
        reason = "confidence below Proofline abstention threshold" if abstained else "advisory result requires human review"
        if redacted:
            reason += "; sensitive fields were redacted before inference"
        provider_model = raw.get("routing", {}).get("model") or getattr(self.adapter, "model", LayaModel.english).value
        model = LayaModel(provider_model) if provider_model in {item.value for item in LayaModel} else getattr(self.adapter, "model", LayaModel.english)
        return LayaDecision(
            decision_id="laya_dec_" + request.request_id.removeprefix("laya_req_"),
            request_id=request.request_id,
            task=request.task,
            model=model,
            provider=self.adapter.provider,
            input_sha256=request_hash(request, sanitized),
            selected_option=None if abstained else selected,
            probabilities={str(key): float(value) for key, value in probabilities.items()},
            confidence=confidence,
            abstained=abstained,
            abstention_reason=reason if abstained else None,
            calibration_status=self.adapter.calibration_status,
            routing_reason=str(raw.get("routing", {}).get("reason", "explicit Proofline advisory task")),
            evidence_refs=request.evidence_refs,
        )
