#!/usr/bin/env python3

import math
import typing

def primeFactors(n: int) -> typing.List[int]:
    maximum = int(math.sqrt(n))
    # Build a list of bools up to sqrt(n)
    primeList = [True for i in range(0, maximum)]
    # Zero and one are not prime
    primeList[0] = False
    primeList[1] = False

    for i in range(2, maximum):
        if primeList[i]:
            for j in range(2 * i, maximum, i):
                primeList[j] = False
    return [index for index, truth in enumerate(primeList) if truth and n % index == 0]  

print(max(primeFactors(600851475143)))
