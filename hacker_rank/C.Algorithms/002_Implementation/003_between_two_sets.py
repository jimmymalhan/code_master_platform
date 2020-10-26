# arrays a = [2, 6] and b = [24,36],
# there are two numbers between them 6 and 12
# 6 % 2 = 0, 6 % 6 = 0, 36 % 6 = 0 for the first value
# Similarly, 12 % 2 = 0, 12 % 6 = 0 and 24 % 12 = 0.
# 36 % 12 = 0

# Sample input
# 2 3
# 2 4
# 16 32 96

# Output
# 3

# Explanation
# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.
# 4, 8 and 16 are the only three numbers for which each element 
# of a is a factor and each is a factor of all elements of b.


import sys
from math import gcd
from functools import reduce


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
A = map(int,input().strip().split(' '))
B = map(int,input().strip().split(' '))

def LCM(a, b):
    return (a*b)//gcd(a,b)

lcm = reduce(LCM, A, 1)
gcd = reduce(gcd, B)

lcm_copy = lcm

count = 0
while lcm <= gcd:
    if(gcd % lcm) == 0:
        count += 1
    lcm = lcm + lcm_copy

print(count)