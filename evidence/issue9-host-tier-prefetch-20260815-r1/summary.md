# Issue #9 host-tier prefetch 1+1 gate

- control host-hit wall: 596474010 ns
- candidate host-hit wall: 631609474 ns
- delta (candidate-control): 35135464 ns
- candidate actor-inflight: 0 ns
- candidate prefetch queue wait / H2D: 570012882 / 3684058 ns
- peak HBM control/candidate: 44175 / 44177 MiB
- exact/lifecycle: pass in both arms
- device transfer overlap: not measured; the zero actor-inflight completion and 570 ms queue wait show the restore remained behind the serial worker boundary
- logical capacity scaling: not measured
- speedup claim: none
- conclusion: negative; candidate regressed host-hit latency by 35135464 ns (5.89%) and pair makespan by 24675320 ns; per preregistration no 3+3 is run
