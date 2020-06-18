print("---------------------------Shift Reduce---------------------------")

"""
Expression Grammer
S -> AA
A -> aA/b
"""

Parse_Table = [
    [ ['s3'],   ['s4'],     ['e'],      [2],    [1]   ],
    [ ['e'],     ['e'],     ['accept'], ['e'],  ['e'] ],
    [ ['s3'],   ['s4'],     ['e'],      [5],    ['e'] ],
    [ ['s3'],   ['s4'],     ['e'],      [6],    ['e'] ],
    [ ['r3'],   ['r3'],     ['r3'],     ['e'],  ['e'] ],
    [ ['e'],     ['e'],     ['r1'],     ['e'],  ['e'] ],
    [ ['r2'],   ['r2'],     ['r2'],     ['e'],  ['e'] ]
]
col = { 'a': 0,	'b': 1,	'$': 2,	'A': 3,	'S': 4 }
grammer = { 'r1': [ 'S','AA' ], 'r2': [ 'A','aA' ],	'r3': [ 'A','b' ] }

Input_String = input("Enter string to parse (using symbol a,b): ") + '$'
stack = [0]
read_pointer = 0

while True:
    print('Stack: \t\t',stack)
    print('Buffer: \t',Input_String[read_pointer:])
    current_symbol = Input_String[read_pointer]

    r = stack[-1]
    c = col[ current_symbol ]
    move = Parse_Table[r][c][0]
    
    print('Action: \t',move)
    print('***********************************************************************************') 
    if move == 'accept':				# deciding what to do on this move
        print("Accepted")				#accept if move is 'accept'
        break

    elif move[0] == 's':				#shift move
        stack.append(current_symbol)
        stack.append( int(move[1]) )
        read_pointer += 1				#inc read pointer only after shifting a symbol on stack and not while reducing
		
    elif move[0] == 'r':				#reduce move
        red = grammer[move]				#obtain the reducing transaction
        l = len( red[1] )
        for i in range(l*2):			#pop out symbols to carry out reduction
            stack.pop()
			
        stack.append(red[0])
        next_state = Parse_Table[ stack[-2] ][ col[stack[-1]] ][0]
        stack.append( next_state )
		
    elif move[0] == 'e':
        print("Not Acceptable")
        break

"""
Example Input
aabb
"""
