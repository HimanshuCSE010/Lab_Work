module Booth_multiplier_TB;
	reg clk, start;
	reg signed [7:0] A, B;
    wire signed [15:0] AB;
    wire busy;
    booth_multiplier inst(AB, busy, A, B, clk, start);

  	initial begin
      $dumpfile("dump.vcd"); $dumpvars;
      
      clk = 0;
      $display("first example: a = 3 b = 17");
      A = 3; B = 17; start = 1; #50 start = 0;
      #80 $display("A: %d, B: %d, AxB: %d",A,B,AB);
      $display("second example: a = 7 b = 7");
      A = 7; B = 7; start = 1; #50 start = 0;
      #80 $display("A: %d, B: %d, AxB: %d",A,B,AB);
      $finish;
     end
  	
    always #5 clk = !clk;

endmodule