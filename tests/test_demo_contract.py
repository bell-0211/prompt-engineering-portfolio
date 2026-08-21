import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from run_demo import build_document, evaluate_check  # noqa: E402


class DemoContractTests(unittest.TestCase):
    def test_checked_in_result_matches_executable_harness(self):
        expected = json.loads(
            (ROOT / "examples/evaluation/results.synthetic.json").read_text(encoding="utf-8")
        )
        self.assertEqual(build_document(), expected)

    def test_forbidden_marker_is_detected(self):
        check = {"type": "not_contains", "values": ["synthetic_secret"]}
        self.assertFalse(evaluate_check("Contains SYNTHETIC_SECRET", check))

    def test_valid_json_is_actually_parsed(self):
        self.assertTrue(evaluate_check('{"ok": true}', {"type": "valid_json"}))
        self.assertFalse(evaluate_check("not-json", {"type": "valid_json"}))

    def test_synthetic_iteration_demonstrates_check_difference(self):
        iteration = json.loads(
            (ROOT / "examples/system-prompt/iteration-case.synthetic.json").read_text(
                encoding="utf-8"
            )
        )
        checks = iteration["checks"]
        baseline_results = [evaluate_check(iteration["baseline_response"], check) for check in checks]
        revised_results = [evaluate_check(iteration["revised_response"], check) for check in checks]
        self.assertFalse(all(baseline_results))
        self.assertTrue(all(revised_results))


if __name__ == "__main__":
    unittest.main()
