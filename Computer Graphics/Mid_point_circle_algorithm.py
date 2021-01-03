import matplotlib.pyplot as plt

def mid_point_circle(radius):
    x,y = 0,radius
    p = 1.25 - radius

    points = []
    while x <= y:
        points.append( (x,y) )
        # print((x,y),p)
        if p < 0:
            p = p + 2*x +3
        else:
            p = p + 2*(x-y) +5
            y -= 1
        x += 1
    # print(points)

    first_quad      =    [ (y,x) for x,y in points ] + points
    sec_quad        =    [ (-x,y) for x,y in first_quad ]
    third_quad      =    [ (x,-y) for x,y in first_quad ]
    four_quad       =    [ (-x,-y) for x,y in first_quad ]
    circle          =    first_quad + sec_quad + third_quad + four_quad

    # print(first_quad)
    # print('\n')

    # print(sec_quad)
    # print('\n')

    # print(third_quad)
    # print('\n')

    # print(four_quad)
    # print('\n')


    x,y = zip(*circle)
    plt.scatter(x,y)
    plt.show()

if __name__ == "__main__":
    mid_point_circle(23)