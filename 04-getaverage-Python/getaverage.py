# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def fun_getaverage(s):
    l=s.split(",")
    print(l)
    res=[]
    for i in l:
        if(isint(i)):
            res.append(i)
    x=[int(i)for i in res]
    if(len(x)==0):
        return 0.0
    avg=0
    count=0
    for i in x:
        avg+=i
        count+=1
    return avg/count
        
        
        
            

        
#s="13,excused,14,absent"        
#print(fun_getaverage(s))
