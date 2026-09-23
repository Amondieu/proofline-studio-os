"""Versioned, provider-neutral contracts for a landing-page project."""

from __future__ import annotations

from datetime import date, datetime
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class Stage(StrEnum):
    discovery = "discovery"
    message = "message"
    direction = "direction"
    build = "build"
    qa = "qa"
    launch = "launch"


class DiscoveryBrief(Contract):
    company_name: str = Field(min_length=2, max_length=160)
    website_url: str | None = None
    market: str = Field(min_length=2, max_length=160)
    offer: str = Field(min_length=10, max_length=1000)
    average_order_value: str = Field(min_length=1, max_length=160)
    target_buyer: str = Field(min_length=10, max_length=1000)
    buying_situation: str = Field(min_length=10, max_length=1000)
    expensive_problem: str = Field(min_length=10, max_length=1000)
    current_alternatives: list[str] = Field(min_length=1, max_length=8)
    buyer_hesitations: list[str] = Field(min_length=1, max_length=8)
    primary_conversion: str = Field(min_length=3, max_length=120)
    secondary_conversion: str | None = None
    current_traffic: str | None = None
    current_conversion_rate: str | None = None
    existing_tools: list[str] = Field(default_factory=list, max_length=20)
    proof: list[str] = Field(default_factory=list, max_length=20)
    brand_assets: list[str] = Field(default_factory=list, max_length=30)
    tone_of_voice: list[str] = Field(min_length=1, max_length=8)
    legal_constraints: list[str] = Field(default_factory=list, max_length=20)
    assumption_map: list[str] = Field(default_factory=list, max_length=30)


class MessageMap(Contract):
    target_audience: str = Field(min_length=10, max_length=1000)
    primary_job_to_be_done: str = Field(min_length=10, max_length=1000)
    core_pain: str = Field(min_length=10, max_length=1000)
    desired_outcome: str = Field(min_length=10, max_length=1000)
    mechanism: str = Field(min_length=10, max_length=1000)
    primary_promise: str = Field(min_length=10, max_length=1000)
    primary_cta: str = Field(min_length=3, max_length=120)
    proof: list[str] = Field(default_factory=list, max_length=20)
    top_objections: list[str] = Field(min_length=3, max_length=8)
    required_sections: list[str] = Field(min_length=6, max_length=14)
    assumptions_to_confirm: list[str] = Field(default_factory=list, max_length=30)
    client_signoff: bool = False
    signed_off_by: str | None = None
    signed_off_at: datetime | None = None


class DesignDirection(Contract):
    direction_id: Literal["precision", "cinematic", "editorial"]
    label: str = Field(min_length=3, max_length=100)
    intended_audience: str = Field(min_length=10, max_length=300)
    visual_principle: str = Field(min_length=10, max_length=600)
    palette: list[str] = Field(min_length=3, max_length=12)
    typography: list[str] = Field(min_length=2, max_length=8)
    motion_principle: str = Field(min_length=10, max_length=300)
    desktop_asset_ref: str | None = None
    mobile_asset_ref: str | None = None
    mobile_preview_reviewed: bool = False
    selected_by_client: bool = False
    selected_by: str | None = None
    selected_at: datetime | None = None


class BuildChecklist(Contract):
    responsive_viewports: list[Literal["360", "390", "768", "1024", "1440"]] = Field(default_factory=list)
    navigation_works: bool = False
    ctas_route_correctly: bool = False
    form_validation_works: bool = False
    form_delivery_tested: bool = False
    calendar_or_secondary_flow_tested: bool = False
    metadata_present: bool = False
    open_graph_present: bool = False
    alt_text_reviewed: bool = False
    privacy_and_legal_links_present: bool = False
    analytics_consent_configured: bool = False
    assets_rights_confirmed: bool = False
    no_fabricated_claims: bool = False
    client_admin_access_ready: bool = False
    backup_export_supplied: bool = False


class AIAssetDetails(Contract):
    tool: str = Field(min_length=2, max_length=160)
    model: str = Field(min_length=1, max_length=160)
    inputs_description: str = Field(min_length=10, max_length=1000)
    client_material_used: Literal[False] = False
    real_likeness_used: Literal[False] = False
    prompt_hash: str | None = None
    approval_record_id: str | None = None
    disclosure_required: bool
    vendor_training_on_inputs: bool


class AssetRecord(Contract):
    """Traceable asset rights record; AI client material is rejected by contract."""

    schema_version: Literal["studio.asset-record.v1"] = "studio.asset-record.v1"
    asset_id: str = Field(pattern=r"^A-[0-9]{4,}$")
    project_id: str = Field(pattern=r"^studio_[a-z0-9_-]{4,80}$")
    filename: str | None = None
    source_type: Literal["own", "client", "stock_free", "stock_paid", "ai_generated", "commissioned"]
    source_url: str | None = None
    licence: str = Field(min_length=2, max_length=240)
    licence_file_path: str | None = None
    date: date
    creator_or_vendor: str = Field(min_length=2, max_length=240)
    model_release: bool | None = None
    ai: AIAssetDetails | None = None
    human_reviewer: str = Field(min_length=2, max_length=160)
    allowed_uses: list[str] = Field(min_length=1, max_length=20)
    restrictions: list[str] = Field(default_factory=list, max_length=20)
    removed_on: date | None = None


