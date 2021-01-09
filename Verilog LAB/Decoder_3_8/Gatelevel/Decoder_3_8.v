module Decoder_3_8 (
  	input [2:0]inp,
  	input enable,
  	output [7:0]out
	);
	
  wire inp_2, inp_1, inp_0;
  not (inp_2,inp[2]);
  not (inp_1,inp[1]);
  not (inp_0,inp[0]);
  
  assign out[0] = inp_2 & inp_1 & inp_0 & enable;
  assign out[1] = inp_2 & inp_1 & inp[0] & enable;
  assign out[2] = inp_2 & inp[1] & inp_0 & enable;
  assign out[3] = inp_2 & inp[1] & inp[0] & enable;
  assign out[4] = inp[2] & inp_1 & inp_0 & enable;
  assign out[5] = inp[2] & inp_1 & inp[0] & enable;
  assign out[6] = inp[2] & inp[1] & inp_0 & enable;
  assign out[7] = inp[2] & inp[1] & inp[0] & enable;
endmodule