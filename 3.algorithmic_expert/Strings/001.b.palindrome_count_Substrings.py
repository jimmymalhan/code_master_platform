#################################################################################################
## Palindromic Substrings ##
# https://leetcode.com/problems/palindromic-substrings/
#################################################################################################

# O(n^2) time | O(n) space
class Solution:
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if self.isPal(s[i:j]):
                    count+=1
        return count
    
    def isPal(self,s):
        return s==s[::-1]

    def countSubstrings_optimized(self, s: str) -> int:
	    L, r = len(s), 0 # L is the length of the string, r is the number of palindromes
	    for i in range(L): 
	    	for a,b in [(i,i),(i,i+1)]: # a and b are the start and end indices of the substring
	    		while a >= 0 and b < L and s[a] == s[b]: a -= 1; b += 1 # while the start and end indices are valid and the characters are equal
	    		r += (b-a)//2 # add the number of palindromes
	    return r

def main():
    stringName = Solution()
    print(stringName.countSubstrings("aaa"))
    print(stringName.countSubstrings_optimized("aaa"))

main()

#################################################################################################
## Count substrings s with k distinct characters ## 
#################################################################################################

# For a strings and an integer k, a selection of substrings is valid if the following conditions are met:
# - The length of every substring is greater than or equal to k. 
# - Each substring isapalindrome.
# - No two substrings overlap.
# - Determine the maximum number of valid substrings that can be formed froms.
# Notes:
# - A substring is a group of adjacent characters in a string.
# - A palindrome is a string that reads the same backward as forward.

# Input:
# s= "aaaaabb"
# k = 2
# output:
# 3

def getMaxSubstrings(s, k):
    while len(s) > 0:
        if len(s) < k: # if the length of the string is less than k, then we can't make a substring of length k
            return 0
        if isPalindrome(s[:k]): # if the first k characters are a palindrome, then we can make a substring of length k
            return 1 + getMaxSubstrings(s[k:], k) # we can make a substring of length k, so we add 1 to the number of substrings
        else:
            return getMaxSubstrings(s[1:], k) # we can't make a substring of length k, so we move on to the next character
    return 0

def isPalindrome(s):
    return s == s[::-1]

print(getMaxSubstrings("aaaaabb", 2)) # 3

#################################################################################################
# Other Notes:
# - https://www.geeksforgeeks.org/count-of-substrings-of-length-k-with-exactly-k-distinct-characters/?ref=lbp
#################################################################################################