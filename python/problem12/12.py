#!/usr/bin/env python3

import math
import typing

def numDivisors(n: int) -> int:
    count = 0
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            count += 1
    return 2 * count

def triangleNumbers(n: int) -> int:
    return (n * (n + 1)) // 2

num = 1
while True:
    if numDivisors(triangleNumbers(num)) > 500:
        print("Triangle number: {}\nValue: {}".format(num, triangleNumbers(num)))
        break
    num += 1


