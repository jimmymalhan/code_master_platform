import math
import os
import random
import re
import sys


def rotateLeft(d, arr):
    return arr[d:] + arr[:d]
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    print(result)

# a = [1, 2, 3, 4, 5]

# print(a[2:] + a[:2])