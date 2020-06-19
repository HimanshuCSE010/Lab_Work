def main():
	no_weights = int(input("Enter number of weights: "))
	
	weights = [0]*no_weights
	print("\nEnter integer weights")
	for i in range(no_weights):
		weights[i] = int(input(f"{i+1}: "))
	
	inputs = [0]*no_weights
	print("\nEnter inputs (1 and -1 only)")
	for i in range(no_weights):
		inputs[i] = int(input(f"{i+1}: "))

	thresh = int(input("Enter Threshhold Value: "))
	
	# getting y_in
	y_in = 0
	for i in range(no_weights):
		y_in += weights[i]*inputs[i]

	print("Y_in : ",y_in)
	if y_in >= thresh:
		print("Output: 1 Neuron Fires")
	else:
		print("Output: 2 Neuron do not fires")

if __name__ == "__main__":
	main()

"""
Example Input (copy and paste in terminal while running program)

3
1
2
3
1
0
0
3

"""