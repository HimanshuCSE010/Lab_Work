print("----------------------------------------------------SLR Parsers----------------------------------------------------")
col = { '+': 0,	'*': 1,	'(': 2,	')': 3,	'id': 4, '$': 5, 'E': 6, 'T': 7, 'F': 8 }
grammer = { 'r1': [ 'E','E+T' ], 'r2': [ 'E','T' ],	'r3': [ 'T','T*F' ], 'r4': [ 'T','F' ],	'r5': [ 'F','(E)' ], 'r6': [ 'F','id' ] }

# here 'e' means error
Parse_table = [
	[ ['e'],	['e'],	['s4'],	['e'],	['s5'],	['e'],		[1],	[2],	[3]  	],
	[ ['s6'],	['e'],	['e'],	['e'],	['e'],	['accept'],	['e'],	['e'],	['e']  	],
	[ ['r2'],	['s7'],	['e'],	['r2'],	['e'],	['r2'],		['e'],	['e'],	['e']  	],
	[ ['r4'],	['r4'],	['e'],	['r4'],	['e'],	['r4'],		['e'],	['e'],	['e']  	],
	[ ['e'],	['e'],	['s4'],	['e'],	['s5'],	['e'],		[8],	[2],	[3]  	],
	[ ['r6'],	['r6'],	['e'],	['r6'],	['e'],	['r6'],		['e'],	['e'],	['e']  	],
	[ ['e'],	['e'],	['s4'],	['e'],	['s5'],	['e'],		['e'],	[9],	[3]  	],
	[ ['e'],	['e'],	['s4'],	['e'],	['s5'],	['e'],		['e'],	['e'],	[10]  	],
	[ ['s6'],	['e'],	['e'],	['s11'],['e'],	['e'],		['e'],	['e'],	['e']  	],
	[ ['r1'],	['s7'],	['e'],	['r1'],	['e'],	['r1'],		['e'],	['e'],	['e']  	],
	[ ['r3'],	['r3'],	['e'],	['r3'],	['e'],	['r3'],		['e'],	['e'],	['e']  	],
	[ ['r5'],	['r5'],	['e'],	['r5'],	['e'],	['r5'],		['e'],	['e'],	['e']  	],
]

Input_String = input("Enter string to parse id, +, *, (, ): ") + '$'
stack = [0]
read_pointer = 0

while True:
	a = 'Stack: ' + ' '.join(map(str, stack))
	b = 'Buffer: '+Input_String[read_pointer:]
	print(f'{a:<40} \t {b:<20}',end='\t')
	current_symbol = Input_String[read_pointer]			# Reading symbols from input buffer
	if current_symbol == 'i':							#if first symbol is 'i' as input character then read 'd' additionally to make 'id'
		current_symbol += 'd'
		read_pointer += 1								#inc pointer by one if char is 'i'

	r = stack[-1]
	c = col[ current_symbol ]	
	move = Parse_table[r][c][0]							# gettting row and column entry for current symbol ans current state
	
	print('Action: ',move)
	print('-'*100)
	if move == 'accept':				# deciding what to do on this move
		print("Accepted")				#accept if move is 'accept'
		break

	elif move[0] == 's':				#shift move
		stack.append(current_symbol)
		stack.append(int(move[1:]))
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
		stack.append( next_state )
		
	elif move[0] == 'e':
		print("Not Acceptable")
		break

"""
check by giving input
id+(id*id) or
id*(id+id)+id
"""