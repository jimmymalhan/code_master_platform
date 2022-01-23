# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.


# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return(next((word for word in words if word == word[::-1]), ""))

def main():
    words = ["abc","car","ada","racecar","cool"]
    print(Solution().firstPalindrome(words))

if __name__ == "__main__":
    main()