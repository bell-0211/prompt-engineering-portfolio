# Prompt Engineering Portfolio

Production-oriented prompt architecture, evaluation, safety, and domain-agent case studies.

[中文说明](README.zh-CN.md) · [Portfolio](docs/portfolio.md) · [Live-page source](docs/index.html)

## What this repository demonstrates

- Modular system-prompt design with explicit priority, context, tool, evidence, safety, and completion contracts.
- Evaluation assets that separate content quality from release readiness.
- Adversarial and high-risk tests treated as release gates instead of being averaged away.
- Structured domain-agent inputs/outputs with traceable evidence references.
- Reproducible local validation using only the Python standard library.

> This is a sanitized portfolio repository. Examples are reconstructed and synthetic; they do not contain private system prompts, internal tool names, production data, or employer-confidential material.

## Portfolio map

| Case study | Problem | Main artifacts |
|---|---|---|
| [System Prompt Architecture](docs/case-studies/01-system-prompt-architecture.md) | Monolithic prompts become hard to govern | Modular prompt sample, runtime boundaries, threat model |
| [LLM EvalOps](docs/case-studies/02-llm-evalops.md) | A high average score can hide critical failures | Test contracts, rubrics, gates, result aggregation |
| [Domain Agent](docs/case-studies/03-domain-agent.md) | Domain output must be structured and traceable | Schemas, manifest, golden cases, evidence references |

## Quick start

Python 3.10+ is sufficient; no third-party package is required.

```bash
python scripts/validate_assets.py
python scripts/run_demo.py
python scripts/aggregate_results.py
python -m unittest discover -s tests -v
```

The demo is intentionally offline and deterministic. It validates the evaluation contract and release-gate logic; it is not presented as a live model benchmark.

## Repository structure

```text
.
├── docs/                  Portfolio narrative and case studies
├── examples/              Sanitized prompt, evaluation, and agent contracts
├── scripts/               Validation, offline demo, and result aggregation
├── tests/                 Regression tests for contracts and gates
├── .github/workflows/     Continuous validation
├── SECURITY.md            Disclosure and redaction policy
└── CHANGELOG.md           Public portfolio versions
```

## Evaluation principles

1. **Evidence before claims** — distinguish static validation, completed execution, model scoring, and product approval.
2. **Critical gates before averages** — injection leakage, unsafe high-impact actions, and crisis-signal misses block release.
3. **Traceability** — prompt version, test-case ID, rubric version, output, score, and decision remain linked.
4. **Reproducibility** — fixtures and aggregation rules are machine-readable and covered by tests.
5. **Honest boundaries** — no fabricated online metrics, user growth, or production-release claims.

## Current scope and limitations

This repository proves prompt/system design, EvalOps, structured output, and safety-governance ability. It does not claim production traffic, independent RAG benchmarking, fine-tuning expertise, or a framework-specific multi-agent deployment. See [limitations](docs/limitations.md).

## Use in interviews

Start with [docs/portfolio.md](docs/portfolio.md), then run the four quick-start commands. The case studies are designed for a 10–15 minute walkthrough and make the decision logic inspectable rather than exposing proprietary prompts.

## License

No open-source license is granted at this stage. The repository is published for portfolio review; all rights are reserved unless a license is added later.
