# 2186. Minimum Number of Steps to Make Two Strings Anagram II

# You are given two strings s and t. In one step, you can append any character to either s or t.

# Return the minimum number of steps to make s and t anagrams of each other.

# An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# Input: s = "leetcode", t = "coats"
# Output: 7
# Explanation: 
# - In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
# - In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
# "leetcodeas" and "coatsleede" are now anagrams of each other.
# We used a total of 2 + 5 = 7 steps.
# It can be shown that there is no way to make them anagrams of each other with less than 7 steps.

import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1 # get(char, 0) is the default value of hashmap[char]
        for char in t:
            hashmap[char] = hashmap.get(char, 0) - 1 # get(char, 0) is the default value of hashmap[char]
        return sum(abs(v) for v in hashmap.values()) # sum(abs(v) for v in hashmap.values()) is the sum of all values in hashmap

print(Solution().minSteps("leetcode", "coats"))