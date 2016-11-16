#!/usr/bin/python

from math import sqrt, ceil

def test_prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    elif num==3:
        return True
    else:
        for i in range(2,ceil(sqrt(num))+1):
            if num%i==0:
                return False
        return True

def find_prime(num):
    prime=1
    i=3
    ret=2
    while prime!=num:
        if test_prime(i):
            ret=i
            prime = prime+1
        i=i+1

    return ret


print(find_prime(10001))

