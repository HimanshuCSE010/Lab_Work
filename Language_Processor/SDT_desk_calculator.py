print("----------------------------------------------------SDT Desk Calculator----------------------------------------------------")
col = { '+': 0,	'*': 1,	'(': 2,	')': 3,	'digit': 4, '$': 5, 'E': 6, 'T': 7, 'F': 8 }
grammer = { 'r2': [ 'E','E+T', "int(values[-1]) + int(values[-3])" ], 'r3': [ 'E','T', "values[-1]" ], 'r4': [ 'T','T*F', "int(values[-1]) * int(values[-3])" ], 
        'r5': [ 'T','F', "values[-1]" ], 'r6': [ 'F','(E)', "values[-2]" ], 'r7': ['F','Fd', " str(values[-2])+ str(values[-1])"], 'r8': ['F','d', "values[-1]"] }

# here 'e' means error
# cnf means conflict

Parse_table = [
	[ ['e'],	['e'],	['s4'],	['e'],	['s5'],	['e'],		[1],	[2],	[3]  	],
	[ ['s7'],	['e'],	['e'],	['e'],	['e'],	['acc'],	['e'],	['e'],	['e']  	],
	[ ['r3'],	['s9'],	['e'],	['r3'],	['e'],	['r3'],		['e'],	['e'],	['e']  	],
	[ ['r5'],	['r5'],	['e'],	['r5'],	['cnf'],['r5'],		['e'],	['e'],	['e']  	],
	[ ['e'],	['e'],	['e'],	['e'],	['e'],	['s5'],		[11],	[2],	[3]  	],
	[ ['r8'],	['r8'],	['e'],	['r8'],	['r8'],	['r8'],		['e'],	['e'],	['e']  	],
	[ ['e'],	['e'],	['e'],	['e'],	['e'],	['acc'],	['e'],	['e'],	['e']  	],
	[ ['e'],	['e'],	['s4'],	['e'],	['s5'],	['e'],		['e'],	[8],	[3]  	],
	[ ['r2'],	['s9'],	['e'],	['r2'],['e'],	['r2'],		['e'],	['e'],	[9]  	],
	[ ['e'],	['e'],	['s4'],	['e'],	['s5'],	['e'],		['e'],	['e'],	[10]  	],
	[ ['r4'],	['r4'],	['e'],	['r4'],	['s5'],	['r4'],		['e'],	['e'],	['e']  	],
	[ ['s7'],	['e'],	['e'],	['s12'],['e'],	['e'],		['e'],	['e'],	['e']  	],
    [ ['r6'],	['r6'],	['e'],	['r6'],	['r6'],	['r6'],		['e'],	['e'],	['e']  	],
    [ ['r7'],	['r7'],	['e'],	['r7'],	['r7'],	['r7'],		['e'],	['e'],	['e']  	]   
]

Input_String = input("Enter string to parse id, +, *, (, ), digits: ") + '$'
stack = [0]
values = []
read_pointer = 0

while True:
    a = 'Stack: '+' '.join(map(str, stack))
    b = 'Input: '+ Input_String[read_pointer:]
    print(f'{a:<30} \t\t {b:<20}')

    current_symbol = Input_String[read_pointer]			# Reading symbols from input buffer

    r = stack[-1]
    if current_symbol in '1234567890':
        c = 4
    else:
        c = col[ current_symbol ]	
    move = Parse_table[r][c][0]							# gettting row and column entry for current symbol ans current state

    if move == 'cnf':                                   # removing conflict by deciding action in confliciting situtation
        if Input_String[read_pointer] in '1234567890':
            move = 's13'
        else:
            move = 'r5'

    c = 'Values: '+' '.join(map(str, values))
    d = 'Action: '+move
    print(f'{c:<30} \t\t {d:<20}')
    print('-'*85) 
    if move == 'acc':				# deciding what to do on this move
        print("Accepted")				#accept if move is 'accept'
        print(values.pop())
        break
    elif move[0] == 's':				#shift move
        if current_symbol in '1234567890':
            stack.append('digit')
            values.append(int(current_symbol))
        else:
            stack.append(current_symbol)
            values.append('_')

        stack.append(int(move[1:]))
        read_pointer += 1				# inc read pointer only after shifting a symbol on stack and not while reducing
		
    elif move[0] == 'r':				# reduce move
        red = grammer[move]				# obtain the reducing transaction
        l = len(red[1])    

        temp = eval( red[2] )           # calculating values of attributes
        for i in range(l*2):			# pop out symbols to carry out reduction
            stack.pop()
        for j in range(l):
            values.pop()
        stack.append(red[0])            # apppending to stack the symbol after reduction
        values.append(temp)


        next_state = Parse_table[ stack[-2]  ][ col[stack[-1]] ][0]
        stack.append( next_state )
		

    elif move[0] == 'e':
        print("Not Acceptable")
        break

"""
id+(id*id)
"""