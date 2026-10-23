# SKY130A physical-design summary

The final fixed-die run completed at a 6.5 ns clock target after seven attempts
at 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, and 6.5 ns. The earlier attempts failed slow-corner
setup checks. The final run completed setup, DRC, and LVS signoff.

| Metric | Final result |
| --- | ---: |
| Die boundary | 150 µm × 150 µm |
| Die area | 22,500 µm² |
| Core area | 17,759.5 µm² |
| Clock period | 6.5 ns |
| Standard-cell area / count | 1,224.92 µm² / 327 |
| Fill / tap cells | 1,550 / 245 |
| Clock / timing-repair buffers | 3 / 17 |
| Routed wirelength | 2,361 µm |
| Worst slow-corner setup slack | 0.14985 ns |
| Post-route frequency estimate | 157.48 MHz |
| Magic / KLayout DRC errors | 0 / 0 |
| LVS errors | 0 |

The post-route frequency estimate is calculated as `1000 / (6.5 - 0.14985)` MHz.
The corresponding detailed metrics are in `metrics.json`; signoff reports are in
`signoff/`.
