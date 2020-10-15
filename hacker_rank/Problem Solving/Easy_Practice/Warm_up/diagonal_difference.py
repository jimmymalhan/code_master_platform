import math
import os
import random
import re
import sys


n = 3
a = [[11, 2, 4], ]

def diagonalDifference(arr):
    l, r = 0, 0
    # single pass, grab both values
    for i in range(len(arr)):
        l += arr[i][i]
        r += arr[i][-i-1]
    return abs(l-r)