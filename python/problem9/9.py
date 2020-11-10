#!/usr/bin/env python3

import math
import itertools

numbers = [i for i in range(1, 1000)]
combos = itertools.combinations(numbers, 2)

for combo in combos:
    c = 1000 - combo[0] - combo[1]
    if combo[0]**2 + combo[1]**2 == c**2:
        print(combo[0] * combo[1] * c)
        break




