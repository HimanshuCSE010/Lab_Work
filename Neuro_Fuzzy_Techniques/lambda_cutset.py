import os
from collections import defaultdict
from Fuzzy_set import get_set, print_set

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

def lambda_cutset(set1,l):
	new = defaultdict(float)
	for i,v in set1.items():
		if v >= l:
			new[i] = v
	return new

while True:
	clear()
	set1 = get_set()
	print_set(set1)
	lambda_value = float(input("Enter lambda value: "))
	print("New Lambda Cut Set: \n")
	print_set(lambda_cutset(set1,lambda_value))
	input()

"""
Example Input
5
2
a 0.2
b 0.5
c 0.9
d 0.25
e 0.35
0.3
"""