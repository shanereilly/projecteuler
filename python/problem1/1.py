#!/usr/bin/env python3

print(sum([i for i in range(3,1000) if not (i % 3)]) + sum([i for i in range(5,1000) if not (i % 5)]) - sum([i for i in range(15,1000) if not (i % 15)]))
