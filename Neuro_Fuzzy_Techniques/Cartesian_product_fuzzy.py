import os
from Fuzzy_set import get_set, print_set

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

def fuzz_product(set1,set2):
	final = []
	for v1 in set1.values():
		temp = []
		for v2 in set2.values():
			temp.append( min(v1,v2) )
		final.append(temp)
	return final

def print_product(set1,set2,product,row='',col=''):
	lst2 = set2.keys()
	# printing matrix
	if len(row) > 0:
		s = f"{row} x {col}"
	else:
		s = ""
	print(f"Fuzzy Cartesian Product : {s}\n")
	# getting header
	header = " | "
	for i in lst2:
		header += f"{i:^4}"
	print(header)

	# printing row by row
	index = 0
	for i in set1.keys():
		string = f'{i}| '+'  '.join(map(str,map(float,product[index])))
		print('_'*len(string))
		print(string)
		index += 1
	print('-'*40+'\n')

if __name__ == "__main__":
	clear()
	set1 = get_set()
	print_set(set1)
	set2 = get_set()
	print_set(set2)

	product = fuzz_product(set1, set2)
	
	print_product(set1,set2,product)
	print( "*" * 30)

"""
Example Input
2
a 0.4
b 0.6
3
c 0.3
d 0.9
e 0.5
"""