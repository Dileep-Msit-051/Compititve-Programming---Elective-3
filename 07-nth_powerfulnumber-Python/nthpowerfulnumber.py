# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math
# reference from geeks for geeks.
# function to check if
# the number is powerful
def isPowerful(n):
 
    # First divide the number repeatedly by 2
    while (n % 2 == 0):
 
        power = 0
        while (n % 2 == 0):
         
            n = n//2
            power = power + 1
         
          
        # If only 2 ^ 1 divides
        # n (not higher powers),
        # then return false
        if (power == 1):
            return False
     
  
    # if n is not a power of 2
    # then this loop will execute
    # repeat above process
    for factor in range(3, int(math.sqrt(n))+1, 2):
     
        # Find highest power of
        # "factor" that divides n
        power = 0
        while (n % factor == 0):
         
            n = n//factor
            power = power + 1
         
  
        # If only factor ^ 1 divides
        # n (not higher powers),
        # then return false
        if (power == 1):
            return False
     
  
     # n must be 1 now if it
     # is not a prime numenr.
     # Since prime numbers are
     # not powerful, we return
     # false if n is not 1.
    return (n == 1)
def nthPowerfulNumber(n):
    count = 0
    i=1
    while count <= n:
        if isPowerful(i):
            count+=1
            res=i
        i+=1
    return res 
