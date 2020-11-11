#!/usr/bin/env python3

import itertools

for c in list(itertools.permutations(range(10)))[999999]:
    print(c, end="")
print()
