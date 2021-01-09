module Decoder_2_4 (
 	input [1:0]inp,
  	input enable,
	output [3:0]out
	);
	
	wire not_i1, noti0;
  	assign not_i1 = ~inp[1];
    assign not_i0 = ~inp[0];
  
	assign out[0] = not_i1 & not_i0 & enable;
  	assign out[1] = not_i1 & inp[0] & enable;
  	assign out[2] = inp[1] & not_i0 & enable;
  	assign out[3] = inp[1] & inp[0] & enable;

endmodule
