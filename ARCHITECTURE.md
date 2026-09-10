# Architecture

## Why this is a primitive

Conventional contracts can compare hashes but cannot decide whether submitted
work satisfies natural-language requirements. Proof of Delivery exposes that
judgment as a bounded state machine that marketplaces and escrow systems can
compose with their own settlement logic.

## Lifecycle

`OPEN -> SUBMITTED -> ACCEPTED`

`OPEN -> SUBMITTED -> REVISION_REQUIRED -> SUBMITTED`

`OPEN -> SUBMITTED -> MANUAL_REVIEW -> ACCEPTED | REVISION_REQUIRED | EXHAUSTED`

`OPEN -> CANCELLED`

## Trust boundaries

Requirements, delivery text, evidence, and model output are all untrusted.
Input bounds protect execution, XML delimiters isolate instructions, output
schema checks reject malformed answers, and validators independently repeat the
semantic judgment. Human review is explicit rather than hidden inside a vague
fallback.

## Equivalence rule

Natural-language rationales may differ, so they are stored but not compared
byte-for-byte. Consensus is instead defined over the decision-bearing fields:
verdict, canonical primary-gap enum, score band, and bounded score distance.
