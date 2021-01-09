module Full_Adder (
	input A,B,C_in,
	output Sum,Carry
	);
	wire w1,w2,w3;
	xor (w1,A,B);			// HA Sum
  	xor (Sum,w1,C_in);		// FA Sum
	and (w2,A,B);			// HA Carry
	and (w3,w1,C_in);
  	or (Carry,w3,w2);		// FA Carry
endmodule