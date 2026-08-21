# Experiment backlog — not yet executed

> Status: **planned, not executed**. This file is a pre-registration, not a result report.

## First live-model baseline

- Compare one minimal baseline prompt with the modular sample.
- Freeze model ID, provider parameters, prompt hashes, test-suite version, and rubric version.
- Split cases into development and held-out sets before tuning.
- Run each stochastic case at least five times.
- Record completion, P0/P1 failures, per-dimension scores, latency, input/output tokens, estimated cost, and raw outputs.
- Use two independent judges for subjective dimensions and human review for threshold disagreements.

## Decision rules

- No P0 failure in any repeated run.
- P1 failures stay within the declared budget.
- Report confidence intervals; do not claim improvement from a point estimate alone.
- A quality gain must disclose latency and cost changes.
- Any test-set change creates a new suite version and invalidates direct comparison unless both candidates are rerun.

## Stop conditions

Stop and report “inconclusive” when provider failures, missing traces, judge disagreement, or insufficient sample size prevent a defensible comparison.
