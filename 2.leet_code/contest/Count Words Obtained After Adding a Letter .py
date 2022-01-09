# You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

# For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.

# The conversion operation is described in the following two steps:

# Append any lowercase letter that is not present in the string to its end.
# For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".
# Rearrange the letters of the new string in any arbitrary order.
# For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.
# Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

# Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.

# Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
# Output: 2
# Explanation:
# - In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk" to "tack".
# - There is no string in startWords that can be used to obtain targetWords[1] = "act".
#   Note that "act" does exist in startWords, but we must append one letter to the string before rearranging it.
# - In order to form targetWords[2] = "acti", we use startWords[1] = "act", append 'i' to it, and rearrange "acti" to "acti" itself.

from typing import List
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def get_next(word):
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c not in word:
                        yield word[:i] + c + word[i:]
        def check(start, target):
            for i in range(len(start)):
                if start[i] != target[i]:
                    return False
            return True
        def dfs(start, target, visited):
            if check(start, target):
                return 1
            if start in visited:
                return 0
            visited.add(start)
            for next_word in get_next(start):
                if dfs(next_word, target, visited):
                    return 1
            return 0
        res = 0
        for target in targetWords:
            for start in startWords:
                if dfs(start, target, set()):
                    res += 1

def main():
    startWords = ["ant","act","tack"]
    targetWords = ["tack","act","acti"]
    print(Solution().wordCount(startWords, targetWords))

main()