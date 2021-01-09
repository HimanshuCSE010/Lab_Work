module Decoder_2_4 (
 	input [1:0]inp,
  	input enable,
	output [3:0]out
	);
	
	wire not_i1, noti0;
	not (not_i1,inp[1]);
    not (not_i0,inp[0]);
  
    and (out[0],not_i1,not_i0,enable);
  	and (out[1],not_i1,inp[0],enable);
    and (out[2],inp[1],not_i0,enable);
  	and (out[3],inp[1],inp[0],enable);

endmodule

module Decoder_3_8 (
  	input [2:0]inp,
  	input enable,
  	output [7:0]out
	);
	
	wire not_i2;
	not (not_i2,inp[2]);
  
    Decoder_2_4 A(inp[1:0], not_i2, out[3:0]);
    Decoder_2_4 B(inp[1:0], inp[2], out[7:4]);
  
endmodule