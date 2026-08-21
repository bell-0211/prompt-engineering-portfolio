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
- Created fixtures for direct, encoded, role-play, indirect, and multi-turn injection.

## Result

The architecture is independently testable and safer to evolve. The most important conclusion is architectural: a sentence saying “do not leak” cannot replace server-side access control, output scanning, and audit logging.

## Inspectable artifacts

- [`examples/system-prompt/system.sample.md`](../../examples/system-prompt/system.sample.md)
- [`examples/system-prompt/task-overlay.sample.md`](../../examples/system-prompt/task-overlay.sample.md)
- [`examples/evaluation/test-cases.json`](../../examples/evaluation/test-cases.json)

## Interview discussion

The useful trade-off is not “short prompt versus long prompt.” It is deciding what must remain stable, what should be loaded on demand, what belongs in structured runtime state, and what cannot safely be delegated to an LLM.
