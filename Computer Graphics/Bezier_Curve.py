import numpy as np
import bezier 
import matplotlib.pyplot as plt

# define all point 
nodes = np.asfortranarray([
	[1,3,-1,2],	# x coordinate
	[1,0,0,-2]	# y coordinate
])

# define degree of curve
curve = bezier.Curve(nodes,degree=3)

x = []
y = []
# here third value define a step or we can pass custome value of t
# in a lst and iterate over it
# lst_t = [0.0,0.25,0.5,0.75,1.0]

# for t in lst_t:
for i in np.arange(0.0,1.0,0.05):	# to use custom lst_t comments this
# for i in [0.0,0.25,0.5,0.75]:
	t = round(i,2)					# this too
	x_t, y_t = curve.evaluate(t)
	x_t, y_t = round(x_t[0],3), round(y_t[0],3)

	# uncomment to get value of points at each value of t
	print(f"t = {t} \t x = {x_t} \t y = {y_t}")
	
	x.append( x_t )
	y.append( y_t )

if t != 1.0:
	t = 1.0
	x_t, y_t = curve.evaluate(t)
	x_t, y_t = round(x_t[0],3), round(y_t[0],3)

	# uncomment to get value of points at each value of t
	print(f"t = {t} \t x = {x_t} \t y = {y_t}")
	
	x.append( x_t )
	y.append( y_t )

plt.plot(x,y,'.',color='r',mew=2)
plt.axis()
plt.grid()
plt.show()

plt.plot(x,y,color='r',mew=2)
plt.show()

