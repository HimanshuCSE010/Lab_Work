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
