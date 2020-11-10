#!/usr/bin/env python3

import typing

def isPalindrome(n: int):
    isPal = True
    num = str(n)
    numDigits = len(num)
    for i in range(numDigits//2):
        if num[i] != num[numDigits - i - 1]:
            isPal = False
    return isPal

maximum = 0

for i in range(100,1000):
    for j in range(100, 1000):
        curr = i * j
        if isPalindrome(curr) and curr > maximum:
            maximum = curr

print(maximum)
