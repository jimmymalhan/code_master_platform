# Chocolate bar as an array of squares, s= [2, 2, 1, 3, 2]
# Lily wants to find segments assuming to Ron's birthday, d= 4
# with a length equalling his birth month, m = 2
# In this, case two segments meeting her criteria:[2, 2] and [1, 3]

# Input Format
# The first line contains an integer n, the number of squares in the chocolate bar
# The second line contains n space-separated where 0 <= i < n
# The third line contains two space-seperated integers,
# d and m, Ron's birthday and his birthday month.

# Constraints
# 1 <= n <= 100
# 1 <= s[i] <=5, where (0 <= i < n)
# 1 <= d <= 31
# 1 <= m <= 12

# Output Format

# Print an integer denoting the total number of ways that Lily can portion her chocolate bar 
# to share with Ron.

# Sample Input
# 5
# 1 2 1 3 2
# 3 2

# # Sample Output
# 2



import math
import os
import random
import re
import sys

# s = sum
# d = day
# m = month

# s =[2,2,1,3,2]
# m = 2
# d = 4 

# Approach
# We are going to solve this problem using brute force approach
# by looping through the squares in the chocolate bar at each possible interval
# of squares that can form a piece of length 'm' and summing the values of the squares
# within that interval. If that sum is equal to 'd', we increment the integer that
# stores the number of ways the chocolate can be shared with Ron. Once we finish
# traversing through all possible intervals, we print the number of ways we can satisfy
# the constraints as output.
# 
# Tip: Be sure to setup your loop to prevent" array index out of bounds" error! 

def birthday(s, d, m):
    count = 0 # to store the number to counts
    total = sum(s[:m]) #sum of first m elements
    if total == d: 
        count += 1
    
    #sliding window
    for i in range(m, len(s)): # ranging from month to length of string
        total += s[i]
        total -= s[i-m]
        if total == d: 
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()
