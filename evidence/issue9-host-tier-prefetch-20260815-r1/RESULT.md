# Historical R1 matched real-NPU result

This is the accepted StateAxis issue #9 prefetch stop-rule gate: Qwen2.5-14B
BF16, TP1, physical Ascend 910B2 NPU3, and one fresh process per arm.

| Metric | Control | Candidate | Delta |
|---|---:|---:|---:|
| Host-tier-hit wall | 596.474 ms | 631.609 ms | +35.135 ms (+5.89%) |
| Concurrent-pair makespan | 619.076 ms | 643.752 ms | +24.675 ms (+3.99%) |
| Prefetch queue wait | 0 | 570.013 ms | +570.013 ms |
| Restore H2D | 2.882 ms | 3.684 ms | +0.802 ms |
| Peak HBM | 44,175 MiB | 44,177 MiB | +2 MiB |
| Measured device overlap | 0 | 0 | none |

Both arms passed exact output, state identity/generation/context and lifecycle
checks. Candidate recorded one prefetch request, one application and zero fallback;
pending work returned to zero. The treatment therefore activated correctly.

The C++ worker processed `ExecuteBatch` synchronously before reading the queued
`RestoreState`, producing 570.013 ms of queue wait and no device transfer/compute
overlap. The preregistered decision rule required stopping after 1+1 in precisely
this case. No performance samples were discarded and running 3+3 would have violated
the frozen protocol.

This supports a workload-scoped historical negative for serialized prefetch only.
It does not show that tiered residency is universally harmful, and it does not
qualify the active v0.2.0 ECPA revision. Async transfer and logical host descriptors
are separate architectural prerequisites.
