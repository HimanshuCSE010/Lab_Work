from Fuzzy_set import get_set, print_set
from Cartesian_product_fuzzy import get_set, print_set, fuzz_product, print_product
from Crisp_Relation_Composition import Min_Max_comp, Max_product_comp
import os
import sys

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

if __name__ == "__main__":
	set1 = get_set("First")
	set2 = get_set("Second")
	set3 = get_set("Third")

	while True:
		clear()

		# get 3 sets to make relation by cross product
		print_set(set1)
		print_set(set2)
		print_set(set3)

		# obtain cartesian product
		prod1 = fuzz_product(set1, set2)
		prod2 = fuzz_product(set2, set3) 

		print("Cartesian Product of set1 and set2: ")
		print_product(set1, set2, prod1, 'set1', 'set2' )
		print("Cartesian Product of set2 and set3: ")
		print_product(set2, set3, prod2, 'set2', 'set3' )

		print("1. Max-Min Composition")
		print("2. Max Product Composition")
		print("3. Exit")
		n = int(input("Enter choice: "))
		
		if n == 1:
			print_product(set1, set3, Min_Max_comp(prod1, prod2), 'prod1', 'prod2')
		elif n == 2:
			print_product(set1, set3, Max_product_comp(prod1,prod2), 'prod1', 'prod2')
		else:
			break
		buffer = input()
		print("-"*30)	

"""
Example input
2
2
a 0.6
b 0.3
3
2
c 0.2
d 0.8
e 0.5
2
2
f 0.9
g 0.7
"""