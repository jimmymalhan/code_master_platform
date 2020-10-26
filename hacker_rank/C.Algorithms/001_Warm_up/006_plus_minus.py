# For array of integers, calculate the ratios of its elements that are positive,
# negative, zero. print the decimal value of each fraction on a new line with 6 place
# after the decimal

# arr = [1, 1 , 0 , -1, -1]
# n = 5
# the ratios are:
# 2/5 = 0.4000000
# 2/5 = 0.4000000
# 1/5 = 0.2000000

# Constraints
# 0 < n <= 100
# -100 <= arr[i] <= 100

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p, n, z  = 0,0,0
    for i in range(len(arr)):
        p = sum(x > 0 for x in arr) / len(arr) 
        n = sum(x < 0 for x in arr) / len(arr) 
        z = sum(x == 0 for x in arr) / len(arr) 

    print(p, n, z, sep='\n')
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
