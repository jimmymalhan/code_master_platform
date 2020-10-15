import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    l, r = 0, 0
    # single pass, grab both values
    for i in range(len(arr)):
        l += arr[i][i]
        r += arr[i][-i-1]
    return abs(l-r)

if __name__ == '__main__':
    fptr = open(os.environ['Users'], 'w')
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()