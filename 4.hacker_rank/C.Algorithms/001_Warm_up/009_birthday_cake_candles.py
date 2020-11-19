# Count how many candles are tallest
# candles = [4, 4, 1, 3]
# The maximum height candles are 4 units high.
# There are 2 of them so return 2

# Constraints
# 1 <= n < 10^5
# 1 <= candles[i] <= 10^7



import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()
