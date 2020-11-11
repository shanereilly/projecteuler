#!/usr/bin/env python3

import string

with open("p022_names.txt", "r") as f:
    names = f.readlines()

alphabet = string.ascii_uppercase
numbers = range(1,27)
values = dict(zip(alphabet, numbers))

totalScore = 0
for index, name in enumerate(names):
    score = 0
    for c in name:
        if c in values:
            score += values[c]
    totalScore += (score * (index + 1))
print(totalScore)

