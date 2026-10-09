# Issue #9 host-tier prefetch closure — 2026-08-15

> **Document role: point-in-time report, not current repository status or a task
> assignment.** Current classification and priorities live only in
> [`NATIVE_ENGINE_STATUS.md`](../../NATIVE_ENGINE_STATUS.md).

## Decision

Close Issue #9's current single-worker prefetch candidate as a matched negative.
The generation-safe directory and default-off serving authority are valid and
remain useful, but the candidate did not satisfy the issue's asynchronous
overlap, latency, HBM, logical-capacity or repeated-campaign acceptance.

This is not a claim that exact tiered residency is impossible. The experiment
identified two architectural prerequisites that are outside this candidate:
an out-of-order transfer-capable worker ([#76](https://github.com/Qixin-Gaoke/statecentric-ascend-engine/issues/76))
and logical host-state descriptors that do not consume device slots
([#77](https://github.com/Qixin-Gaoke/statecentric-ascend-engine/issues/77)).
Cross-instance policy remains separately tracked by #20.

## What was implemented

- A generation-qualified host-tier directory with explicit `offloading`,
  `host_resident` and `restoring` transitions, location epochs, exact byte counts
  and payload SHA-256 binding.
- A default-off prefetch authority that requires the existing host-tier and
  response-first gates, coalesces the same state generation, waits for the exact
  restore acknowledgement before admission, and fails closed on stale or
  malformed completion.
- Bounded telemetry for requests, coalescing, applied/fallback outcomes, pending
  count, queue wait and actor-inflight time. Actor-inflight is explicitly not
  treated as device overlap.

Default-off behavior and the existing device-resident/queued-restore control
remain unchanged. The offline Rust gate passes 233 library tests and all binaries pass
`cargo check --offline`.

## Frozen real-NPU evidence

The preregistered `issue9-host-tier-prefetch-20260815-r1` gate used the local
official `.23` image digest, dynamically selected NPU3 from all AICore-idle cards
by maximum free HBM, and ran one fresh control and one fresh candidate process
with the same Qwen2.5-14B weights, artifact, prompt, oracle, capacity and request
ordering. The experiment container was removed and NPU/process/port cleanup was
recorded.

| Metric | control | candidate | candidate - control |
|---|---:|---:|---:|
| host-tier-hit wall | 596.474 ms | 631.609 ms | +35.135 ms (+5.89%) |
| concurrent-pair makespan | 619.076 ms | 643.752 ms | +24.675 ms |
| prefetch queue wait | 0 | 570.013 ms | +570.013 ms |
| restore H2D | 2.882 ms | 3.684 ms | +0.802 ms |
| peak HBM | 44,175 MiB | 44,177 MiB | +2 MiB |
| prefetch request/applied/fallback | 0/0/0 | 1/1/0 | treatment active |

Both arms passed exact output, state identity/generation/context and lifecycle
checks. Candidate pending returned to zero and retained two host states totaling
50,331,648 bytes. The Rust backend observed two requests in flight, but the C++
worker handles an `ExecuteBatch` frame synchronously before reading the queued
`RestoreState`; consequently actor-inflight completion was zero and no device
transfer-compute overlap was measured.

The preregistration required stopping after 1+1 when prefetch remained only
worker-queued, lacked device overlap, or failed to improve host-hit latency.
Running 3+3 after this result would violate that decision rule, so no runs were
discarded and no additional performance samples were collected.

## Claim boundary and provenance

The valid conclusion is negative: this single-worker prefetch mechanism is
slower and provides no measured HBM or capacity benefit. There is no speedup,
2x-capacity, 8K/16K, cross-runtime or vLLM superiority claim.

Raw evidence is preserved under
`results/issue9-host-tier-prefetch-20260815-r1-gate/`. The frozen run names source
commit `6bfd865372d0a489ec3b8dc53eaea8bd5b778253`; rebasing its two Issue #9 commits
onto the reviewed main tree changed only ancestry. The implementation diff has
the same stable patch ID `ccdcfd39895d181aeefa7bea27308bfc43e4b7f8` before and
after rebase, while binary, runner, workload, preregistration and artifact hashes
remain frozen in the checked-in identity manifest.
