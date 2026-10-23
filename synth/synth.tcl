# Run from the repository root with: yosys -c synth/synth.tcl

if {![info exists ::env(PDK_ROOT)]} {
    error "PDK_ROOT is not set. Select the sky130A PDK before synthesis."
}

set lib "$::env(PDK_ROOT)/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib"

if {![file exists $lib]} {
    error "SKY130 typical-corner Liberty file not found: $lib"
}

yosys read_verilog rtl/full_adder.v rtl/mult_array.v
yosys synth -top mult_array -flatten
yosys dfflibmap -liberty $lib
yosys abc -liberty $lib
yosys opt_clean -purge
yosys tee -o synth/mult_array_stat.rpt stat -liberty $lib
yosys write_verilog -noattr synth/mult_array_netlist.v
