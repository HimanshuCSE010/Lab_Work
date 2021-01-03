import matplotlib.pyplot as plt
	
def plot(points):
	x,y = zip(*points)
	plt.scatter(x,y)
	plt.show()


def Bresenhem_Circle(radius):
	x,y = 0,radius	
	delta = 3 - 2*radius
	up = []
	down = []

	while x <= y:
		up.append( (x,y) )
		down.append( (y,x) )
		# print((x,y),delta)
		if delta < 0:
			delta = delta + 4*x + 6
		else:
			delta = delta + 4*(x-y) + 10
			y -= 1
		x += 1
	# print(up)

	first 	= up + down[::-1]
	sec 	= [(-x,y) for x,y in first]
	third	= [(-x,-y) for x,y in first]
	four	= [(x,-y) for x,y in first]
	circle = first + sec + third + four
	
	for p in first:
		print(p)
	# plot(first)
	plot(circle)
	

if __name__ == "__main__":
	radius = 20
	Bresenhem_Circle(radius)