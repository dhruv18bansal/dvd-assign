# 4-bit Array Multiplier: RTL to GDSII

## Team

| Team member | Roll number |
| --- | --- |
| TODO | TODO |
| TODO | TODO |

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

The source in `rtl/full_adder.v` was not modified by this check. The hand-worked
roll-number example and waveform screenshot will be added after the team roll number is
provided and the waveform view is captured.

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
`synth/mult_array_netlist.v`. The netlist simulation and synthesis results table will
be recorded after running this flow in the PDK environment.
