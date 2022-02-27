# 2185. Counting Words With a Given Prefix

# You are given an array of strings words and a string pref.

# Return the number of strings in words that contain pref as a prefix.

# A prefix of a string s is any leading contiguous substring of s.

# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for word in words if word.startswith(pref))

print(Solution().prefixCount(["pay","attention","practice","attend"], "at")) # 2