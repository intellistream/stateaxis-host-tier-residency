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

Status: **historical prefetch negative; independent activation unqualified**.

Correctness authority is usable, but serialized prefetch and restore crossover were not beneficial in the tested cells.

The copied evidence and its SHA-256 are recorded in `PROVENANCE.json`. Negative,
failed, and inconclusive results are retained. Microbenchmarks and component results
must not be restated as online end-to-end gains.

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
