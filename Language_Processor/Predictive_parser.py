Parsing_Table = [
    [ ["T","E'"],   ["e1"],     ["e1"],     ["T","E'"],    ['e1'],     ['e1']  ],
    [ ['@'],        ["+","T","E'"],   ['@'],       ['@'],       ['@'],       ['@']    ],
    [ ["F","T'"],   ['e1'],     ['e1'],     ["F","T'"],    ['e1'],     ['e1']  ], 
    [ ['@'],        ['@'],       ["*","F","T'"],   ['@'],       ['@'],       ['@']    ],
    [ ['d'],        ['e1'],     ['e1'],     ["(","E",")"],    ['e1'],     ['e1']  ],
    [ ['pop'],      ['e'],      ['e'],      ['e'],      ['e'],      ['e']   ],
    [ ['e'],        ['pop'],    ['e'],      ['e'],      ['e'],      ['e']   ],
    [ ['e'],        ['e'],      ['pop'],    ['e'],      ['e'],      ['e']   ],
    [ ['e'],        ['e'],      ['e'],      ['pop'],    ['e'],      ['e']   ],
    [ ['e2'],       ['e2'],     ['e2'],     ['e2'],     ['pop'],    ['e2']  ],
    [ ['e3'],       ['e3'],     ['e3'],     ['e3'],     ['e3'],     ['Acc'] ]
]
# used d in place of id
# used @ in place of epsilon

row = { "E": 0, "E'": 1, "T":2, "T'":3, "F":4, "d":5, "+":6, "*":7, "(":8, ")":9, "$": 10 }
col = { "d":0, "+":1, "*":2, "(":3, ")":4, "$":5 }
errors = {
    'e': ["Error","Action: Terminating"],
    'e1': ["Error: Misssing Operand",
            "Action: Adding operand on Input"],
    'e2': ["Error: Missing Right Parenthesis",
            "Action: Dropping Right Parenthesis from Stack"],
    'e3': ["Unexpected input symbol","Action: Terminating"]
}

InputString = input("Enter String to Parse: ") + '$'
ReadPointer = 0
Stack = ['$','E']
ErrorsPresent = False

while True:
    print('-'*80)
    print('Stack: ',''.join(Stack), end='\t\t')
    print('Input: ',InputString[ReadPointer:],end='\t\t')

    InputSym = InputString[ ReadPointer ]
    StackTop = Stack.pop()
    Action = Parsing_Table[ row[ StackTop ] ][ col[ InputSym ] ]
    # print("Action: " + StackTop + '->' + ''.join(Action))

    if Action[0] in errors:
        ErrorsPresent = True
        print("Action: " + StackTop + '->' + ''.join(Action))

        print(errors[ Action[0] ][0])
        print(errors[ Action[0] ][1])
        if Action[0] == 'e1':
            InputString = InputString[:ReadPointer] + 'd' + InputString[ReadPointer:]
            Stack.append( StackTop )
        elif Action[0] == 'e2':
            pass
        else:
            break
    elif Action[0] == 'pop':    # pop symbol from stack
        print(f"Action: pop {StackTop} from stack top")
        ReadPointer += 1
    elif Action[0] == 'Acc':    # accept string
        print("Action: " + StackTop + '->Accepted')
        if ErrorsPresent:
            print("Parsed Completely but Error Present")
        else:
            print("Accepted")
        break
    elif Action[0] == '@':      # epsilon production
        print("Action: " + StackTop + '->' + 'Epsilon')
        pass
    else:                       # push over stack
        print("Action: " + StackTop + '->' + ''.join(Action))
        Stack.extend( Action[::-1] )
