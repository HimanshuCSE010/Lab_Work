from collections import defaultdict

def main():
	data = []
	doc_no = int(input("Enter number of documnet: "))
	print("")

	for i in range(doc_no):
		data.append( input(f"DocID: {i+1}: ").split() )
	test_doc = input("Test Doc: ").split()

	pos_docs = list(map(int, input("Enter DocID for positive Class : ").split()))
	neg_docs = list(map(int, input("Enter DocID for negative Class : ").split()))

	pos_dict = defaultdict(int)
	neg_dict = defaultdict(int)
	for i in pos_docs:
		for ele in data[i-1]:
			pos_dict[ele] += 1
	
	for i in neg_docs:
		for ele in data[i-1]:
			neg_dict[ele] += 1
	
	vocabulary = set(pos_dict.keys())
	for e in neg_dict.keys():
		vocabulary.add(e)
	vocabulary = len(vocabulary)
	
	# class probability
	pos = len(pos_docs)/doc_no 
	neg = len(neg_docs)/doc_no
	print("")
	print("Positive Class Prior: ",pos)
	print("Negative Class Prior: ",neg)


	pos_class_len = sum(pos_dict.values())
	neg_class_len = sum(neg_dict.values())

	# for pos class
	for word in test_doc:
		# print(word,(pos_dict[word]+1),'/',(vocabulary + pos_class_len))
		pos *= (pos_dict[word]+1)/(vocabulary + pos_class_len)

	# for neg class
	for word in test_doc:
		# print(word, (neg_dict[word]+1),'/',(vocabulary + neg_class_len) )
		neg *= (neg_dict[word]+1)/(vocabulary + neg_class_len)

	print("Positive Class Score: ",pos)
	print("Negative Class Score: ",neg)

	print("\nResult:-")
	if pos > neg:
		print("Test Doc belong to positive Class")
	elif neg > pos:
		print("Test Doc belong to negative Class")
	else:
		print("Can't Classify") 


if __name__ == "__main__":
	main()

"""
4
Chinese Beijing Chinese
Chinese Chinese Shanghai
Chinese Macao
Tokyo Japan Chinese
Chinese Chinese Chinese Tokyo Japan
1 2 3
4
"""