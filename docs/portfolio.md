# Prompt Engineering Portfolio

## Positioning

I turn model behavior from ad-hoc wording into versioned, testable, traceable, and releasable engineering assets. My focus is System Prompt architecture, context and memory boundaries, tool-use contracts, LLM evaluation, adversarial testing, structured output, and domain-agent productization.

## Capability evidence

| Capability | Public evidence | Confidence |
|---|---|---|
| System Prompt architecture | Modular sample with priorities, context, tools, evidence, safety, completion | Strong |
| Evaluation engineering | Machine-readable cases, rubrics, gates, aggregation, regression tests | Strong |
| Prompt safety | Injection, hidden-context, crisis-signal and high-impact-action fixtures | Strong |
| Structured output | Input/output schemas, manifest, evidence references | Strong |
| Product delivery | Requirements-to-contract-to-release-decision loop | Medium–strong |
| RAG / fine-tuning | No independent public experiment in this version | Planned |

## Project summaries

### 1. Production-oriented System Prompt architecture

**Problem:** identity, tools, response style, safety, and business rules were mixed in a monolithic prompt, increasing conflict and leakage risk.

**Design:** separate stable policy from task-specific overlays, treat runtime schemas as the source of truth for tools, define context priority, and enforce completion checks. Authorization and redaction remain service-side responsibilities.

**Outcome:** an independently versionable prompt architecture plus an explicit threat model. The public sample demonstrates the design without exposing any private production prompt.

[Read the case study](case-studies/01-system-prompt-architecture.md)

### 2. LLM EvalOps and release gates

**Problem:** subjective testing and a single judge can produce high averages while hiding critical unsafe behavior.

**Design:** version test contracts and rubrics, retain case-level traces, classify P0/P1 failures, and compute release decisions after critical gates. Judge disagreement is a signal for human review, not noise to discard.

**Outcome:** a runnable offline contract demo with adversarial fixtures, aggregation logic, and regression tests. Synthetic results are clearly marked and are not claimed as a live-model benchmark.

[Read the case study](case-studies/02-llm-evalops.md)

### 3. Structured domain agent

**Problem:** domain answers mix deterministic facts, interpretation, advice, and uncertainty, making them difficult to audit.

**Design:** validate inputs, delegate calculations to deterministic tools, load one task overlay at a time, and require structured output with evidence references.

**Outcome:** a small manifest, schemas, and golden cases that show a product-ready interface and failure boundaries.

[Read the case study](case-studies/03-domain-agent.md)

## Interview walkthrough

1. Explain why prompt text is only one layer of the system.
2. Open the system-prompt sample and identify runtime-enforced controls.
3. Run the demo and show why a P0 failure blocks release despite good noncritical scores.
4. Inspect a domain output and trace each factual statement back to a structured input path.
5. Close with limitations and the next experiment instead of overstating production evidence.

## Evidence policy

Claims in this repository use one of four states:

- **designed** — the contract or architecture exists;
- **statically validated** — files and schemas pass deterministic checks;
- **executed offline** — the included deterministic demo completed;
- **production verified** — intentionally not claimed in this public version.

This distinction prevents a polished document from being mistaken for live product evidence.
