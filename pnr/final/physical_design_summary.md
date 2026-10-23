# Physical design summary

## Run configuration

- Flow: LibreLane Classic
- Process: SKY130A, `sky130_fd_sc_hd`
- Clock constraint: 10 ns (100 MHz)
- Input and output delays: 1 ns each
- Floorplan utilization: 30%; placement target density: 40%

## Results

| Metric | Result |
| --- | ---: |
| Die area | 4,416.83 µm² |
| Core area | 2,454.85 µm² |
| Standard-cell area | 969.68 µm² |
| Standard-cell instances | 113 |
| Total placed instances | 318 |
| Total reported power | 0.219 mW |
| Worst setup slack, slow corner (`max_ss_100C_1v60`) | 3.778 ns |
| Worst setup slack, typical corner (`nom_tt_025C_1v80`) | 7.013 ns |
| Setup and hold violations | 0 |
| Magic DRC errors | 0 |
| KLayout DRC errors | 0 |
| LVS device/net differences | 0 |

Power is the flow's reported estimate; no testbench activity file was supplied to
the physical-design flow.

## Generated views

- `gds/mult_array.gds`: final streamout for submission
- `render/mult_array.png`: rendered routed layout
- `metrics.json` and `metrics.csv`: LibreLane run metrics
- `nl/mult_array.nl.v`: final gate-level netlist
- `lef/mult_array.lef` and `def/mult_array.def`: layout abstracts and placement
- `signoff/`: DRC, LVS, and timing summaries

The final flow reported **Passed**, with zero setup violations, zero hold
violations, zero Magic/KLayout DRC errors, and matching LVS circuits.
