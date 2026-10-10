# Matched ECPA process evidence — bounded host-tier residency

Evidence label: `matched_process_mock_non_performance`.

This campaign validates the independent version `0.2.0` activation boundary.
It is deterministic protocol/process evidence and is not an NPU performance
measurement.

## Design

- Order: OFF/ON, ON/OFF, OFF/ON.
- Every arm starts a fresh StateAxis service through vLLM-HUST Extension
  Manager/ECPA and stops it through the normal SIGINT lifecycle.
- Each run performs one cold retained request followed by four exact two-token
  continuations.
- OFF has no host-tier authority and no MOD identity.
- ON receives only the hash-bound Manifest 0.3 additional config. No legacy
  `STATE_ENGINE_ISSUE9_*` activation environment variable is supplied.

## Result

- Six of six fresh processes passed; none required forced termination.
- All output tokens were exact and reused-token counts were `[4, 5, 6, 7]`.
- Every ON run recorded five successful response-first offloads (one seed plus
  four replay outputs), four exact restores, zero fallbacks, zero capacity
  rejections, and one bounded host-resident generation at shutdown sampling.
- Every OFF run recorded zero offloads, zero restores, zero host-resident
  generations, and an explicit null MOD identity.
- Every ON run published the exact MOD ID, version, experiment flag and
  research-manifest SHA-256.
- Rust coverage separately proves the two-generation capacity rejection and
  restore-failure fail-closed path.

## Frozen identities

- StateAxis: `a52f9d5a3d6caf960f3d200760f1e5f78f9d84d1`
- MOD: `8c882ef9c9867de326d6ec96b24b5e207dc93b77`
- Extension Manager: `00d1b940dc6ce8d60e2cd28708b80d80e9c33a09`
- Research manifest SHA-256:
  `1536c77e8050277113b4f3aa4243ffa3a974c1a5e2df11e46d2c0e0b3b280359`

The first harness attempt is preserved separately at
`/root/stateaxis-evidence/archives/host-tier-ecpa-prelim-off-key-20261010.tar.gz`
(SHA-256 `acee2cfd3fe83bcc2e0402790637106e5aa29c4efbb90a934294b1bba3bdf9d4`).
It stopped during validation because the OFF identity field was omitted instead
of serialized as null; no result was discarded.

The historical real-NPU serialized-prefetch result remains negative. Nothing in
this campaign changes that conclusion or establishes latency, throughput, HBM,
capacity, or production benefit.
