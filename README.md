# Proof of Delivery — Consensus Quality Gate for GenLayer

Proof of Delivery is a reusable Intelligent Contract primitive for agent
marketplaces, freelance protocols, service escrows, grants, and bounty systems.
It turns plain-language requirements and submitted work into a consensus-backed
lifecycle without pretending that one LLM response is objective truth.

## State machine

- A client creates a work item and assigns a worker.
- Only that worker can submit a delivery and supporting evidence.
- GenLayer validators independently assess requirement compliance.
- `PASS` becomes `ACCEPTED`.
- `FAIL` becomes `REVISION_REQUIRED` until attempts are exhausted.
- `REVIEW` becomes `MANUAL_REVIEW`; only the client may resolve it.

## Consensus design

The leader returns structured JSON containing verdict, score, primary gap, and
rationale. Every validator repeats the assessment. Acceptance requires:

- exact verdict equality;
- exact primary-gap equality;
- scores in the same band (`0-49`, `50-79`, or `80-100`); and
- an absolute score difference of no more than 12.

Deterministic cross-field checks enforce that PASS uses score 80–100 and gap
`NONE`, FAIL uses 0–49 and a real gap, and REVIEW uses 50–79 and a real gap.
Malformed or internally inconsistent outputs fail closed.

## Safety properties

- Role separation between client and assigned worker.
- Bounded requirements, delivery, evidence, and retry counts.
- Prompt-injection boundaries around all untrusted text.
- No leader-only acceptance.
- Manual review for ambiguous results.
- Explicit terminal states for acceptance, cancellation, and exhausted retries.

## Public methods

- `create_work(worker, requirements, max_attempts)`
- `submit_delivery(work_id, delivery, evidence)`
- `evaluate_delivery(work_id)`
- `resolve_manual_review(work_id, approve)`
- `cancel_open_work(work_id)`
- `get_work(work_id)`
- `get_work_count()`

## Tests

```bash
pip install genlayer-test pytest
pytest tests/ -v
```

Tests cover roles, successful acceptance, revision requests, manual review, and
validator disagreement. This contract intentionally records release readiness
instead of transferring tokens because GenLayer Studio does not currently
support token transfers; an integrating protocol can consume the terminal state.

## License

MIT
