# Given a square matrix, calculate the 
# absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  

# the left to right diaginal = 1 + 5 + 9 = 15
# the right to left diagonal = 3 + 5 + 9 = 17
# their absolute difference is |15 - 17| = 2

# Constraints:
# - 100 <= arr[i][j] <= 100

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    l, r = 0, 0
    for i in (range(len(arr))):
        l += arr[i][i]
        r += arr[i][-i-1]
    return abs(l-r)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()