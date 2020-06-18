from Fuzzy_set import print_set, get_set, get_universal_set, fuzzy_negation
from Cartesian_product_fuzzy import fuzz_product, print_product
from Operations_Fuzzy_Relation import fuzzy_relation_union
from Fuzzy_logic import sort_Fuzzy_set
from Crisp_Relation_Composition import Min_Max_comp, Max_product_comp
from collections import OrderedDict
import os

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

if __name__ == "__main__":
	clear()
	print("1. Calculate R = (A x B) U (not A x Y)")
	print("2. Calculate B_prime = A_prime x R\n")
	# a is from universe A
	A = get_universal_set("Universal A")
	# getting all elements of universe A even with zero membership
	a = sort_Fuzzy_set(get_set("A"), A)
	a_prime = sort_Fuzzy_set(get_set("A_Prime"), A)
	neg_a = fuzzy_negation(a,A)

	# b from universe Y
	Y = get_universal_set("Universal Y")
	b = sort_Fuzzy_set(get_set("B"), Y)

	while True:
		clear()
		print("A:")
		print_set(a)
		print("Not A:")
		print_set(neg_a)
		print("A_Prime:")
		print_set(a_prime)
		print("B:")
		print_set(b)

		
		# get A x B
		first = fuzz_product(a,b)
		# get not A x Y
		second = fuzz_product( neg_a, Y )

		# R = (A x B) U (not A x Y) = first x second
		print("\nR = (A x B) U (not A x Y)\n")
		R = fuzzy_relation_union( first, second )
		print_product(A,Y,R)

		# get B_Prime = A_Prime x R
		# R is 3 x 3 so A should be 1 x 3 (a 2 D array)
		a_prime_vector = [ [ v for v in a_prime.values() ] ]
		if input("1. Use Min Max Composition 2. Use Max Product Composition: ") == '1':
			b_prime = Min_Max_comp(a_prime_vector, R)
		else:
			b_prime = Max_product_comp(a_prime_vector, R)

		# to print final result
		print("\nY_Prime: ")
		for r in b_prime:
			i = 0
			for ele in Y.keys():
				print(f"{ele}: {r[i]}")
				i += 1

		# just to halt program until user press any key
		n = input("Press any key or q to exit: \n")
		if n == 'q' or n == 'Q':
			break


"""
Example Input

2
x1 x2 x3
3
2
x1 0.1
x2 0.9
x3 0.0
3
2
x1 0.3
x2 1.0
x3 0.0
2
y1 y2 y3
3
2
y1 0
y2 1
y3 0

"""