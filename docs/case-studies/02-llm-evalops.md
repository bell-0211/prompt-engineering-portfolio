# Case study 02 — LLM EvalOps

## Situation

One-off manual testing and one LLM judge produced inconsistent conclusions. Strong writing quality could hide prompt leakage or unsafe action handling.

## Task

Build an evaluation contract that makes case coverage, scoring, evidence, disagreement, and release decisions inspectable.

## Actions

- Added versioned test cases across normal, adversarial, context, structure, and high-risk categories.
- Defined 1–4 scoring dimensions with case-level evidence.
- Separated content score from critical release gates.
- Kept blocked or missing evidence visible instead of silently skipping it.
- Added deterministic aggregation and regression tests.

## Result

The public demo reliably demonstrates the governance logic: a candidate with otherwise acceptable results is blocked when a P0 safety case fails. This is an offline synthetic demonstration, not a production benchmark.

## Inspectable artifacts

- [`examples/evaluation/rubric.json`](../../examples/evaluation/rubric.json)
- [`scripts/run_demo.py`](../../scripts/run_demo.py)
- [`scripts/aggregate_results.py`](../../scripts/aggregate_results.py)
- [`tests/test_release_gate.py`](../../tests/test_release_gate.py)
