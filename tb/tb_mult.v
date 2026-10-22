`timescale 1ns/1ps

module tb_mult;
    reg clk = 1'b0;
    reg rst_n = 1'b0;
    reg [3:0] a = 4'b0;
    reg [3:0] b = 4'b0;
    wire [7:0] p;

    integer ai, bi;
    integer errors = 0;
    integer checked = 0;

    mult_array dut (.clk(clk), .rst_n(rst_n), .a(a), .b(b), .p(p));
    always #5 clk = ~clk;

    initial begin
        $dumpfile("mult.vcd");
        $dumpvars(0, tb_mult);

        repeat (2) @(posedge clk);
        @(negedge clk);
        rst_n = 1'b1;

        for (ai = 0; ai < 16; ai = ai + 1) begin
            for (bi = 0; bi < 16; bi = bi + 1) begin
                @(negedge clk);
                a = ai[3:0];
                b = bi[3:0];
                @(posedge clk);
                @(posedge clk);
                #1;
                checked = checked + 1;
                if (p !== (ai * bi)) begin
                    errors = errors + 1;
                    $display("Mismatch: a=%0d b=%0d expected=%0d got=%0d", ai, bi, ai*bi, p);
                end
            end
        end

        if (errors == 0)
            $display("PASS: %0d vectors checked, %0d errors", checked, errors);
        else
            $display("FAIL: %0d vectors checked, %0d errors", checked, errors);
        $finish;
    end
endmodule
