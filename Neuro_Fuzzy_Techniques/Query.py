import os
from Fuzzy_Rule_Base import very_alpha, very_very_alpha, not_alpha, plus_alpha
from Fuzzy_Rule_Base import Slightly_alpha, minus_alpha, intensify
from Fuzzy_set import get_set, print_set
from collections import OrderedDict

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

def ask_query(query):
	# sets dictionary contain many fuzzy sets used in dictionary
	sets = {}

	# split string and check words not in keyword
	for q in query.split():
		if q .lower() not in ['and','or','not','very','intensely','plus','minus','slightly']:
			print(f"Define set: {q}")
			sets[q] = get_set(q)
	clear()
	# small = OrderedDict({1:1, 2:0.8, 3:0.6, 4:0.4, 5:0.2})
	# large = OrderedDict({1:0.2, 2:0.4, 3:0.6, 4:0.8, 5:1})

	# seperate the string based on 'or' occurance 
	or_seperated = query.split('or')

	# all values are set to 0 so that we can combine (using max operator) different or result 
	or_set = OrderedDict({1: 0, 2: 0, 3: 0, 4: 0, 5: 0})

	# iterate on each component seperated in 'or' split
	for q_or in or_seperated:
		print('*'*50)
		print("OR Clause: ",q_or)

		# seperate each of the or query on 'and' occurance
		and_seperated = q_or.strip().split('and')

		# all values are set to 1 so that we can combine different and result 
		and_set = OrderedDict({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})

		# iterate on each of the and seperated query
		for q_and in and_seperated:
			print("\tAND Clause: ",q_and.strip())
			
			# spliting or clause further by 'and' values
			words = q_and.split()

			# checking for not prefix in clause
			if words[0] == 'not':
				not_prefix = True
				words.pop(0)
			else:
				not_prefix = False

			if len(words) == 3: 
					if words[0] == 'very' and words[1] == 'very':
						temp =  very_very_alpha( sets[words[2]] )
			elif len(words) == 2:
					if words[0] == 'very':
						temp = very_alpha( sets[words[1]] )
					elif words[0] == 'plus':
						temp = plus_alpha( sets[words[1]] )
					elif words[0] == 'slightly' or words[0] == 'slight':
						temp = Slightly_alpha( sets[words[1]] )
					elif words[0] == 'minus':
						temp = minus_alpha( sets[words[1]] )
					elif words[0] == 'intensify':
						temp = intensify( sets[words[1]] )
			elif len(words) == 1:
					temp = sets[words[0]]

			# if not is present in brgining than obtaing negation
			if not_prefix:
				temp = not_alpha(temp) 

			for i,v in temp.items():
				and_set[i] = min(and_set[i], v)
			print("\nResult of this AND clause: ")
			print_set(and_set)

		for i,v in and_set.items():
			or_set[i] = max(or_set[i], v)
		print('*'*50)

	print("\nFinal result: ")
	print_set(or_set)


if __name__ == "__main__":
	clear()
	query = input("Write a query: ")
	ask_query(query)


"""

not very small and not very very large
5
1
1 1
2 0.8
3 0.6
4 0.4
5 0.2
5
1
1 0.2
2 0.4
3 0.6
4 0.8
5 1

"""