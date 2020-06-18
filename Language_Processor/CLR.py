print("----------------------------------------------------CLR Parsers----------------------------------------------------")
col = { 'id': 0,	'+': 1,	'*': 2,	'$': 3,	'E': 4, 'T': 5, 'F': 6 }
grammer = { 'r1': [ 'E','E+T' ], 'r2': [ 'E','T' ],	'r3': [ 'T','T*F' ], 'r4': [ 'T','F' ],	'r5': [ 'F','id' ] }

# here 'e' means error
Parse_table = [
	[ ['s4'],	['e'],	['e'],	['e'],	[1],	[2],		[3],	 	],
	[ ['e'],	['s5'],	['e'],	['Acc'],[1],	['e'],		['e'],		],
	[ ['e'],	['r2'],	['s6'],	['r2'],	['e'],	['e'],		['e'],		],
	[ ['e'],	['r4'],	['r4'],	['r4'],	['e'],	['e'],		['e'],		],
	[ ['e'],	['r5'],	['r5'],	['r5'],	['e'],	['e'],		['e'],	 	],
	[ ['s4'],	['e'],	['e'],	['e'],	['e'],	[7],		[3],		],
	[ ['s4'],	['e'],	['e'],	['e'],	['e'],	['e'],		[8],	 	],
	[ ['e'],	['r1'],	['s6'],	['r1'],	['e'],	['e'],		['e'],	 	],
	[ ['e'],	['r3'],	['r3'],	['r3'],['e'],	['e'],		['e'],		],
]

Input_String = input("Enter string to parse id, +, *: ") + '$'
stack = [0]
read_pointer = 0

while True:
    print('-'*80)
    a = 'Stack: ' + ' '.join(map(str, stack))
    b = 'Input: ' + Input_String[read_pointer:]
    print(f"{a:<30}\t\t{b:<20}", end = '\t')

    current_symbol = Input_String[read_pointer]			# Reading symbols from input buffer
    if current_symbol == 'i':							#if first symbol is 'i' as input character then read 'd' additionally to make 'id'
        current_symbol += 'd'
        read_pointer += 1								#inc pointer by one if char is 'i'

    r = stack[-1]                                       # getting state on top of stack
    c = col[ current_symbol ]	
    move = Parse_table[r][c][0]							# gettting row and column entry for current symbol ans current state
	
    print('Action: ',move)
    if move == 'Acc':				# deciding what to do on this move
        print("Accepted")				#accept if move is 'accept'
        break

    elif move[0] == 's':				#shift move
        stack.append(current_symbol)
        stack.append(int(move[1]))
        read_pointer += 1				#inc read pointer only after shifting a symbol on stack and not while reducing
		
    elif move[0] == 'r':				#reduce move
        red = grammer[move]				#obtain the reducing transaction
        if red[1][0] == 'i':			#deciding length of RHS so that we can pop 2*l symbol from stack
            l = 1						# len = 1 if LHS is id 
        else:
            l = len(red[1])				#otherwise len is amount of symbol 

        for i in range(l*2):			#pop out symbols to carry out reduction
            stack.pop()
			
        stack.append(red[0])
        next_state = Parse_table[ stack[-2] ][ col[stack[-1]] ][0]
        if next_state == 'e':
            print('Error')
            break
        stack.append( next_state )
		
    elif move[0] == 'e':
        print("Not Acceptable")
        break

"""
check by giving input
id+id*id or
id*id+id*id 
"""