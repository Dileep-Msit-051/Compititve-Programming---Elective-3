# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def nthPowerfulNumber(n):
    count = 0
    i=1
    while count <= n:
        if ispowerfulnumber(i):
            count+=1
            res=i
        i+=1
    return res 
def ispowerfulnumber(n):
    i=1
    j=1
    while(i<n/2+1):
        while(j<n/3+1):
            #print(n,i,j,i**2,j**2)
            if (i**2)*(j**3)==n:
                return True
            j+=1
        i+=1
        j=1
    return False   