# Count the number of substrings of s that contain exactly k distinct characters.
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

def main():
    stringName = Solution()
    print(stringName.countSubstrings("aaa"))

main()