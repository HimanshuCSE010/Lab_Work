import os
if os.name == 'nt':
	clear = lambda : os.system('cls')
else:
	clear = lambda : os.system('clear')

def reflexive(matrix):
	for i in range(len(matrix)):
		if matrix[i][i] != 1:
			return False
	return True

def symmetric(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if matrix[i][j] != matrix[j][i]:
				return False
	return True

def transitive(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if i != j and matrix[i][j] > 0:
				for k in range(len(matrix)):
					if matrix[i][k] < min( matrix[i][j], matrix[j][k] ):
						return False
	return True
				 

if __name__ == "__main__":
	clear()
	matrix = []
	# getting dimension for rel matrix N*N
	d = int(input("Enter dimension pf N*N relation matrix: "))

	# getting values in relation matrix
	for i in range(d):
		lst = list(map(float, input(f"Enter row {i+1}: ").split()))
		if len(lst) > d:
			print("Enter input as there are number of cols")
			break
		matrix.append( lst )

	r = reflexive(matrix)
	s = symmetric(matrix)
	t = transitive(matrix)

	print("-"*30)
	if r and s and t:
		print("Relation is Equivalence")
	else:
		print("Relation is not Equivalence")
	if r and s and not t:
		print("Relation is Tolerance")
	else:
		print("Relation is not Tolerance")
	print("-"*30)
	
"""
Example Input
5
1 0.8 0 0.1 0.2
0.8 1 0.4 0 0.9
0 0.4 1 0 0
0.1 0 0 1 0.5
0.2 0.9 0 0.5 1

or

5
1 0.8 0.4 0.5 0.8
0.8 1 0.4 0.5 0.9
0.4 0.4 1 0.4 0.4
0.5 0.5 0.4 1 0.5
0.8 0.9 0.4 0.5 1
"""
