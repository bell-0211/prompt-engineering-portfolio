# Limitations and next experiments

## What is not claimed

- No production traffic, conversion, retention, or revenue metric.
- No claim that the sample prompt is an authorization or security boundary.
- No independent RAG retrieval/reranking benchmark yet.
- No fine-tuning or reinforcement-learning experiment in this repository.
- No live multi-model comparison; the included run is a deterministic offline contract demo.

## Planned evidence upgrades

1. Add a small public RAG corpus with retrieval, reranking, citation, faithfulness, and latency metrics.
2. Add provider adapters behind a common interface while keeping offline tests as the default.
3. Add repeated-run stability and token/cost reporting.
4. Add a framework-level agent demo with state recovery and tool-call traces.

These items are deliberately separated from completed evidence so the portfolio remains auditable.
