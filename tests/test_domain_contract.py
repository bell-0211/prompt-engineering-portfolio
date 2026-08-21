import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_domain_contract import validate_pair  # noqa: E402


class DomainContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input_doc = json.loads((ROOT / "examples/domain-agent/sample.input.json").read_text(encoding="utf-8"))
        cls.output_doc = json.loads((ROOT / "examples/domain-agent/sample.output.json").read_text(encoding="utf-8"))

    def test_valid_pair(self):
        self.assertEqual(validate_pair(self.input_doc, self.output_doc), [])

    def test_missing_evidence_reference_is_rejected(self):
        output = copy.deepcopy(self.output_doc)
        output["claims"][0]["evidence_refs"] = ["missing-fact"]
        self.assertTrue(any("missing facts" in error for error in validate_pair(self.input_doc, output)))

    def test_empty_evidence_reference_is_rejected_by_schema(self):
        output = copy.deepcopy(self.output_doc)
        output["claims"][0]["evidence_refs"] = []
        self.assertTrue(any("output schema" in error for error in validate_pair(self.input_doc, output)))

    def test_complete_status_with_open_question_is_rejected(self):
        output = copy.deepcopy(self.output_doc)
        output["open_questions"] = ["Synthetic unresolved conflict"]
        self.assertTrue(any("cannot retain" in error for error in validate_pair(self.input_doc, output)))

    def test_request_id_mismatch_is_rejected(self):
        output = copy.deepcopy(self.output_doc)
        output["request_id"] = "different-request"
        self.assertTrue(any("request_id" in error for error in validate_pair(self.input_doc, output)))


if __name__ == "__main__":
    unittest.main()
