from Fuzzy_set import print_set, get_set
import os

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

def not_alpha(fs):
	for i,v in fs.items():
		fs[i] = round(1-v, 2)
	return fs

def very_alpha(fs):
	for i,v in fs.items():
		fs[i] = round(v*v,2)
	return fs
def very_very_alpha(fs):
	for i,v in fs.items():
		fs[i] = round(v**4, 2)
	return fs

def plus_alpha(fs):
	for i,v in fs.items():
		fs[i] = round(v**(1.25), 2)
	return fs

def Slightly_alpha(fs):
	for i,v in fs.items():
		fs[i] = round(v*(0.5), 2)
	return fs

def minus_alpha(fs):
	for i,v in fs.items():
		fs[i] = round(v**(0.75), 2)
	return fs

def intensify(fs):
	for i,v in fs.items():
		if v <= 0.5:
			fs[i] = round(2*v*v, 2)
		else:
			fs[i] = round(1 - 2*( 1 - v )**2, 2)
	return fs

if __name__ == "__main__":
	clear()
	print("Fuzzy Rule Base System")
	
	# define a set alpha 
	alpha = get_set("Alpha")
	flag = True

	while flag:
		clear()
		print("Alpha:")
		print_set(alpha)

		while flag:
			print("1. Very α")
			print("2. Very Very α")
			print("3. Plus α")
			print("4. Slightly α")
			print("5. Minus α")
			print("6. Intensify")
			print("7. Not alpha")
			print("8. Quit")
			n = int(input("Enter Choice: "))
			print('-'*30)

			if n == 1:
				print("Very Alpha")
				print_set( very_alpha(alpha) )
			elif n == 2:
				print("Very Very Alpha")
				print_set( very_very_alpha(alpha) )
			elif n == 3:
				print("Plus Alpha")
				print_set( plus_alpha(alpha) )
			elif n == 4:
				print("Slightly Alpha")
				print_set( Slightly_alpha(alpha) )
			elif n == 5:
				print("Minus Alpha")
				print_set( minus_alpha(alpha) )
			elif n == 6:
				print("Intensify Alpha")
				print_set( intensify(alpha) )
			elif n == 7:
				print("Not Alpha")
				print_set(not_alpha(alpha))
			else:
				quit()

"""
Example Input

5
1
1 1
2 0.8
3 0.6
4 0.4
5 0.2

"""