# Run from the repository root with: sta -exit sta/sta.tcl
if {![info exists ::env(PDK_ROOT)]} {
    error "PDK_ROOT is not set. Select the sky130A PDK before STA."
}

set lib "$::env(PDK_ROOT)/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib"
set netlist "synth/mult_array_netlist.v"

foreach path [list $lib $netlist] {
    if {![file exists $path]} {
        error "Required STA input not found: $path"
    }
}

read_liberty $lib
read_verilog $netlist
link_design mult_array

set period 10.0
if {[info exists ::env(CLOCK_PERIOD)]} {
    set period $::env(CLOCK_PERIOD)
}
create_clock -name clk -period $period [get_ports clk]
set_input_delay 1.0 -clock clk [delete_from_list [all_inputs] [get_ports clk]]
set_output_delay 1.0 -clock clk [all_outputs]

puts "SKY130A typical-corner timing analysis"
puts "Clock period: $period ns"
puts "Input delay: 1.0 ns; output delay: 1.0 ns"
puts ""
report_checks -path_delay max -format full_clock_expanded -digits 3
report_worst_slack -max
report_worst_slack -min
