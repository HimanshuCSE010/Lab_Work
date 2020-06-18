from math import sqrt

def normalize_doc_vector(vector):
	d = 0
	for i in vector:
		d += i**2
	d = sqrt(d)

	for i in range(len(vector)):
		vector[i] = round(vector[i]/d, 2)
	return vector

def main():
	data = []
	doc_no = int(input("Enter number of documnet: "))
	vocabulary = input("Enter terms as vocabulary (space seperated): ").split()

	print("\nEnter 0 or 1 as accordingly as vocabulary term present in document")
	print("In sequence: ",*vocabulary,'\n')
	for i in range(doc_no):
		vector = list(map(int,input(f"DocID: {i+1}: ").split() ))
		data.append( normalize_doc_vector(vector) )
	test_doc = normalize_doc_vector( list(map(int, input("Test Doc: ").split())) )

	# to print normalized document vectors
	# print("\nResulting Normalized Document Vectors: ")
	# for i in range(len(data)):
	# 	print(f"Doc {i+1}: ",*data[i])

	pos_docs = list(map(int, input("Enter DocID for positive Class (μc): ").split()))
	neg_docs = list(map(int, input("Enter DocID for negative Class (not_μc): ").split()))

	# getting μc for pos doc class
	μc = [0]*len(vocabulary)
	for i in pos_docs:
		for j in range(len(vocabulary)):
			μc[j] += data[i-1][j]
	for j in range(len(vocabulary)):
		μc[j] = round(μc[j]/len(pos_docs), 2)

	
	# getting not_μc for pos doc class
	not_μc = [0]*len(vocabulary)
	for i in neg_docs:
		for j in range(len(vocabulary)):
			not_μc[j] += data[i-1][j]
	for j in range(len(vocabulary)):
		not_μc[j] = round(not_μc[j]/len(neg_docs), 2)

	print("\n    μc: ",*μc)
	print("not_μc: ",*not_μc)

	# assigning class to test doc
	for i in range(len(vocabulary)):
		μc[i] -= test_doc[i]
		not_μc[i] -= test_doc[i]
	
	pos = 0
	for ele in μc:
		pos += ele**2
	pos = round(sqrt(pos), 2)

	neg = 0
	for ele in not_μc:
		neg += ele**2
	neg = round(sqrt(neg), 2)

	print("Positive Class distance from test vector: ",pos)
	print("Negative Class distance from test vector: ",neg)

	print("\nResult:-")
	if pos > neg:
		print("Test Doc belong to μc Class")
	elif neg > pos:
		print("Test Doc belong to not_μc Class")
	else:
		print("Can't Classify") 


if __name__ == "__main__":
	main()

"""
4
Chinese Japan Tokyo Macao Beijing Shanghai
0 0 0 0 1 0
0 0 0 0 0 1
0 0 0 1 0 0
0 1 1 0 0 0
0 1 1 0 0 0
1 2 3
4
"""