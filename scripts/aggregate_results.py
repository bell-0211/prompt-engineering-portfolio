#!/usr/bin/env python3
"""Aggregate case-level results and apply critical release gates."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def weighted_case_score(scores: dict[str, float], dimensions: list[dict]) -> float:
    return sum(float(scores[item["id"]]) * item["weight"] for item in dimensions) / 4.0


def release_decision(results_doc: dict, rubric: dict, expected_case_ids: set[str]) -> dict:
    results = results_doc.get("results", [])
    dimensions = rubric["dimensions"]
    result_ids = {result["case_id"] for result in results}
    scored = [weighted_case_score(result["scores"], dimensions) for result in results]
    weighted_score = round(sum(scored) / len(scored), 2) if scored else 0.0

    policy = rubric["release_policy"]
    blocking_severities = set(policy["block_on_failed_severity"])
    critical_failures = [
        result["case_id"]
        for result in results
        if not result.get("passed", False) and result.get("severity") in blocking_severities
    ]
    missing_cases = sorted(expected_case_ids - result_ids)
    all_executed = not missing_cases
    release = (
        weighted_score >= policy["minimum_weighted_score"]
        and not critical_failures
        and (all_executed or not policy["require_all_cases_executed"])
    )
    return {
        "weighted_score": weighted_score,
        "critical_failures": critical_failures,
        "missing_cases": missing_cases,
        "decision": "pass" if release else "blocked",
    }


def main() -> int:
    generated = ROOT / "reports" / "generated" / "results.json"
    source = generated if generated.exists() else ROOT / "examples" / "evaluation" / "results.synthetic.json"
    results_doc = json.loads(source.read_text(encoding="utf-8"))
    rubric = json.loads((ROOT / "examples" / "evaluation" / "rubric.json").read_text(encoding="utf-8"))
    cases_doc = json.loads((ROOT / "examples" / "evaluation" / "test-cases.json").read_text(encoding="utf-8"))
    expected = {case["id"] for case in cases_doc["cases"]}
    decision = release_decision(results_doc, rubric, expected)
    print(json.dumps(decision, ensure_ascii=False, indent=2))
    return 0 if results_doc.get("result_type") == "synthetic_deterministic_demo" else 1


if __name__ == "__main__":
    sys.exit(main())
