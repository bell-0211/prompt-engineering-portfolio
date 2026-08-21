# Case study 02 — Evaluation contract harness

## Situation

One-off manual testing and one LLM judge produced inconsistent conclusions. Strong writing quality could hide prompt leakage or unsafe action handling.

## Task

Build an executable offline contract that makes case coverage, checks, scoring, evidence, and release decisions inspectable without presenting synthetic data as a model benchmark.

## Actions

- Added versioned test cases and response fixtures across normal, adversarial, context, structure, and high-risk categories.
- Replaced pre-filled `passed` values with executable `contains`, `not_contains`, and JSON-structure checks.
- Defined 1–4 scoring dimensions with case-level evidence.
- Separated content score from critical release gates.
- Kept blocked or missing evidence visible instead of silently skipping it.
- Added P0/P1 gate enforcement, deterministic aggregation, fixture-drift detection, and regression tests.

## Result

The public harness demonstrates one narrow fact: the included code detects an intentionally unsafe synthetic response and blocks the candidate despite a high weighted score. It does not demonstrate that any real model is safe, unsafe, better, or worse.

## Inspectable artifacts

- [`examples/evaluation/rubric.json`](../../examples/evaluation/rubric.json)
- [`scripts/run_demo.py`](../../scripts/run_demo.py)
- [`scripts/aggregate_results.py`](../../scripts/aggregate_results.py)
- [`tests/test_release_gate.py`](../../tests/test_release_gate.py)
- [`tests/test_demo_contract.py`](../../tests/test_demo_contract.py)
