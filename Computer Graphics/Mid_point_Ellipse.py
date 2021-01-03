import matplotlib.pyplot as plt

def mid_point_ellipse(a,b):
    """ x-axis and y-axis """
    points = []
    # make variable to save computation
    b_sq = b*b
    a_sq = a*a

    # initialize x and y points
    x, y = 0, b

    # precalculate dx and dy
    dx = 2*x*b_sq
    dy = 2*y*a_sq

    # p1 : decision parameter for first region
    p1 = int(b_sq + (a_sq)/4 - a_sq*b)

    while dx < dy:
        # plot the point
        points.append( (x,y) )

        # if current point is inside the ellipse 
        if p1 < 0:
            # choose next point horizontally
            x += 1
            dx = dx + 2*b_sq
            p1 = p1 + dx + b_sq
        
        # else if current point is outside or on the ellipse
        else:
            # choose next point digonally
            y -= 1
            x += 1
            dx = dx + 2*b_sq
            dy = dy - 2*a_sq
            p1 = p1 + dx - dy + b_sq

    # decision parameter for second region
    p2 = int(b_sq*(x + 0.5)**2 + a_sq*(y-1)**2 - a_sq*b_sq)

    # keep calculating till we reach end of first quad
    while y > 0:
        points.append( (x,y) )

        # if current point is outside ellipse
        if p2 > 0:
            # select point vertically downward
            y -= 1
            dy = dy - 2*a_sq 
            p2 = p2 - dy + a_sq
        
        # if current point lies inside or on the ellipse
        else:
            # diagonal point
            x += 1
            y -= 1
            dy = dy - 2*a_sq
            dx = dx + 2*b_sq
            p2 = p2 + dx - dy + a_sq
        

    # print(points)

    first_quad      =    [ (y,x) for x,y in points ]
    sec_quad        =    [ (-x,y) for x,y in first_quad ]
    third_quad      =    [ (x,-y) for x,y in first_quad ]
    four_quad       =    [ (-x,-y) for x,y in first_quad ]
    ellipse         =    first_quad + sec_quad + third_quad + four_quad

    # print(first_quad)
    # print('\n')

    # print(sec_quad)
    # print('\n')

    # print(third_quad)
    # print('\n')

    # print(four_quad)
    # print('\n')

    x,y = zip(*ellipse)
    plt.scatter(x,y,s=5)
    plt.show()

if __name__ == "__main__":
    # mid_point_ellipse(40,25)
    mid_point_ellipse(16,9)