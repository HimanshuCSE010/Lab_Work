module BCD_Adder(
  output reg COUT, 
  output reg [3:0]SUM,
  input [3:0] A, B,
  input CIN
);
  
  reg [4:0]temp;
  
  always @(A,B,CIN)
  begin
    // temp store total sum along with carry
  	temp = A + B + CIN;
    
    if (temp > 9)
    begin
      temp = temp + 6;
    end
    // assign final value to COUT and SUM
    {COUT,SUM} = temp;
  end
  
endmodule