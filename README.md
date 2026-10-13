# stateaxis-host-tier-residency

Extension ID: `org.vllm-hust.stateaxis-host-tier-residency`

Bounded exact host-tier continuation authority with generation-safe restore.

This repository is the independent MOD boundary for StateAxis issues [#9](https://github.com/Qixin-Gaoke/stateaxis/issues/9), [#77](https://github.com/Qixin-Gaoke/stateaxis/issues/77).
Version `0.2.0` is an active, default-off Manifest 0.3 runtime bridge. It can
only be enabled through vLLM-HUST Extension Manager/ECPA and the StateAxis host
accepts only the exact research-manifest digest and reviewed two-state contract.
The split does not inherit performance or publication qualification from the
aggregate StateAxis repository.

## Evidence boundary

Status: **historical matched real-NPU prefetch negative; active revision
performance-unqualified**.

The frozen Qwen2.5-14B/Ascend 910B2 1+1 gate passed exactness, state identity and
lifecycle checks, but serialized prefetch was slower: host-tier-hit wall time rose
from 596.474 ms to 631.609 ms (+5.89%), concurrent-pair makespan rose from
619.076 ms to 643.752 ms (+24.675 ms), and peak HBM rose by 2 MiB. Candidate
queue wait was 570.013 ms and measured device overlap was zero. The preregistered
stop rule therefore correctly prevented a 3+3 campaign.

This is a historical, workload-scoped negative result, not a statement that exact
tiered residency is always harmful. The later asynchronous transfer lane addresses
the serial worker boundary separately. Version 0.2.0 does not inherit the historical
result and remains performance-unqualified.

The compact machine-readable evidence is under
`evidence/issue9-host-tier-prefetch-20260815-r1/`; its source hashes are recorded
in `SHA256SUMS`. Negative, failed, and inconclusive results are retained.
Microbenchmarks and component results must not be restated as online end-to-end gains.

## Install and inspect

```bash
python -m pip install .
vllm-hust-ext extension inspect org.vllm-hust.stateaxis-host-tier-residency
vllm-hust-ext extension check org.vllm-hust.stateaxis-host-tier-residency
```

Discovery does not enable the MOD. Enabling it claims the exclusive host-tier
residency authority, caps tracked generations at two, binds every transition to
state ID, generation, location epoch, byte count and payload SHA-256, and fails
closed. Prefetch remains disabled because the preserved matched experiment was
negative.

## Validate

```bash
python -m pip install -e '.[test]'
pytest -q
```

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
