module Four_bit_Binary_Counter_TB;
  reg clk;
  reg rst;
  wire [3:0]count;
  
  Four_bit_Binary_Counter inst(clk,rst,count);
  
  // reset the circuit and initialize variable
  initial
    begin
		clk = 1;
      	rst = 1;
      	#2;
      	rst = 0;
    end
  
  initial
    begin
      $dumpfile("dump.vcd");
      $dumpvars;
    end
  
  // change the clock every 5 ns
  always #5 clk = ~ clk;
  
  // setup monitor to display change in input and output
  initial
    begin
      $monitor("time = %0t \t count = %d",$time,count);
    end
  
  initial
    begin
      #200 $finish;
    end 
  
endmodule