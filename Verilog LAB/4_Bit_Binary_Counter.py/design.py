module Four_bit_Binary_Counter (
  input clk, rst,
  output reg [3:0] count    
);

// reset here is posedge triggred
always @ (posedge(clk), posedge(rst))
begin
  // reset if rst = 1
  if (rst) count <= 0;
  // reset to zero if count reached its limit
  else if (count == 4'b1111) count <= 0;
  // count increase by 1
  else count <= count + 1;
end
endmodule