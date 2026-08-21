#!/usr/bin/env python3
"""Aggregate case results and enforce score, coverage, P0, and P1 gates."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def weighted_case_score(scores: dict[str, float], dimensions: list[dict]) -> float:
    return sum(float(scores[item["id"]]) * item["weight"] for item in dimensions) / 4.0


def release_decision(results_doc: dict, rubric: dict, expected_case_ids: set[str]) -> dict:
    results = results_doc.get("results", [])
    dimensions = rubric["dimensions"]
    result_ids = [result["case_id"] for result in results]
    duplicate_cases = sorted(case_id for case_id, count in Counter(result_ids).items() if count > 1)
    scored = [weighted_case_score(result["scores"], dimensions) for result in results]
    weighted_score = round(sum(scored) / len(scored), 2) if scored else 0.0

    policy = rubric["release_policy"]
    blocking_severities = set(policy["block_on_failed_severity"])
    failed_counts = Counter(result["severity"] for result in results if not result.get("passed", False))
    critical_failures = [
        result["case_id"] for result in results
        if not result.get("passed", False) and result.get("severity") in blocking_severities
    ]
    exceeded_failure_budgets = {
        severity: {"actual": failed_counts[severity], "allowed": allowed}
        for severity, allowed in policy.get("max_failed_by_severity", {}).items()
        if failed_counts[severity] > allowed
    }
    missing_cases = sorted(expected_case_ids - set(result_ids))
    unexpected_cases = sorted(set(result_ids) - expected_case_ids)
    coverage_ok = not missing_cases and not unexpected_cases and not duplicate_cases
    release = (
        weighted_score >= policy["minimum_weighted_score"]
        and not critical_failures
        and not exceeded_failure_budgets
        and (coverage_ok or not policy["require_all_cases_executed"])
    )
    return {
        "weighted_score": weighted_score,
        "critical_failures": critical_failures,
        "exceeded_failure_budgets": exceeded_failure_budgets,
        "missing_cases": missing_cases,
        "unexpected_cases": unexpected_cases,
        "duplicate_cases": duplicate_cases,
        "decision": "pass" if release else "blocked",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=ROOT / "examples/evaluation/results.synthetic.json")
    parser.add_argument("--expect", choices=["pass", "blocked"], help="Assert an expected demo decision")
    parser.add_argument("--enforce", action="store_true", help="Return non-zero when release is blocked")
    args = parser.parse_args()

    results_doc = json.loads(args.results.read_text(encoding="utf-8"))
    rubric = json.loads((ROOT / "examples/evaluation/rubric.json").read_text(encoding="utf-8"))
    cases_doc = json.loads((ROOT / "examples/evaluation/test-cases.json").read_text(encoding="utf-8"))
    expected = {case["id"] for case in cases_doc["cases"]}
    decision = release_decision(results_doc, rubric, expected)
    print(json.dumps(decision, ensure_ascii=False, indent=2))
    if args.expect and decision["decision"] != args.expect:
        return 2
    if args.enforce and decision["decision"] == "blocked":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
