# Verified test results

Date: 2026-09-10

Command:

```bash
uv run --with genlayer-test==0.29.2 --with pytest==9.1.1 pytest -q
```

Result:

```text
......                                                                   [100%]
6 passed in 0.14s
```

The Direct Mode suite pins GenVM universal `v0.2.12`, while the deployable
contract declares the current Studio runner `v0.2.16`. The contract logic and
dependency hash are identical across the test and Studio runs.

Covered behavior:

- work creation and retry bounds;
- assigned-worker authorization;
- PASS to ACCEPTED transition;
- FAIL to REVISION_REQUIRED transition;
- REVIEW to MANUAL_REVIEW and client resolution; and
- validator rejection when decision-bearing fields disagree.
