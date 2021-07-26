"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""



def recursionOnlyBinarySearchValues(L,v):
    #print(L,v)
    return binarysearch(L,v,0,len(L)-1)
    
def binarysearch(L,v,low,high,res=[]):
    mid=(low+high)//2 #0,1
    if (L[mid] == v and low<high):#acfgmq #a
        res.append((mid,L[mid]))
        return res
    elif(low == high):#1,1
        res.append((mid,L[mid]))
        return res
    elif(v<L[mid]):#a<f
        high=mid-1 #1 low 0
        res.append((mid,L[mid]))#mid=0
    else:
        low=mid+1
        res.append((mid,L[mid]))
    return binarysearch(L,v,low,high,res)

def binary_search(input_array, value):

