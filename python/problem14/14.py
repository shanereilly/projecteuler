#!/usr/bin/env python3

import typing

prevCollatz = {}

def collatz(n: int) -> int:
    if n in prevCollatz:
        return prevCollatz[n]
    count = 1
    curr = n
    while curr > 1:
        if curr in prevCollatz:
            count += prevCollatz[curr]
            break
        if curr % 2 == 0:
            curr = curr // 2
        else:
            curr = 3 * curr + 1
        count += 1
    prevCollatz[n] = count
    return count

maximum = 0
maximum_i = 0

for i in range(2, 1000000):
    if collatz(i) > maximum:
        maximum = collatz(i)
        maximum_i = i
print(maximum_i, maximum)



