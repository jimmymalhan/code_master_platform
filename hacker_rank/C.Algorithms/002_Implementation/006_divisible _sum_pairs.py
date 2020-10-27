# ar = [ar[0],ar[1]....,ar[n-1], and positive int = k]
# print (i, j) where, i < j  & ar[i] + ar[j] is divisible by k

# For example ar = [1,2,3,4,5,6] and k = 5
# Output as 3pairs  = [1,4], [2,3] and [4,6]

# n = len(ar)
# ar = array of int
# k = int to divide the pair sum by

# Sample Input
# 6 3 
# 1 3 2 6 1 2

# Sample Output
# 5

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n-1): #n-1 is used of the list to not run error 'index out of range'
        j = i+1
        while j < n:
            if ((ar[i] + ar[j]) % k) == 0:
                count += 1
            j += 1
    return count

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    result = divisibleSumPairs(n, k, ar)
    print(result)