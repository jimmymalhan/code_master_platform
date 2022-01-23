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
import itertools

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        ans, n = 0, len(statements)
        for person in itertools.product([0, 1], repeat=n): # use itertools to create a list only contains 0 or 1
            print(person)
            valid = True                                   # initially, we think the `person` list is valid
            for i in range(n):
                if not person[i]: continue                 # only `good` person's statement can lead to a contradiction, we don't care what `bad` person says
                for j in range(n):
                    if statements[i][j] == 2: continue     # ignore is no statement was made
                    if statements[i][j] != person[j]:      # if there is a contradiction, then valid = False
                        valid = False
                        break                              # optimization: break the loop when not valid
                if not valid:                              # optimization: break the loop when not valid
                    break        
            if valid: 
                ans = max(ans, sum(person))                # count sum only when valid == True
        return ans
print(Solution().maximumGood([[2,1,2],[1,2,2],[2,0,2]])) # 2