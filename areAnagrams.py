# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.
from collections import Counter
def areAnagrams(s1, s2):
    a=s1.upper()
    b=s2.upper()
    x=Counter(a)
    print(x)
    y=Counter(b)
    print(y)
    if(x==y):
        return True
    return False
    '''a=s1.upper()#ABA
    b=s2.upper()#BAA
    for i in a:
        print(i)
        x=a.count(i)
        print(x)
        y=b.count(i)
        print(y)
        if(x==y):
            return True
    return False'''
    
s1="Aba"
s2="BAA"
print(areAnagrams(s1,s2))

# write your test cases here...