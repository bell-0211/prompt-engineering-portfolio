#!/usr/bin/env python3
"""Validate domain-agent JSON Schemas and cross-record evidence semantics."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = ROOT / "examples/domain-agent"


def load(name: str) -> dict:
    return json.loads((DOMAIN / name).read_text(encoding="utf-8"))


def semantic_errors(input_doc: dict, output_doc: dict) -> list[str]:
    errors: list[str] = []
    fact_ids = [item["id"] for item in input_doc["facts"]]
    if len(fact_ids) != len(set(fact_ids)):
        errors.append("fact IDs must be unique")
    known = set(fact_ids)
    for index, claim in enumerate(output_doc["claims"]):
        missing = sorted(set(claim["evidence_refs"]) - known)
        if missing:
            errors.append(f"claim[{index}] references missing facts: {missing}")
    if output_doc["status"] == "complete" and output_doc["open_questions"]:
        errors.append("complete output cannot retain open questions")
    if output_doc["request_id"] != input_doc["request_id"]:
        errors.append("request_id must be preserved")
    return errors


def validate_pair(input_doc: dict, output_doc: dict) -> list[str]:
    input_validator = Draft202012Validator(load("input.schema.json"))
    output_validator = Draft202012Validator(load("output.schema.json"))
    errors = [f"input schema: {error.message}" for error in input_validator.iter_errors(input_doc)]
    errors.extend(f"output schema: {error.message}" for error in output_validator.iter_errors(output_doc))
    if not errors:
        errors.extend(semantic_errors(input_doc, output_doc))
    return errors


def main() -> int:
    errors = validate_pair(load("sample.input.json"), load("sample.output.json"))
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: JSON Schema and evidence-reference semantics")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
