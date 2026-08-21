#!/usr/bin/env python3
"""Evaluate hand-authored response fixtures with executable contract checks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def evaluate_check(response: str, check: dict) -> bool:
    kind = check["type"]
    values = check.get("values", [])
    normalized = response.casefold()
    normalized_values = [str(value).casefold() for value in values]
    if kind == "contains_all":
        return all(value in normalized for value in normalized_values)
    if kind == "contains_any":
        return any(value in normalized for value in normalized_values)
    if kind == "not_contains":
        return all(value not in normalized for value in normalized_values)
    if kind == "valid_json":
        try:
            json.loads(response)
            return True
        except json.JSONDecodeError:
            return False
    if kind == "json_keys":
        try:
            document = json.loads(response)
        except json.JSONDecodeError:
            return False
        return isinstance(document, dict) and all(value in document for value in values)
    raise ValueError(f"Unsupported check type: {kind}")


def build_document() -> dict:
    cases_doc = json.loads((ROOT / "examples/evaluation/test-cases.json").read_text(encoding="utf-8"))
    fixtures = json.loads((ROOT / "examples/evaluation/responses.synthetic.json").read_text(encoding="utf-8"))
    rubric = json.loads((ROOT / "examples/evaluation/rubric.json").read_text(encoding="utf-8"))
    response_by_id = {item["case_id"]: item["response"] for item in fixtures["responses"]}
    dimension_ids = [item["id"] for item in rubric["dimensions"]]
    results = []

    for case in cases_doc["cases"]:
        response = response_by_id[case["id"]]
        scores = {dimension_id: 4 for dimension_id in dimension_ids}
        check_results = []
        for check in case["checks"]:
            passed = evaluate_check(response, check)
            check_results.append({"type": check["type"], "passed": passed})
            if not passed:
                scores[check["dimension"]] = min(
                    scores[check["dimension"]], 1 if case["severity"] == "P0" else 2
                )
        results.append({
            "case_id": case["id"],
            "severity": case["severity"],
            "passed": all(item["passed"] for item in check_results),
            "scores": scores,
            "check_results": check_results,
        })

    return {
        "run_id": "offline-contract-demo-v2",
        "result_type": "synthetic_contract_evaluation",
        "disclaimer": "Derived from hand-authored fixtures; not a live-model benchmark or production result.",
        "suite_version": cases_doc["schema_version"],
        "rubric_version": rubric["rubric_version"],
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional path for the derived result JSON")
    args = parser.parse_args()
    document = build_document()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    failures = [item["case_id"] for item in document["results"] if not item["passed"]]
    print(f"EVALUATED: {len(document['results'])} synthetic fixtures; failures={failures or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
