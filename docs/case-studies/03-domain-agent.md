# Case study 03 — Structured domain agent

## Situation

In domain workflows, fluent text can blur calculated facts, interpretation, and advice. Missing fields and unsupported certainty are product risks.

## Task

Design a small, versioned agent contract in which deterministic computation and model explanation have separate responsibilities.

## Actions

- Defined input and output JSON Schemas.
- Added a manifest for prompt and schema compatibility.
- Required unknown fields to remain unknown rather than being guessed.
- Required `evidence_refs` for factual statements.
- Added golden cases for missing data, ambiguity, unsupported claims, and high-risk language.

## Result

The contract supports validation and UI rendering while preserving traceability. It shows how prompt assets become product modules with interfaces and acceptance criteria.

## Inspectable artifacts

- [`examples/domain-agent/manifest.json`](../../examples/domain-agent/manifest.json)
- [`examples/domain-agent/input.schema.json`](../../examples/domain-agent/input.schema.json)
- [`examples/domain-agent/output.schema.json`](../../examples/domain-agent/output.schema.json)
- [`examples/domain-agent/golden-cases.json`](../../examples/domain-agent/golden-cases.json)