class ApprovalGate(StrEnum):
    licence = "licence"
    message = "message"
    direction = "direction"
    accessibility = "accessibility"
    performance = "performance"
    asset_provenance = "asset_provenance"
    ai_asset = "ai_asset"
    ownership = "ownership"
    qa = "qa"
    launch = "launch"
    client_permission = "client_permission"
    testimonial_permission = "testimonial_permission"
    dpa_vendor = "dpa_vendor"


class ApprovalRecord(Contract):
    """Detailed, append-only human approval that supplements the gate hash ledger."""

    schema_version: Literal["studio.approval-record.v1"] = "studio.approval-record.v1"
    approval_id: str = Field(pattern=r"^AP-[0-9]{4,}$")
    gate: ApprovalGate
    subject: str = Field(min_length=2, max_length=500)
    decision: Literal["approved", "rejected", "approved_with_conditions"]
    conditions: list[str] = Field(default_factory=list, max_length=20)
    approver: str = Field(min_length=2, max_length=160)
    date: date
    evidence: list[str] = Field(min_length=1, max_length=30)
    expires_on: date | None = None
    supersedes: str | None = None
    notes: str | None = None


class AccessibilityReceipt(Contract):
    axe_critical: Literal[0] = 0
    axe_serious: Literal[0] = 0
    keyboard_sweep: Literal[True] = True
    focus_not_obscured: Literal[True] = True
    contrast_verified: Literal[True] = True
    target_size_verified: Literal[True] = True
    reduced_motion_verified: Literal[True] = True
    screen_reader_spot_check: bool = False


class PerformanceReceipt(Contract):
    lcp_lab_s: float = Field(ge=0, le=2.5)
    inp_ms: float | None = Field(default=None, ge=0, le=200)
    cls: float = Field(ge=0, le=0.1)
    js_kb: float = Field(ge=0, le=60)
    css_kb: float | None = Field(default=None, ge=0)
    third_party_scripts: int = Field(ge=0, le=1)
    field_data_available: bool = False


class FormReceipt(Contract):
    e2e_test: Literal[True] = True
    error_path_test: Literal[True] = True
    spam_test: Literal[True] = True
    notification_verified: Literal[True] = True


class LegalReceipt(Contract):
    mentions_legales: Literal[True] = True
    privacy_notice: Literal[True] = True
    accessibility_statement: Literal[True] = True
    concept_labels: Literal[True] = True
    counsel_reviewed: bool = False


class OwnershipReceipt(Contract):
    client_verified_access: Literal[True] = True
    accounts: list[str] = Field(default_factory=list, max_length=20)


class RollbackReceipt(Contract):
    rehearsed: Literal[True] = True
    minutes: float = Field(ge=0, le=15)
    restore_proven: Literal[True] = True


class QAWaiver(Contract):
    item: str = Field(min_length=2, max_length=240)
    reason: str = Field(min_length=10, max_length=1000)
    fix_date: date
    approved_by: str = Field(min_length=2, max_length=160)


class QASignOff(Contract):
    founder: str = Field(min_length=2, max_length=160)
    date: date


class QAReceipt(Contract):
    """Human-authored evidence receipt; passing it never grants launch authority."""

    schema_version: Literal["studio.qa-receipt.v1"] = "studio.qa-receipt.v1"
    project_id: str = Field(pattern=r"^studio_[a-z0-9_-]{4,80}$")
    release: str = Field(min_length=1, max_length=120)
    url: str | None = None
    commit: str | None = None
    date: date
    tester: str = Field(min_length=2, max_length=160)
    tool_versions: dict[str, str] = Field(default_factory=dict, max_length=30)
    accessibility: AccessibilityReceipt
    performance: PerformanceReceipt
    forms: FormReceipt
    legal: LegalReceipt
    ownership: OwnershipReceipt
    rollback: RollbackReceipt
    waivers: list[QAWaiver] = Field(default_factory=list, max_length=30)
    sign_off: QASignOff


class LaunchReview(Contract):
    mobile_conversion_pass: bool = False
    technical_pass: bool = False
    trust_pass: bool = False
    legal_pass: bool = False
    reviewer: str | None = None
    client_approval: bool = False
    review_notes: list[str] = Field(default_factory=list, max_length=30)
    reviewed_at: datetime | None = None


class StudioProject(Contract):
    schema_version: Literal["studio.project.v1"] = "studio.project.v1"
    project_id: str = Field(pattern=r"^studio_[a-z0-9_-]{4,80}$")
    client_slug: str = Field(pattern=r"^[a-z0-9][a-z0-9-]{2,60}$")
    current_stage: Stage = Stage.discovery
    discovery: DiscoveryBrief
    message_map: MessageMap | None = None
    design_direction: DesignDirection | None = None
    build: BuildChecklist | None = None
    qa_receipt: QAReceipt | None = None
    launch_review: LaunchReview | None = None
    asset_records: list[AssetRecord] = Field(default_factory=list, max_length=500)
    approvals: list[ApprovalRecord] = Field(default_factory=list, max_length=200)
