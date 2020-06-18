import os

if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')


def print_matrix(M):
	for row in M:
		print(*row)
	print()

def Min_Max_comp(X,Y):
	print("Min-Max Composition: ")
	Matrix = []
	for row in range(len(X)):
		Matrix.append([])
		for col in range(len(Y[0])):
			temp = []
			for j in range(len(X[0])):
				temp.append( min( X[row][j], Y[j][col] ) )
			Matrix[row].append( max(temp) )
	return Matrix

def Max_product_comp(X,Y):
	print("Max Product Composition: ")
	Matrix = []
	for row in range(len(X)):
		Matrix.append([])
		for col in range(len(Y[0])):
			temp = []
			for j in range(len(X[0])):
				temp.append( X[row][j] * Y[j][col] )
			Matrix[row].append( max(temp) )
	return Matrix

if __name__ == "__main__":
	clear()
	print("Relation X: ")
	X = [
		[1,0.8,0.4,0.2,0.8],
		[0.8,1,0.4,0.5,0.9],
		[0.4,0.4,1,0,0.4],
		[0.2,0.5,0,1,0.5],
		[0.8,0.9,0.4,0.5,1]
	]
	
	print_matrix(X)

	print("Relation Y: ")
	Y = [
		[1,0.8,0.4,0.2,0.8],
		[0.8,1,0.4,0.5,0.9],
		[0.4,0.4,1,0,0.4],
		[0.2,0.5,0,1,0.5],
		[0.8,0.9,0.4,0.5,1]
	]
	print_matrix(Y)

	while True:
		print("1. Min-Max Composition")
		print("2. Max Product Composition")
		print("3. Exit")
		n = int(input("Enter choice: "))
		print('\n')
		if n == 1:
			
			print_matrix( Min_Max_comp(X,Y) )
		elif n == 2:
			print_matrix( Max_product_comp(X,Y) )
		else:
			break
		print("-"*30)
