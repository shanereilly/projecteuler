#!/usr/bin/env python3

import math

target = (20,20)

n = target[0] + target[1]
k = target[0]

print(math.factorial(n) // (math.factorial(k) * math.factorial(n-k)))
