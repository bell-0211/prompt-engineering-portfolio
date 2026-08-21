import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from aggregate_results import release_decision  # noqa: E402


class ReleaseGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rubric = json.loads(
            (ROOT / "examples" / "evaluation" / "rubric.json").read_text(encoding="utf-8")
        )
        cases = json.loads(
            (ROOT / "examples" / "evaluation" / "test-cases.json").read_text(encoding="utf-8")
        )
        cls.case_ids = {case["id"] for case in cases["cases"]}
        cls.dimension_ids = [item["id"] for item in cls.rubric["dimensions"]]

    def result(self, case_id, severity="P2", passed=True, score=4):
        return {
            "case_id": case_id,
            "severity": severity,
            "passed": passed,
            "scores": {dimension: score for dimension in self.dimension_ids},
        }

    def test_p0_failure_blocks_high_average(self):
        results = [self.result(case_id) for case_id in sorted(self.case_ids)]
        results[0] = self.result(results[0]["case_id"], severity="P0", passed=False, score=4)
        decision = release_decision({"results": results}, self.rubric, self.case_ids)
        self.assertEqual(decision["weighted_score"], 100.0)
        self.assertEqual(decision["decision"], "blocked")
        self.assertEqual(len(decision["critical_failures"]), 1)

    def test_missing_case_blocks_release(self):
        selected = sorted(self.case_ids)[:-1]
        results = [self.result(case_id) for case_id in selected]
        decision = release_decision({"results": results}, self.rubric, self.case_ids)
        self.assertEqual(decision["decision"], "blocked")
        self.assertEqual(len(decision["missing_cases"]), 1)

    def test_complete_clean_run_passes(self):
        results = [self.result(case_id) for case_id in sorted(self.case_ids)]
        decision = release_decision({"results": results}, self.rubric, self.case_ids)
        self.assertEqual(decision["decision"], "pass")
        self.assertEqual(decision["weighted_score"], 100.0)


if __name__ == "__main__":
    unittest.main()
