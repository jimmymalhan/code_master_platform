# https://leetcode.com/contest/weekly-contest-266/problems/count-vowel-substrings-of-a-string/
# 2062: Count Vowel Substrings

# A substring is a contiguous (non-empty) sequence of characters within a string.

# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

# Given a string word, return the number of vowel substrings in word.

# Example 1:

# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"
# Example 2:

# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.
# Example 3:

# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# Example 4:

# Input: word = "bbaeixoubb"
# Output: 0
# Explanation: The only substrings that contain all five vowels also contain consonants, so there are no vowel substrings.
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase English letters only.

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        return sum(set(word[i:j+1]) == set('aeiou') for i in range(len(word)) for j in range(i+1, len(word)))

def main():
    sol = Solution()
    word = "aeiouu"
    print(sol.countVowelSubstrings(word))

if __name__ == "__main__":
    main()