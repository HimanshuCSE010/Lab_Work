module half_adder_tb;
 
	reg r_BIT1 = 0;
	reg r_BIT2 = 0;
	wire w_SUM;
	wire w_CARRY;

	half_adder half_adder_inst (
		.in1(r_BIT1),
		.in2(r_BIT2),
		.sum(w_SUM),
		.carry(w_CARRY)
	);

	initial
		begin
			$dumpfile("halfadder.vcd");
			$dumpvars;
			r_BIT1 = 1'b0;
			r_BIT2 = 1'b0;
			#10;
			r_BIT1 = 1'b0;
			r_BIT2 = 1'b1;
			#10;
			r_BIT1 = 1'b1;
			r_BIT2 = 1'b0;
			#10;
			r_BIT1 = 1'b1;
			r_BIT2 = 1'b1;
			#10;
		end 
endmodule // half_adder_tb