# Case study 01 — System Prompt architecture

## Situation

A growing assistant accumulated identity, tool instructions, formatting, safety, and scenario rules in one prompt. The result was duplicated rules, unclear precedence, and a larger leakage surface.

## Task

Create a modular architecture that supports versioning and scenario routing while defining which controls must be enforced outside the model.

## Actions

- Defined instruction priority and conflict handling.
- Split stable behavior from task overlays.
- Added explicit context and memory precedence.
- Made runtime tool schemas the source of truth.
- Added evidence boundaries, failure behavior, and completion checks.
- Considered multiple injection forms in the source work; this public repository exposes two sanitized synthetic injection fixtures.

## Result

The modules are independently reviewable and structured to reduce rule duplication. No live-model safety improvement is claimed. The most important conclusion is architectural: a sentence saying “do not leak” cannot replace server-side access control, output scanning, and audit logging.

## Inspectable artifacts

- [`examples/system-prompt/system.sample.md`](../../examples/system-prompt/system.sample.md)
- [`examples/system-prompt/task-overlay.sample.md`](../../examples/system-prompt/task-overlay.sample.md)
- [`examples/evaluation/test-cases.json`](../../examples/evaluation/test-cases.json)
- [Synthetic prompt-iteration case](04-prompt-iteration-synthetic.md)

## Design discussion

The useful trade-off is not “short prompt versus long prompt.” It is deciding what must remain stable, what should be loaded on demand, what belongs in structured runtime state, and what cannot safely be delegated to an LLM.
