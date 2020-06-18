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
			if i != j and matrix[i][j] == 1:
				for k in range(len(matrix)):
					if matrix[j][k] == 1 and matrix[i][k] != 1:
						return False
	return True
				 

if __name__ == "__main__":
	clear()
	matrix = []
	# getting dimension for rel matrix N*N
	d = int(input("Enter dimension pf N*N relation matrix: "))

	# getting values in relation matrix
	for i in range(d):
		lst = list(map(int, input(f"Enter row {i+1}: ").split()))
		if len(lst) > d:
			print("Enter input as there are number of cols")
			break
		matrix.append( lst )

	r = reflexive(matrix)
	s = symmetric(matrix)
	t = transitive(matrix)

	if r and s and t:
		print("Relation is Equivalence")
	else:
		print("Relation is not Equivalence")
	if r and s and not t:
		print("Relation is Tolerance")
	else:
		print("Relation is not Tolerance")

"""
Example Input
5
1 1 0 0 0
1 1 0 0 1
0 0 1 0 0
0 0 0 1 0
0 1 0 0 1

or

5
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
"""
