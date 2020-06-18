def show_matrix(matrix):
	for i in range(len(matrix)):
		print('\t'.join(map(str,matrix[i])))

def editDist(str1,str2,col,row): 
	matrix = [ [0 for i in range(col+1)] for j in range(row+1) ]

	for j in range(col+1):
		matrix[0][j] = j
	for i in range(row+1):
		matrix[i][0] = i

	for i in range(1,row+1):
		for j in range(1,col+1):
			matrix[i][j] = min( 
				matrix[i-1][j-1] + 1-(str1[j-1] == str2[i-1]), 
				matrix[i-1][j]+1, 
				matrix[i][j-1]+1 )
	show_matrix(matrix)
	return matrix[row][col]

def main():
	str1 = input("Enter 1st string: ")
	str2 = input("Enter 2nd string: ")
	col = len(str1)
	row = len(str2)
	print('Edit Distance: ',editDist(str1,str2,col,row) )

if __name__ == "__main__":
	main()