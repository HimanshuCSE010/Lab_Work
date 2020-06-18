import os

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

if __name__ == "__main__":
	set1 = set(input("Enter elements in first set: ").split())
	set2 = set(input("Enter elements in second set: ").split())
	print("-"*50)
	s = set()
	for e1 in set1:
		for e2 in set2:
			s.add( (e1,e2) )
	for tup in s:
		print(*tup) 
	print("Elements in cartesian product: ",len(s))