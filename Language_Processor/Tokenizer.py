from collections import defaultdict
print("\n------------identify token only: continue, while, return, identifier------------")

#taking user input
string = input("Enter a string of keywords specified or identifiers: ").split()
print()

#making default dict which return -1 if instead of keyvalue error if key not present
default = defaultdict(lambda: -1, {})

#table which return another dict corresponding to every state and again we query state 
StateTable = {
				-1: default,
				0: defaultdict(lambda: -1, {'w': 1, 'c': 6, 'r': 14}),	#here we return -1 if start char is found other than w,c,r
				1: {'h': 2},
				2: {'i': 3},
				3: {'l': 4},
				4: {'e': 5},
				5: default,
				6: {'o': 7},
				7: {'n': 8},
				8: {'t': 9},
				9: {'i': 10},
				10: {'n': 11},
				11: {'u': 12},
				12: {'e': 13},
				13: default,
				14: {'e': 15},
				15: {'t': 16},
				16: {'u': 17},
				17: {'r': 18},
				18: {'n': 19},
				19: default					
			 }
StateTable = defaultdict(lambda: -1, StateTable)	#for values which are not in dict default value of -1 is returned



for token in string:
	# initializing current state
	CurrentState = 0

	for char in token:
		# scan input character by character and make transition corresponding to every state
		if CurrentState != -1:
			CurrentState = StateTable[CurrentState][char]
		else:
			break
		
	if CurrentState == 5:
		print("KeyWord: while")
	elif CurrentState == 13:
		print("KeyWord: continue")
	elif CurrentState == 19:
		print("KeyWord: return")
	elif CurrentState == -1:
		print("Identifier: ",token)