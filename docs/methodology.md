# Methodology

## Prompt lifecycle

```text
requirements → risk classification → prompt/runtime contract → test fixtures
→ execution trace → rubric scoring → critical gates → release decision → version record
```

## Design rules

1. Stable behavioral policy stays in the base prompt; task knowledge is loaded as a scoped overlay.
2. The runtime owns authentication, authorization, secrets, tool schemas, logging, and redaction.
3. The model must distinguish observed facts, inference, recommendation, and uncertainty.
4. Every high-risk action requires explicit confirmation and a runtime authorization check.
5. Evaluation records keep prompt version, case version, rubric version, output, score, and decision together.

## Scoring and gates

Dimension scores describe content quality. Release readiness is a separate decision:

```text
release = weighted_score >= threshold
          AND no_P0_failure
          AND P1_failure_count <= budget
          AND required_evidence_present
```

A critical failure cannot be offset by fluent prose or a high average. The included aggregator implements this principle and exposes `--enforce` for a real release job. The default demo intentionally expects a blocked result so CI can prove the negative path works without representing that fixture as a releasable model.
