def DDA(x1,y1,x2,y2):
	from math import floor

	if abs(x1-x2) > abs(y1-y2):
		length = abs(x1-x2)
	else:
		length = abs(y1-y2)

	delta_x = (x2-x1)/length
	delta_y = (y2-y1)/length

	x = x1 + 0.5
	y = y1 + 0.5
	
	set_pixels = []
	i = 1
	while i <= length:
		set_pixels.append( (floor(x),floor(y)) )
		x = x + delta_x
		y = y + delta_y
		i += 1
	return set_pixels

if __name__ == "__main__":
	# in first quad
	
	# initial starting points
	x1,y1 = 0,0
	# final destination points
	x2,y2 = 5,5

	print( DDA(x1,y1,x2,y2) )

	# in third quad
	
	# initial starting points
	x1,y1 = 0,0
	# final destination points
	x2,y2 = -8,-4

	print( DDA(x1,y1,x2,y2) )