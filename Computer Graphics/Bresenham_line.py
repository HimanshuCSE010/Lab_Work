def Bresenham_line(x1,y1,x2,y2):
	from math import floor
	if x1 == x2 and y1 == y2:
		return "Points are equal"

	delta_x = (x2-x1)
	delta_y = (y2-y1)
	m = delta_x/delta_y
	e = m - 0.5
	x,y = x1,y1

	set_pixels = []
	for i in range(1,int(delta_x)+1):
		set_pixels.append( (x,y) )
		while e > 0:
			y += 1
			e -= 1
		x += 1
		e += m

	return set_pixels


if __name__ == "__main__":
	# in first octant
	
	# initial starting points
	x1,y1 = 0,0
	# final destination points
	x2,y2 = 15.55,0

	print( Bresenham_line(x1,y1,x2,y2) )

	# in third octant
	
	# initial starting points
	x1,y1 = 0,0
	# # final destination points
	x2,y2 = -8,-4

	print( Bresenham_line(x1,y1,x2,y2) )