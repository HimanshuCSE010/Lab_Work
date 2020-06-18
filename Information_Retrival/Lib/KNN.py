from math import sqrt

def normalize_doc_vector(vector):
	d = 0
	for i in vector:
		d += i**2
	d = sqrt(d)

	for i in range(len(vector)):
		vector[i] = round(vector[i]/d, 2)
	return vector

def vector_dist_eucledian(t,d):
	s = 0
	for i in range(len(t)):
		s += abs(t[i]-d[i])**2
	return round(sqrt(s), 3)

def main():
	data = []
	doc_no = int(input("Enter number of documnet: "))
	vocabulary = input("Enter terms as vocabulary (space seperated): ").split()

	print("\nEnter 0 or 1 as accordingly as vocabulary term present in document")
	print("In sequence: ",*vocabulary,'\n')
	for i in range(doc_no):
		vector = list(map(int,input(f"DocID: {i+1}: ").split() ))
		doc_class = input("Class of document: ")
		data.append( [normalize_doc_vector(vector), doc_class])
	test_doc = normalize_doc_vector( list(map(int, input("Test Doc: ").split())) )

	# to print normalized document vectors
	# print("\nResulting Normalized Document Vectors: ")
	# for i in range(len(data)):
	# 	print(f"Doc {i+1}: ",*data[i])

	# calculating eucledian distance 
	for i in range(len(data)):
		data[i] = [ vector_dist_eucledian(data[i][0], test_doc) , data[i][1] ]
	
	# getting top k nearest neighbour
	k = int(input("Enter the value of K for KNN classification: "))
	data.sort(key = lambda x: x[0])
	data = data[:k]

	# printing k neighbour
	print(f"\n{k} Nearest Neighbour: ")
	print(f"{'Eucledian Distance':<20} {'Class'}")
	for d,c in data:
		print(f"{d:^20} {c}")

	# getting number of class having max occurance in k NN 
	neighbours = {}
	for v,c in data:
		if c in neighbours:
			neighbours[c] += 1
		else:
			neighbours[c] = 1
	m = max(neighbours.values())

	# collecting all classes of 
	assigned_class = []
	for i,v in neighbours.items():
		if v == m:
			assigned_class.append(i)
	print("\nClass Assigned is: ",*assigned_class)


if __name__ == "__main__":
	main()

"""
4
Chinese Japan Tokyo Macao Beijing Shanghai
0 0 0 0 1 0
positive
0 0 0 0 0 1
positive
0 0 0 1 0 0
positive
0 1 1 0 0 0
negative
0 1 1 0 0 0
1
"""