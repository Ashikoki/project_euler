#!/usr/bin/python

from math import floor

def gcd(a, b):
    if a>b:
        if a%b==0:
            return b
        else:
            return gcd(b, a%b)
    else:
        if b%a==0:
            return a
        else:
            return gcd(a, b%a)
    
    
def smallest_multiple(num):
    val=1
    for i in range(2, num+1):
        for j in range(i,val*i+1):
            if j%i == 0 and j%val == 0:
                val = j
                break
    return val

#we know that the smallest common multiple is equal to
#i*j // gcd(i,j) <---- greatest common divisor
def smallest_multiple_fastest(num):
    ans=1
    for i in range(2,num+1):
        ans = ans*i/gcd(ans,i)
    return ans
        
                   

print(smallest_multiple_fastest(20))

