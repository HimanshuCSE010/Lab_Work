data = [
	# x1   x2  t
	[ [1 , 1],[-1] ],
	[ [1 ,-1],[1 ] ],
	[ [-1, 1],[1 ] ],
	[ [-1,-1],[-1] ]
]

def activating_fun(value):
	if value > 0:
		return 1
	else:
		return -1

def main():
	print("\n*****    Many Adaptive Linear Neuron (MADLINE)    *****\n")
	
	# fixing learning rate
	learning_rate = 0.5
	input_output = [0, 0, 0, 0, 0, 0] # z1_in, z2_in, z1, z2, y_in, y_out
	weights = [0.05, 0.2, 0.3, 0.1, 0.2, 0.15, 0.5, 0.5, 0.5] # w11 w21 b1 w12 w22 b2 v1 v2 b3  
	
	print(f"{'w11':<7} {'w21':<7} {'b1':<7} {'w12':<7} {'w22':<7} {'b2':<7}")
	for i in range(len(data)):
		train, test = data[i]
		test = test[0]

		input_output[0] = round( train[0]*weights[0] + train[1]*weights[1] + weights[2], 3 )	# calculating z1_in
		input_output[1] = round( train[0]*weights[3] + train[1]*weights[4] + weights[5], 3 )	# calculating z2_in
		input_output[2] = round( activating_fun( input_output[0] ), 3 )
		input_output[3] = round( activating_fun( input_output[1] ), 3 )
		input_output[4] = round( input_output[2]*weights[6] + input_output[3]*weights[7] + weights[8], 3 )
		input_output[5] = round( activating_fun( input_output[4] ), 3 )

		if input_output[5] != test:
			if test == 1:
				if abs(input_output[0]) < abs(input_output[1]):
					weights[0] = round( weights[0] + learning_rate * ( 1 - input_output[0] ) * train[0], 3 )
					weights[1] = round( weights[1] + learning_rate * ( 1 - input_output[0] ) * train[1], 3 )
					weights[2] = round( weights[2] + learning_rate * ( 1 - input_output[0] ), 3 )
				else:
					weights[3] = round(weights[3] + learning_rate * ( 1 - input_output[1] ) * train[0], 3 )
					weights[4] = round(weights[4] + learning_rate * ( 1 - input_output[1] ) * train[1], 3 )
					weights[5] = round(weights[5] + learning_rate * ( 1 - input_output[1] ), 3 )
			
			elif test == -1:
				if input_output[0] > 0:
					weights[0] = round( weights[0] + learning_rate * ( -1 - input_output[0] ) * train[0], 3 )
					weights[1] = round( weights[1] + learning_rate * ( -1 - input_output[0] ) * train[1], 3 )
					weights[2] = round( weights[2] + learning_rate * ( -1 - input_output[0] ), 3 )

				if input_output[1] > 0:
					weights[3] = round(weights[3] + learning_rate * ( -1 - input_output[1] ) * train[0], 3 )
					weights[4] = round(weights[4] + learning_rate * ( -1 - input_output[1] ) * train[1], 3 )
					weights[5] = round(weights[5] + learning_rate * ( -1 - input_output[1] ), 3 )
					
			else:
				print("t is neither 1 not -1")
				break
		print(f"{weights[0]:<7} {weights[1]:<7} {weights[2]:<7} {weights[3]:<7} {weights[4]:<7} {weights[5]:<7}")

	print("\nFinal Weights: ")
	print(f"{'w11':<7} {'w21':<7} {'b1':<7} {'w12':<7} {'w22':<7} {'b2':<7}")
	print(f"{weights[0]:<7} {weights[1]:<7} {weights[2]:<7} {weights[3]:<7} {weights[4]:<7} {weights[5]:<7}")

if __name__ == '__main__':
	main()
