module mult_array (
    input  wire       clk,
    input  wire       rst_n,
    input  wire [3:0] a,
    input  wire [3:0] b,
    output reg  [7:0] p
);
    reg [3:0] a_reg;
    reg [3:0] b_reg;

    wire [3:0] pp [0:3];
    wire [3:0] row [0:3];
    wire [3:0] row_sum [1:3];
    wire [4:0] carry [1:3];

    genvar i, j;
    generate
        for (i = 0; i < 4; i = i + 1) begin : partial_products
            assign pp[i] = a_reg & {4{b_reg[i]}};
        end
    endgenerate

    assign row[0] = {1'b0, pp[0][3:1]};

    generate
        for (i = 1; i < 4; i = i + 1) begin : adder_rows
            assign carry[i][0] = 1'b0;
            for (j = 0; j < 4; j = j + 1) begin : adders
                full_adder fa (
                    .a(pp[i][j]),
                    .b(row[i-1][j]),
                    .cin(carry[i][j]),
                    .sum(row_sum[i][j]),
                    .cout(carry[i][j+1])
                );
            end
            assign row[i] = {carry[i][4], row_sum[i][3:1]};
        end
    endgenerate

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            a_reg <= 4'b0;
            b_reg <= 4'b0;
            p     <= 8'b0;
        end else begin
            a_reg <= a;
            b_reg <= b;
            p     <= {carry[3][4], row_sum[3][3:1], row_sum[3][0],
                      row_sum[2][0], row_sum[1][0], pp[0][0]};
        end
    end
endmodule
