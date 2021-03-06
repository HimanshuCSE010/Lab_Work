module MUX_4x1 (
	input a,b,c,d,
	input s1,s0,
	output out
);
	wire w1,w2,w3,w4, s0_bar, s1_bar;
	not (s0_bar,s0);
	not (s1_bar,s1);
	and (w1,a,s0_bar,s1_bar);
	and (w2,b,s0,s1_bar);
	and (w3,c,s0_bar,s1);
	and (w4,d,s0,s1);
	// combine the result of all four output
	or (out,w1,w2,w3,w4);
endmodule