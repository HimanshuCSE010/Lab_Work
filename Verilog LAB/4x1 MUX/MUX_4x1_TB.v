module MUX_4x1_TB;
      reg a,b,c,d;
      reg s1,s0;
      wire out;
      MUX_4x1 inst(
            .a (a),
            .b (b),
            .c (c),
            .d (d),
            .s1 (s1),
            .s0 (s0),
            .out (out)
      );
      // initialize variables
      initial
            begin
                  a = 1'b1; b = 1'b1; c = 1'b1; d = 1'b1;
                  s1 = 1'b0; s0 = 1'b0;
                  #100;
            end
            // check output for all values of s1 and s0
            initial
                  begin
                        $dumpfile ( "dump.vcd" );
                        $dumpvars ;
                        // all four variations
                        a = 1'b1; b = 1'b1; c = 1'b1; d = 1'b1;
                        s1 = 1'b0; s0 = 1'b0;
                        #10;
                        a = 1'b1; b = 1'b0; c = 1'b1; d = 1'b1;
                        s1 = 1'b0; s0 = 1'b1;
                        #10;
                        a = 1'b1; b = 1'b1; c = 1'b1; d = 1'b1;
                        s1 = 1'b1; s0 = 1'b0;
                        #10;
                        a = 1'b1; b = 1'b1; c = 1'b1; d = 1'b0;
                        s1 = 1'b1; s0 = 1'b1;
                        #10;
                  end
            
            // setup monitor to display change in input and output
            initial
                  begin
                        $monitor ( "a=%b, b=%b, c=%b, d=%b, s1=%b s0=%b, out=%b" ,a,b,c,d,s1,s0,out);
                  end
endmodule