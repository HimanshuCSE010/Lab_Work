module Full_Adder_TB;
	reg A_input, B_input, C_input;
	wire Sum_output,C_output;

	Full_Adder Full_Adder_instance (
		.A(A_input),
		.B(B_input),
		.C_in(C_input),
		.Sum(Sum_output),
		.Carry(C_output)
	);

	initial
		begin
	        $dumpfile("Full_Adder.vcd");
			$dumpvars;

			A_input = 1'b0;
			B_input = 1'b0;
			C_input = 1'b0;
			#10;
			A_input = 1'b0;
			B_input = 1'b0;
			C_input = 1'b1;
			#10;
			A_input = 1'b0;
			B_input = 1'b1;
			C_input = 1'b0;
			#10;
			A_input = 1'b0;
			B_input = 1'b1;
			C_input = 1'b1;
			#10;
			A_input = 1'b1;
			B_input = 1'b0;
			C_input = 1'b0;
			#10;
			A_input = 1'b1;
			B_input = 1'b0;
			C_input = 1'b1;
			#10;
			A_input = 1'b1;
			B_input = 1'b1;
			C_input = 1'b0;
			#10;
			A_input = 1'b1;
			B_input = 1'b1;
			C_input = 1'b1;
          	#10;

		end

endmodule