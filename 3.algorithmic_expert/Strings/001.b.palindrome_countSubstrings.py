# Count the number of substrings of s that contain exactly k distinct characters.
# https://leetcode.com/problems/palindromic-substrings/

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

    def countSubstrings(self, s: str) -> int:
	    L, r = len(s), 0 # L is the length of the string, r is the number of palindromes
	    for i in range(L): 
	    	for a,b in [(i,i),(i,i+1)]: # a and b are the start and end indices of the substring
	    		while a >= 0 and b < L and s[a] == s[b]: a -= 1; b += 1
	    		r += (b-a)//2
	    return r

def main():
    stringName = Solution()
    print(stringName.countSubstrings("aaa"))

main()