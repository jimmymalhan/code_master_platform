# There are two types of persons:

# The good person: The person who always tells the truth.
# The bad person: The person who might tell the truth and might lie.
# You are given a 0-indexed 2D integer array statements of size n x n that represents the statements made by n people about each other. More specifically, statements[i][j] could be one of the following:

# 0 which represents a statement made by person i that person j is a bad person.
# 1 which represents a statement made by person i that person j is a good person.
# 2 represents that no statement is made by person i about person j.
# Additionally, no person ever makes a statement about themselves. Formally, we have that statements[i][i] = 2 for all 0 <= i < n.

# Return the maximum number of people who can be good based on the statements made by the n people.

from typing import List
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        good = [0] * n
        bad = [0] * n
        for i in range(n):
            for j in range(n):
                if statements[i][j] == 1:
                    good[i] += 1
                elif statements[i][j] == 0:
                    bad[i] += 1
        ans = 0
        for i in range(n):
            if good[i] == 0:
                ans = max(ans, bad[i])
        return ans

print(Solution().maximumGood([[2,1,2],[1,2,2],[2,0,2]]))