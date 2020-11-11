#!/usr/bin/env python3

import typing

def properDivisors(n: int) -> typing.List[int]:
    divs = [1]
    for i in range(2, n):
        if n % i == 0:
            divs += [i]
    return divs

amicableList = [-1,-1]
for i in range(2,10000):
    amicableList += [sum(properDivisors(i))]
amicableSum = 0
for index, number in enumerate(amicableList):
    if (number < index) and (amicableList[number] == index):
        amicableSum += (number + index)
print(amicableSum) 

