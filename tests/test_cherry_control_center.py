import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "config/studio/cherry-control-center.v1.json"


class CherryControlCenterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_manifest_is_internal_and_proofline_authoritative(self) -> None:
        self.assertEqual("studio.cherry-control-center.v1", self.manifest["schemaVersion"])
        self.assertEqual("internal_desktop_control_plane", self.manifest["mode"])
        self.assertEqual("proofline", self.manifest["authority"])
        self.assertFalse(self.manifest["enabledByDefault"])
        self.assertFalse(self.manifest["security"]["actionAuthorized"])

    def test_all_least_privilege_profiles_exist(self) -> None:
        self.assertEqual(
            {"research", "creative", "build", "qa", "launch_readonly"},
            set(self.manifest["profiles"]),
        )
        for profile in self.manifest["profiles"].values():
            self.assertTrue(profile["allowedActions"] or profile["forbiddenActions"])

    def test_consequential_authority_is_forbidden(self) -> None:
        forbidden = set(self.manifest["forbiddenOperations"])
        for operation in (
            "launch_approval",
            "legal_approval",
            "rights_approval",
            "client_approval",
            "production_deploy",
            "credentials_export",
        ):
            self.assertIn(operation, forbidden)
        self.assertTrue(self.manifest["security"]["requireHumanReview"])

    def test_external_runtimes_are_not_misrepresented_as_native(self) -> None:
        self.assertEqual("adapter_required", self.manifest["externalRuntimeStatus"]["codex"])
        self.assertEqual("adapter_required", self.manifest["externalRuntimeStatus"]["hermes"])
        modules = {module["id"]: module for module in self.manifest["modules"]}
        self.assertEqual("adapter_required", modules["codex"]["status"])
        self.assertEqual("adapter_required", modules["hermes"]["status"])

    def test_architecture_and_spec_keep_installation_deferred(self) -> None:
        architecture = (ROOT / "docs/architecture/CHERRY-STUDIO-CONTROL-CENTER.md").read_text(encoding="utf-8")
        spec = (ROOT / "specs/140-cherry-control-center-v1/spec.md").read_text(encoding="utf-8")
        self.assertIn("internal desktop control plane", architecture.lower())
        self.assertIn("Proofline", architecture)
        self.assertIn("does not install", spec)


if __name__ == "__main__":
    unittest.main()
