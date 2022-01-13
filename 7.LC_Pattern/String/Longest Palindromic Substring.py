# Given a string s, return the longest palindromic substring in s. You may assume that the maximum length of s is 1000.


# input: "babad"
# output: "bab"
# Note: "aba" is also a valid answer.

# input: "cbbd"
# output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: # if s is empty, return ""
            return ""
        if len(s) == 1: # if s is a single character, return s
            return s
        longest = s[0] # if s is a single character, return s
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i) # tmp is "a"
            if len(tmp) > len(longest): # if tmp is longer than longest, then tmp is the new longest
                longest = tmp # update longest
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1) # tmp is "bb"
            if len(tmp) > len(longest): # if tmp is longer than longest, then tmp is the new longest
                longest = tmp
        return longest

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]: # if left >= 0 and right < len(s) and s[left] == s[right], then left and right are still in the range of s
            left -= 1
            right += 1
        return s[left + 1: right]

def main():
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))

main()