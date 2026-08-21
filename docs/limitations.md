# Limitations and next experiments

## What is not claimed

- No production traffic, conversion, retention, or revenue metric.
- No claim that the sample prompt is an authorization or security boundary.
- No independent RAG retrieval/reranking benchmark yet.
- No fine-tuning or reinforcement-learning experiment in this repository.
- No live multi-model comparison; the included run is a deterministic offline contract harness over synthetic responses.
- No inter-rater reliability, confidence interval, repeated-run stability, latency, or token-cost result yet.
- The public structured-agent example is domain-neutral; it does not prove domain-expert knowledge.

## Planned evidence upgrades

1. Execute the pre-registered live-model baseline in [experiment-backlog.md](experiment-backlog.md).
2. Add a small public RAG corpus with retrieval, reranking, citation, faithfulness, and latency metrics.
3. Add repeated-run stability, judge agreement, token, cost, and latency reporting.
4. Add a framework-level agent demo with state recovery and tool-call traces.

These items are deliberately separated from completed evidence so the portfolio remains auditable.
