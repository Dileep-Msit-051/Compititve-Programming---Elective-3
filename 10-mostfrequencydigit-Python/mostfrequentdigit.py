# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
def mostfrequentdigit(n):
    res=[]
    dict={}
    max=0
    temp=0
    if(n==0):
        return 0
    while(n>0):
            x=n%10
            res.append(x)
            n=n//10
	#print(res)
    if(len(res)==2):
            return res[1]
    if(len(res)==1):
            return res[0]
    for i in res:#1,2,2,2,3,4,
            a=res.count(i)
            dict[i]=a
            if(a>max):
                    max=a
                    temp=i
    return temp 
            
    
