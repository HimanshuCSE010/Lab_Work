module BCD_Adder_TB;
  reg clk;
  reg [8:0]count;
  wire [3:0] IN_A, IN_B;
  wire CIN;
  wire COUT; 
  wire [3:0]SUM;
 
  
  BCD_Adder inst(COUT, SUM, IN_A, IN_B, CIN);
  
  // initialize variables
  initial
    begin
		clk = 1;
      	count = -1;
    end
  
  // change the clock every 5 ns
  always #5 clk = ~ clk;
  
  // check output for all values of s1 and s0
  always @(posedge clk)
    begin
      	$dumpfile("dump.vcd");
    	$dumpvars;
      
      	count = count + 1;
        if (count[4:1] > 9)
        	count = count + 12;
      	if (count[8:5] > 9)
        	count = 0;
    end
  
  // assign value to inputs
  assign IN_A = count[8:5];
  assign IN_B = count[4:1];
  assign CIN = count[0];
  
  
  // setup monitor to display change in input and output
  // a is LSB and d is MSB
  initial
    begin
      $monitor("A = %d, B = %d, CIN = %d, \t COUT = %d, SUM = %d",IN_A,IN_B,CIN,COUT,SUM);
    end
  
  initial
    begin
      #300 $finish;
    end 
  
endmodule