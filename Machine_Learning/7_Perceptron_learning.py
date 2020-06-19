def activation_fun(y_in):
	if y_in > 0:
		return 1
	else:
		return 0

def update_weight(vector,weights, learning_rate, y_in):
	temp = learning_rate*(vector[1][0] - activation_fun(y_in))

	weights[0] = weights[0] + temp*vector[0][0]
	weights[1] = weights[1] + temp*vector[0][1]
	weights[2] = weights[2] + temp
	return weights 

data = [
	# x1,x2,b  y
	[ [1, 1, 1], [1] ],
	[ [1, 0, 1], [0] ],
	[ [0, 1, 1], [0] ],
	[ [0, 0, 1], [0] ]
]

# initial weights
weights = [0.1,0.2,0.3] # w1 w2 b
learning_rate = 0.5

while True:
	Modified = False
	for i in range(len(data)):

		# calculate y_in = w1*x1 + w2*x2 + w0*b
		y_in = weights[0]*data[i][0][0] + weights[1]*data[i][0][1] + weights[2]*data[i][0][2]
		
		# update weights
		new_weights = update_weight(data[i], weights, learning_rate, y_in)
		if new_weights != weights:
			Modified = True
		weights = new_weights.copy()

	if not Modified:
		break

print("Final Weights are (w1 w2 b): ",*weights)