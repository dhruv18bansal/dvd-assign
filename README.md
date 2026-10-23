# 4-bit Array Multiplier: RTL to GDSII

## Team

| Team member | Roll number |
| --- | --- |
| Dhruv Bansal | 2023102048 |
| Dataarnoor Singh Oberoi | 2023102047 |

## Part A: RTL design and verification

The multiplier registers its 4-bit inputs and its 8-bit product. The RTL implementation
uses a partial-product array and twelve full-adder instances. The testbench checks all
256 input pairs and writes `mult.vcd`.

Commands run for Part A (from the repository root):

```sh
iverilog -g2012 -o sim tb/tb_mult.v rtl/full_adder.v rtl/mult_array.v
vvp sim
```

Expected successful testbench summary:

```text
PASS: 256 vectors checked, 0 errors
```

Error-detection check: a temporary copy of `full_adder.v` was changed so that the sum
omitted `cin`, then compiled in place of the correct module. The unchanged testbench
reported:

```text
FAIL: 256 vectors checked, 95 errors
```

The source in `rtl/full_adder.v` was not modified by this check. For the required
hand-worked example, Dhruv Bansal's roll number ends in 8, so A = 8 + 5 = 13 and B = 7.
The multiplication is:

```text
       1101  (13)
     x 0111  (7)
     ------
    00001101  pp0
    00011010  pp1, shifted left by 1
    00110100  pp2, shifted left by 2
    00000000  pp3, shifted left by 3
    --------
    01011011  (91)
```

The waveform screenshot remains to be captured and annotated with the two-cycle
latency.

## Part B: logic synthesis

The Yosys flow reads the RTL, flattens the design, maps sequential and combinational
logic to the SKY130 high-density library, writes a cell statistics report, and exports
the mapped netlist.

Command to run inside the assignment's IIC-OSIC-TOOLS environment from the repository
root:

```sh
yosys -c synth/synth.tcl
```

The flow requires `PDK_ROOT` to point to an installation containing the `sky130A`
PDK. Generated outputs are `synth/mult_array_stat.rpt` and
`synth/mult_array_netlist.v`.

The flow was run in IIC-OSIC-TOOLS with `PDK=sky130A`. The resulting report contains
61 cells and a total cell area of 756.976 µm². The design has 16
`sky130_fd_sc_hd__dfrtp_1` flip-flops with 400.384 µm² combined area, or 52.89% of
the total. The most-used cell types are `dfrtp_1` (16), `nand2_1` (7), and
`and2_0` (4); `maj3_1` is tied with `and2_0` at 4 cells.

The synthesized netlist was checked with the assignment's gate-level simulation:

```sh
CELLS="$PDK_ROOT/sky130A/libs.ref/sky130_fd_sc_hd/verilog"
iverilog -g2012 -DFUNCTIONAL '-DUNIT_DELAY=#1' -o gls \
  tb/tb_mult.v "$CELLS/primitives.v" "$CELLS/sky130_fd_sc_hd.v" \
  synth/mult_array_netlist.v
vvp gls
```

Result: `PASS: 256 vectors checked, 0 errors`. The testbench samples 2 ns after the
second active clock edge so the unit-delay standard-cell models have time to settle.
