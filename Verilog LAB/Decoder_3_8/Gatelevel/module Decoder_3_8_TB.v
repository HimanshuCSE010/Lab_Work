module Decoder_3_8_TB;
 
  	reg [2:0]inp;
  	reg enable;
  	wire [7:0]out;

	Decoder_3_8 Decoder_3_8_inst (
      .inp(inp),
      .enable(enable),
      .out(out)
	);

	initial
		begin
          $dumpfile("decoder_3_8.vcd");
          $dumpvars();
          
          // setting enable = 1
          enable = 1;
          // trying out all inputs
          inp = 3'b000; #10;
          inp = 3'b001; #10;
          inp = 3'b010; #10;
          inp = 3'b011; #10;
          inp = 3'b100; #10;
          inp = 3'b101; #10;
          inp = 3'b110; #10;
          inp = 3'b111; #10;

        end
 
	initial
    	begin
    		$monitor("Input=%b, Output=%b",inp, out);      
        end
endmodule