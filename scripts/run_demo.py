#!/usr/bin/env python3
"""Generate deterministic synthetic results for the public evaluation contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build_scores(case_id: str, dimension_ids: list[str]) -> dict[str, int]:
    scores = {dimension_id: 4 for dimension_id in dimension_ids}
    if case_id == "injection-001":
        scores["safety_and_privacy"] = 1
        scores["instruction_following"] = 2
    elif case_id == "tool-001":
        scores["completion_and_transparency"] = 3
    return scores


def build_document() -> dict:
    cases_doc = json.loads((ROOT / "examples" / "evaluation" / "test-cases.json").read_text(encoding="utf-8"))
    rubric = json.loads((ROOT / "examples" / "evaluation" / "rubric.json").read_text(encoding="utf-8"))
    dimension_ids = [item["id"] for item in rubric["dimensions"]]
    results = []
    for case in cases_doc["cases"]:
        intentionally_failed = case["id"] == "injection-001"
        results.append({
            "case_id": case["id"],
            "severity": case["severity"],
            "passed": not intentionally_failed,
            "scores": build_scores(case["id"], dimension_ids),
            "evidence": (
                "Synthetic failure inserted to demonstrate the P0 release gate."
                if intentionally_failed
                else "Deterministic offline fixture satisfied the declared contract."
            ),
        })

    return {
        "run_id": "offline-demo-v1",
        "result_type": "synthetic_deterministic_demo",
        "disclaimer": "Not a live-model benchmark or production result.",
        "prompt_version": "system-sample-v1.0.0",
        "rubric_version": rubric["rubric_version"],
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional path for the generated JSON document")
    args = parser.parse_args()
    document = build_document()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"WROTE: {len(document['results'])} synthetic results to {args.output}")
    else:
        failed = [item["case_id"] for item in document["results"] if not item["passed"]]
        print(
            f"RUN: {len(document['results'])} deterministic synthetic cases; "
            f"intentional failures={','.join(failed) or 'none'}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
