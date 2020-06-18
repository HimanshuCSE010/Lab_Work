import os
if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

lst1 = list(map(int, input("Enter set element: ").split()))
s1 = set(lst1)
print("set1: ",s1)

lst2 = list(map(int, input("Enter set element: ").split()))
s2 = set(lst2)
print("set2: ",s2)

flag = True
while True and flag:
	clear()
	print("S1: ",s1)
	print("S2: ",s2)
	print("----------------------------------")
	while True:
		print("1. Union")
		print("2. Intersection")
		print("3. S1 - S2")
		print("4. S2 - S1")
		print("5. Modify Sets")
		print("6. Symmetric Difference")
		print("7. Exit")
		n = int(input("Enter choice: "))

		if n == 1:
			print("Union: ",s1|s2)
		elif n == 2:
			print("Intersection: ",s1&s2)
		elif n == 3:
			print("S1-S2: ",s1-s2)
		elif n == 4:
			print("S2-S1: ",s2-s1)
		elif n == 5:
			s1 = set(lst1)
			print("set1: ",s1)
			lst2 = list(map(int, input("Enter set element: ").split()))
			s2 = set(lst2)
			print("set2: ",s2)
		elif n == 6:
			print("S1 ^ S2: ",s1^s2)
		else:
			flag = False
			break
		print("----------------------------------")	
"""
enter ex
1 2 3
4 5 6
"""