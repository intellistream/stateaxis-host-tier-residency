# Evidence index

## Current independent revision

- Version: `0.2.0`
- Status: active, default-off, experimental, not performance-qualified
- The Manifest 0.3 contract activates bounded exact host-tier residency through
  Extension Manager/ECPA.
- Fresh matched-process activation evidence will be recorded under `evidence/`.

## Preserved historical evidence

- `evidence/ISSUE9_HOST_TIER_PREFETCH_CLOSURE_20260815.md`
  - matched real-NPU negative for serialized prefetch in its tested cell
  - exact residency authority was correct, but the candidate increased latency
- `evidence/on-off-preflight-20261010/`
  - preserved pre-activation result; ON was not runnable at version `0.1.0.dev0`

Historical evidence does not automatically qualify version `0.2.0`. Negative,
failed, and preflight results remain part of the record.
