# Prompt Engineering Portfolio

Evidence-conscious prompt architecture, executable evaluation contracts, safety gates, and structured-agent case studies.

[中文说明](README.zh-CN.md) · [Portfolio](docs/portfolio.md) · [Live-page source](docs/index.html)

## What this repository demonstrates

- Modular system-prompt design with explicit priority, context, tool, evidence, safety, and completion contracts.
- An executable offline contract harness that derives pass/fail results from response fixtures instead of accepting pre-filled verdicts.
- Adversarial and high-risk tests treated as release gates instead of being averaged away.
- Structured-agent inputs/outputs with schema and cross-reference validation.
- Reproducible local validation with a small, declared development dependency.

> This is a sanitized portfolio repository. Examples are reconstructed and synthetic; they do not contain private system prompts, internal tool names, production data, or employer-confidential material.

## Portfolio map

| Case study | Problem | Main artifacts |
|---|---|---|
| [System Prompt Architecture](docs/case-studies/01-system-prompt-architecture.md) | Monolithic prompts become hard to govern | Modular prompt sample, runtime boundaries, threat model |
| [Evaluation Contract Harness](docs/case-studies/02-llm-evalops.md) | A high average score can hide critical failures | Executable checks, rubrics, gates, result aggregation |
| [Structured Agent Contract](docs/case-studies/03-domain-agent.md) | Agent output must be structured and traceable | Schemas, manifest, semantic validation, golden cases |

## Evidence status at a glance

| Claim | Status | What it means |
|---|---|---|
| Prompt/runtime architecture | Designed | A reviewable public design exists; no production deployment is claimed. |
| Evaluation and release-gate code | Executed offline | Deterministic synthetic fixtures exercise the included code path. |
| Schema and evidence-reference checks | Executed offline | Valid and invalid synthetic records are covered by tests. |
| Live-model quality, latency, cost, and stability | Not measured | No provider benchmark is presented in this version. |
| Production or business impact | Not verified | No traffic, conversion, retention, or revenue claim is made. |

See the full [evidence register](docs/evidence-register.md).

## Quick start

Python 3.10+ is required.

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_assets.py
python scripts/run_demo.py
python scripts/aggregate_results.py --expect blocked
python -m unittest discover -s tests -v
```

The demo is intentionally offline and deterministic. It evaluates synthetic response fixtures with executable checks and demonstrates release-gate behavior. It is not an LLM benchmark. A real release candidate would use `--enforce`, which returns a non-zero exit code when the decision is blocked.

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

This repository provides inspectable evidence of prompt/system design, evaluation-contract implementation, structured output, and safety-gate reasoning. It does not prove live-model quality or production impact. See [limitations](docs/limitations.md) and the [unexecuted experiment backlog](docs/experiment-backlog.md).

## Use in interviews

Start with [docs/portfolio.md](docs/portfolio.md), then run the quick-start commands. For the hardest evidence questions, use [docs/interview-defense.md](docs/interview-defense.md).

## License

No open-source license is granted at this stage. The repository is published for portfolio review; all rights are reserved unless a license is added later.
