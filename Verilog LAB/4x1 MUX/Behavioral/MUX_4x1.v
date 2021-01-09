module MUX_4x1 (
	input wire a,b,c,d,
	input wire s1,s0,
	output reg out
);
	always @(a or b or c or d or s1 or s0)
		begin
			case ({s1,s0})
				2'b00: out = a;
				2'b01: out = b;
				2'b10: out = c;
				2'b11: out = d;
			endcase
		end
endmodule