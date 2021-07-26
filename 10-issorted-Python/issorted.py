# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
    l=len(a)
    print(a)
    for i in range(1,len(a)):
        if (l[i]<l[i-1]):
            return True
        else:
            return False
a=[1,2,3,4,5]
issorted(a)
        