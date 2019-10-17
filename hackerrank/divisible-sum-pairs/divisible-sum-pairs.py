#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    missing = {}
    result = 0
    for x in ar:
        value = x % k
        if value not in missing:
            missing[value] = 0
        missing[value] += 1
    used = set()
    for x in missing.keys():
        if x in used:
            continue
        y = k - x
        if y not in missing:
            continue
        result += missing[x] * missing[y]
        used.add(x)
        used.add(y)
    if 0 in missing:
        result += missing[0] / 2
    return int(result)

# print(divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]))
print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))