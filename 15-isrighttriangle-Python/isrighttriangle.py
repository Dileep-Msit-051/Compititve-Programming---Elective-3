# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
    p= ((x1-x2)**2)+((y1-y2)**2)
    q= ((x1-x3)**2)+((y1-y3)**2)
    r= ((x2-x3)**2)+((y2-y3)**2)
    
    if((p > 0 and q > 0 and r > 0) and (p == (q+r) or q == (p+r) or r == (p+q))):
        return True
    else:
        return False 
	# your code goes here
	
