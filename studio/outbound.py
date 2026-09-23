"""Human-gated outbound intelligence contracts for Proofline Studio."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import Field, model_validator

from .models import Contract


class ProfessionalContact(Contract):
    name: str | None = None
    role: str = Field(min_length=2, max_length=160)
    professional_email: str = Field(min_length=5, max_length=320)
    source_url: str = Field(min_length=8, max_length=1000)


class SourceRecord(Contract):
    source_type: Literal[
        "public_company_website",
        "public_news",
        "public_company_social",
        "public_job_page",
        "permitted_directory",
        "official_register",
        "official_api",
        "inbound_or_referral",
    ]
    url: str = Field(min_length=8, max_length=1000)
    collected_on: date
    terms_reviewed: bool = False
    notes: str | None = None


class SignalRecord(Contract):
    schema_version: Literal["studio.signal-record.v1"] = "studio.signal-record.v1"
    signal_id: str = Field(pattern=r"^sig_[a-z0-9_-]{4,80}$")
    signal_type: str = Field(min_length=3, max_length=160)
    evidence_url: str = Field(min_length=8, max_length=1000)
    observed_on: date
    confidence: Literal["low", "medium", "high"]
    observation: str = Field(min_length=10, max_length=1000)


class ConversionLeak(Contract):
    category: Literal["hero_clarity", "cta", "proof", "mobile", "form", "trust", "performance", "other"]
    observation: str = Field(min_length=10, max_length=1000)
    evidence_url: str = Field(min_length=8, max_length=1000)
    confidence: Literal["low", "medium", "high"]


class ProspectScore(Contract):
    icp_fit: int = Field(ge=0, le=20)
    visible_conversion_leak: int = Field(ge=0, le=20)
    current_trigger: int = Field(ge=0, le=15)
    offer_economics: int = Field(ge=0, le=15)
    decision_maker: int = Field(ge=0, le=10)
    evidence_confidence: int = Field(ge=0, le=10)
    compliance_fit: int = Field(ge=0, le=10)
    total: int = Field(ge=0, le=100)

    @model_validator(mode="after")
    def total_matches_components(self) -> "ProspectScore":
        expected = sum(
            (
                self.icp_fit,
                self.visible_conversion_leak,
                self.current_trigger,
                self.offer_economics,
                self.decision_maker,
                self.evidence_confidence,
                self.compliance_fit,
            )
        )
        if self.total != expected:
            raise ValueError(f"prospect score total must equal components ({expected})")
        return self


class OutreachState(Contract):
    status: Literal[
        "draft_only",
        "pending_human_approval",
        "approved",
        "sent",
        "replied",
        "opted_out",
        "suppressed",
        "closed",
    ] = "draft_only"
    legal_basis: Literal["not_assessed", "legitimate_interest_pending_review", "consent", "not_applicable"] = "not_assessed"
    opt_out_status: Literal["not_contacted", "available", "opted_out", "suppressed"] = "not_contacted"
    send_approved_by: str | None = None
    send_approved_on: date | None = None

    @model_validator(mode="after")
    def sent_requires_approval(self) -> "OutreachState":
        if self.status in {"sent", "replied"} and (not self.send_approved_by or not self.send_approved_on):
            raise ValueError("sent or replied outreach requires a recorded human send approval")
        if self.opt_out_status in {"opted_out", "suppressed"} and self.status not in {"opted_out", "suppressed", "closed"}:
            raise ValueError("opted-out prospects cannot remain sendable")
        return self


class ProspectRecord(Contract):
    schema_version: Literal["studio.prospect-record.v1"] = "studio.prospect-record.v1"
    prospect_id: str = Field(pattern=r"^pr_[0-9]{4}_[0-9]{4,}$")
    company_name: str = Field(min_length=2, max_length=240)
    website_url: str = Field(min_length=8, max_length=1000)
    country: str = Field(min_length=2, max_length=80)
    industry: str = Field(min_length=2, max_length=240)
    archetype_fit: str = Field(min_length=3, max_length=160)
    primary_contact: ProfessionalContact | None = None
    data_source: SourceRecord
    signals: list[SignalRecord] = Field(default_factory=list, max_length=12)
    conversion_leaks: list[ConversionLeak] = Field(default_factory=list, max_length=3)
    score: ProspectScore
    outreach: OutreachState = Field(default_factory=OutreachState)


class AuditFinding(Contract):
    category: Literal["hero_clarity", "cta", "proof", "mobile", "form", "trust", "performance", "other"]
    observation: str = Field(min_length=10, max_length=1000)
    recommendation: str = Field(min_length=10, max_length=1000)
    evidence_url: str = Field(min_length=8, max_length=1000)


class AuditRecord(Contract):
    schema_version: Literal["studio.audit-record.v1"] = "studio.audit-record.v1"
    audit_id: str = Field(pattern=r"^audit_[a-z0-9_-]{4,80}$")
    prospect_id: str = Field(pattern=r"^pr_[0-9]{4}_[0-9]{4,}$")
    findings: list[AuditFinding] = Field(min_length=1, max_length=3)
    suggested_hero: str | None = None
    suggested_conversion_architecture: str | None = None
    status: Literal["draft_only", "human_reviewed", "delivered", "withdrawn"] = "draft_only"
    reviewed_by: str | None = None
    reviewed_on: date | None = None
    human_review_required: Literal[True] = True


class OutreachDraft(Contract):
    schema_version: Literal["studio.outreach-draft.v1"] = "studio.outreach-draft.v1"
    draft_id: str = Field(pattern=r"^draft_[a-z0-9_-]{4,80}$")
    prospect_id: str = Field(pattern=r"^pr_[0-9]{4}_[0-9]{4,}$")
    sequence_step: Literal[1, 2, 3]
    recipient_role: str = Field(min_length=2, max_length=160)
    recipient_email: str = Field(min_length=5, max_length=320)
    subject: str = Field(min_length=3, max_length=240)
    body: str = Field(min_length=20, max_length=12000)
    evidence_urls: list[str] = Field(min_length=1, max_length=8)
    includes_opt_out: Literal[True] = True
    status: Literal["draft_only", "pending_human_approval", "approved", "sent", "blocked"] = "draft_only"
    human_review_required: Literal[True] = True


class SendApproval(Contract):
    schema_version: Literal["studio.send-approval.v1"] = "studio.send-approval.v1"
    approval_id: str = Field(pattern=r"^send_[a-z0-9_-]{4,80}$")
    draft_id: str = Field(pattern=r"^draft_[a-z0-9_-]{4,80}$")
    exact_recipient: str = Field(min_length=5, max_length=320)
    message_sha256: str = Field(pattern=r"^[a-f0-9]{64}$")
    decision: Literal["approved", "rejected"]
    checklist: list[str] = Field(min_length=8, max_length=20)
    approved_by: str = Field(min_length=2, max_length=160)
    approved_on: datetime
    notes: str | None = None


class ReplyRecord(Contract):
    schema_version: Literal["studio.reply-record.v1"] = "studio.reply-record.v1"
    reply_id: str = Field(pattern=r"^reply_[a-z0-9_-]{4,80}$")
    prospect_id: str = Field(pattern=r"^pr_[0-9]{4}_[0-9]{4,}$")
    received_at: datetime
    classification: Literal["positive", "question", "meeting", "negative", "opt_out", "bounce", "no_response", "other"]
    summary: str = Field(min_length=3, max_length=1000)
    next_action: str = Field(min_length=3, max_length=500)
    suppression_applied: bool = False
    human_reviewed_by: str | None = None

    @model_validator(mode="after")
    def opt_out_requires_suppression(self) -> "ReplyRecord":
        if self.classification == "opt_out" and not self.suppression_applied:
            raise ValueError("opt-out replies require suppression_applied=true")
        return self


class SuppressionRecord(Contract):
    """Minimal, append-only suppression evidence; never a campaign target list."""

    schema_version: Literal["studio.suppression-record.v1"] = "studio.suppression-record.v1"
    suppression_id: str = Field(pattern=r"^sup_[a-z0-9_-]{4,80}$")
    identifier: str = Field(min_length=3, max_length=320)
    scope: Literal["person", "domain", "company"]
    suppressed_at: datetime
    reason: Literal["opt_out", "complaint", "manual_add", "bounce_hard", "data_subject_request"]
    source: Literal["reply", "unsubscribe_link", "manual_review", "data_subject_request", "hard_bounce"]
    note: str | None = Field(default=None, max_length=500)
    permanent: bool = True
    expires_on: date | None = None

    @model_validator(mode="after")
    def enforce_suppression_lifetime(self) -> "SuppressionRecord":
        if self.permanent and self.expires_on is not None:
            raise ValueError("permanent suppression records cannot have an expiry date")
        if not self.permanent and self.expires_on is None:
            raise ValueError("temporary suppression records require an expiry date")
        if self.reason in {"opt_out", "complaint", "data_subject_request"} and not self.permanent:
            raise ValueError("objections and data-subject requests require permanent suppression")
        return self


def calculate_prospect_score(**components: int) -> ProspectScore:
    """Calculate the declared score; it never changes outreach state."""

    return ProspectScore(**components, total=sum(components.values()))
