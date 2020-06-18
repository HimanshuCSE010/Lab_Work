from Fuzzy_set import print_set, get_set, get_universal_set, fuzzy_negation
from Cartesian_product_fuzzy import fuzz_product, print_product
from Operations_Fuzzy_Relation import fuzzy_relation_union
from collections import OrderedDict
import os

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

def sort_Fuzzy_set(s,U):
	temp = OrderedDict()
	for i in sorted(U.keys()):
		if i not in s:
			temp[i] = 0
		else:
			temp[i] = s[i]
	del s
	return temp

if __name__ == "__main__":
	clear()
	print("Fuzzy Logic: IF A THEN B ELSE C [ R = ( × B) ∪ (not A × C) ]\n")
	# a is from universe A
	A = get_universal_set("Universal A")
	# getting all elements of universe A even with zero membership
	a = get_set("A")
	a = sort_Fuzzy_set(a,A)
	neg_a = fuzzy_negation(a,A)

	# b and c are from universe Y
	Y = get_universal_set("Universal Y")
	b = get_set("B")
	b = sort_Fuzzy_set(b,Y)
	
	c = get_set("C")
	c = sort_Fuzzy_set(c,Y)

	while True:
		clear()
		print("A")
		print_set(a)
		print("Not A")
		print_set(neg_a)
		print("B")
		print_set(b)
		print("C")
		print_set(c)

		n = input("Press any key or q to exit: \n")
		if n == 'q' or n == 'Q':
			break
		else:		
			first = fuzz_product(a,b)
			print_product(a,b,first,'A','B')

			second = fuzz_product( neg_a, c )
			print_product(neg_a,c,second,'Not A','C')

			print("\nIF A THEN B ELSE C\n")
			R = fuzzy_relation_union( first, second )
			print_product(A,Y,R,)
		input()
		print("-"*30)	

"""
Example Input

1
1 2 3 4
3
1
2 0.6
3 1
4 0.2
1
1 2 3 4 5 6
4
1
2 0.4
3 1
4 0.8
5 0.3
6
1
1 0.3
2 0.5
3 0.6
4 0.6
5 0.5
6 0.3

"""