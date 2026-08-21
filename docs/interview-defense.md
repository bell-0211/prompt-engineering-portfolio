# Interview defense — honest answers to the hardest questions

## “Why do you call this production-oriented without production traffic?”

“Production-oriented” describes the design concerns—runtime authorization, traceability, failure states, versioning, and release gates. It does not mean production-deployed. The evidence register explicitly marks deployment and business impact as unverified.

## “Your demo does not call an LLM. What does it prove?”

It proves only that the evaluation contract, executable checks, result generation, and gate logic work on declared synthetic fixtures. It does not prove model quality. The next valid evidence step is the pre-registered live-model experiment, not stronger wording.

## “Is the P0 failure just self-demonstration?”

The unsafe response is intentionally planted to exercise the negative path. Unlike the first version, the verdict is not pre-filled: the harness derives the failure from machine-readable checks. This validates the mechanism, not its real-world coverage.

## “Where is your baseline?”

There is no live-model baseline in this version, so no improvement claim is made. The experiment backlog defines the baseline, held-out split, repeated runs, metrics, and stopping rules required before such a claim would be valid.

## “Where are cost, latency, and traces?”

They are absent because no provider run is presented. Adding invented estimates would reduce credibility. Provider adapters and trace capture are planned evidence upgrades; until executed, those fields remain “not measured.”

## Authorship discussion

The repository should be defended file by file: explain the decision each artifact encodes, reproduce the release-gate tests, change a severity budget live, and identify limitations without reading the documentation. AI assistance, if used, should be disclosed as tooling; ownership is demonstrated through reasoning, verification, and the ability to modify the system under pressure.
