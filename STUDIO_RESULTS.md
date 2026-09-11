# GenLayer Studio Full Consensus Results

Verified on 2026-09-11 with `Normal (Full Consensus)` and five initial validators.

- Contract: `0x6C92f8f689b88DBd8E19e63dAFD9a0696d2ADCBa`
- Explorer: https://explorer-studio.genlayer.com/address/0x6C92f8f689b88DBd8E19e63dAFD9a0696d2ADCBa
- Deployment: `FINALIZED`
- `create_work`: `FINALIZED`; work count became `1`
- `submit_delivery`: `FINALIZED`; attempt count became `1`
- `evaluate_delivery`: `FINALIZED`

## Consensus assessment

```json
{
  "verdict": "REVIEW",
  "score": 72,
  "primary_gap": "EVIDENCE",
  "status": "MANUAL_REVIEW",
  "rationale": "The delivery claims all required comparison elements and official links are included, but the provided evidence is only descriptive and does not let us verify that the three protocols and each required category are actually present."
}
```

The result demonstrates fail-closed behavior: a plausible but non-verifiable
delivery does not auto-pass. It is routed to explicit client review.

## Transactions

- Deploy: https://explorer-studio.genlayer.com/tx/0xa4c5462d5a936519aff8dc2e62b5021202edefa6b248dc3377a4bf80df721fb6
- Create work: https://explorer-studio.genlayer.com/tx/0x8c6c81ead6f1a1c30272c75ff831d1431dbe9d542c66240ccf6f614aa3b7f51d
- Submit delivery: https://explorer-studio.genlayer.com/tx/0x663af88dca14c59d6244a418b2e560cbe3876deb32fc3d4d143e706df786bd1a
- Evaluate delivery: https://explorer-studio.genlayer.com/tx/0xd909fe633eb89d47af49d2f28ee8ab07597a62f81e418a7be38cea1cd4fe43ed

## Compatibility correction

Hosted Studio supplies address parameters as Python integers. The contract now
accepts the worker as a canonical address string and stores both role identifiers
as strings, preserving authorization while avoiding a runner storage mismatch.
Direct Mode was rerun after the correction: `6 passed`.
