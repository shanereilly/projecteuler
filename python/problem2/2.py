#!/usr/bin/env python3

def fibonacci():
    old = 0
    n = 1
    while True:
        yield n
        temp = old
        old = n
        n = temp + n

sum = 0
fib = fibonacci()
curr = next(fib)
while curr < 4000000:
    if curr % 2 == 0:
        sum += curr
    curr = next(fib)

print(sum)


    
        



