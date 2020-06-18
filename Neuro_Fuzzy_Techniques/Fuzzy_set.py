import os
from collections import OrderedDict

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

def get_universal_set(name = ''):
	s = OrderedDict()
	print("Enter list of objects (Universal Set - No Membership Value)")
	if input("1. Objects are integers \n2. Objects are string literals\n") == '1':
		for i in map(int, input().split()):
			s[i] = 1
	else:
		for i in input().split():
			s[i] = 1
	print('-'*30)
	return s.copy()

def get_set(name = ''):
	while True:
		try:
			print(f"Enter no of element in {name} set: ",end='')
			n = int(input())
			break
		except:
			print("Enter integer number only")
			pass

	s = OrderedDict()
	if input("1. Objects are integers \n2. Objects are string literals\n") == '1':
		while n:
			n -= 1
			a,m = input("Element and Memebership value [0:1] (space seperated): ").split()
			s[int(a)] = float(m)
	else:
		while n:
			n -= 1
			a,m = input("Element and Memebership value [0:1] (space seperated): ").split()
			s[a] = float(m)
	print('-'*30)
	return s.copy()

def print_set(d):
	print(f"{'Element'} -> {'Membership'}")
	for i,v in d.items():
		print(f'{i:^7} -> {v:^10}')
	print('-'*30+'\n')

def fuzzy_union(a,b):
	temp = OrderedDict()
	for i,v in a.items():
		if i in b:
			temp[i] = max(v, b[i])
		else:
			temp[i] = v
	for i,v in b.items():
		if i not in temp:
			temp[i] = v
	return temp

def fuzzy_intersection(a,b):
	temp = OrderedDict()
	for i in a.keys():
		temp[i] = 0
	for i in b.keys():
		temp[i] = 0
	for i,v in a.items():
		if i in b:
			temp[i] = min(v, b[i])
	return temp

def fuzzy_negation(a,u):
	temp = OrderedDict()
	for i in u:
		if i in a:
			temp[i] = round(1-a[i],1)
		else:
			temp[i] = 1
	return temp
def fuzzy_difference(a,not_b):
	return fuzzy_intersection(a,not_b)

if __name__ == "__main__":
	set1 = get_set("First")
	set2 = get_set("Second")
	U = get_universal_set("Universal")
	flag = True
	while True and flag:
		clear()
		print("Set 1: ")
		print_set(set1)
		print("Set 2:")
		print_set(set2)
		print("Universal: ")
		print_set(U)
		print("-"*50)

		while True:
			print("1. Union")
			print("2. Intersection")
			print("3. Not S1")
			print("4. Not S2")
			print("5. S1 | S2")
			print("6. S2 | S1")
			print("7. Modify Sets")
			print("8. Exit")
			n = int(input("Enter choice: "))
			print('\n')
			if n == 1:
				print_set(fuzzy_union(set1, set2))
			elif n == 2:
				print_set(fuzzy_intersection(set1,set2))
			elif n == 3:
				print_set(fuzzy_negation(set1,U))
			elif n == 4:
				print_set(fuzzy_negation(set2,U))
			elif n == 5:
				print_set(fuzzy_difference(set1, fuzzy_negation(set2, U)))
			elif n == 6:
				print_set(fuzzy_difference(set2, fuzzy_negation(set1, U)))
			elif n == 7:
				set1 = get_set()
				set2 = get_set()
				universal = set(input("Enter elements in Universal set: ").split())
			else:
				flag = False
				break
			print("-"*30)	

"""
Example Input
3
2
a 0.3
b 0.6
c 0.7
2
2
d 0.2
e 0.9
2
a b c d e f

"""
