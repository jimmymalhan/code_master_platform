# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/submissions/
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target: return True
            mat = list(list(x)[::-1] for x in zip(*mat))
        return False

print(findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:)