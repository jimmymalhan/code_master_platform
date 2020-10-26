# mini- max
# Input
# 1, 3, 5, 7, 9
# #Explanation
# The minimum sum is 1 + 3 + 5 + 7 = 16
# The maximum sum is 3 + 5 + 7 + 9 = 24

# Output
# 16 24

# Constraints:
# 1 <= arr[i] < 10^9

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    x = sum(arr)
    print(x-(max(arr)), x-(min(arr)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
