# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def frequent(r,n):
    c=0
    while (n!=0):
        if n%10==r:
            c+=1
        n=n//10
    return c
def mostFrequentDigit(n):
    b=0
    for t in range(10):
        if frequent(t,n)>frequent(b,n):
            b=t
    return b