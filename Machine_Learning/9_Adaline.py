data = [
   # x0 x1 x2
	[1, 1, 1],
	[1, 1,-1],
	[1,-1, 1],
	[1,-1,-1]
]

target = [-1,1,-1,-1]
length = len(data)
error = [0]*length

def main():
	print("*****    Adaptive Linear Neuron (ADLINE)    *****\n")
	learning_rate = float(input("Enter learning rate: "))
	weight = list(map(float,input("Enter 3 weight W0 W1 W2: ").split()))
	MSE_current = 0
	MSE_old = MSE_current

	i = 0
	Flag = True
	while True and Flag:
		i += 1
		for j in range(length):
			Net = weight[0]*data[j][0] + weight[1]*data[j][1] + weight[2]*data[j][2]
			if Net != target[j]:
				#update weights
				weight[0] = weight[0] + learning_rate * ( target[j] - Net )*data[j][0]
				weight[1] = weight[1] + learning_rate * ( target[j] - Net )*data[j][1]
				weight[2] = weight[2] + learning_rate * ( target[j] - Net )*data[j][2]
				error[j] = (target[j] - Net)**2
		MSE_old = MSE_current
		MSE_current = sum(error)/length
		print('_'*45)
		print('Result of iteration: ',i)
		print('Weights W0 W1 W2: ',*weight)
		print('MSE:', MSE_current)
		if abs(MSE_current) < 0.1 or abs(MSE_current - MSE_old) < 0.001:	#accuracy of 3 decimal places
			Flag = False
			break

if __name__ == '__main__':
	main()

"""
Example Input

0.2
0.2 0.2 0.2

"""