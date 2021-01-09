module Decoder_2_4_TB;
 
	reg [1:0]inp;
  	reg enable;
  	wire [3:0]out;

	Decoder_2_4 Decoder_2_4_inst (
      .inp(inp),
      .enable(enable),
      .out(out)
	);

	initial
		begin
          $dumpfile("decoder_2_4.vcd");
          $dumpvars();
          // initialize with zero value
		  inp = 2'b00;
          enable = 1'b0;
          $display("Enable=%b, Input=%b, Output=%b",enable, inp, out);
          
          // test with new value
          enable = 1;
          inp = 2'b00;
          #10;
          $display("Enable=%b, Input=%b, Output=%b",enable, inp, out);
          
          // new input
          enable = 1;
          inp = 2'b01;
          #10;
          $display("Enable=%b, Input=%b, Output=%b",enable, inp, out);
          
          // new input
          enable = 1;
          inp = 2'b10;
          #10;
          $display("Enable=%b, Input=%b, Output=%b",enable, inp, out);

          // new input
          enable = 1;
          inp = 2'b11;
          #10;
          $display("Enable=%b, Input=%b, Output=%b",enable, inp, out);

          end 
endmodule