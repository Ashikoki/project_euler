#!/usr/bin/python


#1st we generate the list
fib = [1, 2]

while (fib[-1] <= 4000000):
    fib.append(fib[-1]+fib[-2])

#we compute the sum
total = 0

for num in fib:
    if num%2 != 0:
        total+=num

print(total)
