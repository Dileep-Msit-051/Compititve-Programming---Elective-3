# Write the function isrectangular(L) that takes a possibly-2d 
# list L and returns True  if it is rectangular, so each row has
#  the same number of elements. Return False otherwise.


def fun_isrectangular(l):
    for i in range(len(l)):
        for j in range (1,len(l)):
            if(len(l[i])!=len(l[j])):
                return False
    return True



