CENTER  = 0     # 0000
LEFT    = 1     # 0001
RIGHT   = 2     # 0010
TOP     = 8     # 1000
BOTTOM  = 4     # 0100

def region(clip,point):
    code = CENTER
    x,y = point
    x_min,y_min,x_max,y_max = clip

    if x <  x_min:
        code = code | LEFT
    if x > x_max:
        code = code | RIGHT
    if y < y_min:
        code = code | BOTTOM
    if y > y_max:
        code = code | TOP

    return code

def Cohen_Sutherland(clip,point):
    """ Line clipping algotithm """
    # clip = Tuple() x_min, y_min, x_max, y_max
    # points = ( x1,y1,x2,y2 ) same order as clip, min in x must be at x_min

    # coordinates of line
    x1,y1,x2,y2 = point
    # coordinate of clip
    x_min,y_min,x_max,y_max = clip

    c1 = region(clip, (x1,y1))
    c2 = region(clip, (x2,y2))

    while True:
        # completely inside
        if c1 == 0 and c2 == 0:
            return (x1,y1,x2,y2)
        # compeletely outside
        elif c1 & c2 != 0:
            return ()
        # partially inside
        else:
            # select one end which is outside of clip
            if c2 != 0:
                out = c2
            else:
                out = c1
            # place holder variable which holds value of modified end points
            x = y = 0

            slop = (y2-y1)/(x2-x1)
            if out & LEFT:
                # outside point below x_min then make x to x_min
                y = slop*(x_min - x1) + y1
                x = x_min
            elif out & RIGHT:
                # outside point beyond x_max then make x to x_max 
                y = slop*(x_max - x2) + y2
                x = x_max
            elif out & BOTTOM:
                # outside point below y_min then make y to y_min
                x = (y_min-y1)//slop + x1
                y = y_min
            elif out & TOP:
                # outside point above y_max then make y to y_max
                x = (y_max - y1)//slop + x1
                y = y_max

            # update end point of line
            if out == c1:
                x1,y1 = int(x),int(y)
                c1 = region(clip,(x1,y1))
            else:
                x2,y2 = int(x),int(y)
                c2 = region(clip,(x2,y2))




if __name__ == "__main__":
    point = (10,30,80,90) 
    clip_window = (20,20,90,70)
    print( Cohen_Sutherland(clip_window, point) )

    point = (10,10,70,60) 
    clip_window = (20,20,90,70)
    print( Cohen_Sutherland(clip_window, point) )