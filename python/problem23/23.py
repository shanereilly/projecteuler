#!/usr/bin/env python3

import typing

abundantNumbers = [False] * 28123

def isAbundant(n: int) -> bool:
    properFactors = 0
    for i in range(1, n):
        if n % i == 0:
            properFactors += i
    if properFactors > n:
        return True
    else:
        return False

for i in range(12, 28123):
    if isAbundant(i):
        abundantNumbers[i] = True

summation = 0

for i in range(1,28124):
    canBe = False
    for j in range(1, i):
        if abundantNumbers[j] and abundantNumbers[i-j]:
            canBe = True
    if not canBe:
        summation += i
print(summation)

    
