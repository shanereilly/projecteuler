#!/usr/bin/env python3

import typing

def sieve(n: int, k: int) -> int:
    primeList = [True for i in range(n)]
    primeList[0] = False
    primeList[1] = False

    for i in range(n):
        if primeList[i]:
            for j in range(i+i, n, i):
                primeList[j] = False
    
    count = 0
    for index, truth in enumerate(primeList):
        if truth:
            count += 1
        if count == k:
            return index

print(sieve(10000000, 10001))

