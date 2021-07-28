# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.
i=0
res=[]
def evendigit(n):
    global i
    if(n>0):
        x=n%10
        evendigit(n//10)
        if(x%2==0):
            i=i*10+x
def fun_recursion_onlyevendigits(l):
    if l==[]:
        return l
    global i
    if(len(l)!=0):
        i=0
        evendigit(l[0])
        res.append(i)
        fun_recursion_onlyevendigits(l[1:])
    return res