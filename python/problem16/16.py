#!/usr/bin/env python3

digits = str(2**1000)
summation = 0
for digit in digits:
    summation += int(digit)
print(summation)
