#!/usr/bin/env python3

import typing

def sieve(n: int) -> int:
    primesList = [True for _ in range(n)]
    primesList[0] = False
    primesList[1] = False

    for i in range(n):
        if primesList[i]:
            for j in range(i+i, n, i):
                primesList[j] = False
    summation = 0
    for index, truth in enumerate(primesList):
        if truth:
            summation += index
    return summation

print(sieve(2000000))

