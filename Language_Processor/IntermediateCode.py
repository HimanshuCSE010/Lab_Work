print("----------------------------------------------------Intermediate Code Generator----------------------------------------------------")
col = { '+': 0,	'*': 1,	'(': 2,	')': 3,	'id': 4, '$': 5, 'E': 6, 'T': 7, 'F': 8 }
grammer = { 'r1': [ 'E','E+T', "values[-3]+'+'+values[-1]"], 'r2': [ 'E','T', "values[-1]" ],	'r3': [ 'T','T*F', "values[-3]+'*'+values[-1]" ], 
		'r4': [ 'T','F', "values[-1]" ],	'r5': [ 'F','(E)', "values[-2]"], 'r6': [ 'F','id', "values[-1]" ] }

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
# seperating the part which need to get assigned from the part which evalustion
# spliting the expression from = sign
i = Input_String.index('=')
last = Input_String[:i+1]
Input_String = Input_String[i+2:]

stack = [0]
read_pointer = 0
values = []
result = []
count = 0

while True:
	a = 'Stack: ' + ' '.join(map(str, stack))
	b = 'Buffer: '+Input_String[read_pointer:]
	print(f'{a:<30} \t {b:<20}')
	current_symbol = Input_String[read_pointer]			# Reading symbols from input buffer
	
	if current_symbol not in '*-+()$':
		temp = current_symbol
		current_symbol = 'id'

	r = stack[-1]
	c = col[ current_symbol ]	
	move = Parse_table[r][c][0]							# gettting row and column entry for current symbol ans current state
	
	d = 'Place: '+' '.join(values)
	e = "Action: "+move
	print(f"{d:<30} \t {e:<20}")
	print('-'*80)
	
	if move == 'accept':				# deciding what to do on this move
		print("Accepted")				#accept if move is 'accept'
		result.append( last+' t'+str(count))		# appending the final code
		break

	elif move[0] == 's':				#shift move
		stack.append(current_symbol)
		stack.append(int(move[1:]))
		read_pointer += 1				#inc read pointer only after shifting a symbol on stack and not while reducing
		
		if current_symbol == 'id':
			values.append(temp)
		else:
			values.append('_')

	elif move[0] == 'r':				#reduce move
		red = grammer[move]				#obtain the reducing transaction
		if red[1][0] == 'i':			#deciding length of RHS so that we can pop 2*l symbol from stack
			l = 1						# len = 1 if LHS is id 
		else:
			l = len(red[1])				#otherwise len is amount of symbol 
			
		for i in range(l*2):			#pop out symbols to carry out reduction
			stack.pop()

		if move in 'r1 r3':
			count += 1
			add = eval(red[2])
			result.append('t'+str(count)+' = '+add)

			for i in range(l):
				values.pop()
			values.append('t'+str(count))
		else:
			add = eval(red[2]) 
			for i in range(l):
				values.pop()
			values.append(add)


		stack.append(red[0])
		next_state = Parse_table[ stack[-2] ][ col[stack[-1]] ][0]
		stack.append( next_state )
		
	elif move[0] == 'e':
		print("Not Acceptable")
		break
print("----Intermediate Code----")
for code in result:
	print(code)
"""
check by giving input
id+(id*id) or
id*(id+id)+id
"""