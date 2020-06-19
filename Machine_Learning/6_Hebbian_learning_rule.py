def update_weight(vector,weights):
	weights[0] = weights[0] + vector[0][0]*vector[1][0]
	weights[1] = weights[1] + vector[0][1]*vector[1][0]
	weights[2] = weights[2] + vector[1][0]
	return weights 

data = [
	# x1,x2,b  y
	[ [1,  1, 1], [1] ],
	[ [1, -1, 1], [-1] ],
	[ [-1, 1, 1], [-1] ],
	[ [-1,-1, 1], [-1] ]
]

weights = [0,0,0] # w1 w2 b

for i in range(len(data)):
	weights = update_weight(data[i], weights)

print("Final Weights are (w1 w2 b): ",*weights)