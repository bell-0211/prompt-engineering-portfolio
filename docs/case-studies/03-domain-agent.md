# Case study 03 — Structured agent contract

## Situation

In structured workflows, fluent text can blur supplied facts, interpretation, and advice. Missing fields, invalid evidence references, and unsupported certainty are product risks.

## Task

Design a small, versioned agent contract in which deterministic computation and model explanation have separate responsibilities.

## Actions

- Defined input and output JSON Schemas.
- Added a manifest for prompt and schema compatibility.
- Required unknown fields to remain unknown rather than being guessed.
- Required non-empty `evidence_refs` for every claim.
- Added semantic validation that rejects duplicate fact IDs, missing references, and inconsistent completion status.
- Added golden fixtures for missing data, ambiguity, unsupported claims, and high-risk language.

## Result

The contract supports deterministic validation and UI rendering while preserving traceability. Because this public example is deliberately domain-neutral, it demonstrates interface and validation design—not domain expertise or production readiness.

## Inspectable artifacts

- [`examples/domain-agent/manifest.json`](../../examples/domain-agent/manifest.json)
- [`examples/domain-agent/input.schema.json`](../../examples/domain-agent/input.schema.json)
- [`examples/domain-agent/output.schema.json`](../../examples/domain-agent/output.schema.json)
- [`examples/domain-agent/golden-cases.json`](../../examples/domain-agent/golden-cases.json)
- [`scripts/validate_domain_contract.py`](../../scripts/validate_domain_contract.py)
