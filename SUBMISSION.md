# Portal submission

## Title

Proof of Delivery: Consensus Quality Gate for Agent Workflows

## Notes (under 1000 characters)

Proof of Delivery is a reusable GenLayer Intelligent Contract for agent
marketplaces, service escrows, grants, and bounty workflows. A client creates a
plain-language work specification, an assigned worker submits a delivery with
evidence, and GenLayer consensus evaluates compliance. Validators independently
repeat the assessment. Verdict and canonical primary-gap category must match;
scores must remain in the same band and differ by no more than 12 points.
Deterministic checks reject malformed or inconsistent outputs. PASS becomes
ACCEPTED, FAIL becomes REVISION_REQUIRED until attempts are exhausted, and
ambiguous results enter MANUAL_REVIEW for an explicit client decision. The
contract includes role separation, retry bounds, prompt-injection boundaries,
documented state transitions, automated tests, and validator-disagreement
coverage. It records settlement readiness so external protocols can compose it
with their own payment logic.
