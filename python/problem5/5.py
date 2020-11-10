#!/usr/bin/env python3

import typing

def getFactors(n: int) -> typing.List[int]:
    return [i for i in range(2, n) if n % i == 0]

def simplifyList(l: typing.List[int]) -> typing.List[int]:
    toRemove = []
    for i in l:
        toRemove += getFactors(i)
    for i in toRemove:
        if i in l:
            l.remove(i)
    return l

def isDivisible(n: int, l: typing.List[int]) -> bool:
    retVal = True
    for i in l:
        if n % i != 0:
            retVal = False
            break
    return retVal


l = simplifyList([i for i in range(2,21)])
curr = min(l)
inc = min(l)
while True:
    if isDivisible(curr, l):
        print(curr)
        break
    else:
        curr += inc
