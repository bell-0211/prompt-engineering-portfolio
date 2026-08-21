#!/usr/bin/env python3
"""Validate the public portfolio's machine-readable contracts and redaction rules."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str):
    path = ROOT / relative
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate() -> list[str]:
    errors: list[str] = []
    cases_doc = load_json("examples/evaluation/test-cases.json")
    rubric = load_json("examples/evaluation/rubric.json")
    manifest = load_json("examples/domain-agent/manifest.json")
    input_schema = load_json("examples/domain-agent/input.schema.json")
    output_schema = load_json("examples/domain-agent/output.schema.json")
    golden = load_json("examples/domain-agent/golden-cases.json")
    fixtures = load_json("examples/evaluation/responses.synthetic.json")
    iteration = load_json("examples/system-prompt/iteration-case.synthetic.json")

    cases = cases_doc.get("cases", [])
    ids = [case.get("id") for case in cases]
    require(len(cases) >= 8, "evaluation suite must contain at least 8 cases", errors)
    require(len(ids) == len(set(ids)), "evaluation case IDs must be unique", errors)
    require(all(case.get("severity") in {"P0", "P1", "P2"} for case in cases),
            "every case must have a supported severity", errors)
    require(any(case.get("category") == "prompt_injection" for case in cases),
            "suite must cover prompt injection", errors)
    require(any(case.get("category") == "crisis_signal" for case in cases),
            "suite must cover crisis signals", errors)
    supported_checks = {"contains_all", "contains_any", "not_contains", "valid_json", "json_keys"}
    require(all(case.get("checks") for case in cases), "every case must have executable checks", errors)
    require(all(check.get("type") in supported_checks for case in cases for check in case.get("checks", [])),
            "every evaluation check must use a supported executable type", errors)
    fixture_ids = [item.get("case_id") for item in fixtures.get("responses", [])]
    require(set(fixture_ids) == set(ids), "response fixture IDs must exactly match case IDs", errors)
    require(len(fixture_ids) == len(set(fixture_ids)), "response fixture IDs must be unique", errors)

    require(iteration.get("fixture_type") == "hand_authored_demonstration",
            "prompt iteration must be labelled as a hand-authored demonstration", errors)
    require("not model output" in iteration.get("disclaimer", "").lower(),
            "prompt iteration disclaimer must state that responses are not model output", errors)
    for key in ("input", "baseline_prompt", "baseline_response", "revised_prompt",
                "revised_response", "checks"):
        require(bool(iteration.get(key)), f"prompt iteration is missing {key}", errors)

    weights = [dimension.get("weight", 0) for dimension in rubric.get("dimensions", [])]
    require(sum(weights) == 100, "rubric weights must sum to 100", errors)
    policy = rubric.get("release_policy", {})
    require("P0" in policy.get("block_on_failed_severity", []),
            "release policy must block P0 failures", errors)

    for key in ("prompt", "task_overlay", "input_schema", "output_schema", "golden_cases",
                "sample_input", "sample_output"):
        require(key in manifest, f"manifest is missing {key}", errors)
    require(set(input_schema.get("required", [])) >= {"request_id", "request", "facts"},
            "input schema required fields are incomplete", errors)
    require(set(output_schema.get("required", [])) >=
            {"request_id", "summary", "claims", "open_questions", "status"},
            "output schema required fields are incomplete", errors)
    require(len(golden.get("cases", [])) >= 7, "at least 7 golden cases are required", errors)
    require(all("input" in case and "expected" in case for case in golden.get("cases", [])),
            "golden cases must contain structured input and expected contracts", errors)

    text_extensions = {".md", ".json", ".py", ".yml", ".yaml", ".html"}
    redaction_patterns = {
        "Windows absolute path": re.compile(r"[A-Za-z]:\\"),
        "email address": re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"),
        "credential assignment": re.compile(
            r"(?i)(password|passwd|secret|api[_-]?key)\s*[:=]\s*['\"][^'\"]+"
        ),
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    }
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_extensions:
            continue
        if ".git" in path.parts or "generated" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in redaction_patterns.items():
            require(not pattern.search(text), f"{label} found in {path.relative_to(ROOT)}", errors)

    return errors


def main() -> int:
    try:
        errors = validate()
    except (OSError, json.JSONDecodeError) as exc:
        print(f"VALIDATION ERROR: {exc}")
        return 1
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: executable cases, exact fixtures, rubric policy, structured golden cases, and redaction checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
