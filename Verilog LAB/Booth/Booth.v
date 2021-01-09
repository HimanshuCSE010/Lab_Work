module booth_multiplier(prod, busy, multiplicand, multiplier, clk, start);
	// Input and Output
  	output [15:0] prod;
  	output busy;
	input [7:0] multiplicand, multiplier;
	input clk, start;
  
  	// User defined variables
	reg [7:0] A, Q, M;
	reg Q_1;
	reg [3:0] count;
	wire [7:0] sum, difference;

  always @(posedge clk)
	begin
      	// Initialize the variables 
		if (start) begin
			A <= 8'b0;
			M <= multiplicand;
			Q <= multiplier;
			Q_1 <= 1'b0;
			count <= 4'b0;
		end
      	// Begin booth multiplication
		else begin
          	// Decide the case -> Add or Subtract
			case ({Q[0], Q_1})
            2'b0_1 : {A, Q, Q_1} <= {sum[7], sum, Q};
            2'b1_0 : {A, Q, Q_1} <= {difference[7], difference, Q};
            default: {A, Q, Q_1} <= {A[7], A, Q};
            endcase
		count <= count + 1'b1;
		end
    end
  	
  	alu adder (sum, A, M, 1'b0);
	alu subtracter (difference, A, ~M, 1'b1);
	assign prod = {A, Q};
	assign busy = (count < 8);
  
endmodule


// this help to get sum and difference in two's complement
module alu(out, a, b, cin);
	output [7:0] out;
	input [7:0] a;
	input [7:0] b;
	input cin;
  	// when cin == 0 then sum is given as output 
    // when cout == 1 then differnece is given as output (b here is in one's comp)
	assign out = a + b + cin;
endmodule