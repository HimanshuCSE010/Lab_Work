print("---------------------------Operator Precedence Parser---------------------------\n")

"""
Expression Grammer
E -> E+E
E -> E*E
E -> (E)
E -> D      # D for id
"""

Precedence_Table = [
    [ ['>'], ['>'], ['<'], ['<'], ['<'], ['<'], ['<'], ['>'], ['>'], ],
    [ ['>'], ['>'], ['<'], ['<'], ['<'], ['<'], ['<'], ['>'], ['>'], ],
    [ ['>'], ['>'], ['>'], ['>'], ['<'], ['<'], ['<'], ['>'], ['>'], ],
    [ ['>'], ['>'], ['>'], ['>'], ['<'], ['<'], ['<'], ['>'], ['>'], ],
    [ ['>'], ['>'], ['>'], ['>'], ['<'], ['<'], ['<'], ['>'], ['>'], ],
    [ ['>'], ['>'], ['>'], ['>'], ['e'], ['e'], ['e'], ['>'], ['>'], ],
    [ ['<'], ['<'], ['<'], ['<'], ['<'], ['<'], ['<'], ['='], ['e'], ],
    [ ['>'], ['>'], ['>'], ['>'], ['>'], ['e'], ['e'], ['>'], ['>'], ],
    [ ['<'], ['<'], ['<'], ['<'], ['<'], ['<'], ['<'], ['e'], ['e'], ]
]
index = { '+': 0,	'-': 1,	'*': 2,	'/': 3,	'^': 4, 'D': 5, '(': 6, ')': 7, '$': 8 }
grammer = { 'E+E':'E', 'E*E':'E', '(E)':'E', 'D':'E' }
valid = True

Input_String = input("Enter string to parse (using symbol a,b): ") + '$'
stack = ['$']
read_pointer = 0

while read_pointer < len(Input_String):
    print('-------------------------------')
    print('Stack: ',''.join(stack), end='\t')
    print('Input: ',Input_String[read_pointer:],end='\t')

    stack_top = stack[-1]
    Input_sym = Input_String[read_pointer]
    operator = Precedence_Table[ index[stack_top] ][ index[Input_sym] ][0]
    print("Action: " + stack_top + ' ' + operator + ' ' + Input_sym)
    
    if stack[-1] == '$' and Input_sym == '$':
        break
    elif operator == 'e':
        valid = False
        break
    elif operator == '>':
        while True:
            stack_top = stack.pop()
            operator = Precedence_Table[ index[stack[-1]] ][ index[stack_top] ][0]
            if operator == '<':
                break
    else:       # < =
        stack.append(Input_sym)
        read_pointer += 1


print()
if valid:
    print("Accepted")
else:
    print("String do not belong to this grammer or have error")
