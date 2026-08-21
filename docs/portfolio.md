# Prompt Engineering Portfolio

**Author:** 汪楠

**Target:** 2027 graduate recruitment · AI Product Manager / Prompt Engineering

**Public portfolio period:** June–August 2026

## Positioning

I turn model behavior requirements from ad-hoc wording into versioned, testable, and traceable engineering assets. My public evidence focuses on System Prompt architecture, context and memory boundaries, tool-use contracts, executable evaluation contracts, adversarial fixtures, and structured output. This repository does not claim a production deployment.

## Capability evidence

| Capability | Public evidence | Evidence state |
|---|---|---|
| System Prompt architecture | Modular sample with priorities, context, tools, evidence, safety, completion | Designed |
| Evaluation engineering | Executable fixture checks, rubrics, gates, aggregation, regression tests | Executed offline |
| Prompt safety | Injection, hidden-context, crisis-signal and high-impact-action fixtures | Fixture coverage only |
| Structured output | Schemas, manifest, cross-reference validator, valid/invalid examples | Executed offline |
| Product delivery | Requirements-to-contract-to-release-decision loop | Designed; not production verified |
| RAG / fine-tuning | No independent public experiment in this version | Not evidenced |

## Project summaries

### 1. Production-oriented System Prompt architecture

**Problem:** identity, tools, response style, safety, and business rules were mixed in a monolithic prompt, increasing conflict and leakage risk.

**Design:** separate stable policy from task-specific overlays, treat runtime schemas as the source of truth for tools, define context priority, and enforce completion checks. Authorization and redaction remain service-side responsibilities.

**Outcome:** an independently versionable prompt architecture plus an explicit threat model. The public sample demonstrates the design without exposing any private production prompt.

[Read the case study](case-studies/01-system-prompt-architecture.md)

### 2. Evaluation contract harness and release gates

**Problem:** subjective testing and a single judge can produce high averages while hiding critical unsafe behavior.

**Design:** version test contracts and rubrics, retain case-level traces, classify P0/P1 failures, and compute release decisions after critical gates. Judge disagreement is a signal for human review, not noise to discard.

**Outcome:** a runnable offline contract harness that computes verdicts from response fixtures, exercises P0/P1 gates, and detects result-fixture drift. Synthetic results are clearly marked and are not claimed as a live-model benchmark.

[Read the case study](case-studies/02-llm-evalops.md)

### 3. Structured agent contract

**Problem:** structured agent answers can mix supplied facts, interpretation, advice, and uncertainty, making them difficult to audit.

**Design:** validate inputs, delegate calculations to deterministic tools, load one task overlay at a time, and require structured output with evidence references.

**Outcome:** a small manifest, schemas, semantic cross-reference validation, and golden fixtures that show an inspectable interface and failure boundaries. The sanitized public example is intentionally domain-neutral and does not prove subject-matter expertise.

[Read the case study](case-studies/03-domain-agent.md)

### 4. Synthetic prompt iteration

**Problem:** a vague instruction to use retrieved context does not define whether embedded instructions are data or executable directions.

**Design:** compare a deliberately weak, hand-authored baseline with a revised contract that marks retrieved content as untrusted, forbids hidden-data disclosure, and specifies a safe response.

**Outcome:** the same executable checks reject the synthetic baseline response and accept the synthetic revised response. This demonstrates the check and revision rationale only; it is not evidence that a live model improved.

[Read the case study](case-studies/04-prompt-iteration-synthetic.md)

## Reviewer walkthrough

1. Inspect the prompt architecture and identify which controls remain runtime-enforced.
2. Compare the synthetic prompt iteration and its explicit evidence boundary.
3. Run the demo and verify why a P0 failure blocks release despite strong noncritical scores.
4. Trace a structured output claim back to its declared evidence reference.
5. Review the limitations before drawing conclusions about live-model or production performance.

## Evidence policy

Claims in this repository use one of four states:

- **designed** — the contract or architecture exists;
- **statically validated** — files and schemas pass deterministic checks;
- **executed offline** — the included deterministic demo completed;
- **production verified** — intentionally not claimed in this public version.

This distinction prevents a polished document from being mistaken for live product evidence. See the [evidence register](evidence-register.md) for claim-by-claim boundaries.
