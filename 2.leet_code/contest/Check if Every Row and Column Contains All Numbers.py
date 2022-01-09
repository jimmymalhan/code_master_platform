# Check if Every Row and Column Contains All Numbers
# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.

from typing import List
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                # use set to check if every element is unique
                if len(set(matrix[i])) != n or len(set([row[j] for row in matrix])) != n:
                    return False
        return True

    def checkValid2(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        while n > 0:
            for i in range(n):
                if len(set(matrix[i])) != n or len(set([row[i] for row in matrix])) != n:
                    return False
            n -= 1
        return True
def main():
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    print(Solution().checkValid(matrix))
    matrix1 = [[1,1,1],[1,2,3],[1,2,3]]
    print(Solution().checkValid(matrix1))
    print(Solution().checkValid2(matrix1))

main()