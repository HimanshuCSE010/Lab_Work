from math import sin, cos, pi
import numpy as np

def translate_point(point,diff):
	# translate point by a difference 'diff'
	# both are 2D vectors
	x = point[0] + diff[0]
	y = point[1] + diff[1]

	return (x,y)

def scale_point(point,scale):
	# both are 2D vectors
	x = point[0]*scale[0]
	y = point[1]*scale[1]

	return (x,y)

def rotate(points,about,theta,anti_clockwise):
	arr = np.empty((0,3))
	for p in points:
		arr = np.append( arr, np.array([ [p[0],p[1],1] ]), axis = 0 )
	 
	# in case rotation is anti clockwise
	if not anti_clockwise:
		theta = - theta

	# convert theta to radians
	theta = (pi/180)*theta

	a = -about[0]*cos(theta) + about[1]*sin(theta) + about[0]
	b = -about[0]*sin(theta) - about[1]*cos(theta) + about[1]

	T = np.array(
		[
			[cos(theta), sin(theta), 0],
			[-sin(theta), cos(theta), 0],
			[a, b, 1]
		]
	)
	
	res = np.round(np.dot(arr,T), 2) 
	return res

def reflecion_point(point):
	if op == 1:
		x = point[0]
		y = -point[1]
	elif op == 2:
		x = -point[0]
		y = point[1]
	elif op == 3:
		x = -point[0]
		y = -point[1]
	elif op == 4:
		x = point[1]
		y = point[0]
	elif op == 5:
		x = -point[1]
		y = -point[0]
	else:
		print("Choose correct option")

	return (x,y)

def operation():
	print('1. Translate')
	print('2. Scale')
	print('3. Rotation')
	print('4. Reflect')

	i = int(input('Choice: '))
	print('-----------------------------------------------------------')
	return i

def reflect_op():
	print("1. Reflect across X axis")
	print("2. Reflect across Y axis")
	print("3. Reflect across Origin")
	print("4. Reflect across Y = X")
	print("5. Reflect across Y = -X")

	i = int(input('Choice: '))
	print('-----------------------------------------------------------')
	return i

if __name__ == "__main__":
	# give a point and apply different translation

	print('1. Point')
	print('2. Triangle')
	print('3. Square')
	print('4. Polygon')

	print("Choose Type of Input: ")
	choice = int(input())
	print('-----------------------------------------------------------')

	# point only
	if choice == 1:
		op = operation()
		point = tuple(map( float, input("Enter coordinates X Y: ").split() ))
		
		if op == 1:
			diff = tuple(map(float, input('Enter coordinates dx dy: ').split()))
			res = translate_point(point,diff)
		elif op == 2:
			s = tuple(map(float, input('Enter Scale ration for sx sy: ').split()))
			res = scale_point(point, s)
		elif op == 3:
			theta = float(input('Enter shifting angle wrt current position: '))
			clock = bool(input('Rotate Anti-clockwise Yes = 1 No = 0: '))
			about = tuple(map(int, input('Rotate about the point Xa Ya: ').split()))
			res = rotate([point],about,theta,clock)
			res = (res[0][0], res[0][1])
		elif op == 4:	
			res = reflecion_point(point)
		else:
			print('Enter correct operation')
		print('Result: ',res)

	elif choice == 2:
		op = operation()
		p1 = tuple(map( float, input("Enter coordinates X1 Y1: ").split() ))
		p2 = tuple(map( float, input("Enter coordinates X2 Y2: ").split() ))
		p3 = tuple(map( float, input("Enter coordinates X3 Y3: ").split() ))
		
		if op == 1:
			diff = tuple(map(float, input('Enter coordinates dx dy: ').split()))
				
			p1 = translate_point(p1,diff)
			p2 = translate_point(p2,diff)
			p3 = translate_point(p3,diff)
		elif op == 2:
			s = tuple(map(float, input('Enter coordinates sx sy: ').split()))
			
			p1 = scale_point(p1,s)
			p1 = scale_point(p2,s)
			p1 = scale_point(p3,s)
		elif op == 3:
			theta = float(input('Enter shifting angle wrt current position: '))
			clock = bool(input('Rotate Anti-clockwise Yes = 1 No = 0: '))
			about = tuple(map(int, input('Rotate about the point Xa Ya: ').split()))
			
			res = rotate([p1,p2,p3],about,theta,clock)
			p1 = (res[0][0], res[0][1])
			p2 = (res[1][0], res[1][1])
			p3 = (res[2][0], res[2][1])
		elif op == 4:
			p1 = reflecion_point(p1)
			p2 = reflecion_point(p2)
			p3 = reflecion_point(p3)
		else:
			print("Enter correct option")

		print(p1,p2,p3)
	elif choice == 3:
		pass
	elif choice == 4:
		pass
	else:
		print("Make valid choice")
