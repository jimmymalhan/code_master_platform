class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1 # adding the frequency of each character to a dictionary
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) # sorting the dictionary in descending order
        res = ''
        for c, freq in freq:
            res += c * freq #concatenating the character to the result string
        return res

def main():
    s = Solution()
    print(s.frequencySort("tree"))
    print(s.frequencySort("cccaaa"))
    print(s.frequencySort("Aabb"))

if __name__ == '__main__':
    main()