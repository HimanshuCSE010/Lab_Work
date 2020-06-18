import os

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')


def print_matrix(M):
	for row in M:
		print(*row)
	print()

def crips_relation_union(X,Y):
	Matrix = []
	for row in range(len(X)):
		temp = []
		for col in range(len(X[0])):
			temp.append( max( X[row][col], Y[row][col] ) )
		Matrix.append( temp )
	return Matrix

def crips_relation_intersection(X,Y):
	Matrix = []
	for row in range(len(X)):
		temp = []
		for col in range(len(X[0])):
			temp.append( min( X[row][col], Y[row][col] ) )
		Matrix.append( temp )
	return Matrix

def Negation(X):
	Matrix = []
	for row in range(len(X)):
		temp = []
		for col in range(len(X[0])):
			temp.append( 1-X[row][col] )
		Matrix.append( temp )
	return Matrix

def containment(X,Y):
	flag = True
	for row in range(len(X)):
		for col in range(len(X[0])):
			if X[row][col] > Y[row][col]:
				flag = False
				break
	return flag

if __name__ == "__main__":
	clear()
	print("Relation X: ")
	X = [
		[1,0,1,0],
		[0,1,0,1],
		[1,1,1,1],
		[0,0,0,0]
	]
	print_matrix(X)

	print("Relation Y: ")
	Y = [
		[0,0,0,1],
		[1,0,0,0],
		[1,0,1,0],
		[1,0,1,1]
	]
	print_matrix(Y)

	while True:
		print("1. Union")
		print("2. Intersection")
		print("3. X Complement")
		print("4. Y Complement")
		print("5. Containment X in Y")
		print("6. Containment Y in X")
		print("7. Exit")
		n = int(input("Enter choice: "))
		print('\n')
		if n == 1:
			print("Union: ")
			print_matrix( crips_relation_union(X,Y) )
		elif n == 2:
			print("Intersection: ")
			print_matrix( crips_relation_intersection(X,Y) )
		elif n == 3:
			print("X Complement: ")
			print_matrix( Negation(X) )
		elif n == 4:
			print("Y Complement: ")
			print_matrix( Negation(Y) )
		elif n == 5:
			if containment(X,Y):
				print("X contains in Y")
			else:
				print("X do not contains in Y")
		elif n == 6:
			if containment(Y,X):
				print("Y contains in X")
			else:
				print("Y do not contains in X")
		else:
			break
		print("-"*30)	