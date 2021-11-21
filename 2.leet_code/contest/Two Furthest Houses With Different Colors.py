# There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

# Return the maximum distance between two houses with different colors.

# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

# Input: colors = [1,1,1,6,1,1,1]
# Output: 3
# Explanation: In the above image, color 1 is blue, and color 6 is red.
# The furthest two houses with different colors are house 0 and house 3.
# House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
# Note that houses 3 and 6 can also produce the optimal answer.
from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0 # ans is the max distance between two houses with different colors
        for i, x in enumerate(colors): # i is the index of the house, x is the color of the house
            if x != colors[0]: ans = max(ans, i) # if the color of the house is not the same as the first house, then update the max distance
            if x != colors[-1]: ans = max(ans, len(colors)-1-i) # if the color of the house is not the same as the last house, then update the max distance
        return ans

def main():
    colors = [1,1,1,6,1,1,1]
    print(Solution().maxDistance(colors))

if __name__ == '__main__':
    main()