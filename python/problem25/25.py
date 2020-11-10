#!/usr/bin/env python3

import typing

def fib(n: int) -> int:
    index = 1
    previous = 0
    num = 1
    while len(str(num)) < n:
            temp = num
            num = previous + num
            previous = temp
            index += 1
    return (index, num)

print(fib(1000))



