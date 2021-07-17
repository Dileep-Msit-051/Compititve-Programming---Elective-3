# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    n=abs(n)
    if(n<0):
        return False
    #x=abs(x)
    x=0
    while(n>0):
            y = n%10
            n = n//10
            if(x==y):
                return True
            x=y
    return False
    '''res=[]
    max=0
    while(n>0):
        x=n%10
        res.append(x)
        n=n//10
    for i in res:
        a=res.count[i]
        if(a>max):
            max=a'''
            
            
            
        
	