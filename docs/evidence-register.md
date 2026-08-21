# Evidence register

This register defines what each portfolio claim is allowed to mean.

| Claim | Inspectable evidence | State | Not supported by this evidence |
|---|---|---|---|
| A modular prompt architecture was designed | System prompt, task overlay, methodology | Designed | Production deployment, quality improvement, cost reduction |
| A prompt revision is connected to explicit checks | Hand-authored iteration fixture and regression test | Executed offline | Live-model improvement or causal attribution |
| Evaluation checks execute | Test cases, response fixtures, `run_demo.py`, tests | Executed offline | Live-model accuracy or safety |
| P0/P1 gates are enforced in code | Aggregator, `--enforce`, release-gate tests | Executed offline | Correct business severity policy for a real product |
| Structured records are validated | JSON Schemas, semantic validator, valid/invalid tests | Executed offline | Semantic truth of model-generated content |
| Injection and crisis categories are represented | Synthetic cases and checks | Fixture coverage | Comprehensive red-team coverage or production safety |
| The work is production-oriented | Runtime boundaries, failure states, version contracts | Design orientation | Production traffic or business impact |

## Evidence hierarchy

1. **Designed** — an inspectable architecture or contract exists.
2. **Statically validated** — files, schemas, references, and policies pass deterministic checks.
3. **Executed offline** — included code ran against declared synthetic fixtures.
4. **Live-model measured** — not yet present.
5. **Production verified** — not claimed.

Asset counts are inventory information, not outcome metrics. Any future quality claim must include a baseline, held-out cases, model/version parameters, repeated runs, cost/latency, and raw result records.
