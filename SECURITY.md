# Security and redaction policy

This repository intentionally excludes credentials, personal data, production traces, private prompts, internal tool identifiers, and proprietary datasets.

## Public-example rules

- All example users, outputs, metrics, and incidents are synthetic.
- Tool contracts use generic names and least-privilege assumptions.
- The system prompt describes behavioral boundaries but does not pretend to enforce authorization; sensitive controls belong in the runtime and service layer.
- Critical-risk fixtures are safe text simulations and must not execute external actions.

If you identify accidental disclosure, do not open a public issue containing the sensitive value. Contact the repository owner privately through the GitHub profile.
