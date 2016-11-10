#!/usr/bin/python

from math import sqrt, floor

def is_prime(prime_list, num):
    for prime in prime_list:
        if num%prime == 0:
            return 0
    return 1

to_fact = 600851475143
prime_list = [2]
used_prime = []

#we generate an arbitrary amount of prime
for i in range (3,100000):
    if is_prime(prime_list,i)==1:
        prime_list.append(i)


while 1:
    for prime in prime_list:
        if to_fact%prime == 0:
            to_fact/=prime
            used_prime.append(prime)
            prime_list.remove(prime)
    for prime in used_prime:
        if to_fact%prime == 0:
            too_fact/=prime
    if is_prime(prime_list, to_fact)==1 or is_prime(used_prime, to_fact)==1:
        break

print(used_prime[-1])
