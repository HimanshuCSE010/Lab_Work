def sign(x,y):
	if x == y:
		return 0
	if x < y:
		return -1
	else:
		return 1

def Bresenham_line(x1,y1,x2,y2):
	from math import floor
	if x1 == x2 and y1 == y2:
		return "Points are equal"

	x,y = x1,y1
	delta_x = abs(x2-x1)
	delta_y = abs(y2-y1)
	s1 = sign(x2,x1)
	s2 = sign(y2,y1)
	interchange = 0

	if delta_y > delta_x:
		delta_x, delta_y = delta_y, delta_x
		interchange = 1

	error = 2*delta_y - delta_x
	set_pixel = []

	for i in range(1,int(delta_x)+1):
		set_pixel.append((x,y))
		# print( (x,y), error )
		while error > 0:
			if interchange:
				x += s1
			else:
				y += s2
			error = error - 2*delta_x
		
		if interchange:
			y += s2
		else:
			x += s1
		error += 2*delta_y
	
	return set_pixel

if __name__ == "__main__":
	# in first octant
	
	# initial starting points
	x1,y1 = 7.5,0
	# final destination points
	x2,y2 = 7.5,13

	for p in Bresenham_line(x1,y1,x2,y2):
		print(p)
	print('\n')

	# in third octant
	
	# initial starting points
	x1,y1 = 0,0
	# # final destination points
	x2,y2 = -8,-4

	for p in Bresenham_line(x1,y1,x2,y2):
		print(p)
	print('\n')