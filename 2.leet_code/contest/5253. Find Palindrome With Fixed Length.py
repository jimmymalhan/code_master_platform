# Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

# A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

# Input: queries = [1,2,3,4,5,90], intLength = 3
# Output: [101,111,121,131,141,999]
# Explanation:
# The first few palindromes of length 3 are:
# 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201, ...
# The 90th palindrome of length 3 is 999.

# Input: queries = [2,4,6], intLength = 4
# Output: [1111,1331,1551]
# Explanation:
# The first six palindromes of length 4 are:
# 1001, 1111, 1221, 1331, 1441, and 1551.

import collections
import itertools
from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        # think the palindromes in half
        # e.g. len  = 4 we only consider the first 2 digits
        # half: 10, 11, 12, 13, 14, ..., 19, 20, 
        # full: 1001, 1111, 1221, 1331, ...
        # e.g. len = 5 we consider the first 3 digits
        # half: 100, 101, 102, ...
        # full: 10001, 10101, 10201, ...
        # explain the solution:
        # we can generate the palindromes in half by using the formula:
        # half = (10^(length // 2 - 1)) + (10^(length // 2 - 1) - 1) + ... + 1
        # full = half * 2 + 1
        result = [] # result is the list of palindromes
        
        for i in queries:
            result.append(self.generatePalindrome(intLength, i))
        
        return result
    
    def generatePalindrome(self, length, num):
        index = num -1 # index is the index of num
        
		# if the length is even
		# we only think about the fisrt half of digits
        if length % 2 == 0:
            cur = int('1' + '0' * (length // 2 -1)) # cur is the current palindrome
            maxLength = len(str(cur))
            cur += index
            
            if len(str(cur)) > maxLength:
                return -1
            
            else:
                cur = str(cur)
                cur = cur + cur[::-1]
                cur = int(cur)
                return cur
				
        # if the length is odd
		# we consider first (length // 2 + 1) digits
        else:
            cur = int('1' + '0' * (length // 2))
            maxLength = len(str(cur))
            cur += index
            
            if len(str(cur)) > maxLength:
                return -1
            
            else:
                cur = str(cur)
                temp = str(cur)[:-1]
                cur = cur + temp[::-1]
                cur = int(cur)
                return cur

print(Solution().kthPalindrome([1,2,3,4,5,90], 3)) # [101,111,121,131,141,999]