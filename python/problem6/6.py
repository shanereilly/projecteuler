#!/usr/bin/env python3

import typing
numbers = [i for i in range(1, 101)]
print(sum(numbers)**2 - sum([number**2 for number in numbers]))
