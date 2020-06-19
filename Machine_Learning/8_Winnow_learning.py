def update_weight(vector,weights, diff, alpha):
	for i in range(len(vector)):
		if vector[i] == 1:
			weights[i] *= (alpha)**(diff)
	return weights.copy() 

data = [
	# x1, x2, x3  y
	[ [1, 1, 0], [1] ],
	[ [1, 1, 0], [0] ],
	[ [1, 0, 1], [0] ],
	[ [1, 0, 0], [0] ],
	[ [0, 1, 1], [1] ],
	[ [0, 1, 0], [0] ],
	[ [0, 0, 1], [0] ],
	[ [0, 0, 0], [0] ]
]

# initial weights
weights = [1]*len(data[0][0]) # w1 w2 w3 ....
alpha = 2 # let
thereshold = len(weights) - 0.1

def activation_fun(y_in):
	if y_in > thereshold:
		return 1
	else:
		return 0

iteration = 1
print()
while True:
	old_weight = weights.copy()
	print(f"-----------------Iteration {iteration}------------------")
	print("Weights: ",weights)
	print()
	for i in range(len(data)):
		y_in = weights[0]*data[i][0][0] + weights[1]*data[i][0][1] + weights[2]*data[i][0][2]
		a = activation_fun(y_in)
		t = data[i][1][0]
		if t != a:
			weights = update_weight(data[i][0], weights, t-a, alpha)
	
	if old_weight == weights:
		break
	iteration += 1

print("Final Weights are (w1 w2 w3): ",weights)
