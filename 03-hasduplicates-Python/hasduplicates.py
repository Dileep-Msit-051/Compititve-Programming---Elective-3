# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

from sys import float_repr_style


def hasduplicates(L):
    res=[]
    for i in range(len(L)):#0123
        for j in range(len(L)):#0123
            if L[i][j] not in res:
                res.append(L[i][j])
            else:
                return True
    return False
                
    
                    
                    